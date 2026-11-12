---
title: "Vid2Sim: Realistic and Interactive Simulation from Video for Urban Navigation"
tags: [cvpr2025, simulation-sim2real, navigation, reinforcement-learning]
venue: CVPR 2025
arxiv: "2501.06693"
citations: 53
auto: true
---

> **TL;DR** Vid2Sim은 단안 비디오로부터 사실적이고 물리적으로 상호작용 가능한 3D 도시 시뮬레이션 환경을 생성해 visual navigation agent의 sim2real 성능을 향상시키는 real2sim 프레임워크이다.

**CVPR 2025** · Ziyang Xie, Zhizheng Liu, Zhenghao Peng, Wayne Wu, Bolei Zhou
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Xie_Vid2Sim_Realistic_and_Interactive_Simulation_from_Video_for_Urban_Navigation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.06693) · 인용 53회

**주제:** Simulation & Sim2Real · Navigation · Reinforcement Learning

## 문제
기존 domain randomization과 system identification은 시뮬레이션과 그래픽스 엔진의 현실성 한계로 인해 sim-to-real gap을 충분히 줄이지 못한다.

## 핵심 아이디어
단안 비디오를 입력으로 neural 3D scene reconstruction과 simulation을 결합한 scalable하고 cost-efficient한 real2sim pipeline을 제안한다.

## 방법
Vid2Sim은 monocular video로부터 photo-realistic하고 physically interactable한 3D simulation environment를 생성한다. 이 환경에서 복잡한 urban environment의 visual navigation agent를 reinforcement learning으로 학습시킨다.

## 결과
Vid2Sim으로 학습한 agent는 기존 simulation 방법으로 학습한 agent 대비 digital twins와 real world에서 urban navigation success rate를 각각 31.2%와 68.3% 향상시켰다.

## 연결
- **기반 대표 논문:** DDPM, Domain Randomization (Tobin et al.), Isaac Gym, SimplerEnv — 시뮬레이션으로 실제 정책 평가 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Sim-to-real gap has long posed a significant challenge for robot learning in simulation, preventing the deployment of learned models in the real world. Previous work has primarily focused on domain randomization and system identification to mitigate this gap. However, these methods are often limited by the realism of the simulation and graphics engines. In this work, we propose Vid2Sim, a novel framework that effectively bridges the sim2real gap through a scalable and cost-efficient real2sim pipeline for neural 3D scene reconstruction and simulation. Given a monocular video as input, Vid2Sim can generate photo-realistic and physically interactable 3D simulation environments to enable the reinforcement learning of visual navigation agents in complex urban environments. Extensive experiments demonstrate that Vid2Sim significantly improves the performance of urban navigation in the digital twins and real world by 31.2% and 68.3% in success rate compared with agents trained with prior simulation methods. Code and data will be made publicly available.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
