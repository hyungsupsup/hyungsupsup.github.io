---
description: arXiv 논문으로 노트 생성 (L1 기본, L2 선택)
argument-hint: <arXiv 링크 또는 ID> [L1|L2]
---

논문 노트를 만든다. 인자: $ARGUMENTS

1. arXiv 초록 페이지(`https://arxiv.org/abs/<ID>`)를 읽어 제목, 저자, 연도, 학회, 초록을 확인한다. 깊이가 L2면 본문(HTML 버전 `https://arxiv.org/html/<ID>` 또는 PDF)까지 읽는다.
2. `notes/templates/paper.md` 형식으로 `notes/knowledge/papers/<연도>-<짧은-이름>.md`를 만든다.
   - L1: "L1 — 요약"까지만 채우고 L2/L3 섹션은 비워 둔다.
   - L2: 방법, 실험, 한계까지 채운다. "내 의견"은 사용자가 직접 쓰도록 질문 형태로 남긴다.
   - 논문에서 확인한 사실만 쓴다. 수치는 원문 그대로 쓴다.
3. `notes/knowledge/map.md`에 그 논문이 있으면 상태를 📄(L1) 또는 📖(L2)로 바꾸고 제목에 `[[knowledge/papers/파일명|...]]` 링크를 건다. 없으면 맞는 분야 표에 추가한다.
4. 관련 주제 노트(`notes/knowledge/topics/`)의 "관련 노트"나 "계보"에 링크를 추가한다.
5. 끝나면 파일 경로와 3줄 요약, 그리고 "이 논문에서 생각해 볼 질문" 1~2개를 사용자에게 보여 준다.
