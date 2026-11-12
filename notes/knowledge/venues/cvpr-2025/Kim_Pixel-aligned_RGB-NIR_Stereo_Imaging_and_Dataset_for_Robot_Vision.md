---
title: "Pixel-aligned RGB-NIR Stereo Imaging and Dataset for Robot Vision"
tags: [cvpr2025, dataset-benchmark, embodied-perception]
venue: CVPR 2025
arxiv: "2411.18025"
citations: 13
auto: true
---

> **TL;DR** RGB와 NIR을 픽셀 단위로 정렬한 스테레오 카메라와 LiDAR를 모바일 로봇에 장착해 다양한 조명 조건의 데이터셋을 제안하고, 이를 활용한 RGB-NIR 융합 방법을 제시한다.

**CVPR 2025** · Jinnyeong Kim, Seung-Hwan Baek
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Kim_Pixel-aligned_RGB-NIR_Stereo_Imaging_and_Dataset_for_Robot_Vision_CVPR_2025_paper.html) · [arXiv](https://arxiv.org/abs/2411.18025) · 인용 13회

**주제:** Dataset & Benchmark · Embodied Perception

## 문제
기존 RGB-NIR 데이터셋과 이미징 시스템은 RGB와 NIR 이미지 간 픽셀 수준 정렬이 없어 downstream 작업에 어려움이 있다.

## 핵심 아이디어
두 대의 pixel-aligned RGB-NIR stereo camera와 LiDAR를 모바일 로봇에 장착해 RGB 스테레오, NIR 스테레오, 시간 동기화된 LiDAR point cloud를 동시에 수집한다. 또한 pixel-aligned RGB-NIR 이미지를 활용하는 image fusion 방법과 feature fusion 방법을 제안한다.

## 방법
로봇의 이동성을 활용해 다양한 조명 조건에서 연속 video frame과 pixel-aligned RGB/NIR stereo pair를 포함한 데이터셋을 제공한다. 첫 번째 방법은 기존 RGB-pretrained vision model이 fine-tuning 없이 RGB-NIR 정보를 직접 사용하도록 하고, 두 번째 방법은 기존 vision model을 fine-tuning해 RGB-NIR 정보를 더 효과적으로 활용하도록 한다.

## 결과
실험 결과 다양한 조명 조건에서 pixel-aligned RGB-NIR 이미지를 사용하는 것의 효과를 입증했다.

## 초록 (원문)
Integrating RGB and NIR imaging provides complementary spectral information, enhancing robotic vision in challenging lighting conditions. However, existing datasets and imaging systems lack pixel-level alignment between RGB and NIR images, posing challenges for downstream tasks.In this paper, we develop a robotic vision system equipped with two pixel-aligned RGB-NIR stereo cameras and a LiDAR sensor mounted on a mobile robot. The system simultaneously captures RGB stereo images, NIR stereo images, and temporally synchronized LiDAR point cloud. Utilizing the mobility of the robot, we present a dataset containing continuous video frames with pixel-aligned RGB and NIR stereo pairs under diverse lighting conditions.We introduce two methods that utilize our pixel-aligned RGB-NIR images: an RGB-NIR image fusion method and a feature fusion method. The first approach enables existing RGB-pretrained vision models to directly utilize RGB-NIR information without fine-tuning. The second approach fine-tunes existing vision models to more effectively utilize RGB-NIR information.Experimental results demonstrate the effectiveness of using pixel-aligned RGB-NIR images across diverse lighting conditions.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
