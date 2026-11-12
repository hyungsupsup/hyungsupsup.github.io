---
title: 월드모델 (World Models)
date: 2026-11-12
tags: [topic, world-model]
status: 작성 중
---

## 한 줄 정의
"현재 상태와 행동이 주어지면 다음 상태(관측)를 예측하는" 환경의 학습된 모델. 정책 학습(상상 속 RL), 계획, 데이터 생성, 정책 평가에 쓴다.

## 두 갈래 (채워 나갈 것)
| 갈래 | 특징 | 대표 |
|---|---|---|
| 잠재공간 월드모델 | 압축된 잠재 상태에서 예측, RL과 결합 | World Models, Dreamer 시리즈, DINO-WM |
| 비디오 생성형 월드모델 💡 | 픽셀·비디오를 생성 (주로 diffusion 기반) | UniSim, Genie, Cosmos |

## 로봇에서의 용도
- 정책 학습용 시뮬레이터 대체
- 학습 데이터 증강 (Sim2Real 사이 시각 차이 줄이기 — Cosmos Transfer)
- 정책 평가

## 열린 문제 (내 생각)
-

## 관련 노트
- 실험: (아직 없음)
