---
title: "GarmentPile: Point-Level Visual Affordance Guided Retrieval and Adaptation for Cluttered Garments Manipulation"
tags: [cvpr2025, manipulation, embodied-perception, simulation-sim2real]
venue: CVPR 2025
arxiv: "2503.09243"
citations: 18
auto: true
---

> **TL;DR** 복잡하게 얽힌 의류 더미에서 point-level affordance와 adaptation module을 이용해 의류를 검색하고 조작 가능한 상태로 재배치하는 프레임워크를 제안한다.

**CVPR 2025** · Ruihai Wu, Ziyu Zhu, Yuran Wang, Yue Chen, Jiarui Wang, Hao Dong
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wu_GarmentPile_Point-Level_Visual_Affordance_Guided_Retrieval_and_Adaptation_for_Cluttered_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.09243) · 인용 18회

**주제:** Manipulation · Embodied Perception · Simulation & Sim2Real

## 문제
의류 더미 조작은 변형 가능한 의류의 복잡한 형상과 의류 간 얽힘 및 상호작용 때문에 단일 의류 조작보다 어렵고, 청결과 조작 안정성을 유지해야 한다.

## 핵심 아이디어
의류의 geometry, structure, inter-object relations를 반영한 point-level affordance를 학습하고, 이를 바탕으로 더미를 조작에 유리한 배치로 재구성하는 adaptation module을 도입한 점이 기존 접근과 다르다.

## 방법
복잡한 공간과 다양한 조작 후보를 dense representation인 point-level affordance로 모델링한다. 학습된 affordance를 활용해 cluttered garments를 조작하기 쉬운 configuration으로 재배치하는 adaptation module을 적용한다. 다양한 의류 유형과 pile 시나리오에서 simulation과 real world 실험으로 검증한다.

## 결과
다양한 의류 유형과 더미 시나리오를 포함한 simulation 및 real world 환경에서 프레임워크의 효과성을 보였다.

## 초록 (원문)
Cluttered garments manipulation poses significant challenges in robotics due to the complex, deformable nature of garments and intricate garment relations. Unlike single-garment manipulation, cluttered scenarios require managing complex garment entanglements and interactions, while maintaining garment cleanliness and manipulation stability. To address these demands, we propose to learn point-level affordance, the dense representation modeling the complex space and multi-modal manipulation candidates, with novel designs for the awareness of garment geometry, structure, and inter-object relations. Additionally, we introduce an adaptation module, informed by learned affordance, to reorganize cluttered garments into configurations conducive to manipulation. Our framework demonstrates effectiveness over environments featuring diverse garment types and pile scenarios in both simulation and the real world. Project page: https://garmentpile.github.io/.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
