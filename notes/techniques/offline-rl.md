---
title: "Offline RL"
date: 2026-11-20
tags: [technique, training]
category: "학습 기법"
status: draft
---

> 로봇이 직접 부딪히며 배우지 않고, 과거에 쌓인 로그 데이터만으로 '어떤 행동이 좋은지'를 배우는 학습법

**대표 논문**: Offline Reinforcement Learning: Tutorial, Review, and Perspectives on Open Problems (2020) · **분류**: 학습 기법

## 해결한 문제
기존 online RL은 로봇이 실제로 실패·충돌·고비용 시도를 반복해야 해서 위험하고 느림. 단순히 기록된 행동만 모방하면, 데이터에 없는 상황에서 어떤 행동이 더 좋은지 판단하기 어려움.

## 핵심 아이디어
비유: 운전 영상을 수천 시간 보고 면허를 따는 것. 실제로는 로그에서 상태-행동-보상-다음 상태를 학습하고, 데이터에서 드문 행동에는 낮은 점수를 매겨 과대평가하지 않음. 그 결과 데이터 범위 안에서 안전한 정책을 뽑음.

## 왜 작동하나
탐색을 생략해 비용과 위험을 줄이고, pessimism(데이터 밖 행동에 보수적으로 점수 매기기)이 '없는 보상'을 환각하는 것을 막음. 좋은 로그가 많으면 실제 환경보다 빠르게 정책 개선 가능.

## 트레이드오프
- 데이터에 없는 상황은 잘 못 다루고, 커버리지가 좁으면 성능이 제한됨.
- 너무 보수적으로 만들면 기존 행동보다 개선이 작을 수 있음.
- 오프라인 평가가 어려워 실제 성능을 확인하려면 제한된 온라인 테스트가 필요할 수 있음.

## 계보
**이전**
- Batch Reinforcement Learning
- Imitation Learning
- Supervised Learning
- Model-Based Reinforcement Learning

**이후**
- Conservative Q-Learning (CQL)
- Implicit Q-Learning (IQL)
- TD3+BC
- Decision Transformer
- [[techniques/diffusion-policy|Diffusion Policy]]

## 피지컬 AI에서의 쓰임
- 로봇 팔이 사람이 원격 조종한 잡기 로그만으로 물체 조작 정책을 학습
- 자율주행차가 과거 주행 로그에서 위험하지 않은 차선 변경/감속 규칙을 학습
- VLA 모델이 로봇 실행 로그를 오프라인 RL로 정제해 '보상 낮은 행동'을 줄이는 미세조정

## 💡 아이디어 훅
- LLM 에이전트의 과거 대화 로그를 오프라인 RL로 학습하면 어떤 보상 신호를 안전하게 설계할 수 있을까?
- 로봇 데이터가 부족할 때 시뮬레이션 로그와 실제 로그를 섞어 오프라인 RL을 하면 어떤 문제가 생길까?
- Diffusion Policy 같은 생성형 정책과 오프라인 RL의 보수성을 결합하면 더 안전한 로봇 행동을 만들 수 있을까?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
