# 11. GitHub 협업 워크플로우

## 학습 목표
- Git과 GitHub의 차이를 설명한다.
- 개인 작업 흐름과 팀 작업 흐름의 차이를 이해한다.
- 브랜치를 생성, 작업, PR로 병합한다.
- 병합 충돌(merge conflict)을 해결한다.
- 실수 상황에서 `reflog`, `reset`, `revert`로 복구한다.

## 핵심 개념
- **GitHub Flow**: main 브랜치 + feature 브랜치 + PR 기반 워크플로우
- **main 직접 커밋 금지**: 항상 브랜치에서 작업 후 PR로 진행
- **작업 전후 `git pull`**: 동료 변경 사항 동기화 필수
- **PR 관리**: 작은 PR + 명확한 설명 - 코드 리뷰 효율성 증대
- **강제 푸시 주의**: `--force` 최소화, `--force-with-lease` 권장

## 실습 시나리오
노트북 §8의 8개 시나리오 + 연습문제 Q3

## 참고 자료
- [Pro Git book](https://git-scm.com/book/ko/v2) (공식 문서, 한국어)
- [GitHub Docs - Hello World](https://docs.github.com/en/get-started/quickstart/hello-world)
- [Oh Shit, Git!?!](https://ohshitgit.com/) - 긴급 상황 해결 가이드

## 시리즈 완료
이 단계 완료 후 개인 및 팀 환경에서 안전하게 코드를 관리할 수 있음
