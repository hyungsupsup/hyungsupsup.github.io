---
title: 분야 지도 — Physical AI 대표 논문 계보
date: 2026-11-12
tags: [map]
---

피지컬 AI의 주요 갈래와 대표 논문입니다. **고전에서 최신 순서**로 읽으면 흐름이 잡힙니다.

- 우선순위: ★★★ 필독 / ★★ 권장 / ★ 참고
- 상태: ⬜ 안 읽음 / 📄 L1 요약 / 📖 L2 정독 / 🧪 L3 재현
- 💡는 내 배경(diffusion·CV·LLM)과 바로 연결되는 논문
- 2026년 중반 이후 논문은 [[knowledge/digests/index|주간 다이제스트]]로 보강합니다. arXiv 번호는 처음 읽을 때 한 번 더 확인합니다.

## 0. 기반 기술 (복습용)
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| PPO — Proximal Policy Optimization | 2017 | [1707.06347](https://arxiv.org/abs/1707.06347) | ★★ | ⬜ |
| DDPM 💡 | 2020 | [2006.11239](https://arxiv.org/abs/2006.11239) | ★ | ⬜ |

## 1. 모방학습 (Imitation Learning)
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| BC-Z | 2022 | [2202.02005](https://arxiv.org/abs/2202.02005) | ★ | ⬜ |
| **Diffusion Policy** 💡 | 2023 | [2303.04137](https://arxiv.org/abs/2303.04137) | ★★★ | ⬜ |
| **ACT / ALOHA** | 2023 | [2304.13705](https://arxiv.org/abs/2304.13705) | ★★★ | ⬜ |
| Mobile ALOHA | 2024 | [2401.02117](https://arxiv.org/abs/2401.02117) | ★★ | ⬜ |
| UMI — Universal Manipulation Interface | 2024 | [2402.10329](https://arxiv.org/abs/2402.10329) | ★★ | ⬜ |

## 2. LLM·VLM과 로봇 (VLA 이전)
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| **SayCan** 💡 | 2022 | [2204.01691](https://arxiv.org/abs/2204.01691) | ★★★ | ⬜ |
| Code as Policies 💡 | 2022 | [2209.07753](https://arxiv.org/abs/2209.07753) | ★★ | ⬜ |
| Gato | 2022 | [2205.06175](https://arxiv.org/abs/2205.06175) | ★ | ⬜ |
| PaLM-E | 2023 | [2303.03378](https://arxiv.org/abs/2303.03378) | ★★ | ⬜ |

## 3. 로봇 파운데이션 모델 / VLA
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| **RT-1** | 2022 | [2212.06817](https://arxiv.org/abs/2212.06817) | ★★★ | ⬜ |
| **RT-2** | 2023 | [2307.15818](https://arxiv.org/abs/2307.15818) | ★★★ | ⬜ |
| **Open X-Embodiment** (데이터셋) | 2023 | [2310.08864](https://arxiv.org/abs/2310.08864) | ★★★ | ⬜ |
| DROID (데이터셋) | 2024 | [2403.12945](https://arxiv.org/abs/2403.12945) | ★ | ⬜ |
| Octo | 2024 | [2405.12213](https://arxiv.org/abs/2405.12213) | ★★ | ⬜ |
| **OpenVLA** | 2024 | [2406.09246](https://arxiv.org/abs/2406.09246) | ★★★ | ⬜ |
| **π0** 💡 (flow matching) | 2024 | [2410.24164](https://arxiv.org/abs/2410.24164) | ★★★ | ⬜ |
| OpenVLA-OFT | 2025 | [2502.19645](https://arxiv.org/abs/2502.19645) | ★★ | ⬜ |
| GR00T N1 | 2025 | [2503.14734](https://arxiv.org/abs/2503.14734) | ★★ | ⬜ |
| π0.5 | 2025 | [2504.16054](https://arxiv.org/abs/2504.16054) | ★★ | ⬜ |
| SmolVLA | 2025 | [2506.01844](https://arxiv.org/abs/2506.01844) | ★★ | ⬜ |

## 4. 월드모델 (World Models)
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| **World Models** (Ha & Schmidhuber) | 2018 | [1803.10122](https://arxiv.org/abs/1803.10122) | ★★★ | ⬜ |
| Dreamer (v1) | 2019 | [1912.01603](https://arxiv.org/abs/1912.01603) | ★★ | ⬜ |
| **DreamerV3** | 2023 | [2301.04104](https://arxiv.org/abs/2301.04104) | ★★★ | ⬜ |
| UniSim 💡 | 2023 | [2310.06114](https://arxiv.org/abs/2310.06114) | ★★ | ⬜ |
| Genie 💡 | 2024 | [2402.15391](https://arxiv.org/abs/2402.15391) | ★★ | ⬜ |
| DINO-WM | 2024 | [2411.04983](https://arxiv.org/abs/2411.04983) | ★★ | ⬜ |
| **Cosmos World Foundation Model** 💡 | 2025 | [2501.03575](https://arxiv.org/abs/2501.03575) | ★★★ | ⬜ |
| V-JEPA 2 | 2025 | [2506.09985](https://arxiv.org/abs/2506.09985) | ★★ | ⬜ |

## 5. 시뮬레이션 / Sim2Real / RL
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| **Domain Randomization** (Tobin et al.) | 2017 | [1703.06907](https://arxiv.org/abs/1703.06907) | ★★★ | ⬜ |
| RMA — Rapid Motor Adaptation | 2021 | [2107.04034](https://arxiv.org/abs/2107.04034) | ★★ | ⬜ |
| **Isaac Gym** | 2021 | [2108.10470](https://arxiv.org/abs/2108.10470) | ★★ | ⬜ |
| Learning to Walk in Minutes (legged_gym) | 2021 | [2109.11978](https://arxiv.org/abs/2109.11978) | ★★ | ⬜ |

## 6. 벤치마크 / 평가
| 논문 | 연도 | arXiv | 우선 | 상태 |
|---|---|---|---|---|
| LIBERO | 2023 | [2306.03310](https://arxiv.org/abs/2306.03310) | ★★ | ⬜ |
| SimplerEnv — 시뮬레이션으로 실제 정책 평가 | 2024 | [2405.05941](https://arxiv.org/abs/2405.05941) | ★★ | ⬜ |

## 추천 읽기 순서 (Phase 0 ~ 1)
1. 큰 흐름 잡기: RT-1 → RT-2 → Open X-Embodiment → OpenVLA → π0
2. 강점과 연결: Diffusion Policy → π0 (flow matching) → Cosmos
3. 월드모델 계보: World Models → DreamerV3 → Genie → Cosmos
4. 시뮬레이션: Domain Randomization → Isaac Gym → SimplerEnv
