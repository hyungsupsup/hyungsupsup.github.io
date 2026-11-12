---
title: "Sim-to-Real Causal Transfer: A Metric Learning Approach to Causally-Aware Interaction Representations"
tags: [cvpr2025, simulation-sim2real, navigation, embodied-perception]
venue: CVPR 2025
arxiv: "2312.04540"
citations: 12
auto: true
---

> **TL;DR** 다중 에이전트 상호작용 표현의 인과적 인식성을 metric learning으로 강화하고, cross-domain multi-task learning으로 sim-to-real 인과 전이를 수행하는 방법을 제안한다.

**CVPR 2025** · Ahmad Rahimi, Po-Chien Luan, Yuejiang Liu, Frano Rajič, Alexandre Alahi
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Rahimi_Sim-to-Real_Causal_Transfer_A_Metric_Learning_Approach_to_Causally-Aware_Interaction_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2312.04540) · 인용 12회

**주제:** Simulation & Sim2Real · Navigation · Embodied Perception

## 문제
기존 다중 에이전트 표현은 비인과적 에이전트 perturbation에는 부분적으로 견고하지만, mediator 에이전트를 포함한 간접 인과 효과를 모델링하는 것은 여전히 어렵다.

## 핵심 아이디어
인과 주석으로 latent representation을 regularize하는 metric learning 접근을 도입하고, 실제 인과 주석이 없는 경우에도 cross-domain multi-task learning을 통해 sim-to-real 인과 전이를 가능하게 한다.

## 방법
먼저 CausalAgents benchmark 관점에서 기존 표현의 인과 인식성을 분석하고, 인과 annotation을 이용해 latent representation을 metric learning으로 정규화한다. 이를 실제 환경에 적용하기 위해 cross-domain multi-task learning 기반 sim-to-real causal transfer 방법을 제안한다. trajectory prediction datasets에서 generalization을 평가한다.

## 결과
제안 방법은 더 높은 인과 인식성과 out-of-distribution robustness를 보였고, 실제 인과 주석 없이도 real-world data의 25%만 사용하여 더 높은 예측 정확도를 달성했다.

## 초록 (원문)
Modeling spatial-temporal interactions among neighboring agents is at the heart of multi-agent problems such as motion forecasting and crowd navigation. Despite notable progress, it remains unclear to which extent modern representations can capture the causal relationships behind agent interactions. In this work, we take an in-depth look at the causal awareness of these representations, from computational formalism to real-world practice. First, we revisit the notion of non-causal robustness studied in the recent CausalAgents benchmark. We show that existing representations are already partially resilient to perturbations of non-causal agents, and yet modeling indirect causal effects involving mediator agents remains challenging. To address this challenge, we introduce a metric learning approach that regularizes latent representations with causal annotations. Our controlled experiments show that this approach not only leads to higher degrees of causal awareness but also yields stronger out-of-distribution robustness. To further operationalize it in practice, we propose a sim-to-real causal transfer method via cross-domain multi-task learning. Experiments on trajectory prediction datasets show that our method can significantly boost generalization, even in the absence of real-world causal annotations, where we acquire higher prediction accuracy by only using 25% of real-world data. We hope our work provides a new perspective on the challenges and potential pathways toward causally-aware representations of multi-agent interactions. Our code is available in supplementary materials. Our code is available at https://github.com/vita-epfl/CausalSim2Real.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
