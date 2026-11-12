---
title: 시뮬레이션 & Sim2Real
date: 2026-11-12
tags: [topic, sim2real, isaac-sim]
status: 작성 중
---

## 한 줄 정의
시뮬레이터에서 학습하거나 데이터를 만든 다음, 실제 로봇으로 옮기는 문제. 핵심은 시뮬레이션과 현실 사이의 차이(reality gap)를 다루는 것이다.

## 접근법 (채워 나갈 것)
| 접근 | 내용 | 대표 |
|---|---|---|
| Domain Randomization | 시각·물리 파라미터를 무작위로 바꿔서 학습 | Tobin et al. 2017 |
| 적응 (Adaptation) | 실제 환경에 맞춰 온라인으로 적응 | RMA |
| 생성모델 증강 💡 | 시뮬레이션 영상을 실사처럼 변환 | Cosmos Transfer |
| 대규모 병렬 시뮬레이션 | GPU에서 수천 개 환경을 동시에 돌림 | Isaac Gym, Isaac Lab |

## 도구
- Isaac Sim 6.2 — [[lab/experiments/000-isaac-sim-setup]]

## 관련 노트
- 실험: [[lab/experiments/000-isaac-sim-setup]]
