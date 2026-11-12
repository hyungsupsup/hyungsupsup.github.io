---
title: "CityWalker: Learning Embodied Urban Navigation from Web-Scale Videos"
tags: [cvpr2025, navigation, imitation-learning, dataset-benchmark]
venue: CVPR 2025
arxiv: "2411.17820"
citations: 85
auto: true
---

> **TL;DR** 웹에서 수집한 대규모 도시 보행·주행 영상으로부터 행동 감독을 추출해 embodied agent의 도시 내비게이션 정책을 imitation learning으로 학습하는 방법을 제안한다.

**CVPR 2025** · Xinhao Liu, Jintong Li, Yicheng Jiang, Niranjan Sujay, Zhicheng Yang, Juexiao Zhang 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Liu_CityWalker_Learning_Embodied_Urban_Navigation_from_Web-Scale_Videos_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.17820) · 인용 85회

**주제:** Navigation · Imitation Learning · Dataset & Benchmark

## 문제
기존 visual navigation 방법은 map-free 또는 off-street 환경에서 어려움을 겪어 last-mile delivery robot과 같은 자율 agent의 실제 배치를 제한한다.

## 핵심 아이디어
비싼 annotation 없이 웹 규모의 in-the-wild 도시 보행 및 주행 영상에서 action supervision을 추출하는 확장 가능한 데이터 처리 pipeline을 통해 대규모 imitation learning을 가능하게 한다.

## 방법
수천 시간의 웹 도시 영상으로부터 간단하고 확장 가능한 pipeline으로 action supervision을 추출한다. 이렇게 구축한 대규모·다양한 데이터로 agent의 navigation policy를 imitation learning 방식으로 학습시켜 다양한 도전과 critical scenario에 대응하게 한다.

## 결과
대규모의 다양한 dataset으로 학습하면 navigation 성능이 크게 향상되어 현재 방법들을 능가한다. 이는 풍부한 온라인 영상 데이터로 동적 도시 환경의 embodied agent를 위한 robust navigation policy를 개발할 수 있음을 보여준다.

## 연결
- **기반 대표 논문:** PaLM-E — [[knowledge/map|분야 지도]]

## 초록 (원문)
Navigating dynamic urban environments presents significant challenges for embodied agents, requiring advanced spatial reasoning and adherence to common-sense norms. Despite progress, existing visual navigation methods struggle in map-free or off-street settings, limiting the deployment of autonomous agents like last-mile delivery robots. To overcome these obstacles, we propose a scalable, data-driven approach for human-like urban navigation by training agents on thousands of hours of in-the-wild city walking and driving videos sourced from the web. We introduce a simple and scalable data processing pipeline that extracts action supervision from these videos, enabling large-scale imitation learning without costly annotations. Our model learns sophisticated navigation policies to handle diverse challenges and critical scenarios. Experimental results show that training on large-scale, diverse datasets significantly enhances navigation performance, surpassing current methods. This work shows the potential of using abundant online video data to develop robust navigation policies for embodied agents in dynamic urban settings.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
