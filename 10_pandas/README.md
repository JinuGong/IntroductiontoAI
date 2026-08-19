# 10. Pandas

## 학습 목표
- `Series`와 `DataFrame`을 생성하고 다룬다.
- `read_csv` / `to_csv`로 파일을 읽고 쓴다.
- `loc`, `iloc`로 정확하게 데이터를 슬라이싱한다.
- 새 열 추가 및 부울 인덱싱으로 조건 필터링을 수행한다.
- `describe`, `mean`, `sort_values` 등의 통계 및 정렬 기능을 활용한다.
- `isna`, `fillna`, `dropna`로 결측값을 처리한다.

## 핵심 개념
- **`df['col']` vs `df.loc[label]`**: 열 선택 vs 행 선택 - 혼동 주의
- **복합 조건 필터링**: **`&`, `|` 연산자와 각 조건을 괄호로 감싸기**
- **`to_csv()` 옵션**: `to_csv(..., index=False)` 권장
- **한글 CSV 처리**: `encoding='cp949'` 시도

## 실습 프로젝트
- 선수별 경기당 평균 골 수 계산 및 필터링
- 결측값이 포함된 날씨 데이터의 평균/최댓값 분석

## 시리즈 완료
Python 기초 시리즈 학습 완료 시점부터 NumPy, scikit-learn, PyTorch 등의 고급 AI 라이브러리로 진행 가능
