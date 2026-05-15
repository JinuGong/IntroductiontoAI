# 12. Python 기초로 챗봇 만들기

## 🎯 학습 목표
- HuggingFace Inference API 로 LLM 을 호출할 수 있다.
- 챗봇을 점진적으로 키우면서 이전 챕터들(1-10)을 자연스럽게 응용한다.
- 슬래시 명령어, 페르소나 전환, 에러 재시도 등 실전 챗봇 기능을 구현한다.
- 저장된 대화 데이터를 pandas 로 분석한다.

## 📦 파일
- `notebook.ipynb` — 12 섹션 점진적 빌드 (교육용)
- `chatbot.py` — 터미널에서 바로 실행 가능한 완성판
- `.env.example` — 환경변수 템플릿

## ⚙️ 준비

```bash
# 1. 라이브러리 설치
pip install huggingface-hub python-dotenv pandas

# 2. 토큰 발급
#    https://huggingface.co/settings/tokens (Read 권한)

# 3. .env 파일 만들기
cp .env.example .env
# 에디터로 .env 열어서 HF_TOKEN 채우기

# 4. 실행
python chatbot.py
```

## 🗺️ 이전 챕터 활용 매핑

| 챕터 | 어디서 쓰는가 |
|------|------------|
| Ch1 — 변수/문자열 | f-string, `strip`, `len`, slicing |
| Ch2 — 연산자 | `len(q) > 1000`, `not q` |
| Ch3 — 입력/모듈 | `input()`, `import`, `time.sleep` |
| Ch4 — 조건문 | 명령어 디스패치, `try/except` |
| Ch5 — 반복문 | 챗 루프, 재시도 루프 |
| Ch6 — 리스트 | `messages.append`, 슬라이싱으로 history trim |
| Ch7 — 딕셔너리 | `{"role": ..., "content": ...}`, PERSONAS, Counter |
| Ch8 — 함수 | `ask`, `ask_safe`, 각종 `cmd_*` 핸들러 |
| Ch9 — 파일 I/O | `/save`, `/load`, `.env` 로딩 |
| Ch10 — pandas | 대화 데이터 분석 |

## 🛠️ 챗봇 명령어

| 명령 | 동작 |
|------|------|
| `/quit`            | 종료 |
| `/clear`           | 대화 기록 초기화 |
| `/save [파일명]`     | 대화 저장 (기본 `chat.json`) |
| `/load 파일명`      | 저장된 대화 불러오기 |
| `/persona [이름]`   | 페르소나 전환 / 목록 |
| `/history`         | 메시지 개수 |
| `/maxturns N`      | history 최대 턴 변경 |
| `/help`            | 도움말 |

## 🎭 기본 페르소나
- `default`  — 친절하고 간결한 비서
- `tutor`    — 파이썬 선생님 (예시 코드 포함)
- `reviewer` — 깐깐한 코드 리뷰어
- `comedian` — 농담 섞는 코미디언
- `tsundere` — 츤데레

`chatbot.py` 의 `PERSONAS` 딕셔너리에 추가하면 끝.

## ✏️ 연습문제
노트북 마지막 셀 — 페르소나 추가, 토큰 절약, 요약봇, 디스패치 리팩토링, 로그 분석 확장.

## 🎉 시리즈 진짜 완결
여기까지 따라왔다면 Python 기초로 **진짜 동작하는 제품** 을 만든 것. 다음은 자기만의 페르소나를 만들고 챗봇을 친구에게 보여주는 것!
