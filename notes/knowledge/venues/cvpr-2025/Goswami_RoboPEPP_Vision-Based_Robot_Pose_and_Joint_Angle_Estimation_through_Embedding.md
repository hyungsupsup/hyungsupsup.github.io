---
title: "RoboPEPP: Vision-Based Robot Pose and Joint Angle Estimation through Embedding Predictive Pre-Training"
tags: [cvpr2025, embodied-perception]
venue: CVPR 2025
arxiv: "2411.17662"
citations: 19
auto: true
---

> **TL;DR** RoboPEPP는 masking 기반 self-supervised embedding-predictive pre-training으로 로봇의 physical model 정보를 encoder에 융합해 pose와 joint angle을 추정하는 방법이다.

**CVPR 2025** · Raktim Gautam Goswami, Prashanth Krishnamurthy, Yann LeCun, Farshad Khorrami
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Goswami_RoboPEPP_Vision-Based_Robot_Pose_and_Joint_Angle_Estimation_through_Embedding_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.17662) · 인용 19회

**주제:** Embodied Perception

## 문제
관절 각도를 모르는 articulated robot의 vision-based pose estimation에서 기존 방법은 로봇 이미지에 담긴 physical structure 정보를 충분히 활용하지 못해 occlusion과 truncation 상황에서 성능이 제한된다.

## 핵심 아이디어
로봇의 joint를 mask하고 주변 unmasked 영역에서 joint embedding을 예측하도록 encoder-predictor를 pre-train하여 encoder가 로봇의 physical model을 더 잘 이해하도록 만든다.

## 방법
Masking-based self-supervised embedding-predictive architecture로 encoder-predictor를 pre-train한 뒤 joint angle 및 keypoint prediction networks와 함께 fine-tuning한다. Fine-tuning 중 random masking과 evaluation 중 keypoint filtering을 적용해 robustness를 높인다.

## 결과
여러 dataset에서 robot pose 및 joint angle estimation의 best results를 달성했고 occlusion에 가장 덜 민감하며 lowest execution time을 보인다.

## 초록 (원문)
Vision-based pose estimation of articulated robots with unknown joint angles has applications in collaborative robotics and human-robot interaction tasks. Current frameworks use neural network encoders to extract image features and downstream layers to predict joint angles and robot pose. While images of robots inherently contain rich information about the robot's physical structures, existing methods often fail to leverage it fully; therefore, limiting performance under occlusions and truncations. To address this, we introduce RoboPEPP, a method that fuses information about the robot's physical model into the encoder using a masking-based self-supervised embedding-predictive architecture. Specifically, we mask the robot's joints and pre-train an encoder-predictor model to infer the joints' embeddings from surrounding unmasked regions, enhancing the encoder's understanding of the robot's physical model. The pre-trained encoder-predictor pair, along with joint angle and keypoint prediction networks, is then fine-tuned for pose and joint angle estimation. Random masking of input during fine-tuning and keypoint filtering during evaluation further improves robustness. Our method, evaluated on several datasets, achieves the best results in robot pose and joint angle estimation while being the least sensitive to occlusions and requiring the lowest execution time.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
