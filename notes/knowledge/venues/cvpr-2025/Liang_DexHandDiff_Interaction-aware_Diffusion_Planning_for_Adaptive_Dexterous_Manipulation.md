---
title: "DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation"
tags: [cvpr2025, manipulation]
venue: CVPR 2025
arxiv: "2411.18562"
citations: 33
auto: true
---

> **TL;DR** DexHandDiff는 접촉이 많은 dexterous manipulation을 위한 상호작용 인식 diffusion planning 프레임워크를 제안한다.

**CVPR 2025** · Zhixuan Liang, Yao Mu, Yixiao Wang, Tianxing Chen, Wenqi Shao, Wei Zhan 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Liang_DexHandDiff_Interaction-aware_Diffusion_Planning_for_Adaptive_Dexterous_Manipulation_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.18562) · 인용 33회

**주제:** Manipulation

## 문제
기존 diffusion 기반 planning은 hand contact 없이 object가 움직이는 비현실적인 ghost state를 만들거나 복잡한 sequential interaction에 적응하기 어렵다.

## 핵심 아이디어
pre-interaction contact alignment와 post-contact goal-directed control로 구성된 dual-phase diffusion process를 통해 joint state-action dynamics를 모델링하고, dynamics model 기반 dual guidance와 LLM 기반 자동 guidance function generation을 결합한다.

## 방법
DexHandDiff는 dual-phase diffusion으로 접촉 전 정렬과 접촉 후 목표 지향 제어를 순차적으로 모델링한다. 또한 dynamics model-based dual guidance를 사용하고 LLM으로 guidance function을 자동 생성해 language cue를 통한 다양한 goal adaptation을 가능하게 한다.

## 결과
door opening, pen and block re-orientation, object relocation, hammer striking 실험에서 training distribution 밖의 goal에 대해 기존 방법 대비 평균 성공률 59.2% vs. 29.5%를 달성했고, goal adaptive dexterous tasks에서는 평균 70.7% 성공률을 보였다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, Code as Policies, DDPM, Diffusion Policy — [[knowledge/map|분야 지도]]
- 인용함 → [[knowledge/venues/cvpr-2025/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object|G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation]]

## 초록 (원문)
Dexterous manipulation with contact-rich interactions is crucial for advanced robotics. While recent diffusion-based planning approaches show promise for simple manipulation tasks, they often produce unrealistic ghost states (e.g., the object automatically moves without hand contact) or lack adaptability when handling complex sequential interactions. In this work, we introduce DexHandDiff, an interaction-aware diffusion planning framework for adaptive dexterous manipulation. DexHandDiff models joint state-action dynamics through a dual-phase diffusion process which consists of pre-interaction contact alignment and post-contact goal-directed control, enabling goal-adaptive generalizable dexterous manipulation. Additionally, we incorporate dynamics model-based dual guidance and leverage large language models for automated guidance function generation, enhancing generalizability for physical interactions and facilitating diverse goal adaptation through language cues. Experiments on physical interaction tasks such as door opening, pen and block re-orientation, object relocation, and hammer striking demonstrate DexHandDiff's effectiveness on goals outside training distributions, achieving over twice the average success rate (59.2% vs. 29.5%) compared to existing methods. Our framework achieves an average of 70.7% success rate on goal adaptive dexterous tasks, highlighting its robustness and flexibility in contact-rich manipulation.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
