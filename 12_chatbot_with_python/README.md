# 12. Python 기초로 챗봇 만들기

## 학습 목표
- HuggingFace Inference API로 LLM을 호출한다.
- 챗봇을 점진적으로 구축하면서 이전 챕터(1-10)를 실무 적용한다.
- 슬래시 명령어, 페르소나 전환, 에러 재시도 등 실전 챗봇 기능을 구현한다.
- 저장된 대화 데이터를 Pandas로 분석한다.

## 파일 구성
- `notebook.ipynb`: 12개 섹션 점진적 구축 (교육용)
- `chatbot.py`: ��미널 직접 실행 가능한 완성판
- `.env.example`: 환경변수 템플릿

## 준비

```bash
# 1. 라이브러리 설치
pip install huggingface-hub python-dotenv pandas

# 2. HuggingFace 토큰 발급
# https://huggingface.co/settings/tokens (Read 권한)

# 3. .env 파일 생성
cp .env.example .env
# 에디터로 .env 파일을 열어 HF_TOKEN 입력

# 4. 실행
python chatbot.py
```

## 이전 챕터 활용 매핑

| 챕터 | 활용 위치 |
|------|----------|
| Ch1 - 변수/문자열 | f-string, `strip`, `len`, 슬라이싱 |
| Ch2 - 연산자 | `len(q) > 1000`, `not q` |
| Ch3 - 입력/모듈 | `input()`, `import`, `time.sleep` |
| Ch4 - 조건문 | 명령어 디스패치, `try/except` |
| Ch5 - 반복문 | 챗 루프, 재시도 루프 |
| Ch6 - 리스트 | `messages.append`, 슬라이싱으로 히스토리 제한 |
| Ch7 - 딕셔너리 | `{"role": ..., "content": ...}`, PERSONAS, Counter |
| Ch8 - 함수 | `ask`, `ask_safe`, 다양한 `cmd_*` 핸들러 |
| Ch9 - 파일 I/O | `/save`, `/load`, `.env` 로딩 |
| Ch10 - Pandas | 대화 데이터 분석 |

## 챗봇 명령어

| 명령 | 동작 |
|------|------|
| `/quit` | 프로그램 종료 |
| `/clear` | 대화 기록 초기화 |
| `/save [파일명]` | 대화 저장 (기본값: `chat.json`) |
| `/load 파일명` | 저장된 대화 불러오기 |
| `/persona [이름]` | 페르소나 전환 / 목록 조회 |
| `/history` | 메시지 개수 확인 |
| `/maxturns N` | 히스토리 최대 턴 수 변경 |
| `/help` | 도움말 표시 |

## 기본 페르소나
- `default`: 친절하고 간결한 비서
- `tutor`: Python 강사 (예시 코드 포함)
- `reviewer`: 엄격한 코드 리뷰어
- `comedian`: 유머를 섞은 코미디언
- `tsundere`: 츤데레

`chatbot.py`의 `PERSONAS` 딕셔너리에 추가하여 확장

## 연습문제
노트북 마지막 셀 - 페르소나 추가, 토큰 절약, 요약봇, 디스패치 리팩토링, 로그 분석 확장

## 시리즈 완결
Python 기초로 실제 동작하는 제품을 개발할 수 있는 역량 확보. 다음 단계는 자신만의 페르소나를 구축하고 챗봇을 동료에게 공유
