# 10. Pandas

## 🎯 학습 목표
- `Series` 와 `DataFrame` 을 만들고 다룰 수 있다.
- `read_csv` / `to_csv` 로 파일을 주고받는다.
- `loc`, `iloc` 로 정확하게 슬라이싱한다.
- 새 열 추가, 부울 인덱싱으로 조건 필터링을 한다.
- `describe`, `mean`, `sort_values` 등 통계/정렬을 사용한다.
- `isna`, `fillna`, `dropna` 로 결측값을 처리한다.

## 📖 핵심 개념
- `df['col']` (열) vs `df.loc[label]` (행) — 흔한 헷갈림
- 조건 여러 개 결합 시 **`&`, `|` 와 각 조건 괄호**
- `to_csv(..., index=False)` 가 보통 깔끔
- 한글 CSV: `encoding='cp949'` 시도

## 🛠️ 실습 프로젝트
- 선수별 경기당 평균 골 수 계산 및 필터링
- 결측값이 포함된 날씨 데이터의 평균 / 최댓값 분석

## 🎉 시리즈 완료!
파이썬 기초 시리즈를 끝까지 따라왔다면, 이제 NumPy, scikit-learn, PyTorch 같은 본격적인 AI 라이브러리로 넘어갈 준비가 됐다.
