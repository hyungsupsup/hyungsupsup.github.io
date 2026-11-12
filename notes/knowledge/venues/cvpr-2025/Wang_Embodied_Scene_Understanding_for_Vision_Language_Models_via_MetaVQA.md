---
title: "Embodied Scene Understanding for Vision Language Models via MetaVQA"
tags: [cvpr2025, dataset-benchmark, autonomous-driving, simulation-sim2real]
venue: CVPR 2025
arxiv: "2501.09167"
citations: 25
auto: true
---

> **TL;DR** MetaVQA는 VLM의 공간 추론과 순차적 의사결정을 VQA와 closed-loop simulation으로 평가·향상시키는 benchmark이다.

**CVPR 2025** · Weizhen Wang, Chenda Duan, Zhenghao Peng, Yuxin Liu, Bolei Zhou
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Wang_Embodied_Scene_Understanding_for_Vision_Language_Models_via_MetaVQA_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.09167) · 인용 25회

**주제:** Dataset & Benchmark · Autonomous Driving · Simulation & Sim2Real

## 문제
Embodied AI agent로서 VLM의 공간 관계 이해와 순차적 의사결정 능력을 평가할 표준화된 closed-loop benchmark가 부족하다.

## 핵심 아이디어
Set-of-Mark prompting과 nuScenes 및 Waymo의 top-down view ground-truth annotation을 활용해 다양한 실제 교통 시나리오 기반의 object-centric이고 context-rich한 question-answer pair를 자동 생성한다.

## 방법
MetaVQA는 VQA와 closed-loop simulation을 결합해 VLM의 spatial reasoning 및 scene dynamics 이해를 평가한다. nuScenes와 Waymo 데이터에서 top-down view ground-truth annotation과 Set-of-Mark prompting을 이용해 대규모 question-answer pair를 자동 생성한다. 이를 통해 VLM을 MetaVQA Dataset으로 fine-tuning하여 embodied scene understanding을 향상시킨다.

## 결과
MetaVQA Dataset으로 VLM을 fine-tuning하면 VQA accuracy가 향상될 뿐 아니라 safety-aware driving maneuver가 나타나며, simulation에서 real-world observation으로의 transferability도 강하게 나타난다.

## 연결
- **기반 대표 논문:** OpenVLA — [[knowledge/map|분야 지도]]

## 초록 (원문)
Vision Language Models (VLMs) demonstrate significant potential as embodied AI agents for various mobility applications. However, a standardized, closed-loop benchmark for evaluating their spatial reasoning and sequential decision-making capabilities is lacking. To address this, we present MetaVQA: a comprehensive benchmark designed to assess and enhance VLMs' understanding of spatial relationships and scene dynamics through Visual Question Answering (VQA) and closed-loop simulations. MetaVQA leverages Set-of-Mark prompting and top-down view ground-truth annotations from nuScenes and Waymo datasets to automatically generate extensive question-answer pairs based on diverse real-world traffic scenarios, ensuring object-centric and context-rich instructions. Our experiments show that fine-tuning VLMs with the MetaVQA Dataset significantly improves their embodied scene understanding, which is evident not only in improved VQA accuracy but also in emerging safety-aware driving maneuvers. In addition, the learning exhibits strong transferability from simulation to real-world observation. The project webpage is at https://metadriverse.github.io/metavqa.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
