---
title: "Cross-Attention Conditioning"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> 생성/정책 네트워크의 latent 토큰을 query로, 외부 조건(텍스트·목표 이미지·언어 지시·센서) 시퀀스를 key/value로 삼아 attention으로 주입하는 조건화(conditioning) 방식.

**대표 논문**: High-Resolution Image Synthesis with Latent Diffusion Models (2022) / Photorealistic Text-to-Image Diffusion Models with Deep Language Understanding (Imagen, 2022) · **분류**: Attention·시퀀스

## 해결한 문제
기존 조건화는 class embedding이나 FiLM/AdaGN처럼 조건을 전역(global) 벡터로 압축해 모든 위치에 동일하게 적용했다. 이 때문에 '어느 위치에 무엇을'이라는 공간적·토큰별 대응 관계를 표현할 수 없었고, 가변 길이 텍스트나 여러 객체 참조를 다루기 어려웠다. Cross-Attention Conditioning은 조건 시퀀스 길이를 고정하지 않고 토큰별로 다른 modulation을 줄 수 있게 한다.

## 핵심 아이디어
latent(noisy image patch, action query, observation token)에서 $Q = W_Q h$를, 조건 시퀀스 $c$에서 $K = W_K c,\; V = W_V c$를 만들어 $\mathrm{Attn}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d})\,V$를 계산한다. 각 latent 토큰이 조건 토큰 전체를 softmax 가중 평균으로 조회하므로, 조건 길이가 달라도 동작하고 토큰 순서에 대해 permutation-equivariant하다. 조건 인코더(CLIP text encoder, language model, goal-image encoder)는 별도 모듈로 두고 cross-attention layer만 학습해도 되며, diffusion backbone에는 보통 self-attention 직후에 삽입한다. 로봇 정책에서는 action query(ACT)나 action expert(π0 계열)가 관측·언어 prefix를 KV로 참조하는 형태로 동일한 구조가 쓰인다.

## 왜 작동하나
조건이 전역 벡터로 압축되지 않고 토큰 단위로 남아 있으므로, 디코더가 필요한 정보만 선택적으로 끌어올 수 있다(soft retrieval). Query와 Key의 내적은 조건-위치 간 관련도를 학습된 metric으로 계산하는 것이고, 이는 공간 정렬(grounding)을 명시적 supervision 없이 emergent하게 만든다. 또한 조건 인코더와 생성기를 분리해 두므로 조건 modality를 바꿔도 backbone을 재설계할 필요가 없다.

## 트레이드오프
- 조건 시퀀스 길이에 대해 attention 비용이 $O(N_c^2)$ 또는 $O(N_q N_c)$로 증가 — 긴 지시문/다중 카메라에서 부담
- 긴 프롬프트에서 토큰이 희석되어 세부 속성 무시(attention dilution) 발생
- cross-attention map이 해석 가능하다고 알려져 있으나 실제로는 grounding과 불일치하는 경우가 많음
- 전역 FiLM/AdaGN 대비 파라미터·연산이 늘고, layer별로 self/cross 비율 튜닝이 필요
- 조건 인코더를 freeze하면 인코더-생성기 간 표현 정렬이 어긋날 수 있음
- 정밀한 공간 제어(경계 상자, 픽셀 마스크)에는 부적합해 별도 제어 branch가 필요

## 계보
**이전**
- [[techniques/film|FiLM (Feature-wise Linear Modulation)]]
- AdaGN / class-embedding conditioning (ADM)
- encoder-decoder cross-attention in Transformer (Attention Is All You Need)
- concatenation-based conditioning

**이후**
- MMDiT (Stable Diffusion 3)
- IP-Adapter
- ControlNet (side-branch + zero-conv)
- Perceiver Resampler / Q-Former (Flamingo, BLIP-2)
- ACT (Action Chunking Transformer)의 action-query cross-attention
- π0 계열 action expert의 cross-attention conditioning

## 피지컬 AI에서의 쓰임
- ACT(Action Chunking Transformer): action query 토큰이 observation encoder feature를 cross-attend해 action chunk를 회귀
- CrossFormer: 언어 지시와 다중 시점 관측을 layer-wise cross-attention으로 결합하는 manipulation policy
- RoboFlamingo: Perceiver Resampler로 압축한 vision token을 언어 모델 쪽 cross-attention으로 주입
- π0(flow-matching VLA): action expert가 VLM prefix를 KV로 참조하는 cross-attention 구조
- VIMA: 로봇/객체 토큰 간 cross-attention으로 멀티모달 지시 조건화
- 텍스트 조건 diffusion world model / data augmentation에서 언어-이미지 정렬 조건화

## 💡 아이디어 훅
- layer별로 FiLM(전역)과 cross-attention(토큰별)을 학습 가능한 gate로 혼합하면 조작 정밀도와 지시 준수 사이 trade-off를 얼마나 개선할까
- 촉각/힘 센서 시계열을 조건 시퀀스로 두고 action query가 cross-attend하게 하면 접촉-rich manipulation에서 이득이 있는가
- cross-attention map을 affordance/주시(attention) supervision으로 재활용해 VLA의 grounding을 약지도 학습할 수 있는가
- 장기 horizon에서 조건 시퀀스가 수천 토큰이 될 때 sparse/linear cross-attention이나 memory token 압축이 정책 성능을 유지하는가
- 실패·복구 신호(recovery prompt)를 조건 토큰으로 넣어 cross-attention이 국소 구간만 재조정하게 만드는 test-time steering
- world model에서 미래 latent를 query로, 과거 관측·행동을 KV로 두는 cross-attention이 rollout drift를 줄이는가

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
