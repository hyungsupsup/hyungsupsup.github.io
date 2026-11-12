---
title: "RoboGround: Robotic Manipulation with Grounded Vision-Language Priors"
tags: [cvpr2025, manipulation, vla, embodied-perception]
venue: CVPR 2025
arxiv: "2504.21530"
citations: 77
auto: true
---

> **TL;DR** Grounding mask를 중간 표현으로 사용해 vision-language prior를 로봇 조작 정책에 연결하는 RoboGround를 제안한다.

**CVPR 2025** · Haifeng Huang, Xinyi Chen, Yilun Chen, Hao Li, Xiaoshen Han, Zehan Wang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Huang_RoboGround_Robotic_Manipulation_with_Grounded_Vision-Language_Priors_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.21530) · 인용 77회

**주제:** Manipulation · VLA · Embodied Perception

## 문제
로봇 조작 정책의 일반화 성능을 높이기 위한 효과적인 중간 표현과 대규모 학습 데이터 확보가 필요하다.

## 핵심 아이디어
Grounding mask를 중간 표현으로 사용해 목표 객체와 배치 영역에 대한 공간적 안내와 객체 형상 정보를 동시에 제공하고, 대규모 vision-language model의 grounding 일반화 능력을 활용한다.

## 방법
RoboGround는 grounding mask를 정책 네트워크에 입력하여 객체 조작을 안내하는 grounding-aware 조작 정책이다. 또한 다양한 객체와 지시문을 포함한 대규모 시뮬레이션 데이터를 자동 생성하는 파이프라인을 제안한다. 이를 통해 정책이 공간적 목표와 객체 속성을 더 잘 활용하도록 학습한다.

## 결과
광범위한 실험에서 제안한 데이터셋의 가치와 grounding mask 중간 안내의 효과를 보였으며, 로봇 정책의 일반화 능력을 크게 향상시켰다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, Diffusion Policy, OpenVLA, RT-2 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Recent advancements in robotic manipulation have highlighted the potential of intermediate representations for improving policy generalization. In this work, we explore grounding masks as an effective intermediate representation, balancing two key advantages: (1) effective spatial guidance that specifies target objects and placement areas while also conveying information about object shape and size, and (2) broad generalization potential driven by large-scale vision-language models pretrained on diverse grounding datasets. We introduce \method, a grounding-aware robotic manipulation policy that leverages grounding masks as an intermediate representation to guide policy networks in object manipulation tasks. To further explore and enhance generalization, we propose an automated pipeline for generating large-scale, simulated data with a diverse set of objects and instructions. Extensive experiments show the value of our dataset and the effectiveness of grounding masks as intermediate guidance, significantly enhancing the generalization abilities of robot policies.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
