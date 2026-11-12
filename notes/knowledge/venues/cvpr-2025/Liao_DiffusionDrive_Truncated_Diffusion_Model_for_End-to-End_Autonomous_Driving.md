---
title: "DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving"
tags: [cvpr2025, autonomous-driving, imitation-learning]
venue: CVPR 2025
arxiv: "2411.15139"
citations: 475
auto: true
---

> **TL;DR** DiffusionDrive는 truncated diffusion policy와 cascade diffusion decoder를 사용해 end-to-end 자율주행에서 실시간으로 다양한 주행 action을 생성하는 모델이다.

**CVPR 2025** · Bencheng Liao, Shaoyu Chen, Haoran Yin, Bo Jiang, Cheng Wang, Sixu Yan 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Liao_DiffusionDrive_Truncated_Diffusion_Model_for_End-to-End_Autonomous_Driving_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.15139) · 인용 475회

**주제:** Autonomous Driving · Imitation Learning

## 문제
기존 robotic diffusion policy는 많은 denoising step이 필요해 실시간 자율주행에 적용하기 어렵고, 복잡한 교통 장면에서 다양한 주행 action을 빠르게 생성하기도 어렵다.

## 핵심 아이디어
multi-mode anchor를 prior로 사용하고 diffusion schedule을 truncate하여 anchored Gaussian distribution에서 multi-mode 주행 action distribution으로 denoising하는 truncated diffusion policy를 제안한다.

## 방법
DiffusionDrive는 prior multi-mode anchor와 truncated diffusion schedule을 결합해 적은 step으로 주행 action을 생성한다. 또한 conditional scene context와의 상호작용을 높이기 위한 efficient cascade diffusion decoder를 설계한다.

## 결과
Vanilla diffusion policy 대비 denoising step을 10x 줄였으며 2 steps만으로 우수한 diversity와 quality를 달성한다. NAVSIM에서 aligned ResNet-34 backbone으로 88.1 PDMS를 기록해 새로운 record를 세웠고 NVIDIA 4090에서 45 FPS로 실시간 동작한다.

## 연결
- **기반 대표 논문:** DDPM, Diffusion Policy — [[knowledge/map|분야 지도]]

## 초록 (원문)
Recently, the diffusion model has emerged as a powerful generative technique for robotic policy learning, capable of modeling multi-mode action distributions. Leveraging its capability for end-to-end autonomous driving is a promising direction. However, the numerous denoising steps in the robotic diffusion policy and the more dynamic, open-world nature of traffic scenes pose substantial challenges for generating diverse driving actions at a real-time speed. To address these challenges, we propose a novel truncated diffusion policy that incorporates prior multi-mode anchors and truncates the diffusion schedule, enabling the model to learn denoising from anchored Gaussian distribution to the multi-mode driving action distribution. Additionally, we design an efficient cascade diffusion decoder for enhanced interaction with conditional scene context. The proposed model, DiffusionDrive, demonstrates 10x reduction in denoising steps compared to vanilla diffusion policy, delivering superior diversity and quality in just 2 steps. On the planning-oriented NAVSIM dataset, with the aligned ResNet-34 backbone, DiffusionDrive achieves 88.1 PDMS without bells and whistles, setting a new record, while running at a real-time speed of 45 FPS on an NVIDIA 4090. Qualitative results on challenging scenarios further confirm that DiffusionDrive can robustly generate diverse plausible driving actions.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
