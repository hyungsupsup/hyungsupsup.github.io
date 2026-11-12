---
title: "Neural Motion Simulator Pushing the Limit of World Models in Reinforcement Learning"
tags: [cvpr2025, world-model, reinforcement-learning]
venue: CVPR 2025
arxiv: "2504.07095"
citations: 14
auto: true
---

> **TL;DR** MoSim은 현재 관측과 행동으로부터 embodied system의 미래 물리 상태를 예측하는 world model로, 상상 세계에서의 효율적 skill acquisition과 zero-shot RL을 가능하게 한다.

**CVPR 2025** · Chenjie Hao, Weyl Lu, Yifan Xu, Yubei Chen
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Hao_Neural_Motion_Simulator_Pushing_the_Limit_of_World_Models_in_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.07095) · 인용 14회

**주제:** World Model · Reinforcement Learning

## 문제
Embodied system은 외부 세계의 패턴뿐 아니라 자신의 motion dynamics를 이해해야 하며, 효율적인 skill acquisition과 planning을 위해 motion dynamic model이 필요하다.

## 핵심 아이디어
MoSim은 현재 관측과 행동을 기반으로 미래 physical state를 예측하는 world model이며, 정확한 long-horizon 예측을 통해 imagined world에서의 skill acquisition과 zero-shot reinforcement learning을 가능하게 한다. 또한 model-free RL 알고리즘을 model-based 방식으로 전환해 physical environment modeling과 RL algorithm 개발을 분리한다.

## 방법
MoSim은 현재 observations와 actions를 입력으로 받아 embodied system의 미래 physical state를 예측한다. 이 world model은 임의의 model-free reinforcement learning 알고리즘을 model-based approach로 변환할 수 있으며, 정확한 long-horizon prediction을 통해 imagined worlds에서 skill acquisition을 지원한다.

## 결과
MoSim은 physical state prediction에서 state-of-the-art 성능을 달성하고 다양한 downstream tasks에서 competitive performance를 보인다. 정확한 long-horizon 예측을 통해 imagined worlds에서 효율적 skill acquisition과 zero-shot reinforcement learning을 가능하게 하며, sample efficiency와 generalization capabilities를 향상시킨다.

## 연결
- **기반 대표 논문:** Dreamer (v1), DreamerV3, World Models (Ha & Schmidhuber) — [[knowledge/map|분야 지도]]

## 초록 (원문)
An embodied system must not only model the patterns of the external world but also understand its own motion dynamics. A motion dynamic model is essential for efficient skill acquisition and effective planning. In this work, we introduce the neural motion simulator (MoSim), a world model that predicts the future physical state of an embodied system based on current observations and actions. MoSim achieves state-of-the-art performance in physical state prediction and provides competitive performance across a range of downstream tasks. This works shows that when a world model is accurate enough and performs precise long-horizon predictions, it can facilitate efficient skill acquisition in imagined worlds and even enable zero-shot reinforcement learning. Furthermore, MoSim can transform any model-free reinforcement learning (RL) algorithm into a model-based approach, effectively decoupling physical environment modeling from RL algorithm development. This separation allows for independent advancements in RL algorithms and world modeling, significantly improving sample efficiency and enhancing generalization capabilities. Our findings highlight that world models for motion dynamics is a promising direction for developing more versatile and capable embodied systems.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
