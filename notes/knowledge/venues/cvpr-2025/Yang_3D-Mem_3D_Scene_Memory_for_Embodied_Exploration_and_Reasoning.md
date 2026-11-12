---
title: "3D-Mem: 3D Scene Memory for Embodied Exploration and Reasoning"
tags: [cvpr2025, embodied-perception, navigation]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** 3D-Mem은 embodied agent가 탐험한 영역과 미탐험 영역을 함께 고려하도록 multi-view Memory Snapshots와 Frontier Snapshots를 활용하는 3D 장면 메모리 프레임워크다.

**CVPR 2025** · Yuncong Yang, Han Yang, Jiachen Zhou, Peihao Chen, Hongxin Zhang, Yilun Du 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yang_3D-Mem_3D_Scene_Memory_for_Embodied_Exploration_and_Reasoning_CVPR_2025_paper.html)

**주제:** Embodied Perception · Navigation

## 문제
기존 object-centric 3D scene graph는 장면을 고립된 객체와 제한적 textual relationship으로 단순화해 복잡한 공간 이해가 필요한 질의에 대응하기 어렵고, active exploration과 lifelong memory 관리를 위한 자연스러운机制이 부족하다.

## 핵심 아이디어
탐험 영역의 풍부한 시각 정보를 담는 Memory Snapshots와 미탐험 영역을 보여주는 Frontier Snapshots를 결합해 알려진 정보와 잠재적 신규 정보를 함께 고려하도록 한다. 또한 incremental construction pipeline과 memory retrieval 기법으로 lifelong memory를 지원한다.

## 방법
3D-Mem은 explored region의 multi-view images를 Memory Snapshots로 저장해 compact하고 informative한 3D scene memory를 구성한다. frontier-based exploration에 Frontier Snapshots를 도입해 agent가 known information과 unexplored areas의 potential new information을 함께 고려해 의사결정하게 한다. Active exploration 환경에서 lifelong memory를 위해 incremental construction pipeline과 memory management용 memory retrieval technique을 제시한다.

## 결과
세 개의 benchmark에서 3D-Mem이 3D 환경에서 agent의 exploration 및 reasoning 능력을 크게 향상시킴을 보여 embodied AI 응용 가능성을 입증한다.

## 초록 (원문)
Constructing compact and informative 3D scene representations is essential for effective embodied exploration and reasoning, especially in complex environments over extended periods. Existing representations, such as object-centric 3D scene graphs, oversimplify spatial relationships by modeling scenes as isolated objects with restrictive textual relationships, making it difficult to address queries requiring nuanced spatial understanding. Moreover, these representations lack natural mechanisms for active exploration and memory management, hindering their application to lifelong autonomy. In this work, we propose 3D-Mem, a novel 3D scene memory framework for embodied agents. 3D-Mem employs informative multi-view images, termed Memory Snapshots, to capture rich visual information of explored regions. It further integrates frontier-based exploration by introducing Frontier Snapshots--glimpses of unexplored areas--enabling agents to make decisions by considering both known and potential new information. To support lifelong memory in active exploration settings, we present an incremental construction pipeline for 3D-Mem, as well as a memory retrieval technique for memory management. Experimental results on three benchmarks demonstrate that 3D-Mem significantly enhances agents' exploration and reasoning capabilities in 3D environments, highlighting its potential for advancing applications in embodied AI.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
