---
title: "BIP3D: Bridging 2D Images and 3D Perception for Embodied Intelligence"
tags: [cvpr2025, embodied-perception]
venue: CVPR 2025
arxiv: "2411.14869"
citations: 12
auto: true
---

> **TL;DR** BIP3D는 이미지 중심 특징과 명시적 3D 위치 인코딩을 활용해 embodied intelligence용 3D 인식을 향상시키는 모델이다.

**CVPR 2025** · Xuewu Lin, Tianwei Lin, Lichao Huang, Hongyu Xie, Zhizhong Su
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_BIP3D_Bridging_2D_Images_and_3D_Perception_for_Embodied_Intelligence_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.14869) · 인용 12회

**주제:** Embodied Perception

## 문제
기존 embodied 3D 인식은 주로 point cloud에 의존해 sparsity, noise, data scarcity로 인해 성능이 제한된다. 이 논문은 이러한 point-centric 한계를 극복하는 image-centric 3D 인식 모델을 제안한다.

## 핵심 아이디어
pre-trained 2D vision foundation model의 풍부한 이미지 특징과 explicit 3D position encoding을 결합하고, spatial enhancer module을 도입해 semantic 및 spatial 이해를 동시에 강화한다.

## 방법
BIP3D는 multi-view 이미지 특징을 pre-trained 2D vision foundation model로 추출해 semantic understanding을 높이고, spatial enhancer module로 공간 이해를 개선한다. 이를 통해 multi-view, multi-modal feature fusion과 end-to-end 3D perception을 수행한다.

## 결과
EmbodiedScan benchmark에서 BIP3D는 3D detection task에서 5.69%, 3D visual grounding task에서 15.25%의 성능 향상을 달성하며 state-of-the-art를 outperforms한다.

## 초록 (원문)
In embodied intelligence systems, a key component is 3D perception algorithm, which enables agents to understand their surrounding environments. Previous algorithms primarily rely on point cloud, which, despite offering precise geometric information, still constrain perception performance due to inherent sparsity, noise, and data scarcity. In this work, we introduce a novel image-centric 3D perception model, BIP3D, which leverages expressive image features with explicit 3D position encoding to overcome the limitations of point-centric methods. Specifically, we leverage pre-trained 2D vision foundation models to enhance semantic understanding, and introduce a spatial enhancer module to improve spatial understanding. Together, these modules enable BIP3D to achieve multi-view, multi-modal feature fusion and end-to-end 3D perception. In our experiments, BIP3D outperforms current state-of-the-art results on the EmbodiedScan benchmark, achieving improvements of 5.69% in the 3D detection task and 15.25% in the 3D visual grounding task. Code has been released at https://github.com/HorizonRobotics/BIP3D.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
