---
title: "Coreset Selection"
date: 2026-11-17
tags: [technique, training]
category: "학습 기법"
status: draft
---

> 전체 학습 데이터의 목적함수(그래디언트/손실)를 근사하도록 작은 가중 부분집합(coreset)을 선택해 학습 비용을 줄이는 데이터 선택 기법.

**대표 논문**: Coresets for Data-efficient Training of Machine Learning Models (2020) · **분류**: 학습 기법

## 해결한 문제
균등 랜덤 서브샘플링은 gradient bias가 크고 rare하지만 결정적인 샘플을 놓친다. 또한 웹/로봇 로그처럼 중복이 많은 데이터에서는 대부분의 샘플이 학습 신호를 거의 추가하지 않는데도 full-batch 학습 비용을 그대로 지불한다. Coreset selection은 '전체 데이터로 학습한 결과와 거의 같은 해를 훨씬 적은 샘플로 얻는 것'을 목표로 이 병목을 정면으로 다룬다.

## 핵심 아이디어
가중 부분집합 $S$와 가중치 $w$를 골라 전체 데이터 $D$의 gradient를 근사한다: $\min_{S,w}\max_{\theta}\;\|\sum_{i\in S} w_i \nabla \ell_i(\theta) - \sum_{j\in D}\nabla \ell_j(\theta)\|$. Craig 계열은 샘플 간 gradient 유사도에 대한 submodular maximization으로 이 오차를 줄이고, GraNd/EL2N 계열은 proxy model의 per-sample loss나 gradient norm을 importance score로 써서 훨씬 싸게 근사한다. 또 다른 축은 embedding 공간에서 k-center greedy나 clustering으로 '커버리지'를 보존하는 선택이다. 실무적으로는 proxy model로 점수를 매기고 상위/계층별로 샘플링하는 파이프라인이 흔하다.

## 왜 작동하나
SGD의 수렴 궤적은 개별 샘플이 아니라 gradient의 합(방향과 크기)에 의해 결정되므로, gradient 합을 보존하면 학습 궤적과 최종 해가 보존된다. 중복 샘플을 제거하면 같은 스텝 수에서 유효 학습 신호 밀도가 올라가고, easy/중복 샘플이 만드는 gradient noise가 줄어든다.

## 트레이드오프
- per-sample gradient 계산이 큰 모델에서는 매우 비싸다 (마지막 layer나 projection만 쓰는 근사가 필요)
- 선택된 부분집합의 분포가 전체와 달라져 rare class/edge case 성능이 떨어질 수 있다
- coreset은 학습 초반에 한 번 고정되는 경우가 많아 학습 중 변하는 샘플 중요도를 반영하지 못한다
- importance score가 proxy model 품질에 의존해, proxy와 target의 capacity gap이 크면 선택이 망가진다
- 로봇 데이터는 시간적 상관·multimodal·비iid라 iid 가정 기반 이론 보장이 잘 맞지 않는다
- selection 자체의 하이퍼파라미터(비율, 계층, 거리 metric) 튜닝 비용이 든다

## 계보
**이전**
- Uniform random subsampling
- Importance sampling / hard-example mining
- k-Center Greedy (Herding) subset selection
- Submodular subset selection
- Uncertainty-based active learning

**이후**
- GraNd / EL2N (Deep Learning on a Data Diet)
- Moderate Coreset
- D2 Pruning
- Selection via Proxy (SVP)
- Dataset Distillation
- Data Pruning 기반 neural scaling law 분석
- Self-supervised / label-free coreset selection

## 피지컬 AI에서의 쓰임
- Open X-Embodiment 같은 대규모 로봇 데이터셋에서 도메인·태스크별 서브셋 큐레이션 (적용 사례는 확인 필요)
- OpenVLA / RT-2 계열 VLA fine-tuning 시 demonstration 선별로 학습 스텝 절감
- Diffusion Policy 등 imitation learning에서 에피소드 단위 시연 선별
- DAgger / active learning 루프에서 라벨링(텔레오퍼레이션) 비용 절감
- sim-to-real 데이터 mixture에서 real 데이터의 가중치를 coreset weight로 해석해 재사용

## 💡 아이디어 훅
- 에피소드(trajectory) 단위 submodular coreset: 프레임 단위가 아니라 궤적 전체의 gradient/coverage를 보존하는 선택 기준
- per-sample gradient를 action-token loss와 proprio 입력까지 포함해 정의하면 VLA에 맞는 importance가 나오는가
- coreset을 고정 부분집합이 아니라 학습 중 온라인으로 갱신되는 데이터 mixture weight로 일반화
- world model 학습에서 transition coverage(상태-행동 공간 커버리지)를 보존하는 coreset 기준 설계
- failure/복구 데이터를 강제로 포함시키는 constrained coreset (분포 보존 + 실패 커버리지 동시 최적화)
- coreset selection과 dataset distillation을 결합해 로봇 데이터를 소량 합성 trajectory로 증류
- 선택 편향이 policy의 OOD 견고성에 미치는 영향 분석 (선택된 데이터만으로 학습한 VLA의 실패 모드)

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
