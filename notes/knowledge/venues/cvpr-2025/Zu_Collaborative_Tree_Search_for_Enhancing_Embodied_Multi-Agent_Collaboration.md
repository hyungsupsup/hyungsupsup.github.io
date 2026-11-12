---
title: "Collaborative Tree Search for Enhancing Embodied Multi-Agent Collaboration"
tags: [cvpr2025, other]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** LLM 기반 embodied multi-agent의 협업 계획을 modified Monte Carlo tree와 plan evaluation module로 개선하는 CoTS를 제안한다.

**CVPR 2025** · Lizheng Zu, Lin Lin, Song Fu, Na Zhao, Pan Zhou
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zu_Collaborative_Tree_Search_for_Enhancing_Embodied_Multi-Agent_Collaboration_CVPR_2025_paper.html)

**주제:** Other

## 문제
LLM 기반 embodied agents가 협업 작업에서 효과적인 의사소통과 역할 분담을 달성하기 어렵고, 단순한 communication 패턴이 잘못되거나 일관성 없는 action을 유발해 추가 위험을 만든다.

## 핵심 아이디어
multi-agent가 수정된 Monte Carlo tree 안에서 장기 전략 계획을 논의하고 LLM-driven reward function을 따라 탐색하게 하며, plan evaluation module로 빈번한 plan update로 인한 action 혼란을 막으면서 필요할 때 plan을 갱신한다.

## 방법
CoTS는 multi-agent 토론을 modified Monte Carlo tree search로 구성해 LLM 기반 reward를 따라 협업 plan 후보를 탐색한다. plan evaluation module이 현재 plan의 적합성을 평가해 불필요한 업데이트를 억제하고 부적합할 때만 갱신한다. 이를 통해 long-term complex task에서 planning, communication, collaboration을 개선한다.

## 결과
CWAH와 TDW-MAT embodied environments에서 planning, communication, collaboration 성능이 우수해 long-term complex tasks를 효율적으로 완수하고 기존 방법을 크게 능가한다고 보고한다.

## 초록 (원문)
Embodied agents based on large language models (LLMs) face significant challenges in collaborative tasks, requiring effective communication and reasonable division of labor to ensure efficient and correct task completion. Previous approaches with simple communication patterns carry erroneous or incoherent agent actions, which can lead to additional risks. To address these problems, we propose Cooperative Tree Search (CoTS), a framework designed to significantly improve collaborative planning and task execution efficiency among embodied agents. CoTS guides multi-agents to discuss long-term strategic plans within a modified Monte Carlo tree, searching along LLM-driven reward functions to provide a more thoughtful and promising approach to cooperation. Another key feature of our method is the introduction of a plan evaluation module, which not only prevents agent action confusion caused by frequent plan updates but also ensures plan updates when the current plan becomes unsuitable. Experimental results show that the proposed method performs excellently in planning, communication, and collaboration on embodied environments (CWAH and TDW-MAT), efficiently completing long-term, complex tasks and significantly outperforming existing methods.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
