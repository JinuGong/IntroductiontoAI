"""터미널에서 바로 실행 가능한 챗봇 — 챕터 12 완성판.

준비:
    1. pip install huggingface-hub python-dotenv
    2. .env.example 을 .env 로 복사 후 HF_TOKEN 채우기
    3. python chatbot.py

명령어:
    /quit              종료
    /clear             대화 기록 초기화
    /save [파일명]      대화 저장 (기본: chat.json)
    /load 파일명        저장된 대화 불러오기
    /persona [이름]     페르소나 전환 / 목록
    /history           메시지 개수
    /maxturns N        history 최대 턴 수 변경
    /help              이 도움말
"""
from __future__ import annotations
import json
import os
import sys
import time
from pathlib import Path

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


# ────────────────────────────────────────────────────────────────────
# 설정
# ────────────────────────────────────────────────────────────────────
MODEL       = "meta-llama/Llama-3.2-3B-Instruct"
MAX_TOKENS  = 400
MAX_TURNS   = 10          # 보존할 최근 사용자/봇 턴 쌍 개수

PERSONAS = {
    "default":  "당신은 친절하고 간결한 한국어 AI 비서입니다.",
    "tutor":    "당신은 파이썬 초보자를 가르치는 친절한 선생님입니다. "
                "모든 답변에 짧은 코드 예시를 포함하세요.",
    "reviewer": "당신은 깐깐한 코드 리뷰어입니다. "
                "사용자가 보여주는 코드의 버그, 스타일, 개선점을 짚어주세요.",
    "comedian": "당신은 코미디언입니다. 모든 답변을 농담과 함께 하세요.",
    "tsundere": "당신은 츤데레 캐릭터입니다. 도와주면서도 시큰둥하게 답하세요. "
                "그래도 정보는 정확하게.",
}


# ────────────────────────────────────────────────────────────────────
# 초기화
# ────────────────────────────────────────────────────────────────────
def setup_client() -> InferenceClient:
    load_dotenv()
    token = os.environ.get("HF_TOKEN")
    if not token:
        print("❌ HF_TOKEN 이 설정되지 않았습니다.")
        print("   .env.example 을 .env 로 복사 후 토큰을 채우세요.")
        sys.exit(1)
    return InferenceClient(token=token)


# ────────────────────────────────────────────────────────────────────
# 모델 호출 (재시도 포함)
# ────────────────────────────────────────────────────────────────────
def ask_safe(
    client: InferenceClient,
    messages: list[dict],
    retries: int = 3,
    base_delay: float = 1.0,
) -> str:
    last_error: Exception | None = None
    for attempt in range(retries):
        try:
            response = client.chat_completion(
                messages=messages, model=MODEL, max_tokens=MAX_TOKENS,
            )
            return response.choices[0].message.content
        except Exception as e:
            last_error = e
            if attempt == retries - 1:
                break
            wait = base_delay * (2 ** attempt)
            print(f"⚠️  [{attempt+1}/{retries}] 실패: {type(e).__name__}. "
                  f"{wait:.1f}초 후 재시도…")
            time.sleep(wait)
    return f"❌ {retries}회 재시도 후 실패: {last_error}"


# ────────────────────────────────────────────────────────────────────
# History 관리 — 최근 N턴만 유지 (system 은 항상 보존)
# ────────────────────────────────────────────────────────────────────
def trim_history(messages: list[dict], max_turns: int) -> list[dict]:
    if len(messages) <= 1 + 2 * max_turns:
        return messages
    return [messages[0]] + messages[-2 * max_turns:]


# ────────────────────────────────────────────────────────────────────
# 명령어 핸들러
# ────────────────────────────────────────────────────────────────────
HELP_TEXT = """\
사용 가능한 명령어:
  /quit              종료
  /clear             대화 기록 초기화 (system 만 남김)
  /save [파일명]      대화 저장 (기본: chat.json)
  /load 파일명        저장된 대화 불러오기
  /persona [이름]     페르소나 전환 / 목록 보기
  /history           현재 메시지 개수
  /maxturns N        history 최대 턴 수 설정
  /help              이 도움말
"""


