---
title: "TASTE-Rob: Advancing Video Generation of Task-Oriented Hand-Object Interaction for Generalizable Robotic Manipulation"
tags: [cvpr2025, dataset-benchmark, manipulation, imitation-learning]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** TASTE-Rob는 로봇 모방 학습용 task-oriented hand-object interaction 비디오 생성을 위해 100,856개의 ego-centric 비디오 데이터셋과 pose-refinement 파이프라인을 제안한다.

**CVPR 2025** · Hongxiang Zhao, Xingchen Liu, Mutian Xu, Yiming Hao, Weikai Chen, Xiaoguang Han
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhao_TASTE-Rob_Advancing_Video_Generation_of_Task-Oriented_Hand-Object_Interaction_for_Generalizable_CVPR_2025_paper.html)

**주제:** Dataset & Benchmark · Manipulation · Imitation Learning

## 문제
기존 Ego4D 등 데이터셋은 시점이 일관되지 않고 상호작용이 정렬되지 않아 정밀한 로봇 모방 학습용 비디오 생성에 한계가 있다.

## 핵심 아이디어
일관된 카메라 시점과 언어 지시에 정렬된 대규모 hand-object interaction 비디오 데이터셋을 구축하고, 생성 비디오의 손 자세 정확도를 높이는 three-stage pose-refinement 파이프라인을 도입한다.

## 방법
TASTE-Rob 데이터셋으로 Video Diffusion Model (VDM)을 fine-tuning하여 현실적인 물체 상호작용 비디오를 생성한다. 이후 three-stage pose-refinement 파이프라인을 적용해 생성된 비디오에서 관찰되는 손 grasping posture의 불일치를 개선한다. 이렇게 생성된 고품질 task-oriented 비디오를 로봇 조작 학습에 활용한다.

## 결과
TASTE-Rob과 pose-refinement 프레임워크를 통해 고품질 task-oriented hand-object interaction 비디오 생성에서 성능 향상을 보였고, 더 우수한 generalizable robotic manipulation을 달성했다.

## 초록 (원문)
We address key limitations in existing datasets and models for task-oriented hand-object interaction video generation, a critical approach of generating video demonstrations for robotic imitation learning. Current datasets, such as Ego4D, often suffer from inconsistent view perspectives and misaligned interactions, leading to reduced video quality and limiting their applicability for precise imitation learning tasks. Towards this end, we introduce TASTE-Rob -- a pioneering large-scale dataset of 100,856 ego-centric hand-object interaction videos. Each video is meticulously aligned with language instructions and recorded from a consistent camera viewpoint to ensure interaction clarity. By fine-tuning a Video Diffusion Model (VDM) on TASTE-Rob, we achieve realistic object interactions, though we observed occasional inconsistencies in hand grasping postures. To enhance realism, we introduce a three-stage pose-refinement pipeline that improves hand posture accuracy in generated videos. Our curated dataset, coupled with the specialized pose-refinement framework, provides notable performance gains in generating high-quality, task-oriented hand-object interaction videos, resulting in achieving superior generalizable robotic manipulation. To foster further advancements in the field, TASTE-Rob dataset and source code will be made publicly available on our website https://taste-rob.github.io.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
