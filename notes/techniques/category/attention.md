---
title: "🎯 Attention·시퀀스"
date: 2026-11-17
tags: [technique-category]
---

<p class="tc-lead">Transformer의 심장. attention 연산과 이를 길고 빠르게 만드는 방법들.</p>
<div class="mh-section"><span>기본 연산</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/scaled-dot-product-attention"><h4>Scaled Dot-Product Attention</h4><p>Query와 Key의 내적을 …로 스케일링한 뒤 softmax로 가중치를 만들어 Value를 집계하는 attention 연산.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/multi-head-attention"><h4>Multi-Head Attention</h4><p>쿼리·키·값을 서로 다른 여러 개의 학습된 선형 사영으로 나누어 병렬로 scaled dot-product attention을 수행하고 결과를 concat하는 attention 구성 방식.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/cross-attention-conditioning"><h4>Cross-Attention Conditioning</h4><p>생성/정책 네트워크의 latent 토큰을 query로, 외부 조건(텍스트·목표 이미지·언어 지시·센서) 시퀀스를 key/value로 삼아 attention으로 주입하는 조건화(conditioning) 방식.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>효율화</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/flash-attention"><h4>Flash Attention</h4><p>Attention 연산을 HBM에 N×N 행렬로 materialize하지 않고, SRAM 단위 tiling + online softmax + backward recomputation으로 IO를 줄여 exact attention을 빠르고 메모리 효율적으로 계산하는 IO-aware kernel 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/sparse-attention"><h4>Sparse Attention</h4><p>Full … attention 행렬을 미리 정한(또는 학습/라우팅으로 정한) 희소 패턴 … 위에서만 계산해 긴 시퀀스의 attention 비용을 줄이는 기법군.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/linear-attention"><h4>Linear Attention</h4><p>softmax attention의 … 유사도를 커널 특징맵 …로 분해해, attention을 …에서 …(또는 상수 메모리 recurrent state)으로 바꾸는 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/sliding-window-attention"><h4>Sliding Window Attention</h4><p>각 토큰이 고정 크기 …의 국소 이웃에만 attention하는 sparse attention 패턴으로, 시퀀스 길이에 선형인 비용으로 long-context를 처리하는 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/dilated-attention"><h4>Dilated Attention</h4><p>Self-attention을 dilation rate …와 segment 길이 …로 희소화해, 국소 패턴과 장거리 의존성을 동시에 잡으면서 시퀀스 길이에 선형인 복잡도를 얻는 sparse attention 기법.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>Grouped-Query Attention</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>위치·캐시</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>RoPE</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>KV Cache</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>

[[techniques/index|← 기법 사전 전체]]
