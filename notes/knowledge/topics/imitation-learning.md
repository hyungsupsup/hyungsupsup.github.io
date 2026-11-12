---
title: 모방학습 (Imitation Learning)
date: 2026-11-12
tags: [topic, imitation-learning]
status: 작성 중
---

## 한 줄 정의
사람이나 전문가가 보여 준 시연(관측-행동 쌍)을 따라 하도록 정책을 학습하는 방법. 가장 단순한 형태는 지도학습 방식의 Behavior Cloning(BC)이다.

## 핵심 이슈 (채워 나갈 것)
- **분포 이동(compounding error)**: 작은 실수가 쌓여서 학습 때 보지 못한 상태로 빠짐
- **다봉(multimodal) 행동**: 같은 상황에서 여러 정답이 있음 → Diffusion Policy 💡, ACT(CVAE)로 해결
- **Action chunking**: 여러 스텝의 동작을 한 번에 예측 (ACT)

## 관련 노트
- 논문: Diffusion Policy, ACT — [[knowledge/map]]
- 실험: (아직 없음)
