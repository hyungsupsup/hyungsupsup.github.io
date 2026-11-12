---
description: 지난 1주일 arXiv 피지컬 AI 논문 다이제스트 작성
argument-hint: "[YYYY-Www] (생략하면 지난주)"
---

주간 다이제스트를 만든다. 대상 주: $ARGUMENTS (비어 있으면 오늘 기준 지난 ISO 주)

1. 해당 주(월~일)에 arXiv cs.RO에 제출된 논문과, cs.LG·cs.CV 중 `notes/knowledge/digests/index.md`의 추적 키워드에 해당하는 논문을 찾는다.
   - arXiv API를 우선 쓴다: `http://export.arxiv.org/api/query?search_query=...&sortBy=submittedDate&sortOrder=descending&max_results=200`
   - 보조 자료: Hugging Face Daily Papers, 주요 연구실(Physical Intelligence, NVIDIA GEAR, Google DeepMind Robotics, Stanford·Berkeley·CMU) 발표
2. 관련성이 높은 논문을 15~30편 골라 `notes/templates/digest.md` 형식으로 `notes/knowledge/digests/<YYYY-Www>.md`에 정리한다.
   - 각 항목: `- **제목** — 한 줄 요약 ([arXiv](링크))`
   - 하이라이트 2~3편은 사용자 관심사(`notes/roadmap/index.md`의 관심 방향, `notes/open-questions.md`)와 연결해서 고른다.
   - 초록에서 확인한 내용만 쓴다.
3. `notes/knowledge/digests/index.md`의 "주간 목록" 맨 위에 링크를 추가한다.
4. 그 달의 마지막 주라면, 그 달의 다이제스트를 묶어 "월간 트렌드 정리" 3~5줄 초안도 제안한다.
5. 하이라이트 3편과 "정독 추천 1편 + 이유"를 사용자에게 보여 준다.
