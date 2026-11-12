---
title: "Unleashing the Potential of Multi-modal Foundation Models and Video Diffusion for 4D Dynamic Physical Scene Simulation"
tags: [cvpr2025, simulation-sim2real, world-model]
venue: CVPR 2025
arxiv: "2411.14423"
citations: 41
auto: true
---

> **TL;DR** PhysFlow는 multi-modal foundation models와 video diffusion을 활용해 재료 물성과 객체 상호작용을 반영한 4D 동적 장면 시뮬레이션을 수행한다.

**CVPR 2025** · Zhuoman Liu, Weicai Ye, Yan Luximon, Pengfei Wan, Di Zhang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_Unleashing_the_Potential_of_Multi-modal_Foundation_Models_and_Video_Diffusion_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.14423) · 인용 41회

**주제:** Simulation & Sim2Real · World Model

## 문제
기존 동적 장면 시뮬레이션은 제한된 기본 재료 유형과 예측 가능한 파라미터에 국한되어 실제 세계 재료의 복잡성을 표현하기 어렵다.

## 핵심 아이디어
이미지 질의를 통해 재료 유형과 초기 물성 파라미터를 얻고, differentiable MPM과 optical flow guidance를 사용한 video diffusion으로 물성을 정교화하는 통합 프레임워크를 제안한다. render loss나 Score Distillation Sampling (SDS) loss 대신 optical flow guidance를 사용하는 점이 차별점이다.

## 방법
multi-modal models로 material types를 식별하고 material parameters를 초기화하며, 동시에 3D Gaussian splats로 상세한 장면 표현을 추론한다. 이후 video diffusion과 differentiable Material Point Method (MPM), optical flow guidance를 결합해 material parameters를 refine한다. 이 통합 프레임워크가 실제 시나리오의 동적 상호작용을 예측하고 사실적으로 시뮬레이션하도록 한다.

## 결과
실제 시나리오의 동적 상호작용을 보다 정확하고 유연하게 예측 및 시뮬레이션할 수 있음을 주장하며, physics-based simulations의 정확도와 유연성을 향상시킨다.

## 초록 (원문)
Realistic simulation of dynamic scenes requires accurately capturing diverse material properties and modeling complex object interactions grounded in physical principles. However, existing methods are constrained to basic material types with limited predictable parameters, making them insufficient to represent the complexity of real-world materials. We introduce PhysFlow, a novel approach that leverages multi-modal foundation models and video diffusion to achieve enhanced 4D dynamic scene simulation. Our method utilizes multi-modal models to identify material types and initialize material parameters through image queries, while simultaneously inferring 3D Gaussian splats for detailed scene representation. We further refine these material parameters using video diffusion with a differentiable Material Point Method (MPM) and optical flow guidance rather than render loss or Score Distillation Sampling (SDS) loss. This integrated framework enables accurate prediction and realistic simulation of dynamic interactions in real-world scenarios, advancing both accuracy and flexibility in physics-based simulations.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
