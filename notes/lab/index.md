---
title: 실험실
date: 2026-11-12
tags: [lab]
---

Isaac Sim, VLA, 월드모델을 직접 돌려 보면서 **무엇이 되고 무엇이 안 되는지** 기록합니다.
코드는 저장소의 `lab/experiments/` 아래에 실험 번호별로 있습니다.

## 실험 환경
- GPU: RTX 4060 8GB (로컬) + 필요할 때 클라우드 GPU
- Isaac Sim 6.2.0.0 (pip, Python 3.12)

## 실험 목록
| # | 실험 | 상태 | 관련 |
|---|---|---|---|
| 000 | [[lab/experiments/000-isaac-sim-setup\|Isaac Sim 설치]] | ✅ 완료 | [[knowledge/topics/sim2real]] |

## 다음 실험 후보 (Phase 0~1)
- 001 Franka pick & place 스크립트 제어 (RMPflow)
- 002 카메라 기반 색 분류 pick & place
- 003 시연 데이터 자동 생성기 (도메인 랜덤화)
- 004 Diffusion Policy 학습·재현
