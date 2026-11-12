---
title: "RL-RC-DoT: A Block-level RL agent for Task-Aware Video Compression"
tags: [cvpr2025, autonomous-driving, other]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** RL로 macro-block별 QP를 제어해 autonomous driving의 car detection과 ROI encoding 같은 downstream task에 맞춰 video compression을 최적화하는 방법이다.

**CVPR 2025** · Uri Gadot, Assaf Shocher, Shie Mannor, Gal Chechik, Assaf Hallak
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Gadot_RL-RC-DoT_A_Block-level_RL_agent_for_Task-Aware_Video_Compression_CVPR_2025_paper.html)

**주제:** Autonomous Driving · Other

## 문제
기존 video encoder는 human perception을 위해 reconstruction error와 bit-rate를 최적화하지만, autonomous driving 등에서는 대부분의 video가 object recognition이나 segmentation 같은 AI task의 입력이므로 downstream task 성능을 기준으로 encoding을 최적화할 필요가 있다. 그러나 이를 기존 표준 video encoder와 결합하는 것이 어렵다.

## 핵심 아이디어
macro-block 수준에서 QP를 제어해 task-relevant region을 우선 encoding하고, QP 선택을 RL로 학습해 task 성능과 bit-rate 제약의 장기적 trade-off를 균형 잡는다. Inference 시 downstream task를 입력으로 요구하지 않아 streaming과 edge device에 적합하다.

## 방법
Agent가 frame 내 macro-block별 QP를 선택하는 policy를 학습하며, 선택이 downstream task 성능과 bit-rate에 미치는 long-term 영향을 고려하도록 RL로 최적화한다. 이 granular control로 task-relevant region에 bit를 더 배분한다.

## 결과
car detection과 ROI (saliency) encoding 두 task에서 주어진 bit rate 대비 task-agnostic encoding보다 task 성능을 향상시켰다고 보고한다.

## 초록 (원문)
Video encoders optimize compression for human perception by minimizing reconstruction error under bit-rate constraints. In many modern applications such as autonomous driving, an overwhelming majority of videos serve as input for AI systems performing tasks like object recognition or segmentation, rather than being watched by humans. It is therefore useful to optimize the encoder for a downstream task instead of for perceptual image quality. However, a major challenge is how to combine such downstream optimization with existing standard video encoders, which are highly efficient and popular. Here, we address this challenge by controlling the Quantization Parameters (QPs) at the macro-block level to optimize the downstream task. This granular control allows us to prioritize encoding for task-relevant regions within each frame. We formulate this optimization problem as a Reinforcement Learning (RL) task, where the agent learns to balance long-term implications of choosing QPs on both task performance and bit-rate constraints. Notably, our policy does not require the downstream task as an input during inference, making it suitable for streaming applications and edge devices such as vehicles. We demonstrate significant improvements in two tasks, car detection, and ROI (saliency) encoding. Our approach improves task performance for a given bit rate compared to traditional task agnostic encoding methods, paving the way for more efficient task-aware video compression.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