def cmd_clear(state: dict) -> None:
    persona = state['persona']
    state['messages'] = [{"role": "system", "content": PERSONAS[persona]}]
    print("🗑️  대화 기록 초기화")


def cmd_save(state: dict, args: str) -> None:
    filename = args.strip() or "chat.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(state['messages'], f, ensure_ascii=False, indent=2)
    print(f"💾 저장됨: {filename}")


def cmd_load(state: dict, args: str) -> None:
    filename = args.strip()
    if not filename:
        print("⚠️  사용법: /load 파일명")
        return
    if not Path(filename).exists():
        print(f"⚠️  파일 없음: {filename}")
        return
    with open(filename, encoding="utf-8") as f:
        state['messages'] = json.load(f)
    print(f"📂 불러옴: {filename} ({len(state['messages'])} 메시지)")


def cmd_persona(state: dict, args: str) -> None:
    name = args.strip()
    if not name:
        print(f"현재: {state['persona']}.  사용 가능: {list(PERSONAS)}")
        return
    if name not in PERSONAS:
        print(f"⚠️  없는 페르소나. 사용 가능: {list(PERSONAS)}")
        return
    state['persona']  = name
    state['messages'] = [{"role": "system", "content": PERSONAS[name]}]
    print(f"🎭 전환: {name}")


def cmd_history(state: dict) -> None:
    n = len(state['messages'])
    print(f"📜 {n} 개 메시지 (system 1 + 대화 {n-1})")


def cmd_maxturns(state: dict, args: str) -> None:
    try:
        n = int(args.strip())
        if n < 1:
            raise ValueError
    except (ValueError, TypeError):
        print("⚠️  사용법: /maxturns 정수(>=1)")
        return
    state['max_turns'] = n
    print(f"⚙️  최대 턴 수: {n}")


def handle_command(state: dict, line: str) -> bool:
    """슬래시 명령을 처리. 처리됐으면 True, 일반 메시지면 False."""
    if not line.startswith("/"):
        return False
    parts = line.split(maxsplit=1)
    cmd   = parts[0]
    args  = parts[1] if len(parts) > 1 else ""

    if cmd == "/quit":
        print("👋 안녕!")
        sys.exit(0)
    elif cmd == "/help":     print(HELP_TEXT)
    elif cmd == "/clear":    cmd_clear(state)
    elif cmd == "/save":     cmd_save(state, args)
    elif cmd == "/load":     cmd_load(state, args)
    elif cmd == "/persona":  cmd_persona(state, args)
    elif cmd == "/history":  cmd_history(state)
    elif cmd == "/maxturns": cmd_maxturns(state, args)
    else:
        print(f"⚠️  모르는 명령: {cmd}.  /help 참고")
    return True


# ────────────────────────────────────────────────────────────────────
# 메인 루프
# ────────────────────────────────────────────────────────────────────
def main():
    client = setup_client()
    state = {
        'persona':   'default',
        'messages':  [{"role": "system", "content": PERSONAS['default']}],
        'max_turns': MAX_TURNS,
    }

    print(f"🤖 HuggingFace 챗봇 (model: {MODEL})")
    print(f"   /help 로 명령어 보기, /quit 으로 종료\n")

    while True:
        try:
            q = input(f"나 [{state['persona']}] > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n👋 안녕!")
            break

        if not q:
            continue
        if handle_command(state, q):
            continue

        # 일반 대화
        state['messages'].append({"role": "user", "content": q})
        state['messages'] = trim_history(state['messages'], state['max_turns'])

        reply = ask_safe(client, state['messages'])
        state['messages'].append({"role": "assistant", "content": reply})
        print(f"봇 > {reply}\n")


if __name__ == "__main__":
    main()
