---
title: "RoboBrain: A Unified Brain Model for Robotic Manipulation from Abstract to Concrete"
tags: [cvpr2025, vla, manipulation, dataset-benchmark]
venue: CVPR 2025
arxiv: "2502.21257"
citations: 225
auto: true
---

> **TL;DR** RoboBrain은 로봇 조작을 위한 planning, affordance perception, trajectory prediction 능력을 강화한 MLLM 기반 통합 brain model이다.

**CVPR 2025** · Yuheng Ji, Huajie Tan, Jiayu Shi, Xiaoshuai Hao, Yuan Zhang, Hengyuan Zhang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ji_RoboBrain_A_Unified_Brain_Model_for_Robotic_Manipulation_from_Abstract_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2502.21257) · 인용 225회

**주제:** VLA · Manipulation · Dataset & Benchmark

## 문제
기존 MLLM은 long-horizon manipulation에 필요한 Planning Capability, Affordance Perception, Trajectory Prediction이 부족해 로봇 시나리오에 적용하기 어렵다.

## 핵심 아이디어
task planning, object affordance, end-effector trajectory를 포함한 ShareRobot 데이터셋을 구축하고, 이를 바탕으로 robotic data와 general multi-modal data를 결합해 RoboBrain을 학습한다.

## 방법
ShareRobot은 multi-dimensional 정보를 라벨링하고 세 명의 human annotator가 정제한 heterogeneous dataset이다. RoboBrain은 이 데이터와 general multi-modal data를 함께 사용하며, multi-stage training strategy와 long videos, high-resolution images를 활용해 manipulation 능력을 향상한다.

## 결과
Extensive experiments에서 RoboBrain은 다양한 robotic tasks에서 state-of-the-art 성능을 달성해 robotic brain capabilities 향상 가능성을 보였다.

## 연결
- **기반 대표 논문:** DROID (데이터셋), Open X-Embodiment (데이터셋), OpenVLA, PaLM-E, RT-1, RT-2, SayCan — [[knowledge/map|분야 지도]]

## 초록 (원문)
Recent advancements in Multimodal Large Language Models (MLLMs) have shown remarkable capabilities across various multimodal contexts. However, their application in robotic scenarios, particularly for long-horizon manipulation tasks, reveals significant limitations. These limitations arise from the current MLLMs lacking three essential robotic brain capabilities: Planning Capability, which involves decomposing complex manipulation instructions into manageable sub-tasks; Affordance Perception, the ability to recognize and interpret the affordances of interactive objects; and Trajectory Prediction, the foresight to anticipate the complete manipulation trajectory necessary for successful execution. To enhance the robotic brain's core capabilities from abstract to concrete, we introduce ShareRobot, a high-quality heterogeneous dataset that labels multi-dimensional information such as task planning, object affordance, and end-effector trajectory. ShareRobot's diversity and accuracy have been meticulously refined by three human annotators. Building on this dataset, we developed RoboBrain, an MLLM-based model that combines robotic and general multi-modal data, utilizes a multi-stage training strategy, and incorporates long videos and high-resolution images to improve its robotic manipulation capabilities.Extensive experiments demonstrate that RoboBrain achieves state-of-the-art performance across various obotic tasks, highlighting its potential to advance robotic brain capabilities.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
