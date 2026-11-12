---
title: "Reasoning Mamba: Hypergraph-Guided Region Relation Calculating for Weakly Supervised Affordance Grounding"
tags: [cvpr2025, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** R-Mamba는 hypergraph로 객체 구성 요소 간 관계를 포착해 weakly supervised affordance grounding의 영역 위치 추정 정확도를 높이는 방법을 제안한다.

**CVPR 2025** · Yuxuan Wang, Aming Wu, Muli Yang, Yukuan Min, Yihang Zhu, Cheng Deng
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Reasoning_Mamba_Hypergraph-Guided_Region_Relation_Calculating_for_Weakly_Supervised_Affordance_CVPR_2025_paper.html)

**주제:** Embodied Perception

## 문제
기존 WSAG 방법은 affordance 영역을 독립적으로 보고 class activation map으로 직접 localization하여 객체 구성 요소 간 관계를 무시해 성능이 제한된다.

## 핵심 아이디어
exo-centric 및 egocentric 이미지에서 hypergraph를 구성해 국소 영역 관계를 포착하고, 이를 Hypergraph-guided State Space (HSS) block으로 전역적으로 재조직하는 R-Mamba 프레임워크를 제안한다.

## 방법
먼저 exo-centric과 egocentric 이미지에서 feature embedding을 추출해 여러 vertex와 hyperedge로 이루어진 hypergraph를 구성하여 시각 구성 요소 간 in-context 국소 관계를 포착한다. 이후 HSS block이 이러한 국소 관계를 전역 관점에서 재조직한다. 이렇게 포착된 관계를 활용해 affordance 영역의 localization 정확도를 향상시킨다.

## 결과
광범위한 실험과 시각화 분석을 통해 제안 방법의 우수성을 입증하였다.

## 초록 (원문)
This paper pays attention to Weakly Supervised Affordance Grounding (WSAG) task that aims to train model to identify affordance regions using human-object interaction images and egocentric images without the need for costly pixel-level annotations. Most existing methods usually consider the affordance regions to be isolated and directly employ class activation maps to conduct localization, ignoring the relationships with other object components and weakening the performance. For example, a cup's handle is combined with its body to achieve the pouring ability. Obviously, capturing the region relationships is beneficial for improving the localization accuracy of affordance regions. To this end, we first explore exploiting hypergraph to discover these relations and propose a Reasoning Mamba (R-Mamba) framework. We first extract feature embeddings from exo-centric and egocentric images to construct the hypergraphs consisting of multiple vertices and hyperedges, which capture the in-context local region relationships between different visual components. Subsequently, we design a Hypergraph-guided State Space (HSS) block to reorganize these local relationships from the global perspective. By this mechanism, the model could leverage the captured relationships to improve the localization accuracy of affordance regions. Extensive experiments and visualization analyses demonstrate the superiority of our method.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
