---
title: "DexGrasp Anything: Towards Universal Robotic Dexterous Grasping with Physics Awareness"
tags: [cvpr2025, manipulation, dataset-benchmark]
venue: CVPR 2025
arxiv: "2503.08257"
citations: 82
auto: true
---

> **TL;DR** 물리 제약을 diffusion 기반 생성 모델의 학습과 샘플링에 통합해 다양한 객체에 대한 범용 dexterous grasping을 수행하는 DexGrasp Anything과 3.4M 규모의 새로운 grasping 데이터셋을 제안한다.

**CVPR 2025** · Yiming Zhong, Qi Jiang, Jingyi Yu, Yuexin Ma
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhong_DexGrasp_Anything_Towards_Universal_Robotic_Dexterous_Grasping_with_Physics_Awareness_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.08257) · 인용 82회

**주제:** Manipulation · Dataset & Benchmark

## 문제
Dexterous hand는 자유도가 높고 객체 다양성이 커서, 로봇이 임의의 객체에 대해 고품질이고 실제로 사용 가능한 grasping pose를 안정적으로 생성하기 어렵다.

## 핵심 아이디어
기존 diffusion 기반 grasping 생성과 달리, 물리적 제약을 학습 단계와 샘플링 단계 모두에 효과적으로 통합하여 물리적으로 타당한 grasping pose를 생성한다.

## 방법
Diffusion-based generative model을 사용해 dexterous grasping pose를 생성하며, 학습과 샘플링 과정에 physical constraints를 반영한다. 또한 15k개 이상의 객체에 대해 3.4 million개 이상의 다양한 grasping pose를 포함한 새로운 dexterous grasping dataset을 구축한다.

## 결과
제안 방법은 거의 모든 open dataset에서 state-of-the-art 성능을 달성했으며, 3.4 million개 이상의 grasping pose와 15k개 이상의 객체를 포함한 dataset을 공개할 예정이다.

## 연결
- **기반 대표 논문:** DDPM, Isaac Gym — [[knowledge/map|분야 지도]]

## 초록 (원문)
A dexterous hand capable of grasping any object is essential for the development of general-purpose embodied intelligent robots. However, due to the high degree of freedom in dexterous hands and the vast diversity of objects, generating high-quality, usable grasping poses in a robust manner is a significant challenge. In this paper, we introduce DexGrasp Anything, a method that effectively integrates physical constraints into both the training and sampling phases of a diffusion-based generative model, achieving state-of-the-art performance across nearly all open datasets. Additionally, we present a new dexterous grasping dataset containing over 3.4 million diverse grasping poses for more than 15k different objects, demonstrating its potential to advance universal dexterous grasping. The code of our method and our dataset will be publicly released soon.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
