---
title: "PhysicsGen: Can Generative Models Learn from Images to Predict Complex Physical Relations?"
tags: [cvpr2025, simulation-sim2real, dataset-benchmark]
venue: CVPR 2025
arxiv: "2503.05333"
citations: 4
auto: true
---

> **TL;DR** PhysicsGen은 300k image-pairs 데이터셋과 세 가지 물리 시뮬레이션 task benchmark를 통해 generative model이 이미지로부터 복잡한 물리 관계를 학습하고 미분방정식 기반 시뮬레이션을 대체할 수 있는지 평가한다.

**CVPR 2025** · Martin Spitznagel, Jan Vaillant, Janis Keuper
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Spitznagel_PhysicsGen_Can_Generative_Models_Learn_from_Images_to_Predict_Complex_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.05333) · 인용 4회

**주제:** Simulation & Sim2Real · Dataset & Benchmark

## 문제
Generative model의 image-to-image 변환은 발전했지만, 물리 시뮬레이션에서 물리적 정확성을 얼마나 보장할 수 있는지는 체계적으로 검증되지 않았다.

## 핵심 아이디어
300k image-pairs 데이터셋과 세 가지 물리 시뮬레이션 task에 대한 baseline 평가를 제공하여, 복잡한 물리 관계 학습 가능성과 미분방정식 기반 시뮬레이션 대체 시 speedup을 함께 조사하는 benchmark를 제안한다.

## 방법
입력-출력 이미지 쌍으로 구성된 300k 데이터셋을 구축하고 세 가지 물리 시뮬레이션 task에서 현재 generative model들을 baseline으로 평가한다. 각 모델이 복잡한 물리 관계를 학습하는지와 미분방정식 기반 시뮬레이션 대비 어느 정도 speedup을 얻는지를 분석한다.

## 결과
Baseline 평가는 높은 speedup 가능성을 보였지만 물리적 정확성 측면에서는 강한 한계를 드러냈으며, 이는 물리적 정확성을 강제하는 새로운 방법의 필요성을 보여준다.

## 연결
- **기반 대표 논문:** DDPM — [[knowledge/map|분야 지도]]

## 초록 (원문)
The image-to-image translation abilities of generative learning models have recently made significant progress in the estimation of complex (steered) mappings between image distributions. While appearance based tasks like image in-painting or style transfer have been studied at length, we propose to investigate the potential of generative models in the context of physical simulations. Providing a dataset of 300k image-pairs and baseline evaluations for three different physical simulation tasks, we propose a benchmark to investigate the following research questions: i) are generative models able to learn complex physical relations from input-output image pairs? ii) what speedups can be achieved by replacing differential equation based simulations? While baseline evaluations of different current models show the potential for high speedups (ii), these results also show strong limitations toward the physical correctness (i). This underlines the need for new methods to enforce physical correctness.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
