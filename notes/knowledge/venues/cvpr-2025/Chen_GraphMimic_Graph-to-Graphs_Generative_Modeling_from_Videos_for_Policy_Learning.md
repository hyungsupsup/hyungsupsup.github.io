---
title: "GraphMimic: Graph-to-Graphs Generative Modeling from Videos for Policy Learning"
tags: [cvpr2025, imitation-learning, manipulation, world-model]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** GraphMimic은 비디오 프레임을 그래프로 추상화하고 미래 그래프를 생성하도록 사전학습하여 소량의 action-labeled 데이터로 로봇 정책을 학습하는 방법이다.

**CVPR 2025** · Guangyan Chen, Te Cui, Meiling Wang, Chengcai Yang, Mengxiao Hu, Haoyang Lu 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Chen_GraphMimic_Graph-to-Graphs_Generative_Modeling_from_Videos_for_Policy_Learning_CVPR_2025_paper.html)

**주제:** Imitation Learning · Manipulation · World Model

## 문제
로봇 skill acquisition에서 action-labeled robot data 수집 비용이 큰 bottleneck이며, 풍부한 video data를 policy learning에 효과적으로 활용하는 방법이 필요하다.

## 핵심 아이디어
비디오 프레임을 object 및 visual action vertices로 구성된 graph로 표현하고, graph-to-graphs generative modeling으로 미래 graph를 예측하며, 이를 control policy의 condition으로 사용한다.

## 방법
GraphMimic은 각 video frame을 state representation graph로 추상화하고 graph generative network가 graph 내부 구조와 spatial relationship을 모델링해 future graph를 생성한다. 생성된 graph는 robot action으로 mapping되는 control policy의 condition으로 쓰이며, transferable graph representation은 cross-embodiment video에서 manipulation skill 학습을 돕는다.

## 결과
GraphMimic은 단 20%의 action-labeled data만으로 우수한 성능을 보이고, simulation 및 real-world 실험에서 state-of-the-art method를 각각 over 17%, 23% 능가하며 cross-embodiment transfer 실험에서 over 33% 개선을 달성한다.

## 초록 (원문)
Learning from demonstration is a powerful method for robotic skill acquisition. However, the significant expense of collecting such action-labeled robot data presents a major bottleneck. Video data, a rich data source encompassing diverse behavioral and physical knowledge, emerges as a promising alternative. In this paper, we present GraphMimic, a novel paradigm that leverages video data via graph-to-graphs generative modeling, which pre-trains models to generate future graphs conditioned on the graph within a video frame. Specifically, GraphMimic abstracts video frames into object and visual action vertices, and constructs graphs for state representations. The graph generative modeling network then effectively models internal structures and spatial relationships within the constructed graphs, aiming to generate future graphs. The generated graphs serve as conditions for the control policy, mapping to robot actions. Our concise approach captures important spatial relations and enhances future graph generation accuracy, enabling the acquisition of robust policies from limited action-labeled data. Furthermore, the transferable graph representations facilitate the effective learning of manipulation skills from cross-embodiment videos. Our experiments exhibit that GraphMimic achieves superior performance using merely 20% action-labeled data. Moreover, our method outperforms the state-of-the-art method by over 17% and 23% in simulation and real-world experiments, and delivers improvements of over 33% in cross-embodiment transfer experiments.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
