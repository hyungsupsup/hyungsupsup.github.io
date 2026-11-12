---
title: "GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation in End-to-End Autonomous Driving"
tags: [cvpr2025, autonomous-driving]
venue: CVPR 2025
arxiv: "2503.05689"
citations: 178
auto: true
---

> **TL;DR** GoalFlow는 goal point와 Flow Matching을 활용해 end-to-end 자율주행에서 고품질 multimodal trajectory를 생성하는 방법이다.

**CVPR 2025** · Zebin Xing, Xingyu Zhang, Yang Hu, Bo Jiang, Tong He, Qian Zhang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Xing_GoalFlow_Goal-Driven_Flow_Matching_for_Multimodal_Trajectories_Generation_in_End-to-End_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.05689) · 인용 178회

**주제:** Autonomous Driving

## 문제
자율주행에서는 단일 정답 trajectory가 거의 없지만, 기존 multimodal trajectory 모델링은 trajectory divergence와 guidance-장면 정보 불일치로 인해 trajectory 선택이 복잡하고 품질이 저하된다.

## 핵심 아이디어
GoalFlow는 scene 정보 기반 scoring으로 candidate goal point를 선택해 생성 과정을 제약하고, Flow Matching과 refined scoring을 결합해 multimodal trajectory를 효율적으로 생성·선택한다.

## 방법
GoalFlow는 end-to-end 자율주행 방식으로, scene 정보를 바탕으로 가장 적절한 goal point를 scoring하여 선택하고 이를 조건으로 trajectory 생성을 제약한다. 이후 Flow Matching을 사용해 multimodal trajectory를 생성하고, refined scoring mechanism으로 candidate 중 최적 trajectory를 선택한다.

## 결과
Navsim에서 GoalFlow는 PDMS 90.3을 달성해 다른 방법들을 크게 능가하며 state-of-the-art 성능을 보였고, diffusion-policy 기반 방법들과 비교해 단일 denoising step만으로 우수한 성능을 얻는다.

## 연결
- **기반 대표 논문:** DDPM, Diffusion Policy — [[knowledge/map|분야 지도]]

## 초록 (원문)
We propose GoalFlow, an end-to-end autonomous driving method for generating high-quality multimodal trajectories. In autonomous driving scenarios, there is rarely a single suitable trajectory. Recent methods have increasingly focused on modeling multimodal trajectory distributions. However, they suffer from trajectory selection complexity and reduced trajectory quality due to high trajectory divergence and inconsistencies between guidance and scene information. To address these issues, we introduce GoalFlow, a novel method that effectively constrains the generative process to produce high-quality, multimodal trajectories. To resolve the trajectory divergence problem inherent in diffusion-based methods, GoalFlow constrains the generated trajectories by introducing a goal point. GoalFlow establishes a novel scoring mechanism that selects the most appropriate goal point from the candidate points based on scene information. Furthermore, GoalFlow employs an efficient generative method, Flow Matching, to generate multimodal trajectories, and incorporates a refined scoring mechanism to select the optimal trajectory from the candidates. Our experimental results, validated on the Navsim, demonstrate that GoalFlow achieves state-of-the-art performance, delivering robust multimodal trajectories for autonomous driving. GoalFlow achieved PDMS of 90.3, significantly surpassing other methods. Compared with other diffusion-policy-based methods, our approach requires only a single denoising step to obtain excellent performance. The code is available at https://github.com/YvanYin/GoalFlow.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
