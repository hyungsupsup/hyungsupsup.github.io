---
title: "CarPlanner: Consistent Auto-regressive Trajectory Planning for Large-Scale Reinforcement Learning in Autonomous Driving"
tags: [cvpr2025, autonomous-driving, reinforcement-learning]
venue: CVPR 2025
arxiv: "2502.19908"
citations: 54
auto: true
---

> **TL;DR** CarPlanner는 auto-regressive 구조와 consistency를 활용한 RL 기반 다중 모달 궤적 계획기로 nuPlan에서 기존 SOTA를 능가한다.

**CVPR 2025** · Dongkun Zhang, Jiaming Liang, Ke Guo, Sha Lu, Qi Wang, Rong Xiong 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_CarPlanner_Consistent_Auto-regressive_Trajectory_Planning_for_Large-Scale_Reinforcement_Learning_in_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2502.19908) · 인용 54회

**주제:** Autonomous Driving · Reinforcement Learning

## 문제
기존 RL 기반 자율주행 궤적 계획기는 학습 효율이 낮고 대규모 실제 주행 시나리오를 다루기 어렵다.

## 핵심 아이디어
multi-modal 궤적 생성을 위한 consistent auto-regressive Planner 구조를 도입해 대규모 RL 학습 효율과 시간적 일관성을 동시에 확보한다.

## 방법
CarPlanner는 RL을 사용해 multi-modal 궤적을 auto-regressive하게 생성하며, 시간 단계 간 consistency를 유지해 안정적인 정책 학습을 유도한다. 또한 generation-selection 프레임워크, expert-guided reward function, invariant-view module을 결합해 RL 학습을 단순화하고 성능을 높인다.

## 결과
CarPlanner는 대규모 실제 데이터셋 nuPlan에서 RL-, IL-, rule-based SOTA를 모두 능가했으며, RL 기반 planner가 IL 및 rule-based SOTA를 넘어선 첫 사례로 제시된다.

## 연결
- **기반 대표 논문:** PPO — Proximal Policy Optimization — [[knowledge/map|분야 지도]]

## 초록 (원문)
Trajectory planning is vital for autonomous driving, ensuring safe and efficient navigation in complex environments. While recent learning-based methods, particularly reinforcement learning (RL), have shown promise in specific scenarios, RL planners struggle with training inefficiencies and managing large-scale, real-world driving scenarios.In this paper, we introduce CarPlanner, a Consistent auto-regressive Planner that uses RL to generate multi-modal trajectories. The auto-regressive structure enables efficient large-scale RL training, while the incorporation of consistency ensures stable policy learning by maintaining coherent temporal consistency across time steps. Moreover, CarPlanner employs a generation-selection framework with an expert-guided reward function and an invariant-view module, simplifying RL training and enhancing policy performance.Extensive analysis demonstrates that our proposed RL framework effectively addresses the challenges of training efficiency and performance enhancement, positioning CarPlanner as a promising solution for trajectory planning in autonomous driving.To the best of our knowledge, we are the first to demonstrate that the RL-based planner can surpass both ILand rule-based state-of-the-arts (SOTAs) on the challenging large-scale real-world dataset nuPlan. Our proposed CarPlanner surpasses RL-, IL-, and rule-based SOTA approaches within this demanding dataset.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
