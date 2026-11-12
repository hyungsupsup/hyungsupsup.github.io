---
title: "G3Flow: Generative 3D Semantic Flow for Pose-aware and Generalizable Object Manipulation"
tags: [cvpr2025, imitation-learning, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2411.18369"
citations: 57
auto: true
---

> **TL;DR** G3Flow는 foundation models를 활용해 실시간 object-centric 3D semantic flow를 구축하고 diffusion policy에 통합한 조작 프레임워크다.

**CVPR 2025** · Tianxing Chen, Yao Mu, Zhixuan Liang, Zanxin Chen, Shijia Peng, Qiangyu Chen 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_G3Flow_Generative_3D_Semantic_Flow_for_Pose-aware_and_Generalizable_Object_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.18369) · 인용 57회

**주제:** Imitation Learning · Manipulation · Embodied Perception

## 문제
3D 로봇 조작을 위한 diffusion-based imitation learning에서 기하학적 정밀도와 semantic understanding을 함께 달성하고, occlusion 상황에서도 수동 annotation 없이 객체를 이해하는 것이 문제다.

## 핵심 아이디어
3D generative model로 digital twin을 만들고 vision foundation model의 semantic feature와 robust pose tracking을 결합해 실시간으로 갱신되는 semantic flow를 구성한 점이 기존 방법과 다르다.

## 방법
G3Flow는 3D generative model 기반 digital twin 생성, vision foundation model 기반 semantic feature extraction, continuous pose tracking을 결합해 object-centric 3D semantic flow를 실시간 구축한다. 이 semantic flow를 diffusion policy에 통합하여 terminal-constrained manipulation과 cross-object generalization을 가능하게 한다.

## 결과
다섯 개 simulation task에서 G3Flow는 기존 방법보다 일관되게 우수했으며, terminal-constrained manipulation과 cross-object generalization에서 각각 최대 68.3%와 50.1%의 평균 success rate를 달성했다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, DDPM, Diffusion Policy — [[knowledge/map|분야 지도]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Wu_AffordDP_Generalizable_Diffusion_Policy_with_Transferable_Affordance|AffordDP: Generalizable Diffusion Policy with Transferable Affordance]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Liang_DexHandDiff_Interaction-aware_Diffusion_Planning_for_Adaptive_Dexterous_Manipulation|DexHandDiff: Interaction-aware Diffusion Planning for Adaptive Dexterous Manipulation]]

## 초록 (원문)
Recent advances in imitation learning for 3D robotic manipulation have shown promising results with diffusion-based policies. However, achieving human-level dexterity requires seamless integration of geometric precision and semantic understanding. We present G3Flow, a novel framework that constructs real-time semantic flow, a dynamic, object-centric 3D semantic representation by leveraging foundation models. Our approach uniquely combines 3D generative models for digital twin creation, vision foundation models for semantic feature extraction, and robust pose tracking for continuous semantic flow updates. This integration enables complete semantic understanding even under occlusions while eliminating manual annotation requirements. By incorporating semantic flow into diffusion policies, we demonstrate significant improvements in both terminal-constrained manipulation and cross-object generalization. Extensive experiments across five simulation tasks show that G3Flow consistently outperforms existing approaches, achieving up to 68.3% and 50.1% average success rates on terminal-constrained manipulation and cross-object generalization tasks respectively. Our results demonstrate the effectiveness of G3Flow in enhancing real-time dynamic semantic feature understanding for robotic manipulation policies.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
