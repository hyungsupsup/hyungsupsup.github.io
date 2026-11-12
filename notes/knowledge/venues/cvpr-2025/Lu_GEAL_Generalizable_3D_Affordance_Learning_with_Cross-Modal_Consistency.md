---
title: "GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency"
tags: [cvpr2025, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2412.09511"
citations: 29
auto: true
---

> **TL;DR** GEAL은 대규모 2D 사전학습 모델을 활용해 3D affordance 학습의 일반화와 robustness를 향상시키는 프레임워크다.

**CVPR 2025** · Dongyue Lu, Lingdong Kong, Tianxin Huang, Gim Hee Lee
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lu_GEAL_Generalizable_3D_Affordance_Learning_with_Cross-Modal_Consistency_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.09511) · 인용 29회

**주제:** Embodied Perception · Dataset & Benchmark

## 문제
기존 3D affordance 학습은 제한된 annotated data와 geometric encoding 중심의 3D backbone에 의존해 real-world noise와 data corruption에 취약하고 일반화가 어렵다.

## 핵심 아이디어
Gaussian splatting 기반 dual-branch architecture로 3D point cloud와 2D representation 간 일관된 mapping을 구축하고, granularity-adaptive fusion과 2D-3D consistency alignment를 통해 2D model의 풍부한 semantics와 일반화 능력을 3D branch로 전이한다.

## 방법
Sparse point cloud로부터 realistic 2D rendering을 생성하고 dual-branch 구조로 3D와 2D 특징을 함께 처리한다. Granularity-adaptive fusion module과 2D-3D consistency alignment module이 cross-modal alignment와 knowledge transfer를 강화한다. 또한 robustness를 종합적으로 평가하기 위해 corruption-based benchmarks인 PIAD-C와 LASO-C를 제안한다.

## 결과
Public datasets와 PIAD-C, LASO-C에서 seen 및 novel object categories와 corrupted data 모두에서 GEAL이 기존 방법보다 일관되게 우수한 affordance prediction을 보인다.

## 연결
- 인용됨 ← [[knowledge/venues/cvpr-2025/Yu_SeqAfford_Sequential_3D_Affordance_Reasoning_via_Multimodal_Large_Language_Model|SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model]]

## 초록 (원문)
Identifying affordance regions on 3D objects from semantic cues is essential for robotics and human-machine interaction. However, existing 3D affordance learning methods struggle with generalization and robustness due to limited annotated data and a reliance on 3D backbones focused on geometric encoding, which often lack resilience to real-world noise and data corruption. We propose GEAL, a novel framework designed to enhance the generalization and robustness of 3D affordance learning by leveraging large-scale pre-trained 2D models. We employ a dual-branch architecture with Gaussian splatting to establish consistent mappings between 3D point clouds and 2D representations, enabling realistic 2D renderings from sparse point clouds. A granularity-adaptive fusion module and a 2D-3D consistency alignment module further strengthen cross-modal alignment and knowledge transfer, allowing the 3D branch to benefit from the rich semantics and generalization capacity of 2D models. To holistically assess the robustness, we introduce two new corruption-based benchmarks: PIAD-C and LASO-C. Extensive experiments on public datasets and our benchmarks show that GEAL consistently outperforms existing methods across seen and novel object categories, as well as corrupted data, demonstrating robust and adaptable affordance predictions. The code and datasets are publicly available.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
