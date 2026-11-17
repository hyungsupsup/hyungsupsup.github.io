---
title: "Sparse Attention"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> Full $O(n^2)$ attention 행렬을 미리 정한(또는 학습/라우팅으로 정한) 희소 패턴 $S(i)$ 위에서만 계산해 긴 시퀀스의 attention 비용을 줄이는 기법군.

**대표 논문**: Generating Long Sequences with Sparse Transformers (2019) · **분류**: Attention·시퀀스

## 해결한 문제
Dense self-attention은 시퀀스 길이 $n$에 대해 시간·메모리가 $O(n^2)$로 증가해, 긴 문서·오디오·비디오·로봇 관측 히스토리처럼 토큰이 수천~수만 개인 입력을 사실상 처리할 수 없다. 또한 긴 시퀀스에서는 attention 행렬의 대부분 원소가 거의 0에 가까워 dense 계산이 낭비라는 관찰이 있었다. Sparse Attention은 '중요한 연결만 남긴다'는 전제로 이 이차원 병목을 깬다.

## 핵심 아이디어
각 query $i$마다 전체 key가 아니라 부분집합 $S(i)$에만 attention을 건다: $\mathrm{Attn}(i)=\sum_{j\in S(i)}\frac{\exp(q_i^\top k_j)}{\sum_{l\in S(i)}\exp(q_i^\top k_l)}v_j$. 대표적으로 local window(이웃 $w$개) + strided/dilated 연결(멀리 떨어진 토큰을 $k$ 간격으로) + 소수 global token(모든 query가 참조하는 허브)을 조합해 $O(n\sqrt{n})$ 또는 $O(nw)$ 수준으로 낮춘다. 패턴은 block 단위로 정의해 GPU kernel이 실제로 이득을 보도록 구현하는 것이 핵심이며, 후속 연구들은 패턴을 수작업 대신 content-based routing(LSH, clustering, learned block selection)으로 정한다.

## 왜 작동하나
언어·영상·로봇 궤적 데이터의 의존성은 대부분 국소적이고, 장거리 의존성은 소수의 허브 토큰이나 국소 연결의 다단 합성을 통해 전달된다. 따라서 window+global 조합만으로도 dense attention의 표현력을 근사할 수 있고, 남는 계산을 시퀀스 길이 확장에 재투자할 수 있다. 또한 block-sparse 형태는 메모리 접근이 규칙적이어서 실제 wall-clock 이득으로 이어지기 쉽다.

## 트레이드오프
- 희소 패턴이 수작업·고정이면 태스크 의존적이며, dense가 필요한 장거리 검색형 태스크에서 품질이 떨어진다
- 이론적 FLOPs 감소가 GPU에서 그대로 속도가 되지 않음 — 전용 kernel/block layout 없으면 dense+FlashAttention보다 느릴 수 있다
- autoregressive decoding 시 KV cache가 불규칙해져 메모리 관리·배칭이 어려움
- content-adaptive routing은 라우팅 자체의 오버헤드와 학습 불안정성을 동반
- 패턴 설계가 inductive bias로 굳어져 사전학습 후 태스크 변경 시 재설계 필요
- 요즘은 중간 길이(수~수십K)에서는 IO-aware dense attention이 더 실용적인 경우가 많음

## 계보
**이전**
- Dense scaled dot-product self-attention
- Sliding-window / local attention
- Dilated(strided) convolution의 수용영역 아이디어
- Block-sparse matrix 연산

**이후**
- Longformer
- BigBird
- Routing Transformer
- Reformer (LSH attention)
- Blockwise/Blocksparse attention
- StreamingLLM (attention sink)
- Native Sparse Attention (DeepSeek NSA)
- MoBA (Mixture of Block Attention)
- Quest / MInference (long-context inference용 동적 희소화)

## 피지컬 AI에서의 쓰임
- Long-horizon VLA 정책에서 수백 프레임의 관측·언어·action 토큰을 window+global token으로 압축해 컨텍스트 확장
- 비디오/3D 월드모델의 diffusion transformer에서 spatio-temporal block-sparse attention으로 프레임 수 확장
- 실시간 로봇 제어 루프에서 attention sink + 희소 KV 유지로 디코딩 지연을 일정하게 유지(StreamingLLM 계열)
- 다중 카메라·다중 로봇(embodiment) 토큰을 block-sparse로 연결해 cross-embodiment 파운데이션 모델 학습
- 긴 조작 시연 데이터(action chunk)에 대한 causal block-sparse attention으로 궤적 생성 모델 경량화

## 💡 아이디어 훅
- 로봇 kinematics tree(관절 계층)를 그대로 attention 희소 패턴으로 쓰면 물리적 inductive bias가 되는가?
- proprioception·vision·language 토큰을 서로 다른 희소율로 처리하는 이종(heterogeneous) sparse attention 설계
- 50Hz 제어 루프에서 KV cache eviction 정책과 희소 패턴을 공동 최적화해 지연 상한(latency bound)을 보장하는 연구
- 월드모델 rollout에서 예측 불확실성이 높은 토큰만 dense로 승격하는 uncertainty-gated sparse attention
- 희소 패턴을 학습하되 로봇 태스크 분포 변화에 온라인 적응시키는 continual routing
- sparse attention으로 확장한 컨텍스트가 실제로 조작 성공률에 기여하는지에 대한 통제된 ablation(대부분의 VLA 논문에서 미보고)

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
