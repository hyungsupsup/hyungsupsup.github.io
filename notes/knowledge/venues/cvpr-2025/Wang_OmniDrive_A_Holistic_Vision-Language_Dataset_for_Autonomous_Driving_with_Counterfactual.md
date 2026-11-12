---
title: "OmniDrive: A Holistic Vision-Language Dataset for Autonomous Driving with Counterfactual Reasoning"
tags: [cvpr2025, autonomous-driving, dataset-benchmark, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** OmniDrive는 counterfactual reasoning을 통해 3D 자율주행 task와 vision-language agent를 정렬하는 dataset과 agent framework를 제안한다.

**CVPR 2025** · Shihao Wang, Zhiding Yu, Xiaohui Jiang, Shiyi Lan, Min Shi, Nadine Chang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_OmniDrive_A_Holistic_Vision-Language_Dataset_for_Autonomous_Driving_with_Counterfactual_CVPR_2025_paper.html)

**주제:** Autonomous Driving · Dataset & Benchmark · Embodied Perception

## 문제
VLM의 강한 reasoning 능력을 자율주행에 활용하려 하지만, 이를 2D에서 full 3D understanding으로 확장하는 것이 실제 적용에 중요하다. 또한 planning trajectory와 language-based reasoning을 연결하는 denser supervision이 필요하다.

## 핵심 아이디어
counterfactual-based synthetic data annotation으로 potential scenarios와 그 outcomes를 평가해 large-scale, high-quality dataset을 생성하고, planning trajectories와 language reasoning을 연결하는 denser supervision을 제공한다. Omni-L과 Omni-Q를 통해 vision-language alignment와 3D perception의 중요성을 비교한다.

## 방법
OmniDrive는 counterfactual reasoning을 기반으로 agent model을 3D driving task에 정렬하는 holistic vision-language dataset이다. 이 synthetic annotation process가 대규모 고품질 데이터를 생성해 planning trajectory와 language-based reasoning 사이의 supervision을 강화한다. 또한 Omni-L과 Omni-Q 두 OmniDrive-Agent framework를 탐구해 vision-language alignment와 3D perception의 역할을 평가한다.

## 결과
DriveLM Q&A benchmark와 nuScenes open-loop planning에서 significant improvements를 보여 dataset과 method의 효과를 입증한다.

## 초록 (원문)
The advances in vision-language models (VLMs) have led to a growing interest in autonomous driving to leverage their strong reasoning capabilities. However, extending these capabilities from 2D to full 3D understanding is crucial for real-world applications. To address this challenge, we propose OmniDrive, a holistic vision-language dataset that aligns agent models with 3D driving tasks through counterfactual reasoning. This approach enhances decision-making by evaluating potential scenarios and their outcomes, similar to human drivers considering alternative actions. Our counterfactual-based synthetic data annotation process generates large-scale, high-quality datasets, providing denser supervision signals that bridge planning trajectories and language-based reasoning. Futher, we explore two advanced OmniDrive-Agent frameworks, namely Omni-L and Omni-Q, to assess the importance of vision-language alignment versus 3D perception, revealing critical insights into designing effective LLM-agents. Significant improvements on the DriveLM Q&A benchmark and nuScenes open-loop planning demonstrate the effectiveness of our dataset and methods.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
