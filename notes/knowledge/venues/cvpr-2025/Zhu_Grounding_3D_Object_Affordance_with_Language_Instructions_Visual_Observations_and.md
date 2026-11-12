---
title: "Grounding 3D Object Affordance with Language Instructions, Visual Observations and Interactions"
tags: [cvpr2025, embodied-perception, dataset-benchmark, manipulation]
venue: CVPR 2025
arxiv: "2504.04744"
citations: 26
auto: true
---

> **TL;DR** 언어 지시, 시각 관측, 상호작용을 바탕으로 3D 객체 affordance를 grounding하는 새 task와 AGPIL 데이터셋, LMAffordance3D 모델을 제안한다.

**CVPR 2025** · He Zhu, Quyu Kong, Kechun Xu, Xunlong Xia, Bing Deng, Jieping Ye 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhu_Grounding_3D_Object_Affordance_with_Language_Instructions_Visual_Observations_and_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.04744) · 인용 26회

**주제:** Embodied Perception · Dataset & Benchmark · Manipulation

## 문제
지능형 로봇이 인간 지시에 따라 객체의 affordance를 정확히 찾고 조작하려면 3D 공간에서 언어와 시각, 상호작용 정보를 함께 활용해야 하지만, 이를 위한 task와 데이터가 부족하다.

## 핵심 아이디어
언어 지시, 시각 관측, 상호작용을 결합해 3D 객체 affordance를 grounding하는 새로운 task를 정의하고, full-view·partial-view·rotation-view 관점을 포함한 AGPIL 데이터셋을 구축한다. 또한 vision-language model로 2D/3D 공간 특징과 의미 특징을 융합하는 첫 multi-modal, language-guided 3D affordance grounding 네트워크 LMAffordance3D를 제안한다.

## 방법
AGPIL은 Points, Images, Language instructions로 구성되며 full-view, partial-view, rotation-view에서의 affordance 추정을 포함한다. LMAffordance3D는 vision-language model을 적용해 2D 및 3D 공간 특징을 semantic features와 융합하여 언어 지시에 맞는 3D affordance를 예측한다.

## 결과
AGPIL에 대한 종합 실험에서 LMAffordance3D의 효과와 우수성을 보였으며, unseen experimental settings에서도 성능을 입증했다.

## 초록 (원문)
Grounding 3D object affordance is a task that locates objects in 3D space where they can be manipulated, which links perception and action for embodied intelligence. For example, for an intelligent robot, it is necessary to accurately ground the affordance of an object and grasp it according to human instructions. In this paper, we introduce a novel task that grounds 3D object affordance based on language instructions, visual observations and interactions, which is inspired by cognitive science. We collect an Affordance Grounding dataset with Points, Images and Language instructions (AGPIL) to support the proposed task. In the 3D physical world, due to observation orientation, object rotation, or spatial occlusion, we can only get a partial observation of the object. So this dataset includes affordance estimations of objects from full-view, partial-view, and rotation-view perspectives. To accomplish this task, we propose LMAffordance3D, the first multi-modal, language-guided 3D affordance grounding network, which applies a vision-language model to fuse 2D and 3D spatial features with semantic features. Comprehensive experiments on AGPIL demonstrate the effectiveness and superiority of our method on this task, even in unseen experimental settings.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
