---
title: "Sliding Window Attention"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> 각 토큰이 고정 크기 $w$의 국소 이웃에만 attention하는 sparse attention 패턴으로, 시퀀스 길이에 선형인 비용으로 long-context를 처리하는 기법.

**대표 논문**: Longformer: The Long-Document Transformer (2020) · **분류**: Attention·시퀀스

## 해결한 문제
표준 full self-attention은 시퀀스 길이 $n$에 대해 $O(n^2)$ 시간·메모리를 요구해 긴 문서나 긴 로봇 궤적/관측 히스토리를 다루기 어렵다. 단순히 시퀀스를 자르면 멀리 떨어진 토큰 간 의존성이 끊기고, recurrent 계열은 병렬화가 안 된다. Sliding Window Attention은 국소성(locality) 가정을 attention sparsity로 명시해 이 병목을 완화한다.

## 핵심 아이디어
각 위치 $i$의 query가 $[i-w, i+w]$ (또는 causal이면 $[i-w, i]$) 범위의 key에만 attention한다. 레이어 $l$에서의 수용 영역(receptive field)은 $l \times w$로 선형 증가하므로, $L$개 레이어를 쌓으면 이론상 $L \cdot w$ 거리까지 정보가 전파된다. 비용은 $O(n \cdot w)$로 시퀀스 길이에 선형이며, attention mask를 banded matrix로 만들어 기존 커널로도 구현 가능하다. Longformer는 여기에 dilated sliding window와 소수 토큰의 global attention을 결합해 task-specific 전역 정보를 보존했고, Mistral 7B 등 LLM은 순수 sliding window(예: window 4096)와 rolling buffer KV cache로 이를 채택했다.

## 왜 작동하나
자연어·센서 시계열·로봇 궤적 모두 인접 토큰 간 상관이 지배적이라 국소 attention만으로 대부분의 정보가 보존된다. 레이어를 쌓을수록 국소 정보가 hop-by-hop으로 확산되어 실효 수용 영역이 넓어지고, banded mask는 GPU에서 dense 연산 대비 메모리 대역폭을 크게 줄인다. 또한 KV cache를 window 크기로 고정(rolling buffer)할 수 있어 추론 시 메모리가 시퀀스 길이와 무관해진다.

## 트레이드오프
- 수용 영역이 $L \cdot w$로 제한되어 진짜 장거리 의존성(문서 전체 요약, 장기 계획)은 global token이나 추가 메커니즘 없이는 놓칠 수 있음
- banded mask는 dense attention 대비 커널 효율이 낮아 실제 wall-clock 이득이 이론 복잡도만큼 크지 않을 수 있음
- window 크기 $w$가 새로운 하이퍼파라미터가 되어 task별 튜닝 필요
- causal LM에서 rolling buffer cache는 위치가 밀릴 때 cache 재사용·재계산 관리가 복잡
- global attention을 섞으면 구현이 복잡해지고, 어떤 토큰을 global로 둘지 설계 의존적

## 계보
**이전**
- Full Self-Attention (Transformer)
- Sparse Transformer
- Recurrent/convolutional long-sequence 모델

**이후**
- Longformer의 dilated + global attention 변형
- Mistral 7B의 sliding window + rolling buffer cache
- BigBird (random + window + global 조합)
- StreamingLLM의 attention sink + window
- Gemma 2 / Gemma 3의 interleaved local-global attention
- HuggingFace sliding_window / FlashAttention 계열 block-sparse 커널

## 피지컬 AI에서의 쓰임
- VLA 정책에서 긴 관측·액션 히스토리를 다룰 때 국소 attention으로 KV cache 고정 (예: 실시간 chunked action decoding)
- Mistral 7B 기반 오픈소스 VLM/VLA 백본에서 긴 멀티모달 컨텍스트 처리
- 월드모델의 latent rollout에서 최근 $w$ 프레임만 attention해 메모리 절감
- 로봇 텔레옵 시계열(관절·카메라 토큰) 스트리밍 추론에서 rolling buffer로 무한 길이 스트림 처리

## 💡 아이디어 훅
- 로봇에서 window를 시간축이 아니라 공간(관절 체인, 센서 토폴로지)에 맞춰 정의한 'kinematic sliding window attention'은?
- window 크기를 고정하지 않고 예측 불확실성이나 접촉 이벤트에 따라 동적으로 늘리는 adaptive window attention
- sliding window + attention sink를 VLA action chunking에 결합해 장기 태스크에서 초기 instruction을 보존하는 설계
- 월드모델에서 국소 attention의 수용 영역 $L \cdot w$가 실제 예측 가능 horizon과 어떻게 대응하는지 실증 분석
- sliding window로 학습한 정책이 분포 이동(긴 지연, occlusion)에서 얼마나 취약한지 진단하는 벤치마크

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
