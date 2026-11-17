---
title: "Teacher Forcing"
date: 2026-11-18
tags: [technique, training]
category: "학습 기법"
status: draft
---

> Autoregressive 모델 학습 시 이전 시점의 모델 예측 대신 ground-truth 이전 토큰(또는 상태)을 입력으로 넣어주는 학습 기법.

**대표 논문**: A Learning Algorithm for Continually Running Fully Recurrent Neural Networks (1989) · **분류**: 학습 기법

## 해결한 문제
순환 신경망을 free-running 방식으로 학습하면 모델 자신의 출력이 다음 스텝 입력으로 되먹임되면서 초반의 작은 오차가 빠르게 증폭되고, BPTT gradient가 불안정해져 수렴이 느리거나 발산한다. 또한 각 스텝의 학습 신호가 모델 자신의 (아직 엉성한) 예측 분포에 조건화되어 있어 supervision이 흐려진다.

## 핵심 아이디어
길이 $T$의 시퀀스 $(y_1,\dots,y_T)$와 조건 $x$가 주어졌을 때, 학습 중에는 항상 정답 prefix를 조건으로 사용해 $\sum_{t=1}^{T} \log p_\theta(y_t \mid y_{<t}, x)$ 를 최대화한다. 즉 $t$ 시점의 입력으로 $\hat{y}_{t-1}$ 이 아니라 $y_{t-1}$ 을 넣는다. 이렇게 하면 전체 시퀀스의 조건이 미리 알려져 있으므로 causal mask를 씌운 단일 forward pass로 모든 스텝의 loss를 병렬 계산할 수 있다. 추론 시에는 다시 자기 예측을 되먹이는 free-running/autoregressive decoding으로 전환한다.

## 왜 작동하나
각 스텝이 '올바른 문맥이 주어졌을 때의 다음 토큰 예측'이라는 잘 정의된 지도학습 문제가 되어, gradient가 안정적이고 수렴이 빠르다. 또한 정답 prefix가 고정되어 있으므로 시퀀스 차원의 병렬화가 가능해 학습 효율이 크게 오른다.

## 트레이드오프
- Exposure bias: 학습 분포(정답 prefix)와 추론 분포(자기 예측 prefix)가 불일치하여, 추론 시 오차가 누적되고 한 번의 실수가 이후 전체를 오염시킨다
- 모델이 '스스로 실수에서 복구하는 법'을 배우지 못한다 — 학습 중에는 실수 상태를 방문하지 않는다
- 연속 제어(action chunk)에서는 정답 궤적 근방만 커버하므로 분포 이동·외란에 취약
- 다봉(multimodal) action 분포를 MSE/CE로 회귀하면 mode averaging이 발생 (diffusion/flow policy가 이를 우회)
- 긴 horizon일수록 학습-추론 불일치가 누적되어 compounding error가 커진다

## 계보
**이전**
- Free-running (autorecurrent) RNN training
- Backpropagation Through Time (BPTT)
- Maximum likelihood sequence modeling

**이후**
- Scheduled Sampling
- Professor Forcing
- Sequence-level / reinforcement training of seq2seq (MIXER, SEARNN)
- [[techniques/dagger|DAgger (imitation learning에서의 동일 문제 의식)]]
- Self-Forcing (video/월드모델 autoregressive rollout 안정화, 연도 확인 필요)
- Diffusion Policy / Flow Matching Policy (teacher forcing의 exposure bias를 회피하는 대안 계열)

## 피지컬 AI에서의 쓰임
- Behavior Cloning 기반 조작 정책 전반 — ACT/action chunking transformer는 expert action chunk를 조건으로 teacher forcing 학습
- VLA 모델: RT-2, OpenVLA, Octo, π0 계열에서 action token(또는 action expert)을 expert 궤적 prefix에 조건화해 학습
- Language-conditioned manipulation에서 instruction + 이전 action token을 조건으로 next action token 예측
- 자율주행/내비게이션 정책의 waypoint sequence 예측
- 월드모델의 autoregressive video/latent rollout 학습 (프레임 예측을 정답 프레임 조건으로)

## 💡 아이디어 훅
- VLA 학습에 DAgger식 on-policy 교정 데이터를 섞으면 exposure bias가 실제 로봇 성능에 얼마나 기여하는가? (teacher forcing vs. on-policy aggregation ablation)
- Action chunk horizon에 scheduled sampling을 적용해 '중간에 실패했을 때 복구하는' 정책을 명시적으로 학습
- Teacher forcing으로 학습한 VLA를 inference 시 자기 예측 prefix로 rollout할 때 분포 이동을 측정하는 진단 지표 설계
- Diffusion/flow policy와 teacher forcing 정책을 동일 데이터·동일 파라미터로 비교해 mode averaging vs. exposure bias 트레이드오프 정량화
- 월드모델에서 teacher forcing으로 학습한 latent dynamics를 long-horizon rollout에 쓸 때의 drift를 self-forcing / noise-injection으로 완화
- 실패 복구 데이터를 합성적으로 만들어(정답 prefix를 일부러 오염시켜) teacher forcing 학습에 노이즈 prefix를 주입하는 커리큘럼

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
