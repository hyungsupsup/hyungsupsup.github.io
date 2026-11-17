---
title: "Dilated Attention"
date: 2026-11-17
tags: [technique, attention]
category: "Attention·시퀀스"
status: draft
---

> Self-attention을 dilation rate $r$와 segment 길이 $w$로 희소화해, 국소 패턴과 장거리 의존성을 동시에 잡으면서 시퀀스 길이에 선형인 복잡도를 얻는 sparse attention 기법.

**대표 논문**: LongNet: Scaling Transformers to 1,000,000,000 Tokens (2023) — 원형은 DiNAT: Dilated Neighborhood Attention Transformer (2022)의 dilated neighborhood attention · **분류**: Attention·시퀀스

## 해결한 문제
Dense self-attention은 $O(n^2)$ 비용·메모리 때문에 긴 시퀀스(수만~수백만 토큰)에서 확장 불가. Longformer/BigBird류 sparse attention은 고정된 window+global 패턴이라 국소 해상도와 장거리 도달 범위를 동시에 유지하기 어렵고, 멀리 떨어진 토큰은 여러 layer를 거쳐야만 간접적으로 연결된다. Dilated Attention은 dilated convolution의 다중 스케일 아이디어를 attention 패턴에 이식해 이 둘을 분리한다.

## 핵심 아이디어
시퀀스를 길이 $w$의 segment로 나누고, 각 segment 안에서 query $i$가 $j \equiv i \pmod r$이고 $|i-j| < w$인 key만 보게 한다: $\mathcal{D}_r^w = \{(i,j) : j \equiv i \pmod r,\ |i-j| < w\}$. 여기서 $r$이 dilation rate, $w$가 attention span이다. 서로 다른 head(또는 layer 그룹)에 $r = 1, 2, 4, \dots$ 와 $w, 2w, 4w, \dots$를 할당하면 작은 $r$은 조밀한 국소 문맥을, 큰 $r$은 드문드문하지만 먼 토큰을 담당한다. 각 패턴의 비용은 $O(n \cdot w)$이고 dilation group 수가 $O(\log n)$이므로 전체가 시퀀스 길이에 선형이 된다. 여러 layer를 쌓으면 receptive field가 dilated CNN처럼 지수적으로 커지며, 패턴이 규칙적이어서 FlashAttention식 블록 연산과 분산 학습으로 구현할 수 있다.

## 왜 작동하나
정보 병목이 '얼마나 멀리 보는가'와 '얼마나 촘촘히 보는가'로 분해되고, 다중 스케일 head 집합이 두 요구를 각각 저비용으로 충족한다. 고정 stride 덕분에 attention 행렬이 블록 대각 구조로 정렬되어 GPU 커널에서 낭비 없이 계산되고, 국소 window가 세밀한 토큰 상호작용(문법, 인접 프레임)을 보존한다.

## 트레이드오프
- 패턴이 학습되지 않는 고정 구조라, 데이터가 요구하는 희소성과 어긋나면 dense attention 대비 품질 손실
- 임의의 두 토큰이 한 layer에서 직접 상호작용하지 못하고 여러 layer를 거쳐야 함(직접 비교가 필요한 retrieval/alignment 과제에 불리)
- dilation rate·segment 길이·group 수 같은 하이퍼파라미터 선택이 성능과 속도를 크게 좌우
- 큰 $r$에서는 유효 attention 밀도가 낮아 KV 캐시·메모리 이득이 구현 세부에 의존
- LongNet의 billion-token 스케일 주장은 특정 구현·하드웨어 조건에 의존 (재현성 확인 필요)

## 계보
**이전**
- Longformer (sliding-window + global attention)
- BigBird (sparse attention, random+window+global)
- Sparse Transformer (strided/fixed attention pattern)
- Dilated Convolution / WaveNet (다중 스케일 dilation 개념의 원천)
- Neighborhood Attention Transformer (NAT)

**이후**
- DiNAT (Dilated Neighborhood Attention Transformer) — 비전 쪽 dilated neighborhood attention
- LongNet 계열 long-context LLM 학습 레시피 및 분산 학습 구현 변형 (확인 필요)
- Native Sparse Attention 등 최근 학습형/구조형 sparse attention 계열과의 결합 시도 (확인 필요)

## 피지컬 AI에서의 쓰임
- 장기 horizon episode를 다루는 Decision Transformer 계열 정책에서 수만 step 관측 토큰 스트림 처리
- VLA 모델에서 긴 observation history + 다중 카메라 토큰 + 언어 지시를 하나의 시퀀스로 넣을 때의 선형 비용 attention
- 월드모델의 긴 rollout 컨텍스트(수백~수천 프레임 latent)에서 국소 물리 dynamics와 장기 과제 구조를 동시에 포착
- DiNAT 계열 dilated neighborhood attention을 로봇 perception backbone(dense prediction, segmentation)에 사용

## 💡 아이디어 훅
- dilation rate를 제어 주기(control frequency)나 시간 계층(프레임→초→분)에 정렬시키는 '시간 스케일 정합' dilated attention — 물리적 시간 상수가 다른 현상을 한 layer에서 분리 포착
- VLA에서 action chunk 토큰과 관측 토큰에 서로 다른 dilation 패턴을 주는 modality-aware dilation
- dilation rate를 고정하지 않고 라우팅/학습으로 선택하게 만들면 long-horizon 로봇 데이터에서 어떤 시간 스케일이 실제로 쓰이는지 분석 가능
- 실시간 로봇 추론을 위한 dilated attention + KV 캐시 eviction/압축의 결합(큰 $r$ 그룹의 캐시만 sparse하게 유지)
- 월드모델에서 예측 오차가 큰 시간 스케일을 자동으로 촘촘히 보게 하는 uncertainty-driven dilation 스케줄

---
*LLM 초안 — 직접 검토 후 `status: draft`를 지울 것.*
