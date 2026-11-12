---
title: "MPDrive: Improving Spatial Understanding with Marker-Based Prompt Learning for Autonomous Driving"
tags: [cvpr2025, autonomous-driving, embodied-perception]
venue: CVPR 2025
arxiv: "2504.00379"
citations: 24
auto: true
---

> **TL;DR** MPDrive는 자율주행 VQA에서 공간 좌표를 시각적 marker로 표현하는 Marker-based Prompt learning 프레임워크를 제안한다.

**CVPR 2025** · Zhiyuan Zhang, Xiaofan Li, Zhihao Xu, Wenjie Peng, Zijian Zhou, Miaojing Shi 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Zhang_MPDrive_Improving_Spatial_Understanding_with_Marker-Based_Prompt_Learning_for_Autonomous_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.00379) · 인용 24회

**주제:** Autonomous Driving · Embodied Perception

## 문제
기존 AD-VQA 방법들은 공간 정보를 텍스트 좌표로 표현해 시각적 좌표 표현과 텍스트 설명 사이의 semantic gap이 발생하고, 공간 정보 전달 정확도가 떨어지며 표현 부담이 커진다.

## 핵심 아이디어
복잡한 텍스트 좌표 생성 대신 객체 영역에 숫자 라벨을 오버레이한 marker 이미지를 사용해 공간 좌표를 간결한 시각적 marker 예측으로 변환하고, 언어적 표현 일관성과 공간 이해를 높인다.

## 방법
Detection expert로 객체 영역에 numerical label을 입힌 marker 이미지를 생성하고, 이를 원본 이미지와 융합한 scene-level feature 및 detection prior 기반 instance-level feature를 만든다. 이렇게 구성한 dual-granularity visual prompt로 LLM의 공간 지각 능력을 자극한다.

## 결과
DriveLM과 CODA-LM 데이터셋에서 MPDrive가 state-of-the-art 성능을 달성했으며, 특히 복잡한 공간 이해가 필요한 경우에 우수하다.

## 초록 (원문)
Autonomous driving visual question answering (AD-VQA) aims to answer questions related to perception, prediction, and planning based on given driving scene images, heavily relying on the model's spatial understanding capabilities. Prior works typically express spatial information through textual representations of coordinates, resulting in semantic gaps between visual coordinate representations and textual descriptions. This oversight hinders the accurate transmission of spatial information and increases the expressive burden. To address this, we propose a novel Marker-based Prompt learning framework (MPDrive), which represents spatial coordinates by concise visual markers, ensuring linguistic expressive consistency and enhancing the accuracy of both visual perception and spatial expression in AD-VQA. Specifically, we create marker images by employing a detection expert to overlay object regions with numerical labels, converting complex textual coordinate generation into straightforward text-based visual marker predictions. Moreover, we fuse original and marker images as scene-level features and integrate them with detection priors to derive instance-level features. By combining these features, we construct dual-granularity visual prompts that stimulate the LLM's spatial perception capabilities. Extensive experiments on the DriveLM and CODA-LM datasets show that MPDrive achieves state-of-the-art performance, particularly in cases requiring sophisticated spatial understanding.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
