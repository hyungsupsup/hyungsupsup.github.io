---
title: "Visual Agentic AI for Spatial Reasoning with a Dynamic API"
tags: [cvpr2025, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2502.06787"
citations: 72
auto: true
---

> **TL;DR** LLM 에이전트가 새로운 함수를 스스로 생성하는 동적 Pythonic API를 만들어 3D 공간 추론 문제를 푸는 agentic program synthesis 방법과 새로운 벤치마크를 제안한다.

**CVPR 2025** · Damiano Marsili, Rohun Agrawal, Yisong Yue, Georgia Gkioxari
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Marsili_Visual_Agentic_AI_for_Spatial_Reasoning_with_a_Dynamic_API_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2502.06787) · 인용 72회

**주제:** Embodied Perception · Dataset & Benchmark

## 문제
3D 장면에서 동작하는 embodied agent에게 시각적 추론은 중요하지만, 기존 vision/language 모델은 3D 공간 추론 과제에서 성능이 크게 떨어진다. 또한 기존 접근은 사람이 미리 정의한 정적 API에 의존해 처리 가능한 질의 범위가 제한된다.

## 핵심 아이디어
정적이고 수작업으로 정의된 API 대신, LLM 에이전트들이 협력하여 공통 하위 문제를 해결하는 새로운 함수를 포함한 Pythonic API를 즉석에서 생성하도록 한다. 이를 통해 더 다양한 3D 공간 추론 질의를 처리할 수 있다.

## 방법
LLM 에이전트들이 협업하여 하위 문제용 함수들을 담은 Pythonic API를 program synthesis 방식으로 생성하고, 생성된 프로그램을 실행해 질의를 해결한다. 또한 grounding과 inference가 여러 단계로 이어지는 질의들로 구성된 3D 이해 벤치마크를 새로 제안하여 평가한다.

## 결과
제안 방법은 3D 시각 추론에서 기존 zero-shot 모델들을 능가하며, agentic 프레임워크가 3D 공간 추론 과제에 효과적임을 실험적으로 검증했다.

## 초록 (원문)
Visual reasoning -- the ability to interpret the visual world -- is crucial for embodied agents that operate within three-dimensional scenes. Progress in AI has led to vision and language models capable of answering questions from images. However, their performance declines when tasked with 3D spatial reasoning. To tackle the complexity of such reasoning problems, we introduce an agentic program synthesis approach where LLM agents collaboratively generate a Pythonic API with new functions to solve common subproblems. Our method overcomes limitations of prior approaches that rely on a static, human-defined API, allowing it to handle a wider range of queries. To assess AI capabilities for 3D understanding, we introduce a new benchmark of queries involving multiple steps of grounding and inference. We show that our method outperforms prior zero-shot models for visual reasoning in 3D and empirically validate the effectiveness of our agentic framework for 3D spatial reasoning tasks. Project website: https://glab-caltech.github.io/vadar/

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
