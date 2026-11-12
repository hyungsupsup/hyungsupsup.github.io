---
title: "GROVE: A Generalized Reward for Learning Open-Vocabulary Physical Skill"
tags: [cvpr2025, reinforcement-learning, simulation-sim2real]
venue: CVPR 2025
arxiv: "2504.04191"
citations: 17
auto: true
---

> **TL;DR** GROVE는 LLM과 VLM의 상호 보완적 피드백으로 수동 보상 설계나 task-specific demonstration 없이 simulated agent의 open-vocabulary physical skill 학습을 가능하게 하는 일반화된 reward framework이다.

**CVPR 2025** · Jieming Cui, Tengyu Liu, Ziyu Meng, Jiale Yu, Ran Song, Wei Zhang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Cui_GROVE_A_Generalized_Reward_for_Learning_Open-Vocabulary_Physical_Skill_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.04191) · 인용 17회

**주제:** Reinforcement Learning · Simulation & Sim2Real

## 문제
기존 reinforcement learning은 수동 reward 설계의 확장성 한계와 demonstration 기반 방법의 학습 분포 밖 일반화 한계로 인해 다양한 물리 기술을 open-vocabulary로 학습하기 어렵다.

## 핵심 아이디어
LLM이 task requirement를 precise physical constraint로 생성하고 VLM이 motion semantics와 naturalness를 평가하며, iterative design process로 VLM feedback이 LLM-generated constraint를 지속적으로 정제해 self-improving reward system을 만든다. 또한 Pose2CLIP으로 rendering 없이 agent pose를 semantic feature space에 projection해 simulation과 natural image 사이 domain gap을 줄인다.

## 방법
GROVE는 LLM-generated physical constraint와 VLM-based feedback를 반복적으로 정제하여 reward를 구성한다. Pose2CLIP은 lightweight mapper로 agent pose를 semantic feature space에 직접 projection해 computationally expensive rendering 없이 sim-to-natural image domain gap을 완화한다. 이 reward를 diverse embodiments와 learning paradigms에서 reinforcement learning 학습에 사용한다.

## 결과
다양한 embodiments와 learning paradigms 실험에서 GROVE는 이전 방법보다 motion naturalness를 22.2% 높이고 task completion score를 25.7% 개선하면서 training을 8.4x faster로 달성했다.

## 연결
- **기반 대표 논문:** Code as Policies, Isaac Gym, PPO — Proximal Policy Optimization — [[knowledge/map|분야 지도]]

## 초록 (원문)
Learning open-vocabulary physical skills for simulated agents presents a significant challenge in artificial intelligence. Current reinforcement learning approaches face critical limitations: manually designed rewards lack scalability across diverse tasks, while demonstration-based methods struggle to generalize beyond their training distribution. We introduce GROVE, a generalized reward framework that enables open-vocabulary physical skill learning without manual engineering or task-specific demonstrations. Our key insight is that Large Language Models (LLMs) and Vision Language Models (VLMs) provide complementary guidance---LLMs generate precise physical constraints capturing task requirements, while VLMs evaluate motion semantics and naturalness. Through an iterative design process, VLM-based feedback continuously refines LLM-generated constraints, creating a self-improving reward system. To bridge the domain gap between simulation and natural images, we develop Pose2CLIP, a lightweight mapper that efficiently projects agent poses directly into semantic feature space without computationally expensive rendering. Extensive experiments across diverse embodiments and learning paradigms demonstrate GROVE's effectiveness, achieving 22.2% higher motion naturalness and 25.7% better task completion scores while training 8.4x faster than previous methods. These results establish a new foundation for scalable physical skill acquisition in simulated environments.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
