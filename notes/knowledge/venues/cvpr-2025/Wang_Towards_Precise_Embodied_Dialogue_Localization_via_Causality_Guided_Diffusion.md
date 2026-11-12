---
title: "Towards Precise Embodied Dialogue Localization via Causality Guided Diffusion"
tags: [cvpr2025, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** CGD는 causality guided diffusion으로 vision-dialogue 기반 embodied localization의 좌표 분포를 직접 모델링해 정확도를 높이는 프레임워크다.

**CVPR 2025** · Haoyu Wang, Le Wang, Sanping Zhou, Jingyi Tian, Zheng Qin, Yabing Wang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Towards_Precise_Embodied_Dialogue_Localization_via_Causality_Guided_Diffusion_CVPR_2025_paper.html)

**주제:** Embodied Perception

## 문제
기존 embodied localization 방법은 heatmap 예측을 image translation 문제로 다뤄 해상도에 크게 의존하고 정확도가 부족하며, confounder로 인한 spurious correlation 문제가 있다.

## 핵심 아이디어
encoder-decoder 기반 heatmap 예측 대신 denoising network로 좌표를 직접 regress하고, diffusion 과정에 BDA와 FDA causal adjustment를 통합해 confounder와 spurious correlation을 줄인다.

## 방법
CGD는 denoising network가 좌표 분포를 회귀하도록 하며, diffusion process 중 back-door adjustment와 front-door adjustment를 적용한다. Causal adjustment로 denoising을 guide해 intensity를 유연하게 제어하고 diffusion model과 통합한다. 이를 통해 고해상도 의존성을 줄이면서 unbiased learning을 유도한다.

## 결과
실험 결과 CGD는 모든 metric에서 state-of-the-art 방법을 능가하며, multi-shot setting에서도 일관되게 높은 정확도를 달성한다.

## 초록 (원문)
Embodied localization based on vision and natural language dialogues presents a persistent challenge in embodied intelligence. Existing methods often approach this task as an image translation problem, leveraging encoder-decoder architectures to predict heatmaps. However, these methods frequently experience a deficiency in accuracy, largely due to their heavy reliance on resolution. To address this issue, we introduce CGD, a novel framework that utilizes causality guided diffusion model to directly model coordinate distributions. Specifically, CGD employs a denoising network to regress coordinates, while integrating causal learning modules, namely back-door adjustment (BDA) and front-door adjustment (FDA) to mitigate confounders during the diffusion process. This approach reduces the dependency on high resolution for improving accuracy, while effectively minimizing spurious correlations, thereby promoting unbiased learning. By guiding the denoising process with causal adjustments, CGD offers flexible control over intensity, ensuring seamless integration with diffusion models. Experimental results demonstrate that CGD outperforms state-of-the-art methods across all metrics. Additionally, we also evaluate CGD in a multi-shot setting, achieving consistently high accuracy.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
