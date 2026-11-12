---
title: "SplatAD: Real-Time Lidar and Camera Rendering with 3D Gaussian Splatting for Autonomous Driving"
tags: [cvpr2025, autonomous-driving, simulation-sim2real]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** SplatAD는 자율주행 장면에서 카메라와 lidar 데이터를 실시간으로 사실적으로 렌더링하는 3D Gaussian Splatting 기반 방법이다.

**CVPR 2025** · Georg Hess, Carl Lindström, Maryam Fatemi, Christoffer Petersson, Lennart Svensson
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Hess_SplatAD_Real-Time_Lidar_and_Camera_Rendering_with_3D_Gaussian_Splatting_CVPR_2025_paper.html)

**주제:** Autonomous Driving · Simulation & Sim2Real

## 문제
자율주행 로봇의 안전 검증에는 다양한 주행 시나리오의 대규모 시뮬레이션이 필요하지만, 기존 NeRF 기반 센서 사실적 렌더링은 속도가 느리고 3DGS 기반 방법은 카메라만 지원해 lidar 렌더링이 불가능하다.

## 핵심 아이디어
SplatAD는 동적 장면에서 카메라와 lidar를 모두 실시간으로 사실적으로 렌더링하는 첫 3DGS 기반 방법으로, 센서별 특수 현상을 명시적으로 모델링한다.

## 방법
rolling shutter 효과, lidar intensity, lidar ray dropouts와 같은 센서 특화 현상을 purpose-built 알고리즘으로 모델링해 렌더링 효율을 최적화한다. 세 개의 자율주행 데이터셋에서 렌더링 품질과 속도를 평가한다.

## 결과
SplatAD는 NVS에서 최대 +2 PSNR, reconstruction에서 최대 +3 PSNR의 state-of-the-art 렌더링 품질을 달성하면서 NeRF 기반 방법보다 렌더링 속도를 order of magnitude 향상시킨다.

## 초록 (원문)
Ensuring the safety of autonomous robots, such as self-driving vehicles, requires extensive testing across diverse driving scenarios. Simulation is a key ingredient for conducting such testing in a cost-effective and scalable way. Neural rendering methods have gained popularity, as they can build simulation environments from collected logs in a data-driven manner. However, existing neural radiance field (NeRF) methods for sensor-realistic rendering of camera and lidar data suffer from low rendering speeds, limiting their applicability for large-scale testing. While 3D Gaussian Splatting (3DGS) enables real-time rendering, current methods are limited to camera data and are unable to render lidar data essential for autonomous driving. To address these limitations, we propose SplatAD, the first 3DGS-based method for realistic, real-time rendering of dynamic scenes for both camera and lidar data. SplatAD accurately models key sensor-specific phenomena such as rolling shutter effects, lidar intensity, and lidar ray dropouts, using purpose-built algorithms to optimize rendering efficiency. Evaluation across three autonomous driving datasets demonstrates that SplatAD achieves state-of-the-art rendering quality with up to +2 PSNR for NVS and +3 PSNR for reconstruction while increasing rendering speed over NeRF-based methods by an order of magnitude. Code to be released upon publication.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
