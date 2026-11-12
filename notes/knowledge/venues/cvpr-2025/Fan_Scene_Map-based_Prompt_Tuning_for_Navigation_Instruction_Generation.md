---
title: "Scene Map-based Prompt Tuning for Navigation Instruction Generation"
tags: [cvpr2025, navigation, embodied-perception]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** MAPInstructor는 scene map 기반 prompt tuning으로 LLM을 활용해 navigation instruction을 생성하는 프레임워크다.

**CVPR 2025** · Sheng Fan, Rui Liu, Wenguan Wang, Yi Yang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Fan_Scene_Map-based_Prompt_Tuning_for_Navigation_Instruction_Generation_CVPR_2025_paper.html)

**주제:** Navigation · Embodied Perception

## 문제
기존 navigation instruction generation 방법은 복잡한 3D 환경의 공간적 이해와 전역 지도 맥락을 충분히 활용하지 못한다.

## 핵심 아이디어
지도에 대한 텍스트 설명을 LLM에 직접 입력하는 대신, scene map 기반 prompt tuning으로 map context를 LLM decoder에 통합한다.

## 방법
Egocentric observation을 3D voxel로 투영해 scene representation을 인코딩하고, 전체 trajectory의 topological map representation을 LLM 기반 decoder에 map prompt로 통합한다. 또한 landmark uncertainty assessment를 통해 landmark 예측의 hallucination을 완화한다.

## 결과
R2R, REVERIE, RxR 세 navigation dataset에서 실험을 통해 알고리즘의 일반화 성능과 효과를 확인했다.

## 초록 (원문)
Navigation instruction generation (NIG), which provides interactive feedback and guidance to humans along a trajectory, is vital for developing embodied agents capable of human-machine communication and collaboration through natural language. Early data-driven methods directly map sequences of past observations to trajectory descriptions on limited datasets, lacking the necessary spatial understanding in complex 3D environments. While recent approaches leverage Large Language Models (LLMs) to improve NIG, they often overlook the global spatial context in navigation, such as the inherent space discretization in maps. Instead of straightforwardly feeding textual descriptions of the map into LLMs, we propose a scene map-based prompt tuning framework for NIG, MAPInstructor, which incorporates map context for parameter-efficient updating of LLMs. MAPInstructor comprises three key components: (i) scene representation encoding, where egocentric observations are projected into 3D voxels for fine-grained scene understanding; (ii) map prompt tuning, which integrates a topological map representation of the entire trajectory into an LLM-based decoder; and (iii) landmark uncertainty assessment, which mitigates hallucinations in landmark predictions, thereby enhancing the reliability and coherence of instruction generation. Extensive experiments on three navigation datasets (i.e., R2R, REVERIE, RxR) confirm the generalization and effectiveness of our algorithm.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
