---
title: "GREAT: Geometry-Intention Collaborative Inference for Open-Vocabulary 3D Object Affordance Grounding"
tags: [cvpr2025, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2411.19626"
citations: 33
auto: true
---

> **TL;DR** GREAT는 임의의 지시에 대해 3D 객체의 행동 가능 영역을 예측하는 open-vocabulary 3D object affordance grounding 프레임워크와 대규모 PIADv2 데이터셋을 제안한다.

**CVPR 2025** · Yawen Shao, Wei Zhai, Yuhang Yang, Hongchen Luo, Yang Cao, Zheng-Jun Zha
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Shao_GREAT_Geometry-Intention_Collaborative_Inference_for_Open-Vocabulary_3D_Object_Affordance_Grounding_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.19626) · 인용 33회

**주제:** Embodied Perception · Dataset & Benchmark

## 문제
기존 open-vocabulary 3D object affordance grounding 방법은 외부 상호작용 사전지식에 의존해 제한된 의미 공간에 머물며, 객체의 불변 기하 구조와 잠재적 상호작용 의도를 충분히 활용하지 못한다.

## 핵심 아이디어
GREAT는 객체의 불변 기하 속성을挖掘하고 잠재적 상호작용 시나리오에서 유추적 추론을 수행해 affordance 지식을 형성한 뒤, 이를 기하와 시각 내용에 결합해 3D 객체 affordance를 grounding한다.

## 방법
GREAT는 Geometry-Intention Collaborative Inference를 통해 객체의 invariant geometry attributes와 potential interaction intentions를 함께 추론한다. 이후 유추적 추론으로 형성한 affordance knowledge를 3D geometry 및 visual contents와 결합하여 open-vocabulary affordance grounding을 수행한다. 또한 이를 지원하기 위해 현재 가장 큰 3D object affordance 데이터셋인 PIADv2를 도입한다.

## 결과
광범위한 실험에서 GREAT의 효과성과 우수성을 입증했으며, PIADv2는 현재 가장 큰 3D object affordance 데이터셋으로 제시된다.

## 연결
- 인용됨 ← [[knowledge/venues/cvpr-2025/Yu_SeqAfford_Sequential_3D_Affordance_Reasoning_via_Multimodal_Large_Language_Model|SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model]]

## 초록 (원문)
Open-Vocabulary 3D object affordance grounding aims to anticipate "action possibilities" regions on 3D objects with arbitrary instructions, which is crucial for robots to generically perceive real scenarios and respond to operational changes. Existing methods focus on combining images or languages that depict interactions with 3D geometries to introduce external interaction priors. However, they are still vulnerable to a limited semantic space by failing to leverage implied invariant geometries and potential interaction intentions. Normally, humans address complex tasks through multi-step reasoning and respond to diverse situations by leveraging associative and analogical thinking. In light of this, we propose GREAT (Geometry-Intention Collaborative Inference) for Open-Vocabulary 3D Object Affordance Grounding, a novel framework that mines the object invariant geometry attributes and performs analogically reason in potential interaction scenarios to form affordance knowledge, fully combining the knowledge with both geometries and visual contents to ground 3D object affordance. Besides, we introduce the Point Image Affordance Dataset v2 (PIADv2), the largest 3D object affordance dataset at present to support the task. Extensive experiments demonstrate the effectiveness and superiority of GREAT. The code and dataset are available at https://yawen-shao.github.io/GREAT/.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
