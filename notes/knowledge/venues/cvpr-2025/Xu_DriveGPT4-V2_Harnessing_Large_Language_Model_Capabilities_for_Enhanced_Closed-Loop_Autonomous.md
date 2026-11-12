---
title: "DriveGPT4-V2: Harnessing Large Language Model Capabilities for Enhanced Closed-Loop Autonomous Driving"
tags: [cvpr2025, autonomous-driving, imitation-learning, vla]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** DriveGPT4-V2는 MLLM을 활용해 카메라 이미지와 차량 상태로부터 저수준 제어 신호를 생성하는 closed-loop 자율주행 모델이다.

**CVPR 2025** · Zhenhua Xu, Yan Bai, Yujia Zhang, Zhuoling Li, Fei Xia, Kwan-Yee K. Wong 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Xu_DriveGPT4-V2_Harnessing_Large_Language_Model_Capabilities_for_Enhanced_Closed-Loop_Autonomous_CVPR_2025_paper.html)

**주제:** Autonomous Driving · Imitation Learning · VLA

## 문제
기존 DriveGPT4-V1은 open-loop 작업에 초점을 맞추어, LLM의 추론 능력을 closed-loop 자율주행에 활용하는 것이 필요하다.

## 핵심 아이디어
다중 시점 시각 토크나이저(MV-VT)로 넓은 환경을 인식하면서 세부 정보를 유지하고, 특권 정보를 활용하는 expert LLM과의 online imitation learning으로 예측과 추론 속도를 개선한다.

## 방법
DriveGPT4-V2는 카메라 이미지와 차량 상태를 입력받아 end-to-end 차량 운전을 위한 저수준 제어 신호를 출력한다. MV-VT를 통해 다중 시점 환경을 효율적으로 토큰화하며, 의사결정 예측과 추론 속도를 높이도록 모델 구조를 개선했다. 또한 주변 객체의 특권 정보에 접근할 수 있는 expert LLM을 추가로 학습해 online imitation learning을 수행한다.

## 결과
실험 결과 DriveGPT4-V2는 challenging CARLA Longest6 benchmark에서 모든 baseline을 능가했으며, 코드와 데이터는 공개될 예정이다.

## 초록 (원문)
Multimodal large language models (MLLMs) possess the ability to comprehend visual images or videos, and show impressive reasoning ability thanks to the vast amounts of pretrained knowledge, making them highly suitable for autonomous driving applications. Unlike the previous work, DriveGPT4-V1, which focused on open-loop tasks, this study explores the capabilities of LLMs in enhancing closed-loop autonomous driving. DriveGPT4-V2 processes camera images and vehicle states as input to generate low-level control signals for end-to-end vehicle operation. A multi-view visual tokenizer (MV-VT) is employed enabling DriveGPT4-V2 to perceive the environment with an extensive range while maintaining critical details. The model architecture has been refined to improve decision prediction and inference speed. To further enhance the performance, an additional expert LLM is trained for online imitation learning. The expert LLM, sharing a similar structure with DriveGPT4-V2, can access privileged information about surrounding objects for more robust and reliable predictions. Experimental results show that DriveGPT4-V2 outperforms all baselines on the challenging CARLA Longest6 benchmark. The code and data of DriveGPT4-V2 will be publicly available.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
