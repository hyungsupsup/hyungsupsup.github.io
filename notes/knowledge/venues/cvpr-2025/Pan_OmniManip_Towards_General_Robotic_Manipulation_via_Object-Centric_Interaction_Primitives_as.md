---
title: "OmniManip: Towards General Robotic Manipulation via Object-Centric Interaction Primitives as Spatial Constraints"
tags: [cvpr2025, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2501.03841"
citations: 118
auto: true
---

> **TL;DR** VLM의 상식 추론과 정밀 조작 사이를 객체 중심 상호작용 프리미티브로 연결한 open-vocabulary 로봇 조작 시스템을 제안한다.

**CVPR 2025** · Mingjie Pan, Jiyao Zhang, Tianshu Wu, Yinghao Zhao, Wenlong Gao, Hao Dong
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Pan_OmniManip_Towards_General_Robotic_Manipulation_via_Object-Centric_Interaction_Primitives_as_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.03841) · 인용 118회

**주제:** Manipulation · Embodied Perception

## 문제
비정형 환경에서 일반 로봇 조작을 수행하려면 VLM의 고수준 상식 추론과 정밀 조작에 필요한 세밀한 3D 공간 이해를 결합해야 하지만, VLA fine-tuning은 데이터 수집 비용과 일반화 문제가 있다.

## 핵심 아이디어
객체의 functional affordances로 정의되는 canonical space에서 points와 directions 같은 interaction primitives를 표현해, VLM의 상식 추론을 3D 공간 제약으로 변환하는 객체 중심 표현을 사용한다.

## 방법
고수준 루프에서는 primitive resampling, interaction rendering, VLM checking을 통해 계획하고, 저수준 루프에서는 6D pose tracking으로 실행하는 dual closed-loop 구조를 사용한다. 이 설계는 VLM fine-tuning 없이 실시간 제어와 zero-shot 일반화를 가능하게 한다.

## 결과
다양한 로봇 조작 작업에서 강한 zero-shot 일반화를 보였으며, 대규모 데이터 생성 자동화 가능성을 시사한다.

## 연결
- **기반 대표 논문:** Diffusion Policy, OpenVLA, PaLM-E, RT-1, RT-2, UMI — Universal Manipulation Interface — [[knowledge/map|분야 지도]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Long_CheckManual_A_New_Challenge_and_Benchmark_for_Manual-based_Appliance_Manipulation|CheckManual: A New Challenge and Benchmark for Manual-based Appliance Manipulation]]

## 초록 (원문)
The development of general robotic systems capable of manipulating in unstructured environments is a significant challenge. While Vision-Language Models(VLM) excel in high-level commonsense reasoning, they lack the fine-grained 3D spatial understanding required for precise manipulation tasks. Fine-tuning VLM on robotic datasets to create Vision-Language-Action Models(VLA) is a potential solution, but it is hindered by high data collection costs and generalization issues. To address these challenges, we propose a novel object-centric representation that bridges the gap between VLM's high-level reasoning and the low-level precision required for manipulation. Our key insight is that an object's canonical space, defined by its functional affordances, provides a structured and semantically meaningful way to describe interaction primitives, such as points and directions. These primitives act as a bridge, translating VLM's commonsense reasoning into actionable 3D spatial constraints. In this context, we introduce a dual closed-loop, open-vocabulary robotic manipulation system: one loop for high-level planning through primitive resampling, interaction rendering and VLM checking, and another for low-level execution via 6D pose tracking. This design ensures robust, real-time control without requiring VLM fine-tuning. Extensive experiments demonstrate strong zero-shot generalization across diverse robotic manipulation tasks, highlighting the potential of this approach for automating large-scale data generation.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
