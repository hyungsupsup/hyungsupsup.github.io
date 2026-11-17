---
title: "Distribution Matching Distillation"
date: 2026-11-18
tags: [technique, generative]
category: "생성모델"
status: draft
---

> 사전학습된 diffusion/flow 교사의 score 차이를 이용해, 학생 생성기를 단일 스텝(또는 소수 스텝)으로 데이터 분포 자체에 매칭시키는 증류 기법.

**대표 논문**: One-step Diffusion with Distribution Matching Distillation (2023, CVPR 2024) — 후속 DMD2: Improved Distribution Matching Distillation for Fast Image Synthesis (2024) · **분류**: 생성모델

## 해결한 문제
Progressive Distillation·Consistency Model 계열은 교사의 샘플링 궤적(trajectory)이나 노이즈-데이터 대응관계를 회귀 대상으로 삼기 때문에, 스텝 수를 1~2개로 줄이면 궤적 근사 오차가 누적되고 교사의 ODE를 정확히 따라가는 데만 집중해 실제 데이터 분포와의 괴리가 남는다. 또한 per-sample 회귀는 모드 커버리지를 보장하지 않아 다양성이 떨어지거나 블러가 생긴다. DMD는 '궤적을 맞추는' 대신 '분포를 맞추는' 목표로 이 병목을 우회한다.

## 핵심 아이디어
생성기 $G_\theta$가 노이즈 $z$에서 한 번에 $x=G_\theta(z)$를 뽑는다고 하자. 목표는 $p_{fake}$를 $p_{real}$에 KL-divergence로 맞추는 것이고, 그 gradient는 score 차이로 표현된다: $\nabla_\theta \mathrm{KL} = \mathbb{E}_{t,z}\big[(\mu_{fake}(x_t,t)-\mu_{real}(x_t,t))\,\tfrac{\partial x}{\partial\theta}\big]$, $x_t=\alpha_t x+\sigma_t\epsilon$. 여기서 $\mu_{real}$은 frozen된 사전학습 diffusion 교사의 score(고정), $\mu_{fake}$는 생성기 출력에 denoising score matching으로 계속 갱신되는 보조 네트워크다. 즉 교사와의 샘플별 대응 없이, 두 score의 차이가 '실데이터가 더 진한 방향'을 가리키므로 생성기 파라미터를 그 방향으로 밀어 분포 질량을 이동시킨다. 원 논문은 안정화를 위해 noise-conditioned regression loss를 함께 썼고, DMD2는 이를 제거하고 GAN loss + two-time-scale update rule로 대체해 1-step 품질을 크게 올렸다.

## 왜 작동하나
KL divergence의 gradient는 정확히 $\log p_{real}-\log p_{fake}$의 기대값, 즉 두 score의 차이다. 따라서 각 샘플에서 'fake가 과대평가한 영역은 밀어내고 과소평가한 영역은 끌어당기는' 힘이 생겨, 개별 궤적을 복제하지 않아도 분포 수준에서 질량이 재배치된다. 또 $\mu_{fake}$를 온라인으로 학습시켜 생성 분포 변화를 추적하므로, 생성기가 이동해도 gradient가 계속 유효한 방향을 가리킨다.

## 트레이드오프
- 보조 fake score network를 동시에 학습해야 해 메모리·연산 오버헤드가 크고, 대규모 배치가 필요해 학습이 불안정해지기 쉽다
- 원 DMD는 regression loss에 의존해 1-step 품질이 제한적이었고, DMD2에서 GAN loss를 추가해야 실용적 품질에 도달했다
- time step 샘플링 분포·가중치에 민감하고, 모드 붕괴/다양성 손실 위험이 있다
- 교사 분포를 넘어설 수 없고, 교사 자체의 편향(예: 사람 이미지 prior)을 그대로 상속한다
- few-step으로 갈수록 디테일·텍스트 정렬이 multi-step 대비 열세인 경우가 있다

## 계보
**이전**
- Progressive Distillation
- Consistency Models
- Score Distillation Sampling (SDS)
- Variational Score Distillation (Progressive3D)
- Rectified Flow / Reflow

**이후**
- DMD2
- SDXL-Lightning (DMD2 계열 2단계 증류로 알려짐, 확인 필요)
- Flash Diffusion
- Decoupled DMD
- Self-Forcing (자기회귀 비디오 diffusion의 DMD식 증류)
- TwinFlow / MeanFlow 계열과의 결합 시도 (확인 필요)

## 피지컬 AI에서의 쓰임
- Diffusion Policy 계열 action head를 1-step으로 증류해 고주파(수십~수백 Hz) 로봇 제어 루프에 탑재 — OneDP(One-Step Diffusion Policy)가 관련 접근을 사용(정확한 DMD 채택 여부는 확인 필요)
- VLA의 flow-matching/diffusion action expert(예: π0 계열)를 DMD로 소수 스텝화해 추론 지연을 줄이는 용도
- 비디오 diffusion 월드모델을 실시간 rollout 가능하도록 증류해 model-based planning/MPC에 사용
- 시뮬레이터 없이 로봇 시연 데이터 분포를 직접 매칭하는 소수 스텝 생성 정책 학습(오프라인 RL/행동 생성)

## 💡 아이디어 훅
- DMD의 score 차이 항을 action chunk 분포에 적용해 '궤적 회귀'가 아닌 '행동 분포 매칭'으로 증류하면, multimodal 시연(양손·다중 전략)의 모드 커버리지가 개선되는가?
- 로봇 상태·언어 조건부에서 $\mu_{real}$을 고정 교사 대신 온라인으로 갱신되는 world model score로 두면, 배포 중 분포 이동(domain shift)에 적응하는 1-step 정책이 가능한가?
- DMD2의 two-time-scale update를 action head와 critic/value network 사이의 비대칭 학습률로 재해석해, 오프라인 RL에서의 actor-critic 안정화에 쓸 수 있는가?
- 실시간 제어에서 1-step 생성기의 실패 모드를 score 차이 크기로 사전 감지(불확실성 추정)해, 필요할 때만 multi-step으로 fallback하는 anytime 정책 설계
- flow-matching VLA와 DMD를 결합할 때 time-step 샘플링 분포를 로봇 제어 주기·horizon에 맞춰 재가중하면 품질-지연 trade-off가 어떻게 변하는가?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
