---
title: "Reasoning in Visual Navigation of End-to-end Trained Agents: A Dynamical Systems Approach"
tags: [cvpr2025, navigation, embodied-perception, reinforcement-learning]
venue: CVPR 2025
arxiv: "2503.08306"
citations: 10
auto: true
---

> **TL;DR** 실제 로봇의 대규모 navigation 실험을 통해 end-to-end 학습 agent의 dynamics, latent memory, planning, value function 기반 reasoning을 분석한 연구이다.

**CVPR 2025** · Steeven Janny, Hervé Poirier, Leonid Antsfeld, Guillaume Bono, Gianluca Monaci, Boris Chidlovskii 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Janny_Reasoning_in_Visual_Navigation_of_End-to-end_Trained_Agents_A_Dynamical_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.08306) · 인용 10회

**주제:** Navigation · Embodied Perception · Reinforcement Learning

## 문제
Embodied AI의 end-to-end navigation agent 평가와 benchmark가 여전히 simulation에 치중되어 있어, 빠르게 움직이는 실제 로봇에서 어떤 reasoning이 나타나는지 충분히 알려져 있지 않다.

## 핵심 아이디어
실제 환경에서 대규모 navigation episode를 수행하고, agent가 학습한 open-loop forecasting dynamics와 sensing의 상호작용, latent memory, planning, value function을 체계적으로 probing하여 end-to-end 학습에서 emerging하는 reasoning을 분석한다.

## 방법
물리 로봇으로 실제 환경에서 대규모 navigation episode를 수집하고, agent가 학습한 realistic dynamics와 sensing의 interplay를 분석한다. latent memory가 scene structure와 exploration 정보를 어떻게 보유하는지, 제한된 horizon의 plan 증거가 있는지, learned value function이 long-term planning과 어떻게 관련되는지를 post-hoc analysis로 조사한다.

## 결과
agent의 memory에서 제한된 horizon에 대한 다소 정밀한 plan 증거를 발견했고, learned value function이 long-term planning과 관련됨을 보였다. 또한 interactive tool을 제공한다.

## 연결
- **기반 대표 논문:** Open X-Embodiment (데이터셋), PPO — Proximal Policy Optimization, RMA — Rapid Motor Adaptation, World Models (Ha & Schmidhuber) — [[knowledge/map|분야 지도]]

## 초록 (원문)
Progress in Embodied AI has made it possible for end-to-end-trained agents to navigate in photo-realistic environments with high-level reasoning and zero-shot or language-conditioned behavior, but evaluations and benchmarks are still dominated by simulation. In this work, we focus on the fine-grained behavior of fast-moving real robots and present a large-scale experimental study involving \numepisodes navigation episodes in a real environment with a physical robot, where we analyze the type of reasoning emerging from end-to-end training. In particular, we study the presence of realistic dynamics which the agent learned for open-loop forecasting, and their interplay with sensing. We analyze the way the agent uses latent memory to hold elements of the scene structure and information gathered during exploration. We probe the planning capabilities of the agent, and find in its memory evidence for somewhat precise plans over a limited horizon. Furthermore, we show in a post-hoc analysis that the value function learned by the agent relates to long-term planning. Put together, our experiments paint a new picture on how using tools from computer vision and sequential decision making have led to new capabilities in robotics and control. An interactive tool is available at https://visual-navigation-reasoning.github.io

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
