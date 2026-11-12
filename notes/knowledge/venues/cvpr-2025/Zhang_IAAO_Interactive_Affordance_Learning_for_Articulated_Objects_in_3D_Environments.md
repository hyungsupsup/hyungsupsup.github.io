---
title: "IAAO: Interactive Affordance Learning for Articulated Objects in 3D Environments"
tags: [cvpr2025, embodied-perception, manipulation]
venue: CVPR 2025
arxiv: "2504.06827"
citations: 15
auto: true
---

> **TL;DR** IAAO는 intelligent agent가 상호작용을 통해 articulated objects의 affordance와 part articulation을 이해하도록 명시적 3D 모델을 구축하는 프레임워크이다.

**CVPR 2025** · Can Zhang, Gim Hee Lee
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_IAAO_Interactive_Affordance_Learning_for_Articulated_Objects_in_3D_Environments_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.06827) · 인용 15회

**주제:** Embodied Perception · Manipulation

## 문제
기존 방법은 task-specific networks와 movable parts에 대한 가정에 의존해 articulated objects를 일반적으로 이해하고 상호작용하기 어렵다.

## 핵심 아이디어
large foundation models를 활용해 interactive affordances와 part articulations를 추정하고, 여러 object state의 3D 장면을 병합·정제해 affordance 기반 상호작용과 manipulation을 가능하게 한다.

## 방법
먼저 multi-view images에서 mask features와 view-consistent labels를 distill하여 3D Gaussian Splatting (3DGS) 기반의 hierarchical features와 label fields를 각 object state마다 구축한다. 이후 3D Gaussian primitives에 object-level 및 part-level query를 수행해 static/articulated elements를 식별하고 global transformations, local articulation parameters, affordances를 추정한다. 마지막으로 서로 다른 state의 장면을 추정된 transformation에 따라 merge and refine하여 robust한 affordance-based interaction and manipulation을 지원한다.

## 결과
실험 결과는 제안 방법의 효과성을 입증하며, articulated objects에 대한 affordance 기반 상호작용과 manipulation이 가능함을 보여준다.

## 초록 (원문)
This work presents IAAO, a novel framework that builds an explicit 3D model for intelligent agents to gain understanding of articulated objects in their environment through interaction. Unlike prior methods that rely on task-specific networks and assumptions about movable parts, our IAAO leverages large foundation models to estimate interactive affordances and part articulations in three stages. We first build hierarchical features and label fields for each object state using 3D Gaussian Splatting (3DGS) by distilling mask features and view-consistent labels from multi-view images. We then perform objectand part-level queries on the 3D Gaussian primitives to identify static and articulated elements, estimating global transformations and local articulation parameters along with affordances. Finally, scenes from different states are merged and refined based on the estimated transformations, enabling robust affordance-based interaction and manipulation of objects. Experimental results demonstrate the effectiveness of our method.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
