---
title: "VisionPAD: A Vision-Centric Pre-training Paradigm for Autonomous Driving"
tags: [cvpr2025, autonomous-driving, embodied-perception, simulation-sim2real]
venue: CVPR 2025
arxiv: "2411.14716"
citations: 23
auto: true
---

> **TL;DR** VisionPAD는 이미지만을 감독 신호로 사용하는 3D Gaussian Splatting 기반의 자율주행용 자기지도 사전학습 패러다임이다.

**CVPR 2025** · Haiming Zhang, Wending Zhou, Yiyao Zhu, Xu Yan, Jiantao Gao, Dongfeng Bai 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_VisionPAD_A_Vision-Centric_Pre-training_Paradigm_for_Autonomous_Driving_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.14716) · 인용 23회

**주제:** Autonomous Driving · Embodied Perception · Simulation & Sim2Real

## 문제
자율주행의 vision-centric 알고리즘은 값비싼 레이블과 명시적 depth 감독에 의존하는 사전학습 방식에 의존해 왔다. 본 논문은 순수 이미지 감독만으로 3D 표현을 효과적으로 학습하는 방법을 다룬다.

## 핵심 아이디어
명시적 depth 감독을 쓰는 neural rendering 대신 더 효율적인 3D Gaussian Splatting으로 다시점 표현을 재구성하고, 복셀 속도 추정과 다중 프레임 photometric consistency를 자기지도 방식으로 결합한다.

## 방법
복셀을 인접 프레임으로 warping하고 렌더링 출력을 감독하여 순차 데이터의 motion cue를 학습한다. 또한 렌더링된 depth와 상대 pose를 기반으로 인접 프레임을 현재 프레임에 투영하는 multi-frame photometric consistency를 적용해 3D 기하 표현을 강화한다.

## 결과
자율주행 데이터셋 실험에서 3D object detection, occupancy prediction, map segmentation 성능을 크게 향상시켰으며, 기존 state-of-the-art 사전학습 전략을 상당한 차이로 능가했다.

## 초록 (원문)
This paper introduces VisionPAD, a novel self-supervised pre-training paradigm designed for vision-centric algorithms in autonomous driving. In contrast to previous approaches that employ neural rendering with explicit depth supervision, VisionPAD utilizes more efficient 3D Gaussian Splatting to reconstruct multi-view representations using only images as supervision. Specifically, we introduce a self-supervised method for voxel velocity estimation. By warping voxels to adjacent frames and supervising the rendered outputs, the model effectively learns motion cues in the sequential data. Furthermore, we adopt a multi-frame photometric consistency approach to enhance geometric perception. It projects adjacent frames to the current frame based on rendered depths and relative poses, boosting the 3D geometric representation through pure image supervision. Extensive experiments on autonomous driving datasets demonstrate that VisionPAD significantly improves performance in 3D object detection, occupancy prediction and map segmentation, surpassing state-of-the-art pre-training strategies by a considerable margin.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
