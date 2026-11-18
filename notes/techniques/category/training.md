---
title: "🎓 학습 기법"
date: 2026-11-19
tags: [technique-category]
---

<p class="tc-lead">모방학습, 강화학습, 선호 학습. 정책을 어떻게 가르치는가.</p>
<div class="mh-section"><span>모방학습</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/behavior-cloning"><h4>Behavior Cloning</h4><p>전문가가 운전하는 모습을 옆에서 지켜보고 '이 상황에선 이렇게 움직이더라'를 통째로 외워서 따라 하는 학습법 — 즉 로봇판 '보고 배우기(모방 학습)'의 가장 기본형.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>DAgger</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>강화학습</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/ppo"><h4>PPO</h4><p>정책(policy, 상황을 보고 행동을 고르는 규칙)을 업데이트하되 '한 번에 너무 멀리 가지 않도록 목줄을 채우는' 강화학습 기법 — 새 정책이 옛 정책에서 크게 벗어나면 이득을 잘라버린다.</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>Offline RL</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>선호 정렬</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>RLHF</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><div class="tc-card tc-todo"><h4>DPO</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>학습 전략</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>Curriculum Learning</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/chain-of-thought"><h4>Chain-of-Thought</h4><p>LLM이 최종 답을 바로 내지 않고 중간 추론 단계(reasoning steps)를 명시적으로 생성하도록 유도해 복잡한 다단계 추론 성능을 끌어올리는 프롬프팅/학습 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/coreset-selection"><h4>Coreset Selection</h4><p>전체 학습 데이터의 목적함수(그래디언트/손실)를 근사하도록 작은 가중 부분집합(coreset)을 선택해 학습 비용을 줄이는 데이터 선택 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/teacher-forcing"><h4>Teacher Forcing</h4><p>Autoregressive 모델 학습 시 이전 시점의 모델 예측 대신 ground-truth 이전 토큰(또는 상태)을 입력으로 넣어주는 학습 기법.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/continual-learning"><h4>Continual Learning</h4><p>AI가 국어를 배운 뒤 수학을 배워도 국어를 까먹지 않도록, 새로운 것을 순서대로 계속 배우게 하는 학습 방식 (새 과목을 배워도 이전 과목 노트가 지워지지 않는 공부법)</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>Harness Optimization</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/agent-evolution"><h4>Agent Evolution</h4><p>여러 에이전트 '변이체'를 만들어 실제 과제로 채점하고, 잘한 놈만 남겨 다음 세대를 만드는 다윈식 에이전트 개선법</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/proposer-selection-loop"><h4>Proposer-Selection Loop</h4><p>후보를 마구 찍어내는 '제안자(proposer)'와 그중 좋은 것만 골라내는 '선택자(selector)'를 번갈아 돌려, 모델이 자기 출력으로 스스로를 가르치는 학습 루프 — '작가 여러 명에게 초안을 잔뜩 쓰게 하고 편집자가 최고만 골라 다음 호 교재로 쓰는 출판사'.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/in-context-learning"><h4>In-context Learning</h4><p>시험지 맨 앞에 '예시 답안' 몇 개를 붙여주면, 모델이 가중치를 하나도 안 바꾸고 그 자리에서 새 과제 규칙을 눈치껏 파악해 답하는 능력</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>불확실성 추정</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/conformal-prediction"><h4>Conformal Prediction</h4><p>모델 출력에 대해 분포 가정 없이 유한 표본(finite-sample) 보장된 예측 집합/구간을 만들어주는 사후 보정(post-hoc calibration) 프레임워크.</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/evaluation-noise"><h4>Evaluation Noise</h4><p>시험 채점에 약간의 흔들림을 넣거나 여러 번 채점해서, 운 좋은 한 번의 점수에 속지 않고 진짜 실력을 보게 만드는 학습 보조 기법.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>평가 방법론</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/statistical-significance"><h4>Statistical Significance</h4><p>실험 점수 차이가 '진짜 실력 차이'인지 '운 좋게 나온 우연'인지 구분해 주는 통계적 판정 도구 — 동전 10번 던져 앞면 7번 나왔다고 조작이라 단정할 수 없는 것과 같은 이치</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
