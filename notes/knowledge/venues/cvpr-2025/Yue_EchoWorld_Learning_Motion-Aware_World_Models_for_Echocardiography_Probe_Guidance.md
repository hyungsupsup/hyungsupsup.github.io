---
title: "EchoWorld: Learning Motion-Aware World Models for Echocardiography Probe Guidance"
tags: [cvpr2025, world-model, embodied-perception, other]
venue: CVPR 2025
arxiv: "2504.13065"
citations: 25
auto: true
---

> **TL;DR** EchoWorld는 심초음파 probe guidance를 위해 anatomical knowledge와 probe motion에 따른 visual dynamics를 학습하는 motion-aware world model이다.

**CVPR 2025** · Yang Yue, Yulin Wang, Haojun Jiang, Pan Liu, Shiji Song, Gao Huang
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Yue_EchoWorld_Learning_Motion-Aware_World_Models_for_Echocardiography_Probe_Guidance_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2504.13065) · 인용 25회

**주제:** World Model · Embodied Perception · Other

## 문제
심초음파 probe guidance 모델은 heart anatomy와 probe motion과 visual signal의 복잡한 상호작용을 이해해야 하지만 기존 방법은 이를 효과적으로 포착하지 못한다. 이는 experienced sonographer 의존과 정확한 standard plane acquisition의 어려움으로 이어진다.

## 핵심 아이디어
world modeling 원리에 착안한 pre-training으로 masked anatomical regions 예측과 probe 조정의 visual outcome simulation을 수행하고, fine-tuning에서 motion-aware attention으로 past visual-motion sequences를 통합한다.

## 방법
EchoWorld는 pre-training 단계에서 masked anatomical region prediction과 probe adjustment에 따른 visual outcome simulation을 통해 anatomical knowledge와 motion-induced visual dynamics를 학습한다. Fine-tuning 단계에서는 motion-aware attention mechanism을 도입해 historical visual-motion data를 효과적으로 결합한다. 이를 통해 real-time movement instructions를 위한 precise and adaptive probe guidance를 제공한다.

## 결과
more than one million ultrasound images from over 200 routine scans로 학습되어 qualitative analysis에서 key echocardiographic knowledge 포착을 검증했다. 기존 visual backbones 및 guidance frameworks 대비 guidance errors를 significantly reduces하며 single-frame and sequential evaluation protocols 모두에서 우수하다.

## 연결
- **기반 대표 논문:** Dreamer (v1), DreamerV3, Open X-Embodiment (데이터셋), OpenVLA, RT-2, World Models (Ha & Schmidhuber) — [[knowledge/map|분야 지도]]

## 초록 (원문)
Echocardiography is crucial for cardiovascular disease detection but relies heavily on experienced sonographers. Echocardiography probe guidance systems, which provide real-time movement instructions for acquiring standard plane images, offer a promising solution for AI-assisted or fully autonomous scanning. However, developing effective machine learning models for this task remains challenging, as they must grasp heart anatomy and the intricate interplay between probe motion and visual signals. To address this, we present EchoWorld, a motion-aware world modeling framework for probe guidance that encodes anatomical knowledge and motion-induced visual dynamics, while effectively leveraging past visual-motion sequences to enhance guidance precision. EchoWorld employs a pre-training strategy inspired by world modeling principles, where the model predicts masked anatomical regions and simulates the visual outcomes of probe adjustments. Built upon this pre-trained model, we introduce a motion-aware attention mechanism in the fine-tuning stage that effectively integrates historical visual-motion data, enabling precise and adaptive probe guidance. Trained on more than one million ultrasound images from over 200 routine scans, EchoWorld effectively captures key echocardiographic knowledge, as validated by qualitative analysis. Moreover, our method significantly reduces guidance errors compared to existing visual backbones and guidance frameworks, excelling in both single-frame and sequential evaluation protocols. Code is available at https://github.com/LeapLabTHU/EchoWorld.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
