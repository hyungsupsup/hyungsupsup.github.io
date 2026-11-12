---
title: "Learning Physics From Video: Unsupervised Physical Parameter Estimation for Continuous Dynamical Systems"
tags: [cvpr2025, simulation-sim2real]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** 단일 비디오에서 알려진 연속 동역학계의 물리 파라미터를 비지도로 추정하는 방법을 제안하고, 실제 Delfys75 데이터셋으로 검증한다.

**CVPR 2025** · Alejandro Castañeda Garcia, Jan Warchocki, Jan van Gemert, Daan Brinks, Nergis Tomen
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Garcia_Learning_Physics_From_Video_Unsupervised_Physical_Parameter_Estimation_for_Continuous_CVPR_2025_paper.html)

**주제:** Simulation & Sim2Real

## 문제
비디오 기반 물리 파라미터 추정은 라벨이 필요한 supervised 학습에 의존하거나, 기존 unsupervised 방법이 긴 학습 시간·초기화 불안정·운동 기반 시스템에 국한되고 주로 synthetic data에서 평가되는 문제가 있다.

## 핵심 아이디어
프레임 예측 대신 latent space의 KL-divergence 기반 loss를 사용해 trivial solution을 피하고 모델 크기와 계산량을 줄이며, 운동 외 다양한 동역학계와 초기화에 robust한 unsupervised parameter estimation을 가능하게 한다.

## 방법
알려진 연속 지배 방정식을 가정하고 단일 비디오로부터 물리 파라미터를 비지도 추정한다. Frame prediction 없이 latent space에서 KL-divergence loss를 적용해 학습하며, synthetic data와 5가지 동역학계 유형의 75개 실제 비디오로 구성된 Delfys75에서 평가한다.

## 결과
Synthetic data와 Delfys75(75개 비디오, 5가지 동역학계 유형)에서 기존 방법보다 우수한 성능을 보인다. Code와 data는 공개되어 있다.

## 초록 (원문)
Extracting physical dynamical system parameters from recorded observations is key in natural science. Current methods for automatic parameter estimation from video train supervised deep networks on large datasets. Such datasets require labels, which are difficult to acquire. While some unsupervised techniques--which depend on frame prediction--exist, they suffer from long training times, initialization instabilities, only consider motion-based dynamical systems, and are evaluated mainly on synthetic data. In this work, we propose an unsupervised method to estimate the physical parameters of known, continuous governing equations from single videos suitable for different dynamical systems beyond motion and robust to initialization. Moreover, we remove the need for frame prediction by implementing a KL-divergence-based loss function in the latent space, which avoids convergence to trivial solutions and reduces model size and compute. We first evaluate our model on synthetic data, as commonly done. After which, we take the field closer to reality by recording Delfys75: our own real-world dataset of 75 videos for five different types of dynamical systems to evaluate our method and others. Our method compares favorably to others. Code and data are available online: https://github.com/Alejandro-neuro/Learning_physics_from_video.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
