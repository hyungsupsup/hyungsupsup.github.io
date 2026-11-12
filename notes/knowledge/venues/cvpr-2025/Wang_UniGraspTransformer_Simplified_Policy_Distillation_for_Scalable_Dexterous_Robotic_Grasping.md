---
title: "UniGraspTransformer: Simplified Policy Distillation for Scalable Dexterous Robotic Grasping"
tags: [cvpr2025, manipulation, imitation-learning, reinforcement-learning]
venue: CVPR 2025
arxiv: "2412.02699"
citations: 28
auto: true
---

> **TL;DR** UniGraspTransformer는 객체별 RL 정책을 단일 Transformer로 distillation하여 확장 가능한 dexterous robotic grasping을 수행하는 방법이다.

**CVPR 2025** · Wenbo Wang, Fangyun Wei, Lei Zhou, Xi Chen, Lin Luo, Xiaohan Yi 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_UniGraspTransformer_Simplified_Policy_Distillation_for_Scalable_Dexterous_Robotic_Grasping_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.02699) · 인용 28회

**주제:** Manipulation · Imitation Learning · Reinforcement Learning

## 문제
기존 UniDexGrasp++ 등은 복잡한 다단계 학습 파이프라인을 필요로 하며, 다양한 객체와 자세로 확장하기 어렵다.

## 핵심 아이디어
객체별 RL 정책이 생성한 성공적인 grasp trajectory를 하나의 universal Transformer 네트워크로 단순화된 distillation 과정을 통해 학습한다.

## 방법
먼저 각 객체에 대해 reinforcement learning으로 dedicated policy network를 학습해 성공적인 grasp trajectory를 생성한다. 이후 이 trajectory들을 단일 universal network로 distill하며, 최대 12개의 self-attention block을 사용해 수천 개 객체와 다양한 pose를 처리한다. State-based 및 vision-based 설정에서 이상적 입력과 실제 입력 모두에 대한 일반화를 평가한다.

## 결과
Vision-based 설정에서 UniDexGrasp++ 대비 seen objects, unseen objects within seen categories, completely unseen objects에서 각각 3.5%, 7.7%, 10.1%의 success rate 향상을 달성했다.

## 초록 (원문)
We introduce UniGraspTransformer, a universal Transformer-based network for dexterous robotic grasping that simplifies training while enhancing scalability and performance. Unlike prior methods such as UniDexGrasp++, which require complex, multi-step training pipelines, UniGraspTransformer follows a streamlined process: first, dedicated policy networks are trained for individual objects using reinforcement learning to generate successful grasp trajectories; then, these trajectories are distilled into a single, universal network. Our approach enables UniGraspTransformer to scale effectively, incorporating up to 12 self-attention blocks for handling thousands of objects with diverse poses. Additionally, it generalizes well to both idealized and real-world inputs, evaluated in state-based and vision-based settings. Notably, UniGraspTransformer generates a broader range of grasping poses for objects in various shapes and orientations, resulting in more diverse grasp strategies. Experimental results demonstrate significant improvements over state-of-the-art, UniDexGrasp++, across various object categories, achieving success rate gains of 3.5%, 7.7%, and 10.1% on seen objects, unseen objects within seen categories, and completely unseen objects, respectively, in the vision-based setting. Project page: https://dexhand.github.io/UniGraspTransformer/

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
