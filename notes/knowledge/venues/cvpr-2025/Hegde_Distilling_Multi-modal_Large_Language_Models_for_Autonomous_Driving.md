---
title: "Distilling Multi-modal Large Language Models for Autonomous Driving"
tags: [cvpr2025, autonomous-driving]
venue: CVPR 2025
arxiv: "2501.09757"
citations: 66
auto: true
---

> **TL;DR** DiMA는 multi-modal LLM의 지식을 vision-based end-to-end planner로 distillation하여 inference 시 LLM 없이 효율적이고 안전한 autonomous driving planning을 가능하게 한다.

**CVPR 2025** · Deepti Hegde, Rajeev Yasarla, Hong Cai, Shizhong Han, Apratim Bhattacharyya, Shweta Mahajan 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Hegde_Distilling_Multi-modal_Large_Language_Models_for_Autonomous_Driving_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2501.09757) · 인용 66회

**주제:** Autonomous Driving

## 문제
LLM을 planner로 사용하는 end-to-end autonomous driving은 long-tail scenario 일반화에는 도움이 되지만 test time computational cost가 높다. 이를 해결하면서 LLM의 world knowledge를 유지하는 효율적인 planner가 필요하다.

## 핵심 아이디어
DiMA는 multi-modal LLM에서 vision-based end-to-end planner로 specially designed surrogate tasks를 통해 정보를 distill한다. 공통 scene encoder를 joint training하여 structured representation이 semantic grounding과 final planning objective alignment를 동시에 갖도록 한다.

## 방법
DiMA는 multi-modal LLM과 vision-based planner가 공유하는 scene encoder를 두고, LLM의 정보를 surrogate tasks로 vision planner에 전달하도록 joint training한다. 이때 structured representation은 의미론적으로 grounded되고 planning objective에 정렬된다. Inference에서는 LLM을 optional로 두어 효율적인 planning을 유지한다.

## 결과
DiMA training으로 vision-based planner의 L2 trajectory error가 37% 감소하고 collision rate가 80% 감소했으며, long-tail scenario에서 trajectory error가 44% 감소했다. 또한 nuScenes planning benchmark에서 state-of-the-art 성능을 달성했다.

## 초록 (원문)
Autonomous driving demands safe motion planning, especially in critical "long-tail" scenarios. Recent end-to-end autonomous driving systems leverage large language models (LLMs) as planners to improve generalizability to rare events. However, using LLMs at test time introduces high computational costs. To address this, we propose DiMA, an end-to-end autonomous driving system that maintains the efficiency of an LLM-free (or vision-based) planner while leveraging the world knowledge of an LLM. DiMA distills the information from a multi-modal LLM to a vision-based end-to-end planner through a set of specially designed surrogate tasks. Under a joint training strategy, a scene encoder common to both networks produces structured representations that are semantically grounded as well as aligned to the final planning objective. Notably, the LLM is optional at inference, enabling robust planning without compromising on efficiency. Training with DiMA results in a 37% reduction in the L2 trajectory error and an 80% reduction in the collision rate of the vision-based planner, as well as a 44% trajectory error reduction in long-tail scenarios. \ours also achieves state-of-the-art performance on the nuScenes planning benchmark.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
