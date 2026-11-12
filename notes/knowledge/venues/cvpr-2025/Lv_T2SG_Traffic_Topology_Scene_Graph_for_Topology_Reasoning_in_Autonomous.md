---
title: "T2SG: Traffic Topology Scene Graph for Topology Reasoning in Autonomous Driving"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2411.18894"
citations: 44
auto: true
---

> **TL;DR** 자율주행을 위해 차선과 도로 신호, 차선 간 토폴로지 관계를 통합적으로 모델링하는 T2SG와 이를 생성하는 TopoFormer를 제안한 논문이다.

**CVPR 2025** · Changsheng Lv, Mengshi Qi, Liang Liu, Huadong Ma
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lv_T2SG_Traffic_Topology_Scene_Graph_for_Topology_Reasoning_in_Autonomous_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.18894) · 인용 44회

**주제:** Autonomous Driving · Embodied Perception

## 문제
기존 HD mapping 방법은 차선과 도로 신호 간의 제어·안내 관계 및 차선 간 토폴로지 관계를 충분히 모델링하지 못한다.

## 핵심 아이디어
차선, 도로 신호, 이들 간 토폴로지 관계를 명시적으로 표현하는 Traffic Topology Scene Graph(T2SG)를 정의하고, 이를 한 단계로 생성하는 TopoFormer를 제안한다.

## 방법
TopoFormer는 차선 중심선 간 기하학적 거리를 이용해 전역 정보를 집계하는 Lane Aggregation Layer(LAL)와 counterfactual intervention 아래 차선 간 합리적인 도로 구조를 모델링하는 Counterfactual Intervention Layer(CIL)를 포함한다. 생성된 T2SG는 교통 장면의 토폴로지 구조를 더 정확하고 설명 가능하게 기술한다.

## 결과
TopoFormer는 T2SG 생성 과제에서 기존 방법을 능가하며, 생성된 T2SG가 하위 traffic topology reasoning을 크게 향상시켜 OpenLane-V2 benchmark에서 46.3 OLS의 state-of-the-art 성능을 달성한다.

## 초록 (원문)
Understanding the traffic scenes and then generating high-definition (HD) maps present significant challenges in autonomous driving. In this paper, we defined a novel \underline T raffic \underline T opology \underline S cene \underline G raph (\text T ^2\text SG ), a unified scene graph explicitly modeling the lane, controlled and guided by different road signals ( e.g. , right turn), and topology relationships among them, which is always ignored by previous high-definition (HD) mapping methods. For the generation of \text T ^2\text SG , we propose TopoFormer, a novel one-stage \underline Topo logy Scene Graph Trans\underline Former with two newly-designed layers. Specifically, TopoFormer incorporates a Lane Aggregation Layer (LAL) that leverages the geometric distance among the centerline of lanes to guide the aggregation of global information. Furthermore, we proposed a Counterfactual Intervention Layer (CIL) to model the reasonable road structure ( e.g. , intersection, straight) among lanes under counterfactual intervention. Then the generated \text T ^2\text SG can provide a more accurate and explainable description of the topological structure in traffic scenes. Experimental results demonstrate that TopoFormer outperforms existing methods on the \text T ^2\text SG generation task, and the generated \text T ^2\text SG significantly enhances traffic topology reasoning in downstream tasks, achieving a state-of-the-art performance of 46.3 OLS on the OpenLane-V2 benchmark. Our source code is available at https://github.com/MICLAB-BUPT/T2SG.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
