---
title: "SeqAfford: Sequential 3D Affordance Reasoning via Multimodal Large Language Model"
tags: [cvpr2025, embodied-perception, dataset-benchmark, manipulation]
venue: CVPR 2025
arxiv: "2412.01550"
citations: 33
auto: true
---

> **TL;DR** SeqAfford는 복잡한 사용자 의도를 순차적 3D affordance segmentation으로 분해하는 Sequential 3D Affordance Reasoning task와 180K instruction-point cloud pairs 벤치마크를 제안하고, 3D multimodal LLM 기반 모델로 이를 수행한다.

**CVPR 2025** · Chunlin Yu, Hanqing Wang, Ye Shi, Haoyang Luo, Sibei Yang, Jingyi Yu 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yu_SeqAfford_Sequential_3D_Affordance_Reasoning_via_Multimodal_Large_Language_Model_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2412.01550) · 인용 33회

**주제:** Embodied Perception · Dataset & Benchmark · Manipulation

## 문제
기존 3D affordance segmentation은 single-object, single-affordance 패러다임에 머물러 장기 작업이나 순차적 affordance를 요구하는 복잡한 사용자 의도를 능동적으로 추론하지 못한다.

## 핵심 아이디어
Sequential 3D Affordance Reasoning task를 정의하고 첫 instruction-based affordance segmentation benchmark를 180K instruction-point cloud pairs로 구축하며, 3D multi-modal large language model에 affordance segmentation 능력을 부여해 world knowledge reasoning과 fine-grained affordance grounding을 통합한다.

## 방법
SeqAfford는 3D multi-modal large language model을 확장해 사용자 의도를 해석하고 이를 일련의 segmentation maps로 분해한다. multi-granular language-point integration module을 도입해 3D dense prediction을 가능하게 하며, single 및 sequential affordance reasoning을 포함하는 benchmark에서 학습 및 평가된다.

## 결과
광범위한 실험에서 SeqAfford는 기존 well-established methods를 능가하고 sequential reasoning abilities를 갖춘 open-world generalization을 보인다.

## 연결
- 인용함 → [[knowledge/venues/cvpr-2025/Lu_GEAL_Generalizable_3D_Affordance_Learning_with_Cross-Modal_Consistency|GEAL: Generalizable 3D Affordance Learning with Cross-Modal Consistency]]
- 인용함 → [[knowledge/venues/cvpr-2025/Wu_AffordDP_Generalizable_Diffusion_Policy_with_Transferable_Affordance|AffordDP: Generalizable Diffusion Policy with Transferable Affordance]]
- 인용함 → [[knowledge/venues/cvpr-2025/Shao_GREAT_Geometry-Intention_Collaborative_Inference_for_Open-Vocabulary_3D_Object_Affordance_Grounding|GREAT: Geometry-Intention Collaborative Inference for Open-Vocabulary 3D Object Affordance Grounding]]
- 인용됨 ← [[knowledge/venues/cvpr-2025/Wu_AffordDP_Generalizable_Diffusion_Policy_with_Transferable_Affordance|AffordDP: Generalizable Diffusion Policy with Transferable Affordance]]

## 초록 (원문)
3D affordance segmentation aims to link human instructions to touchable regions of 3D objects for embodied manipulations. Existing efforts typically adhere to single-object, single-affordance paradigms, where each affordance type or explicit instruction strictly corresponds to a specific affordance region and are unable to handle long-horizon tasks. Such a paradigm cannot actively reason about complex user intentions that often imply sequential affordances. In this paper, we introduce the Sequential 3D Affordance Reasoning task, which extends the traditional paradigm by reasoning from cumbersome user intentions and then decomposing them into a series of segmentation maps. Toward this, we construct the first instruction-based affordance segmentation benchmark that includes reasoning over both single and sequential affordances, comprising 180K instruction-point cloud pairs. Based on the benchmark, we propose our model, SeqAfford, to unlock the 3D multi-modal large language model with additional affordance segmentation abilities, which ensures reasoning with world knowledge and fine-grained affordance grounding in a cohesive framework. We further introduce a multi-granular language-point integration module to endow 3D dense prediction. Extensive experimental evaluations show that our model excels over well-established methods and exhibits open-world generalization with sequential reasoning abilities.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
