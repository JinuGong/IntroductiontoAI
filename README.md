# 🐍 Python Basics — AI를 위한 파이썬 기초

AI 강의용 파이썬 입문 시리즈. 각 챕터는 독립된 노트북이며, 위에서 아래로 순서대로 학습하면 된다.

## 📚 챕터

| #   | 챕터 | 핵심 주제 |
|-----|------|----------|
| 01  | [변수와 자료형](01_variables_and_types/) | `print`, 주석, `int/float/str/bool`, 형변환 |
| 02  | [연산자](02_operators/) | 산술 · 비교 · 논리 · 비트 연산자, 복합 할당 |
| 03  | [입력과 모듈](03_input_and_modules/) | `input()`, `split/map`, `random`, `math` |
| 04  | [조건문](04_conditionals/) | `if/elif/else`, BMI 계산기, 미니 게임 |
| 05  | [반복문](05_loops/) | `for`, `while`, `range`, `break/continue`, Hangman |
| 06  | [리스트와 튜플](06_lists_and_tuples/) | 리스트 연산, 인덱싱/슬라이싱, 정렬, 컴프리헨션 |
| 07  | [딕셔너리와 집합](07_dicts_and_sets/) | `dict` CRUD, `set` 연산, 빈도 분석 |
| 08  | [함수](08_functions/) | `def`, 매개변수, `return`, 스코프, `lambda`, 재귀 |
| 09  | [파일 입출력](09_file_io/) | `open`, `with`, `csv` 모듈, URL 읽기 |
| 10  | [Pandas](10_pandas/) | `DataFrame`, `read_csv`, 슬라이싱, 결측값 처리 |
| 11  | [GitHub 협업](11_github_collaboration/) | 브랜치, PR, 충돌 해결, 일상 시나리오 8개 |
| 12  | [챗봇 만들기 (캡스톤)](12_chatbot_with_python/) | HuggingFace API + Ch1~10 종합 응용 |

## 🚀 시작하기

```bash
git clone <this-repo>
cd python-basics
pip install -r requirements.txt
jupyter notebook
```

또는 각 챕터를 [Google Colab](https://colab.research.google.com/) 으로 열어도 된다.

## 📁 폴더 구조

```
python-basics/
├── README.md
├── requirements.txt
├── .gitignore
└── NN_topic/
    ├── notebook.ipynb   ← 실습 노트북
    └── README.md         ← 챕터 학습 목표 / 핵심 개념 / 연습문제
```

## 📝 라이선스

학습 · 강의 자료용. 자유롭게 사용하되 출처는 남겨주세요.
