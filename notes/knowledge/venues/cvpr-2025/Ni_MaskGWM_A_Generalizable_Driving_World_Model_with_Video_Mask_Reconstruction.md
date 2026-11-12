---
title: "MaskGWM: A Generalizable Driving World Model with Video Mask Reconstruction"
tags: [cvpr2025, world-model, autonomous-driving]
venue: CVPR 2025
arxiv: "2502.11663"
citations: 42
auto: true
---

> **TL;DR** MaskGWM은 pixel-level video prediction과 MAE-style feature-level mask reconstruction을 결합한 일반화 가능한 driving world model이다.

**CVPR 2025** · Jingcheng Ni, Yuxin Guo, Yichen Liu, Rui Chen, Lewei Lu, Zehuan Wu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ni_MaskGWM_A_Generalizable_Driving_World_Model_with_Video_Mask_Reconstruction_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2502.11663) · 인용 42회

**주제:** World Model · Autonomous Driving

## 문제
기존 driving world model은 주로 pixel-level video prediction에 의존해 예측 가능한 시간 길이와 일반화 성능에 한계가 있다.

## 핵심 아이디어
pixel-level generation loss와 MAE-style feature-level context learning을 결합하고, diffusion process에 맞춘 mask token과 spatial-temporal row-wise mask를 도입한다.

## 방법
확장 가능한 Diffusion Transformer (DiT)에 mask construction task를 추가해 학습한다. diffusion-related mask token으로 mask reconstruction과 generative diffusion 간의 모호한 관계를 처리하고, row-wise mask를 shifted self-attention에 적용해 spatial-temporal 영역으로 확장하며 row-wise cross-view module로 multi-view를 정렬한다. MaskGWM-long은 long-horizon prediction, MaskGWM-mview는 multi-view generation에 초점을 둔다.

## 결과
NuScenes 일반 검증, OpenDV-2K long-horizon rollout, Waymo zero-shot 검증에서 제안 방법이 최신 driving world model을 notably 능가하는 성능을 보인다.

## 초록 (원문)
World models that forecast environmental changes from actions are vital for autonomous driving models with strong generalization. The prevailing driving world model mainly build on pixel-level video prediction model. Although these models can produce high-fidelity video sequences with advanced diffusion-based generator, they are constrained by their predictive duration and overall generalization capabilities. In this paper, we explore to solve this problem by combining pixel-level generation loss with MAE-style feature-level context learning. In particular, we instantiate this target with three key design: (1) A more scalable Diffusion Transformer (DiT) structure trained with extra mask construction task. (2) we devise diffusion-related mask tokens to deal with the fuzzy relations between mask reconstruction and generative diffusion process. (3) we extend mask construction task to spatial-temporal domain by utilizing row-wise mask for shifted self-attention rather than masked self-attention in MAE. Then, we adopt a row-wise cross-view module to align with this mask design. Based on above improvement, we propose MaskGWM: a Generalizable driving World Model embodied with Video Mask reconstruction. Our model contains two variants: MaskGWM-long, focusing on long-horizon prediction, and MaskGWM-mview, dedicated to multi-view generation.Comprehensive experiments on standard benchmarks validate the effectiveness of the proposed method, which contain normal validation of Nuscene dataset, long-horizon rollout of OpenDV-2K dataset and zero-shot validation of Waymo dataset. Quantitative metrics on these datasets show our method notably improving state-of-the-art driving world model.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
