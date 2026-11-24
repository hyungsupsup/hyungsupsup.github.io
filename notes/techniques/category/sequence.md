---
title: "🐍 시퀀스 대안"
date: 2026-11-25
tags: [technique-category]
---

<p class="tc-lead">attention 없이 긴 시퀀스를 다루는 recurrent / state space 계열.</p>
<div class="mh-section"><span>State Space Model</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/state-space-model"><h4>State Space Model (S4)</h4><p>S4(Structured State Space Sequence model, 구조화된 상태 공간 시퀀스 모델)는 긴 시퀀스를 '작은 기억 상자'로 요약하고, 그 상자를 시간 규칙으로 빠르게 갱신해서 다음 출력을 만드는 시퀀스 모델이다.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/mamba"><h4>Mamba</h4><p>Transformer처럼 모든 단어를 서로 비교하지 않고, 컨베이어 벨트처럼 흐름을 따라가며 중요한 정보만 골라 기억하는 고속 시퀀스 모델</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Recurrent</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/rwkv"><h4>RWKV</h4><p>Transformer처럼 병렬로 학습하고 RNN처럼 순서대로 기억을 갱신하는 경량 시퀀스 모델</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
