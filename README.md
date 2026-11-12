# 섭노트

피지컬 AI(로봇 학습, VLA, 월드모델)를 공부하고 실험한 개인 연구 노트입니다.
`notes/`가 [Quartz](https://quartz.jzhao.xyz)로 빌드되어 https://hyungsupsup.github.io 에 올라갑니다.

```
robot/
├── notes/        # 사이트에 올라가는 노트 (Obsidian vault로 열어도 됨)
│   ├── index.md          홈
│   ├── roadmap/          학습 로드맵 · 주간 회고
│   ├── knowledge/        📚 분야 지도, 논문 노트, 주제 정리, 주간 다이제스트
│   ├── lab/              🧪 실험 기록
│   ├── open-questions.md 연구 질문 모음
│   └── templates/        노트 템플릿
├── lab/          # 실험 코드 · 환경 설치 기록
├── site/         # Quartz 엔진
└── .claude/commands/  # /paper-note, /weekly-digest, /weekly-review, /new-experiment
```

## 로컬 미리보기
```powershell
cd site
npm i                                   # 최초 1회
npx quartz build -d ../notes --serve    # http://localhost:8080
```

## 배포
`main` 브랜치에 push하면 `.github/workflows/deploy.yml`이 자동으로 빌드하고 GitHub Pages에 배포합니다.
