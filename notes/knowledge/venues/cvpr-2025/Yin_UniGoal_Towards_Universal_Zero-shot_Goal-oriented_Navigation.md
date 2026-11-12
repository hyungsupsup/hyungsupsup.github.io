---
title: "UniGoal: Towards Universal Zero-shot Goal-oriented Navigation"
tags: [cvpr2025, navigation, embodied-perception]
venue: CVPR 2025
arxiv: "2503.10630"
citations: 132
auto: true
---

> **TL;DR** UniGoal은 object category, instance image, text description 등 다양한 goal을 통합 graph로 표현해 하나의 zero-shot navigation 모델로 처리하는 framework이다.

**CVPR 2025** · Hang Yin, Xiuwei Xu, Linqing Zhao, Ziwei Wang, Jie Zhou, Jiwen Lu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yin_UniGoal_Towards_Universal_Zero-shot_Goal-oriented_Navigation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.10630) · 인용 132회

**주제:** Navigation · Embodied Perception

## 문제
기존 zero-shot goal-oriented navigation 방법들은 특정 task에 맞춰 LLM 기반 pipeline을 설계해 goal 유형 간 일반화가 어렵다.

## 핵심 아이디어
서로 다른 goal들을 uniform graph representation으로 통일하고, agent observation을 online scene graph로 유지해 LLM이 explicit graph-based reasoning을 수행하도록 한다.

## 방법
매 time instant마다 scene graph와 goal graph를 matching하고, zero-matched, partial matching, perfect matching 상태에 따라 long-term exploration goal을 생성하는 전략을 적용한다. Partial matching에서는 coordinate projection과 anchor pair alignment로 goal location을 추론하며, scene graph correction과 goal verification, blacklist mechanism으로 stage 간 robust switching을 지원한다.

## 결과
여러 benchmark 실험에서 UniGoal은 하나의 모델로 세 가지 navigation task에서 state-of-the-art zero-shot 성능을 달성했으며, task-specific zero-shot 방법과 supervised universal 방법보다도 우수한 성능을 보였다.

## 초록 (원문)
In this paper, we propose a general framework for universal zero-shot goal-oriented navigation. Existing zero-shot methods build inference framework upon large language models (LLM) for specific tasks, which differs a lot in overall pipeline and fails to generalize across different types of goal. Towards the aim of universal zero-shot navigation, we propose a uniform graph representation to unify different goals, including object category, instance image and text description. We also convert the observation of agent into an online maintained scene graph. With this consistent scene and goal representation, we preserve most structural information compared with pure text and are able to leverage LLM for explicit graph-based reasoning.Specifically, we conduct graph matching between the scene graph and goal graph at each time instant and propose different strategies to generate long-term goal of exploration according to different matching states. The agent first iteratively searches subgraph of goal when zero-matched. With partial matching, the agent then utilizes coordinate projection and anchor pair alignment to infer the goal location. Finally scene graph correction and goal verification are applied for perfect matching. We also present a blacklist mechanism to enable robust switch between stages.Extensive experiments on several benchmarks show that our UniGoal achieves state-of-the-art zero-shot performance on three studied navigation tasks with a single model, even outperforming task-specific zero-shot methods and supervised universal methods.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
