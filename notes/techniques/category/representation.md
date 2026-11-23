---
title: "👁️ 표현학습"
date: 2026-11-24
tags: [technique-category]
---

<p class="tc-lead">라벨 없이 좋은 표현을 배우는 법. VLA의 비전 인코더가 여기서 나온다.</p>
<div class="mh-section"><span>Vision-Language</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>CLIP</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/siglip"><h4>SigLIP</h4><p>이미지와 글을 '짝이면 1, 아니면 0'으로 하나하나 채점하는 방식으로 CLIP을 더 가볍고 유연하게 만든 이미지-텍스트 대조 학습법 — 반 전체 등수 매기기 대신 짝별 O/X 퀴즈로 공부시키는 셈.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Self-Supervised Vision</span></div>
<div class="tc-grid"><div class="tc-card tc-todo"><h4>DINO</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div><a class="tc-card internal" href="/techniques/dinov2"><h4>DINOv2</h4><p>라벨 없이 사진 여러 장을 보고, 같은 사물을 다른 크기·다른 각도로 잘라보며 '이건 같은 물건이야'라고 스스로 맞추는 비전 표현학습</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/mae"><h4>MAE</h4><p>이미지의 일부 조각을 가리고 남은 조각으로 가려진 부분을 복원하게 해, 모델이 '무엇이 무엇인지'와 '공간이 어떻게 이어지는지'를 스스로 배우게 하는 방법</p><span class="tc-badge">초안</span></a><div class="tc-card tc-todo"><h4>Contrastive Learning (SimCLR)</h4><p>아직 작성 전 — 데일리에서 순서대로 추가됨</p><span class="tc-badge">예정</span></div></div>
<div class="mh-section"><span>Predictive</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/jepa"><h4>JEPA</h4><p>사진의 모든 픽셀을 그대로 베끼는 대신 '장면의 의미'만 요약해서 예측하는 자기지도 학습 틀 — 눈 감고 그림 그리기가 아니라 눈 감고 '분위기' 맞히기.</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>Dimensionality Reduction</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/principal-component-analysis"><h4>Principal Component Analysis</h4><p>데이터에서 가장 크게 움직이는 방향 몇 개만 골라 뽑아, 복잡한 정보를 간단히 요약하는 '차원 압축기'</p><span class="tc-badge">초안</span></a><a class="tc-card internal" href="/techniques/partial-least-squares"><h4>Partial Least Squares</h4><p>입력 데이터와 목표값이 서로 가장 잘 설명하는 '공통 언어'를 찾아 차원을 줄이는 지도 학습형 압축 기법</p><span class="tc-badge">초안</span></a></div>
<div class="mh-section"><span>3D Representation</span></div>
<div class="tc-grid"><a class="tc-card internal" href="/techniques/3d-gaussian-splatting"><h4>3D Gaussian Splatting</h4><p>수천만 개의 작은 반투명 색구름을 3D 공간에 뿌려 놓고, 카메라 방향에 따라 겹쳐서 그림을 그리는 3D 장면 표현</p><span class="tc-badge">초안</span></a></div>

[[techniques/index|← 기법 사전 전체]]
