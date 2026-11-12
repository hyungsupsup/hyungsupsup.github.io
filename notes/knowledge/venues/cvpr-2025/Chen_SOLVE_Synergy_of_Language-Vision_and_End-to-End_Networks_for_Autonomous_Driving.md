---
title: "SOLVE: Synergy of Language-Vision and End-to-End Networks for Autonomous Driving"
tags: [cvpr2025, autonomous-driving, vla]
venue: CVPR 2025
arxiv: "2505.16805"
citations: 40
auto: true
---

> **TL;DR** SOLVE는 VLM과 end-to-end 자율주행 모델을 결합해 실시간 계획 성능과 해석 가능성을 높이는 프레임워크다.

**CVPR 2025** · Xuesong Chen, Linjiang Huang, Tao Ma, Rongyao Fang, Shaoshuai Shi, Hongsheng Li
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_SOLVE_Synergy_of_Language-Vision_and_End-to-End_Networks_for_Autonomous_Driving_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2505.16805) · 인용 40회

**주제:** Autonomous Driving · VLA

## 문제
기존 VLM 기반 자율주행 시스템은 계산량이 커서 효율적인 통합과 실시간 의사결정에 어려움을 겪는다.

## 핵심 아이디어
shared visual encoder를 통해 VLM과 E2E 모델이 feature level에서 지식을 공유하고, Trajectory Chain-of-Thought(T-CoT)로 궤적 예측을 점진적으로 정교화한다.

## 방법
SOLVE는 공유 visual encoder 기반으로 VLM과 E2E 구성요소를 상호작용시키고, T-CoT를 통해 궤적 예측의 불확실성을 줄인다. 또한 temporal decoupling 전략으로 VLM의 고품질 출력과 E2E의 실시간 성능을 비동기적으로 정렬한다.

## 결과
nuScenes dataset에서 SOLVE는 궤적 예측 정확도가 크게 향상됨을 보여 더 견고하고 신뢰할 수 있는 자율주행 시스템 가능성을 제시한다.

## 초록 (원문)
The integration of Vision-Language Models (VLMs) into autonomous driving systems has shown promise in addressing key challenges such as learning complexity, interpretability, and common-sense reasoning. However, existing approaches often struggle with efficient integration and real-time decision-making due to computational demands. In this paper, we introduce SOLVE, an innovative framework that synergizes VLMs with end-to-end (E2E) models to enhance autonomous vehicle planning. Our approach emphasizes knowledge sharing at the feature level through a shared visual encoder, enabling comprehensive interaction between VLM and E2E components. We propose a Trajectory Chain-of-Thought (T-CoT) paradigm, which progressively refines trajectory predictions, reducing uncertainty and improving accuracy. By employing a temporal decoupling strategy, SOLVE achieves efficient asynchronous cooperation, aligning high-quality VLM outputs with E2E real-time performance. Evaluated on the nuScenes dataset, our method demonstrates significant improvements in trajectory prediction accuracy, paving the way for more robust and reliable autonomous driving systems.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
