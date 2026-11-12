---
title: "PhysVLM: Enabling Visual Language Models to Understand Robotic Physical Reachability"
tags: [cvpr2025, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2503.08481"
citations: 36
auto: true
---

> **TL;DR** 로봇의 물리적 도달 가능성을 통합 표현한 S-P Map과 이를 처리하는 PhysVLM을 제안해 embodied visual reasoning 성능을 높인다.

**CVPR 2025** · Weijie Zhou, Manli Tao, Chaoyang Zhao, Haiyun Guo, Honghui Dong, Ming Tang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhou_PhysVLM_Enabling_Visual_Language_Models_to_Understand_Robotic_Physical_Reachability_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.08481) · 인용 36회

**주제:** Embodied Perception · Dataset & Benchmark

## 문제
기존 VLM은 환경 인지는 잘하지만 로봇의 physical reachability를 이해하지 못해 embodied visual reasoning에서 부정확하거나 실행 불가능한 답을 생성한다.

## 핵심 아이디어
다양한 로봇 구성에 독립적인 Space-Physical Reachability Map(S-P Map)으로 reachability를 일반화하고, 추가 feature encoder로 VLM에 통합해 일반 vision-language 능력을 유지한다.

## 방법
S-P Map은 로봇의 물리적 도달 가능성을 일반화된 공간 표현으로 추상화한다. PhysVLM은 기존 VLM에 S-P Map 처리용 feature encoder를 추가해 physical reachability를 추론한다. Phys100K 데이터셋과 EQA-phys 벤치마크로 학습 및 평가한다.

## 결과
EQA-phys에서 GPT-4o 대비 14% 향상되었고 RoboVQA-val과 OpenEQA에서 RoboMamba 및 SpatialVLM을 능가했으며, S-P Map을 GPT-4o-mini에 통합하면 7.1% 성능 향상을 보인다.

## 연결
- **기반 대표 논문:** Code as Policies, PaLM-E, SayCan — [[knowledge/map|분야 지도]]

## 초록 (원문)
Understanding the environment and a robot's physical reachability is crucial for task execution. While state-of-the-art vision-language models (VLMs) excel in environmental perception, they often generate inaccurate or impractical responses in embodied visual reasoning tasks due to a lack of understanding of robotic physical reachability. To address this issue, we propose a unified representation of physical reachability across diverse robots, i.e., Space-Physical Reachability Map (S-P Map), and PhysVLM, a vision-language model that integrates this reachability information into visual reasoning. Specifically, the S-P Map abstracts a robot's physical reachability into a generalized spatial representation, independent of specific robot configurations, allowing the model to focus on reachability features rather than robot-specific parameters. Subsequently, PhysVLM extends traditional VLM architectures by incorporating an additional feature encoder to process the S-P Map, enabling the model to reason about physical reachability without compromising its general vision-language capabilities. To train and evaluate PhysVLM, we constructed a large-scale multi-robot dataset, Phys100K, and a challenging benchmark, EQA-phys, which includes tasks for six different robots in both simulated and real-world environments. Experimental results demonstrate that PhysVLM outperforms existing models, achieving a 14% improvement over GPT-4o on EQA-phys and surpassing advanced embodied VLMs such as RoboMamba and SpatialVLM on the RoboVQA-val and OpenEQA benchmarks. Additionally, the S-P Map shows strong compatibility with various VLMs, and its integration into GPT-4o-mini yields a 7.1% performance improvement.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
