---
title: "⚡ 효율화·적응"
date: 2026-11-26
tags: [technique-category]
---

<p class="tc-lead">큰 모델을 적은 자원으로 학습·적응·배포하는 기법.</p>
<div class="mh-section"><span>Parameter-Efficient Fine-Tuning</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/lora"><h4>LoRA</h4><p>거대 모델의 몸통은 얼려두고, 옆에 얇은 '덧대기 판' 두 장만 붙여 학습하는 초경량 미세조정 기법 — 두꺼운 사전에 포스트잇만 붙이는 셈.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>QLoRA</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/adapter"><h4>Adapter</h4><p>큰 모델 안에 끼워 넣는 작은 '변환 플러그'로, 전체를 다시 학습하지 않고 특정 작업에 빠르게 적응시키는 방법</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/prefix-tuning"><h4>Prefix Tuning</h4><p>모델 몸통은 그대로 두고, 주의력(attention) 메모리에 붙이는 작은 '지시문 스티커'만 학습해서 새 일에 적응시키는 방법</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>압축·경량화</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/knowledge-distillation"><h4>Knowledge Distillation</h4><p>큰 '선생님' 모델이 정답을 맞히는 요령(확신의 정도까지)을 작은 '학생' 모델에게 과외로 옮겨 담는 효율화 기술</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/quantization"><h4>Quantization</h4><p>고해상도 사진을 JPEG로 저장하듯, 숫자를 굵직한 눈금으로 반올림해 모델을 4분의 1~8분의 1 크기로 눌러 담는 경량화 기법</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/structured-pruning"><h4>Structured Pruning</h4><p>가중치 하나하나를 자르는 대신, 쓸모없는 필터·채널·attention head 같은 덩어리를 통째로 뽑아 모델의 모양을 깔끔하게 줄이는 방법</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>조건부 계산</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/mixture-of-experts"><h4>Mixture of Experts</h4><p>MoE는 큰 병원에 전문의가 많지만, 접수대(라우터)가 환자마다 필요한 전문의 1~2명만 부르는 방식이다.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>추론 가속</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/speculative-decoding"><h4>Speculative Decoding</h4><p>작은 모델이 빠르게 '초안'을 여러 개 던지고, 큰 모델이 그걸 한 번에 채점해서 맞는 것만 채택하는 방식으로 LLM 추론을 2~3배 빠르게 만드는 기법 — 빠른 조수가 받아쓰고 선생님이 검토하는 회의록과 비슷하다.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Model Merging</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/task-arithmetic"><h4>Task Arithmetic</h4><p>미리 학습된 모델에 '작업별 변화량'을 더하거나 빼서 능력을 조합하는, 모델 가중치용 레고 블록 놀이.</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
