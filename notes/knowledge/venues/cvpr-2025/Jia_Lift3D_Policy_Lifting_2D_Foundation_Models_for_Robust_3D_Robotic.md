---
title: "Lift3D Policy: Lifting 2D Foundation Models for Robust 3D Robotic Manipulation"
tags: [cvpr2025, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** Lift3D는 2D foundation model을 implicit/explicit 3D robotic representation으로 확장해 견고한 3D 조작 정책을 구축하는 프레임워크이다.

**CVPR 2025** · Yueru Jia, Jiaming Liu, Sixiang Chen, Chenyang Gu, Zhilve Wang, Longzan Luo 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Jia_Lift3D_Policy_Lifting_2D_Foundation_Models_for_Robust_3D_Robotic_CVPR_2025_paper.html)

**주제:** Manipulation · Embodied Perception

## 문제
3D 기하 정보는 조작에 필수적이지만, 대규모 로봇 3D 데이터 부족과 기존 3D 특징 추출 과정의 공간 기하 손실 문제가 있다.

## 핵심 아이디어
2D foundation model을 그대로 활용하면서 task-aware masked autoencoder와 2D model-lifting을 통해 implicit 및 explicit 3D 표현을 점진적으로 강화한다.

## 방법
먼저 task-relevant affordance patch를 마스킹하고 depth를 재구성하는 task-aware masked autoencoder로 2D foundation model의 implicit 3D 표현을 향상한다. 이후 입력 3D point와 2D model positional embedding 사이의 positional mapping을 설정해 2D foundation model이 point cloud를 직접 인코딩하도록 한다. 이를 통해 대규모 pretrained knowledge를 활용해 explicit 3D robotic representation을 구축하고 공간 정보 손실을 줄인다.

## 결과
Lift3D는 여러 simulation benchmark와 real-world scenario에서 이전 state-of-the-art 방법들을 일관되게 능가한다.

## 초록 (원문)
3D geometric information is essential for manipulation tasks, as robots need to perceive the 3D environment, reason about spatial relationships, and interact with intricate spatial configurations. Recent research has increasingly focused on the explicit extraction of 3D features, while still facing challenges such as the lack of large-scale robotic 3D data and the potential loss of spatial geometry. To address these limitations, we propose the Lift3D framework, which progressively enhances 2D foundation models with implicit and explicit 3D robotic representations to construct a robust 3D manipulation policy. Specifically, we first design a task-aware masked autoencoder that masks task-relevant affordance patches and reconstructs depth information, enhancing the 2D foundation model's implicit 3D robotic representation. After self-supervised fine-tuning, we introduce a 2D model-lifting strategy that establishes a positional mapping between the input 3D points and the positional embeddings of the 2D model. Based on the mapping, Lift3D utilizes the 2D foundation model to directly encode point cloud data, leveraging large-scale pretrained knowledge to construct explicit 3D robotic representations while minimizing spatial information loss. In experiments, Lift3D consistently outperforms previous state-of-the-art methods across several simulation benchmarks and real-world scenarios.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
