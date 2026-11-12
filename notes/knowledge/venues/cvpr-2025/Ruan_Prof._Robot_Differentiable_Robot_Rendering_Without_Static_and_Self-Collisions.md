---
title: "Prof. Robot: Differentiable Robot Rendering Without Static and Self-Collisions"
tags: [cvpr2025, manipulation, embodied-perception]
venue: CVPR 2025
arxiv: "2503.11269"
citations: 2
auto: true
---

> **TL;DR** Differentiable robot rendering 기반 action optimization에 neural collision classifier와 Eikonal regularization을 추가해 static environment 및 self-collision을 피하는 방법을 제안한다.

**CVPR 2025** · Quanyuan Ruan, Jiabao Lei, Wenhao Yuan, Yanglin Zhang, Dekun Lu, Guiliang Liu 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Ruan_Prof._Robot_Differentiable_Robot_Rendering_Without_Static_and_Self-Collisions_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2503.11269) · 인용 2회

**주제:** Manipulation · Embodied Perception

## 문제
기존 differentiable robot rendering은 image-space supervision으로 로봇 action을 학습하지만 물리적 충돌을 인식하지 못해 action optimization 중 충돌이 발생할 수 있다.

## 핵심 아이디어
Neural robotic collision classifier를 학습해 static, non-interactable environment와 로봇 self-collision에 대한 물리적 인식을 제공하고, Eikonal regularization으로 일관된 gradient를 보장한다.

## 방법
Differentiable robot rendering framework에 collision classifier를 통합해 action optimization 시 충돌 회피 gradient를 제공한다. Classifier의 gradient 최적화 문제를 분석하고 Eikonal regularization을 적용해 안정적인 gradient를 유도한다. 이 방식은 기존 differentiable robot rendering 프레임워크에 seamless하게 결합될 수 있다.

## 결과
Qualitative 및 quantitative 실험을 통해 제안 방법이 이전 솔루션 대비 충돌 회피의 필요성과 효과를 입증했다.

## 초록 (원문)
Differentiable rendering has gained significant attention in the field of robotics, with differentiable robot rendering emerging as an effective paradigm for learning robotic actions from image-space supervision. However, the lack of physical world perception in this approach may lead to potential collisions during action optimization. In this work, we introduce a novel improvement on previous efforts by incorporating physical awareness of collisions through the learning of a neural robotic collision classifier. This enables the optimization of actions that avoid collisions with static, non-interactable environments as well as the robot itself. To facilitate effective gradient optimization with the classifier, we identify the underlying issue and propose leveraging Eikonal regularization to ensure consistent gradients for optimization. Our solution can be seamlessly integrated into existing differentiable robot rendering frameworks, utilizing gradients for optimization and providing a foundation for future applications of differentiable rendering in robotics with improved reliability of interactions with the physical world. Both qualitative and quantitative experiments demonstrate the necessity and effectiveness of our method compared to previous solutions.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
