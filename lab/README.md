# lab — 실험 코드

- `experiments/NNN-이름/` — 실험별 코드. 기록은 `notes/lab/experiments/NNN-이름.md`
- `envs/` — 가상환경 설치 기록 (프레임워크마다 따로)
- `common/` — 여러 실험에서 재사용하는 코드 (카메라, 제어기, 데이터 저장)

대용량 산출물(`data/`, `checkpoints/`, `outputs/`)은 git에서 제외됩니다. 공개할 그림만 `notes/`로 복사하세요.

## 가상환경
| 이름 | 위치 | 용도 | 기록 |
|---|---|---|---|
| Isaac Sim 6.2 | `../.venv` | 시뮬레이션 | [envs/isaac-sim.md](envs/isaac-sim.md) |
