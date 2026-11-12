# paper-db

탑티어 학회 논문 → Physical AI 관련 논문 필터 → LLM 요약 → 인용 관계 → Quartz 노트.

## 설정
저장소 루트에 `.env` (`.env.example` 참고, git 제외)
```
LLM_BASE_URL=https://.../v1        # OpenAI 호환 API
DEFAULT_LLM_MODEL=...
LLM_API_KEY=sk-...
S2_API_KEY=                        # 선택
```

## 실행 (저장소 루트에서)
```powershell
python tools/paper-db/paperdb.py all --venue cvpr --year 2025
```
단계별:
| 단계 | 하는 일 | 출처 |
|---|---|---|
| `collect` | 학회 전체 논문 목록, 제목 키워드로 1차 후보 표시 | CVF Open Access |
| `abstracts` | 후보 논문 초록 수집 | CVF 논문 페이지 |
| `summarize` | LLM이 관련성 판정 + 한국어 요약 (중단 후 재실행하면 이어서) | `.env`의 LLM |
| `link` | 인용수·참고문헌 → 논문 간 연결 | Semantic Scholar |
| `export` | `notes/knowledge/venues/<학회-연도>/` 노트 생성 | — |

테스트: `summarize --limit 5`

## 데이터
`data/<venue><year>.jsonl` — 논문 1편 = 1줄. 요약 결과가 캐시되므로 다시 돌려도 이미 요약한 논문은 건너뜀.

## 지원 학회
현재 CVF 계열(CVPR/ICCV/ECCV/WACV). 다음: OpenReview(ICLR/NeurIPS/CoRL), DBLP(ICRA/IROS/RSS).
