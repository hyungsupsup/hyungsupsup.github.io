# 섭노트 — 프로젝트 규칙

## 목적
피지컬 AI(로봇 학습, VLA, 월드모델)를 공부하고 실험하는 개인 연구 노트.
1. **로드맵·회고** — 학습 계획, 주간 회고, 연구 질문 (`notes/roadmap/`, `notes/open-questions.md`)
2. **지식 창고** — 대표·최신 논문 노트와 트렌드 요약 (`notes/knowledge/`)
3. **실험실** — Isaac Sim / VLA / 월드모델 소규모 실험 (`lab/` 코드, `notes/lab/` 기록)

`notes/`는 Quartz(`site/`)로 빌드되어 GitHub Pages(https://hyungsupsup.github.io)에 **공개**된다.
개인적인 목표와 맥락은 `CLAUDE.local.md`(git 제외)에 있다.

## 디렉터리 규칙
| 경로 | 내용 | 공개 |
|---|---|---|
| `notes/` | 사이트에 올라가는 모든 노트 (Obsidian vault로 열어도 됨) | 공개 |
| `notes/templates/` | 노트 템플릿 (Quartz가 무시) | 사이트 제외 |
| `notes/knowledge/papers/` | 논문 노트. 파일명 `YYYY-짧은이름.md` (예: `2023-diffusion-policy.md`) | 공개 |
| `notes/knowledge/digests/` | 주간 arXiv 요약 `YYYY-Www.md` | 공개 |
| `notes/lab/experiments/` | 실험 기록 `NNN-이름.md` | 공개 |
| `notes/roadmap/weekly/` | 주간 회고 `YYYY-Www.md` | 공개 |
| `lab/` | 실험 코드 (`lab/experiments/NNN-이름/`), 환경 설치 기록 | 저장소 공개, 사이트 제외 |
| `private/`, `CLAUDE.local.md` | 개인 메모 | **git 제외** |
| `site/` | Quartz 엔진. 내용 수정은 `notes/`에서만 | — |

## 작성 규칙
- 노트는 한국어, 논문·모델·기술 용어는 영어 원문 유지.
- 노트끼리는 Obsidian 위키링크 `[[파일명]]`으로 연결한다. 논문 노트 ↔ 실험 노트 ↔ 주제 노트를 반드시 상호 링크.
- 모든 노트에 frontmatter: `title`, `date`, `tags` (필요시 `status`).
- 논문 노트 깊이: `L1`(요약) / `L2`(정독+의견) / `L3`(코드 실행·재현). frontmatter `depth`로 표기.
- 실험 노트는 `목표/가설 → 설정 → 결과 → 문제점·질문` 순서. 실패도 반드시 기록.
- 실험 중 생긴 연구 질문은 `notes/open-questions.md`에 추가하고 출처 실험을 링크.
- 사실(논문 내용, 수치, 링크)은 확인한 것만 쓴다. 미확인은 `(확인 필요)`로 표기.
- **공개 파일(`notes/`, `lab/`, `README.md`, `CLAUDE.md`, `.claude/`)에는 `CLAUDE.local.md`·`private/`의 개인적인 목표나 계획을 절대 쓰지 않는다.** 개인 연구 노트의 톤을 유지한다.

## 환경
- OS: Windows 11, GPU: RTX 4060 8GB (Isaac Sim 공식 최소사양 미만), Driver 566.36 (업데이트 권장)
- Isaac Sim 6.2.0.0: `.venv/` (Python 3.12, uv로 설치). 실행: `.venv\Scripts\isaacsim.exe`
- 프레임워크별 가상환경 분리 (Isaac Sim / LeRobot / VLA는 torch·CUDA 요구가 충돌하기 쉬움). 설치 기록은 `lab/envs/`.
- 7B급 VLA·월드모델 학습/추론은 클라우드 GPU 사용.

## 커스텀 명령 (`.claude/commands/`)
- `/paper-note <arXiv 링크|ID> [L1|L2]` — 논문 노트 생성
- `/weekly-digest` — 지난 1주 arXiv 피지컬 AI 논문 요약
- `/weekly-review` — 주간 회고 작성
- `/new-experiment <이름>` — 실험 노트 + 코드 폴더 생성
