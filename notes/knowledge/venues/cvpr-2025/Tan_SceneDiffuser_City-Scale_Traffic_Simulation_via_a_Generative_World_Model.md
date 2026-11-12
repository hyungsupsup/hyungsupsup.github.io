---
title: "SceneDiffuser++: City-Scale Traffic Simulation via a Generative World Model"
tags: [cvpr2025, world-model, autonomous-driving, simulation-sim2real]
venue: CVPR 2025
arxiv: ""
citations: 
auto: true
---

> **TL;DR** SceneDiffuser++는 단일 loss로 학습된 end-to-end generative world model로 도시 규모의 point A-to-B 교통 시뮬레이션을 수행한다.

**CVPR 2025** · Shuhan Tan, John Lambert, Hong Jeon, Sakshum Kulshrestha, Yijing Bai, Jing Luo 외
[CVF](https://openaccess.thecvf.com/content/CVPR2025/html/Tan_SceneDiffuser_City-Scale_Traffic_Simulation_via_a_Generative_World_Model_CVPR_2025_paper.html)

**주제:** World Model · Autonomous Driving · Simulation & Sim2Real

## 문제
AV 테스트와 검증에 필요한 수동 주행 거리가 제한적이므로, 이를 보완할 대규모 synthetic miles와 도시 규모의 generative simulation이 필요하다.

## 핵심 아이디어
Scene generation, agent behavior modeling, occlusion reasoning, dynamic scene generation, environment simulation을 통합해 단일 loss function으로 학습된 첫 end-to-end generative world model을 제안한다.

## 방법
SceneDiffuser++는 도시 지도와 AV software stack이 주어졌을 때 AV 주변을 채우고 차량·보행자 등 dynamic agents와 traffic light 상태를 제어하며 point A-to-B 주행을 시뮬레이션한다. 또한 dynamic scene generation으로 agent를 seamless하게 spawn/remove하고, 더 큰 map region을 지원하도록 augmented된 Waymo Open Motion Dataset (WOMD)에서 평가한다.

## 결과
SceneDiffuser++의 city-scale traffic simulation 능력을 보이고, 긴 simulation 조건에서 더 우수한 realism을 보인다.

## 초록 (원문)
The goal of traffic simulation is to augment a potentially limited amount of manually-driven miles that is available for testing and validation, with a much larger amount of simulated synthetic miles. The culmination of this vision would be a generative simulated city, where given a map of the city and an autonomous vehicle (AV) software stack, the simulator can seamlessly simulate the trip from point A to point B by populating the city around the AV and controlling all aspects of the scene, from animating the dynamic agents (e.g., vehicles, pedestrians) to controlling the traffic light states. We refer to this vision as CitySim, which requires an agglomeration of simulation technologies: scene generation to populate the initial scene, agent behavior modeling to animate the scene, occlusion reasoning, dynamic scene generation to seamlessly spawn and remove agents, and environment simulation for factors such as traffic lights. While some key technologies have been separately studied in various works, others such as dynamic scene generation and environment simulation have received less attention in the research community. We propose SceneDiffuser++, the first end-to-end generative world model trained on a single loss function capable of point A-to-B simulation on a city scale integrating all the requirements above. We demonstrate the city-scale traffic simulation capability of SceneDiffuser++ and study its superior realism under long simulation conditions.We evaluate the simulation quality on an augmented version of the Waymo Open Motion Dataset (WOMD) with larger map regions to support trip-level simulation.

> 자동 생성된 요약입니다. 직접 읽은 메모는 아래에 추가하세요.

## 내 메모
