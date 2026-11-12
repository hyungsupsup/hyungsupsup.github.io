---
description: 새 실험 노트와 코드 폴더 생성
argument-hint: <실험-이름> [목표 한 줄]
---

새 실험을 만든다. 인자: $ARGUMENTS

1. `notes/lab/experiments/`에서 가장 큰 번호를 찾아 다음 번호 NNN(3자리)을 정한다.
2. `notes/templates/experiment.md` 형식으로 `notes/lab/experiments/NNN-<이름>.md`를 만든다. 목표가 주어졌으면 채우고, 가설은 사용자에게 물어본다.
3. 코드 폴더 `lab/experiments/NNN-<이름>/`을 만들고 `README.md`(실행 방법, 사용할 가상환경)와 `src/`를 준비한다.
4. `notes/lab/index.md`의 실험 목록 표에 행을 추가한다.
5. 실험에 Isaac Sim이 필요하면 `.venv\Scripts\python.exe`(Isaac Sim 6.2)를 쓴다. 다른 프레임워크가 필요하면 별도 가상환경을 만들고 설치 과정을 `lab/envs/`에 기록한다.
