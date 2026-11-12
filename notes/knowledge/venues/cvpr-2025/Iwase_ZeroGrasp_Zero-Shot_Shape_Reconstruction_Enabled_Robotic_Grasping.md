---
title: "ZeroGrasp: Zero-Shot Shape Reconstruction Enabled Robotic Grasping"
tags: [cvpr2025, manipulation, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2504.10857"
citations: 28
auto: true
---

> **TL;DR** ZeroGrasp는 3D 재구성과 grasp pose 예측을 동시에 수행하는 near real-time 프레임워크로, 대규모 합성 데이터를 활용해 실제 물체로 일반화되는 로봇 grasping을 달성한다.

**CVPR 2025** · Shun Iwase, Muhammad Zubair Irshad, Katherine Liu, Vitor Guizilini, Robert Lee, Takuya Ikeda 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Iwase_ZeroGrasp_Zero-Shot_Shape_Reconstruction_Enabled_Robotic_Grasping_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.10857) · 인용 28회

**주제:** Manipulation · Embodied Perception · Dataset & Benchmark

## 문제
기존 grasping 방법은 부분 정보만으로 직접 grasp를 출력하고 장면의 기하 구조를 모델링하지 않아 최적이 아닌 움직임이나 충돌을 초래할 수 있다.

## 핵심 아이디어
occlusion reasoning과 물체 간 공간 관계 모델링이 정확한 3D 재구성과 grasping 모두에 유리하다는 점을 활용해 두 작업을 동시에 수행한다.

## 방법
ZeroGrasp는 3D reconstruction과 grasp pose prediction을 near real-time으로 함께 수행하는 프레임워크다. Objaverse-LVIS의 12K objects에 대해 1M photo-realistic images, high-resolution 3D reconstructions, 11.3B physically-valid grasp pose annotations를 포함하는 대규모 합성 데이터셋과 결합된다. GraspNet-1B benchmark와 실제 로봇 실험으로 평가된다.

## 결과
ZeroGrasp는 state-of-the-art 성능을 달성하고 합성 데이터를 활용해 새로운 실제 물체로 일반화됨을 보인다.

## 연결
- **기반 대표 논문:** Isaac Gym — [[knowledge/map|분야 지도]]

## 초록 (원문)
Robotic grasping is a cornerstone capability of embodied systems. Many methods directly output grasps from partial information without modeling the geometry of the scene, leading to suboptimal motion and even collisions. To address these issues, we introduce ZeroGrasp, a novel framework that simultaneously performs 3D reconstruction and grasp pose prediction in near real-time. A key insight of our method is that occlusion reasoning and modeling the spatial relationships between objects is beneficial for both accurate reconstruction and grasping. We couple our method with a novel large-scale synthetic dataset, which comprises 1M photo-realistic images, high-resolution 3D reconstructions and 11.3B physically-valid grasp pose annotations for 12K objects from the Objaverse-LVIS dataset. We evaluate ZeroGrasp on the GraspNet-1B benchmark as well as through real-world robot experiments. ZeroGrasp achieves state-of-the-art performance and generalizes to novel real-world objects by leveraging synthetic data.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
