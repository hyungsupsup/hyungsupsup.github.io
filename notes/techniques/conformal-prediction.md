---
title: "Conformal Prediction"
date: 2026-11-18
tags: [technique, training]
category: "학습 기법"
status: draft
---

> 모델 출력에 대해 분포 가정 없이 유한 표본(finite-sample) 보장된 예측 집합/구간을 만들어주는 사후 보정(post-hoc calibration) 프레임워크.

**대표 논문**: Algorithmic Learning in a Random World (2005) — Vovk, Gammerman, Shafer의 저서로 체계화; 실무에서 널리 쓰이는 split conformal은 Distribution-Free Predictive Inference for Regression (2018) 계열에서 정리됨 · **분류**: 학습 기법

## 해결한 문제
기존 uncertainty 정량화(Bayesian NN, Gaussian process, deep ensemble)는 모델 가정이나 근사에 의존해 '커버리지(coverage)'를 보장하지 못하고, 검증 손실로는 실제 실패율을 통제할 수 없다. 또한 분포가 바뀌거나 소량의 calibration 데이터만 있을 때 신뢰할 수 있는 예측 구간을 주는 방법이 없었다.

## 핵심 아이디어
데이터를 학습셋과 calibration셋으로 나누고, calibration셋에서 비순응도 점수(nonconformity score) $s(x,y)$(예: $|y-\hat{f}(x)|$ 또는 quantile regression residual)를 계산한다. 교환가능성(exchangeability) 가정 아래 점수의 $\lceil (n+1)(1-\alpha)\rceil/n$ 경험적 분위수 $\hat{q}$를 취하면, 새 입력 $x$에 대한 예측 집합 $C(x)=\{y : s(x,y)\le \hat{q}\}$가 $P(Y\in C(X))\ge 1-\alpha$를 만족한다. 즉 모델을 재학습하지 않고도 임의의 black-box predictor 위에 얇은 보정 레이어만 얹어 유한 표본 커버리지를 얻는다. 점수 설계만 바꾸면 분류(집합), 회귀(구간), 구조화 출력(궤적, action chunk)에 모두 적용된다.

## 왜 작동하나
핵심은 교환가능성 하나뿐이다. calibration 점수들과 테스트 점수가 대칭적(exchangeable)이므로, 테스트 점수의 순위가 균등분포가 되고, 따라서 상위 $\alpha$ 분위를 잘라내면 정확히 $1-\alpha$ 확률로 참값이 남는다. 모델의 정확도가 아니라 점수의 순위만 쓰기 때문에 모델이 틀려도 커버리지는 유지되고, 대신 집합 크기가 커져 '모른다'를 정직하게 표현한다.

## 트레이드오프
- 보장은 marginal coverage이며, 입력별 conditional coverage는 보장하지 않는다(heteroscedastic 구간에서 특정 영역 과소/과대 커버 가능)
- 교환가능성 가정이 깨지면(로봇 배포 후 분포 이동, 시계열 상관) 보장이 무너진다 — weighted CP나 Adaptive Conformal Inference 같은 변형이 필요
- calibration셋 크기가 곧 통계적 해상도를 결정: $\alpha$가 작을수록(예: 1%) 훨씬 많은 calibration 샘플 필요
- 고차원 출력(연속 action, 긴 궤적)에서는 점수 설계가 어렵고 집합이 비실용적으로 커질 수 있다
- full conformal은 모든 후보 $y$에 대해 재학습이 필요해 계산 비용이 크다(split conformal로 회피)
- 커버리지가 보장돼도 집합이 크면 의사결정에 쓸모없다 — 효율(efficiency)은 별도 문제

## 계보
**이전**
- Quantile Regression
- Bayesian Neural Network / Gaussian Process 불확실성 추정
- Bootstrap 신뢰구간
- PAC / PAC-Bayes 일반화 경계

**이후**
- Conformalized Quantile Regression (CQR)
- Adaptive Conformal Inference (ACI)
- Conformal Prediction under Covariate Shift (weighted CP)
- Conformal Risk Control
- Conformal Language Modeling
- EnbPI (시계열 conformal)
- Conformal Prediction for structured outputs (mask/궤적)

## 피지컬 AI에서의 쓰임
- 자율주행/휴먼 로봇의 보행자·차량 궤적 예측에서 CQR 기반 예측 구간으로 안전 반경 산정
- 로봇 조작 정책의 성공 확률·잔차에 conformal risk control을 적용해 실패율 상한을 통제
- VLA/diffusion policy의 action chunk 후보들을 conformal 점수로 필터링해 위험 action 제거(연구 단계)
- 월드모델 rollout의 상태 예측 불확실성을 conformal 구간으로 감싸 MPC/안전 필터에 전달
- sim-to-real에서 시뮬레이터로 calibration 후 실기 배포 시 coverage 재검증

## 💡 아이디어 훅
- VLA의 action chunking에 temporal conformal을 적용: 청크 간 상관을 어떻게 교환가능성 위반으로 다룰 것인가?
- diffusion policy의 다중 모드 샘플링과 conformal 집합을 결합해 '안전 모드만 남기는' 샘플 프루닝
- 월드모델 latent rollout에 대한 conformal 보장을 planning 비용(risk-sensitive MPC)에 직접 넣기
- 언어 조건이 바뀌는 task distribution shift에서 weighted CP의 가중치를 language embedding으로 추정
- conformal calibration을 online으로 갱신하며 로봇이 배포 중 스스로 커버리지를 유지하는 continual CP
- LLM 기반 task planner의 하위 목표(subgoal) 집합에 conformal을 적용해 실행 가능성 보장

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
