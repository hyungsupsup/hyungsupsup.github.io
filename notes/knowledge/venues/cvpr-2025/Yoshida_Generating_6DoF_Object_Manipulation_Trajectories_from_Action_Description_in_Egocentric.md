---
title: "Generating 6DoF Object Manipulation Trajectories from Action Description in Egocentric Vision"
tags: [cvpr2025, manipulation, dataset-benchmark, embodied-perception]
venue: CVPR 2025
arxiv: "2506.03605"
citations: 14
auto: true
---

> **TL;DR** Exo-Ego4D 영상에서 대규모 조작 궤적을 추출하고 action description으로부터 6DoF 객체 조작 궤적을 생성하는 모델과 데이터셋을 제안한다.

**CVPR 2025** · Tomoya Yoshida, Shuhei Kurita, Taichi Nishimura, Shinsuke Mori
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yoshida_Generating_6DoF_Object_Manipulation_Trajectories_from_Action_Description_in_Egocentric_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2506.03605) · 인용 14회

**주제:** Manipulation · Dataset & Benchmark · Embodied Perception

## 문제
다양한 객체 조작 궤적을 학습하려면 대규모의 세밀한 조작 시연 데이터가 필요하지만, 이를 대규모로 수집하는 것은 거의 불가능하다.

## 핵심 아이디어
Exo-Ego4D의 ego/exo-centric 비디오를 활용해 조작 궤적과 textual action description을 대규모로 추출하고, 이를 기반으로 visual 및 point cloud-based language model 기반 궤적 생성 모델을 학습한다.

## 방법
Exo-Ego4D에서 다양한 조작 궤적을 추출하고 associated textual action description과 연결한다. 이 데이터로 visual 및 point cloud-based language model 기반 trajectory generation models를 개발한다. HOT3D의 egocentric vision 기반 trajectory dataset에서 6DoF object trajectory 생성 성능을 검증한다.

## 결과
HOT3D에서 모델이 valid object trajectories를 성공적으로 생성함을 확인하여, egocentric vision에서 action description으로부터 6DoF manipulation trajectories를 생성하는 새로운 task의 training dataset과 baseline models를 확립했다.

## 연결
- **기반 대표 논문:** ACT / ALOHA, OpenVLA, RT-1, RT-2 — [[knowledge/map|분야 지도]]

## 초록 (원문)
Learning to use tools or objects in common scenes, particularly handling them in various ways as instructed, is a key challenge for developing interactive robots. Training models to generate such manipulation trajectories requires a large and diverse collection of detailed manipulation demonstrations for various objects, which is nearly unfeasible to gather at scale. In this paper, we propose a framework that leverages large-scale egoand exo-centric video datasets --- constructed globally with substantial effort --- of Exo-Ego4D to extract diverse manipulation trajectories at scale. From these extracted trajectories with the associated textual action description, we develop trajectory generation models based on visual and point cloud-based language models. In the recently proposed egocentric vision-based in-a-quality trajectory dataset of HOT3D, we confirmed that our models successfully generate valid object trajectories, establishing a training dataset and baseline models for the novel task of generating 6DoF manipulation trajectories from action descriptions in egocentric vision.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
