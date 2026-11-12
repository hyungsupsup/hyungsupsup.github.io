---
title: "VLMs-Guided Representation Distillation for Efficient Vision-Based Reinforcement Learning"
tags: [cvpr2025, reinforcement-learning, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** VLM의 state representation을 self-supervised learning과 함께 compact VRL agent에 distill하여 sample efficiency를 높이는 DGC를 제안한다.

**CVPR 2025** · Haoran Xu, Peixi Peng, Guang Tan, Yiqian Chang, Luntong Li, Yonghong Tian
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_VLMs-Guided_Representation_Distillation_for_Efficient_Vision-Based_Reinforcement_Learning_CVPR_2025_paper.html)

**주제:** Reinforcement Learning · Autonomous Driving · Embodied Perception

## 문제
Vision-based RL은 고차원이고 복잡한 visual data와 제한된 interaction-collected data 때문에 high-quality state representation 학습과 task-relevant semantic constraint 확보가 어렵다.

## 핵심 아이디어
VLM의 decision-making 능력이 아니라 state representation 능력을 활용해 historical observations와 actions를 supervision signal로 변환하는 prompting-reasoning pipeline으로 semantic representation을 distill한다.

## 방법
DGC는 historical observations와 actions를 novel prompting-reasoning pipeline을 통해 usable supervision으로 변환하고, 이를 self-supervised learning과 함께 compact visual encoder에 distill한다. 이렇게 얻은 semantic representation을 사용해 VRL agent의 policy learning을 수행한다.

## 결과
Carla benchmark에서 state-of-the-art performance를 달성했으며 distilled semantic representations를 통해 sample efficiency가 크게 향상되었다고 주장한다.

## 초록 (원문)
Vision-based Reinforcement Learning (VRL) attempts to establish associations between visual inputs and optimal actions through interactions with the environment. Given the high-dimensional and complex nature of visual data, it becomes essential to learn policy upon high-quality state representation. To this end, existing VRL methods primarily rely on interaction-collected data, combined with self-supervised auxiliary tasks. However, two key challenges remain: limited data samples and a lack of task-relevant semantic constraints. To tackle this, we propose DGC, a method that distills guidance from Visual Language Models (VLMs) alongside self-supervised learning into a compact VRL agent. Notably, we leverage the state representation capabilities of VLMs, rather than their decision-making abilities. Within DGC, a novel prompting-reasoning pipeline is designed to convert historical observations and actions into usable supervision signals, enabling semantic understanding within the compact visual encoder. By leveraging these distilled semantic representations, the VRL agent achieves significant improvements in the sample efficiency. Extensive experiments on the Carla benchmark demonstrate our state-of-the-art performance.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
