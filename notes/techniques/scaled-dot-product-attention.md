---
title: "Scaled Dot-Product Attention"
date: 2026-11-12
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> Query와 Key의 내적을 $\sqrt{d_k}$로 스케일링한 뒤 softmax로 가중치를 만들어 Value를 집계하는 attention 연산.

**대표 논문**: Attention Is All You Need (2017) · **분류**: Attention·시퀀스

## 해결한 문제
RNN/CNN 기반 seq2seq는 시퀀스 길이에 따라 순차 계산이 필요해 병렬화와 장거리 의존성 학습에 병목이 있었다. 또한 기존 dot-product attention은 차원 $d_k$가 커질수록 내적 값의 분산이 커져 softmax가 포화되고 gradient가 불안정해지는 문제가 있었다. Scaled dot-product attention은 이 두 병목을 단순한 행렬 연산과 차원 스케일링으로 완화했다.

## 핵심 아이디어
입력 토큰 표현을 Query $Q$, Key $K$, Value $V$로 선형 투영하고, 각 Query에 대해 모든 Key와의 내적 유사도를 계산한다. 이때 점수 행렬을 $QK^\top/\sqrt{d_k}$로 스케일링한 뒤 softmax를 적용해 attention weight를 얻고, 이를 Value의 가중합으로 집계한다: $\mathrm{Attention}(Q,K,V)=\mathrm{softmax}(QK^\top/\sqrt{d_k})V$. 전체 연산은 시퀀스 길이에 대한 순차 recurrence 없이 행렬곱과 softmax로 표현되어 GPU/TPU에서 병렬화된다. causal mask를 추가하면 autoregressive 생성에도 그대로 쓸 수 있다.

## 왜 작동하나
Query와 Key의 각 차원이 독립적이고 분산이 일정하다고 볼 때 내적의 분산은 $d_k$에 비례해 커지므로, $\sqrt{d_k}$로 나누면 logit 스케일을 안정화해 softmax gradient가 죽는 것을 줄인다. 또한 attention weight를 데이터 의존적으로 계산하므로 토큰 간 장거리 관계를 고정된 convolution receptive field 없이 직접 모델링할 수 있다. 순차 의존성이 없어 학습 시 시퀀스 위치들을 병렬로 처리할 수 있다는 점도 핵심이다.

## 트레이드오프
- 시퀀스 길이 $n$에 대해 attention 행렬이 $O(n^2)$ 메모리/계산을 요구해 긴 로봇 trajectory나 고해상도 visual token에서 비용이 커진다.
- softmax attention은 기본적으로 위치 정보를 포함하지 않아 positional encoding이나 구조적 bias가 필요하다.
- 스케일링 계수 $\sqrt{d_k}$는 차원과 분포가 균일하다는 가정에 기반하며, 이질적인 multimodal token 분포에서는 최적이 아닐 수 있다.
- causal mask 없이 쓰면 미래 정보 누출이 가능하고, 반대로 mask를 쓰면 양방향 문맥 활용이 제한된다.
- attention weight가 해석 가능하다는 주장은 multi-head/깊은 층에서 항상 성립하지 않는다.

## 계보
**이전**
- Additive attention (Bahdanau attention)
- Dot-product attention (Luong attention)
- RNN/CNN 기반 seq2seq
- Soft attention mechanism

**이후**
- Multi-Head Attention
- [[techniques/flash-attention|FlashAttention]]
- [[techniques/sparse-attention|Sparse Attention]]
- [[techniques/linear-attention|Linear Attention]]
- Cross-Attention in Transformer-based VLA/world models

## 피지컬 AI에서의 쓰임
- OpenVLA의 vision-language-action token 간 attention
- RT-2 계열 VLA의 vision-language token과 action token 결합
- Octo 등 Transformer 기반 robot policy의 observation-action attention
- π0 계열 VLA에서 multimodal token 및 action expert의 attention 연산
- IRIS/Genie 계열 world model에서 latent token 간 temporal attention

## 💡 아이디어 훅
- 로봇의 visual token, proprio token, action token은 분포와 차원이 다른데, $d_k$별 learned temperature로 attention logit 스케일을 적응적으로 조정할 수 있는가?
- action chunking/autoregressive action generation에서 causal mask와 양방향 observation attention을 어떻게 혼합하면 지연과 성능을 동시에 개선할 수 있는가?
- 실시간 로봇 제어에서 $O(n^2)$ attention을 피하기 위해 action token에만 sparse/linear attention을 적용하는 hybrid 구조는 어떤 tradeoff를 갖는가?
- attention entropy를 uncertainty 신호로 사용해 VLA의 실패 감지나 intervention trigger에 활용할 수 있는가?
- SE(3) equivariance나 spatial locality를 attention score에 주입하면 manipulation에서 sample efficiency가 개선되는가?

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
