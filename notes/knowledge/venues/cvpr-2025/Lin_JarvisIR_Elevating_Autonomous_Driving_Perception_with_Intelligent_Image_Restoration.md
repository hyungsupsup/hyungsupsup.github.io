---
title: "JarvisIR: Elevating Autonomous Driving Perception with Intelligent Image Restoration"
tags: [cvpr2025, autonomous-driving, embodied-perception, dataset-benchmark]
venue: CVPR 2025
arxiv: "2504.04158"
citations: 62
auto: true
---

> **TL;DR** JarvisIR는 VLM을 컨트롤러로 사용해 여러 expert restoration 모델을 관리하여 악천후에서 자율주행 인지 성능을 향상시키는 agent이다.

**CVPR 2025** · Yunlong Lin, Zixu Lin, Haoyu Chen, Panwang Pan, Chenxin Li, Sixiang Chen 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Lin_JarvisIR_Elevating_Autonomous_Driving_Perception_with_Intelligent_Image_Restoration_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.04158) · 인용 62회

**주제:** Autonomous Driving · Embodied Perception · Dataset & Benchmark

## 문제
야외의 예측 불가능하고 복합적인 날씨 열화로 인해 vision-centric 자율주행 인지 시스템이 성능 저하를 겪으며, 기존 해법은 특정 degradation prior에 의존하거나 큰 domain gap을 가진다.

## 핵심 아이디어
Llava-Llama3 기반 VLM agent가 여러 expert restoration 모델을 선택·관리하고, supervised fine-tuning과 human feedback alignment의 two-stage framework로 real-world adverse weather에서 robustness와 generalizability를 높인다.

## 방법
JarvisIR는 VLM을 controller로 두고 expert restoration models를 운용하며, 1단계 supervised fine-tuning 후 2단계 human feedback alignment로 대규모 real-world unpaired data에서 unsupervised 방식으로 fine-tuning한다. 또한 150K synthetic 및 80K real instruction-response pairs를 포함한 CleanBench를 구축해 학습과 평가에 사용한다.

## 결과
CleanBench-Real에서 기존 방법 대비 모든 perception metrics 평균 50% 향상을 달성하고 우수한 decision-making 및 restoration capabilities를 보인다.

## 초록 (원문)
Vision-centric perception systems often struggle with unpredictable and coupled weather degradations in the wild. Current solutions are often limited, as they either depend on specific degradation priors or suffer from significant domain gaps. To enable robust and autonomous operation in real-world conditions, we propose JarvisIR, a VLM-powered agent that leverages the VLM (e.g., Llava-Llama3) as a controller to manage multiple expert restoration models. To further enhance system robustness, reduce hallucinations, and improve generalizability in real-world adverse weather, JarvisIR employs a novel two-stage framework consisting of supervised fine-tuning and human feedback alignment. Specifically, to address the lack of paired data in real-world scenarios, the human feedback alignment enables the VLM to be fine-tuned effectively on large-scale real-world data in an unsupervised manner. To support the training and evaluation of JarvisIR, we introduce CleanBench, a comprehensive dataset consisting of high-quality and large-scale instruction-responses pairs, including 150K synthetic entries and 80K real entries. Extensive experiments demonstrate that JarvisIR exhibits superior decision-making and restoration capabilities. Compared with existing methods, it achieves a 50% improvement in the average of all perception metrics on CleanBench-Real.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
