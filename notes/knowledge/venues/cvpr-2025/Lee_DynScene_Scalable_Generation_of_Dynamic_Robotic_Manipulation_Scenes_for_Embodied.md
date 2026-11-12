---
title: "DynScene: Scalable Generation of Dynamic Robotic Manipulation Scenes for Embodied AI"
tags: [cvpr2025, dataset-benchmark, manipulation]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** DynScene은 텍스트 지시로부터 동적 로봇 조작 장면과 action trajectory를 생성하는 diffusion 기반 프레임워크다.

**CVPR 2025** · Sangmin Lee, Sungyong Park, Heewon Kim
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lee_DynScene_Scalable_Generation_of_Dynamic_Robotic_Manipulation_Scenes_for_Embodied_CVPR_2025_paper.html)

**주제:** Dataset & Benchmark · Manipulation

## 문제
기존 로봇 조작 데이터 수집은 느리고 비싸며 수작업 의존도가 높아, 현실적 객체 상호작용과 물리 역학을 반영한 대규모 고품질 데이터셋 확보가 어렵다.

## 핵심 아이디어
정적 장면 합성과 action trajectory 생성을 두 단계로 분해하고, scene refinement와 residual action representation을 통해 하나의 정적 구성에서 다양한 궤적을 생성한다.

## 방법
DynScene은 textual instruction에서 출발해 먼저 static scene을 합성하고 이어서 action trajectory를 생성한다. layout sampling과 quaternion quantization으로 장면을 refine하며, residual action representation으로 action augmentation을 수행해 다양한 trajectory를 만든다.

## 결과
DynScene은 human-crafted data 대비 26.8x faster generation, 1.84x higher accuracy, 28% greater action diversity를 달성했고, DynScene으로 학습한 agents는 복잡한 manipulation tasks에서 최대 19.4% higher success rates를 보였다.

## 초록 (원문)
Robotic manipulation in embodied AI critically depends on large-scale, high-quality datasets that reflect realistic object interactions and physical dynamics. However, existing data collection pipelines are often slow, expensive, and heavily reliant on manual efforts. We present DynScene, a diffusion-based framework for generating dynamic robotic manipulation scenes directly from textual instructions. Unlike prior methods that focus solely on static environments or isolated robot actions, DynScene decomposes the generation into two phases static scene synthesis and action trajectory generation allowing fine-grained control and diversity. Our model enhances realism and physical feasibility through scene refinement (layout sampling, quaternion quantization) and leverages residual action representation to enable action augmentation, generating multiple diverse trajectories from a single static configuration. Experiments show DynScene achieves 26.8x faster generation, 1.84x higher accuracy, and 28% greater action diversity than human-crafted data. Furthermore, agents trained with DynScene exhibit up to 19.4% higher success rates across complex manipulation tasks. Our approach paves the way for scalable, automated dataset generation in robot learning.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
