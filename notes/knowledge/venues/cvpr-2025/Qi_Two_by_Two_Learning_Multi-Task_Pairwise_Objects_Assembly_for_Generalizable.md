---
title: "Two by Two: Learning Multi-Task Pairwise Objects Assembly for Generalizable Robot Manipulation"
tags: [cvpr2025, dataset-benchmark, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2504.06961"
citations: 23
auto: true
---

> **TL;DR** 2BY2는 일상적인 pairwise object assembly를 위한 대규모 annotated dataset과 assembly constraints를 활용한 two-step SE(3) pose estimation method를 제안한다.

**CVPR 2025** · Yu Qi, Yuanchen Ju, Tianming Wei, Chi Chu, Lawson L.S. Wong, Huazhe Xu
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Qi_Two_by_Two_Learning_Multi-Task_Pairwise_Objects_Assembly_for_Generalizable_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.06961) · 인용 23회

**주제:** Dataset & Benchmark · Manipulation · Embodied Perception

## 문제
기존 benchmark와 dataset은 geometric fragments나 factory parts 조립에 치중되어 일상 object 간 interaction과 assembly의 복잡성을 충분히 다루지 못한다.

## 핵심 아이디어
18개의 fine-grained daily assembly tasks를 포함하는 2BY2 dataset을 구축하고, equivariant features를 이용해 assembly constraints를 반영하는 two-step SE(3) pose estimation method를 제안한다.

## 방법
2BY2 dataset은 pose와 symmetry annotation을 포함한 1,034 instances 및 517 pairwise objects로 구성된다. 제안 방법은 two-step SE(3) pose estimation과 equivariant features를 통해 geometric shape 정렬 및 object 간 functional/spatial relationship을 고려한 assembly constraints를 만족하도록 한다.

## 결과
제안 방법은 2BY2 dataset의 all 18 tasks에서 previous shape assembly methods 대비 state-of-the-art performance를 달성했으며, robot experiments로 complex 3D assembly tasks에 대한 reliability와 generalization ability를 검증했다.

## 연결
- **기반 대표 논문:** Domain Randomization (Tobin et al.) — [[knowledge/map|분야 지도]]

## 초록 (원문)
3D assembly tasks, such as furniture assembly and component fitting, play a crucial role in daily life and represent essential capabilities for future home robots. Existing benchmarks and datasets predominantly focus on assembling geometric fragments or factory parts, which fall short in addressing the complexities of everyday object interactions and assemblies. To bridge this gap, we present 2BY2, a large-scale annotated dataset for daily pairwise objects assembly, covering 18 fine-grained tasks that reflect real-life scenarios, such as plugging into sockets, arranging flowers in vases, and inserting bread into toasters. 2BY2 dataset includes 1,034 instances and 517 pairwise objects with pose and symmetry annotations, requiring approaches that align geometric shapes while accounting for functional and spatial relationships between objects. Leveraging the 2BY2 dataset, we propose a two-step SE(3) pose estimation method with equivariant features for assembly constraints. Compared to previous shape assembly methods, our approach achieves state-of-the-art performance across all 18 tasks in the 2BY2 dataset. Additionally, robot experiments further validate the reliability and generalization ability of our method for complex 3D assembly tasks. More details and demonstrations can be found at https://tea-lab.github.io/TwoByTwo/.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
