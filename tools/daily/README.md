# daily

매일 인사이트 생성 + 기법 사전 자동 확장 + 즐겨찾기 논문 동기화. LLM·DB 설정은 루트 `.env` (paper-db와 공유).

```powershell
python tools/daily/daily.py run                          # 오늘 것 1회 생성
python tools/daily/daily.py serve --push                 # 상주: 매일 07:30 생성 후 push ('생성 중' 페이지를 먼저 올림) + 1시간마다 즐겨찾기 동기화
python tools/daily/daily.py serve --at 07:30 --push --cards 3   # 기법 카드 하루 3장
python tools/daily/daily.py card "Mamba" --category "시퀀스 대안" # 카드 1장 수동 생성
python tools/daily/daily.py saved --push                 # alphaXiv 북마크 → 즐겨찾기 논문 즉시 동기화
python tools/daily/daily.py export                       # DB → notes/ md 전부 다시 쓰기
python tools/daily/daily.py migrate                      # (한 번) 예전 json/md 파일 → DB
```

## 저장소

데이터 원본은 PostgreSQL (`.env`의 `SUPNOTE_DB_HOST/PORT/NAME/USER/PASSWORD/SCHEMA`, 기본 스키마 `supnote`). 테이블은 처음 접속할 때 자동 생성된다.

| 테이블 | 내용 |
|---|---|
| `categories` | 기법 사전 카테고리 |
| `techniques` | 기법 목록 (카테고리·세부 분류, `origin`: seed / paper 자동 추가) |
| `technique_cards` | 기법 카드 (LLM 원본 JSON + 렌더링된 md) |
| `daily_runs` | 날짜별 데일리 (상태 generating/done, 흐름·질문, 렌더링된 md) |
| `daily_papers` | 날짜별 논문 20편 (출처·순위·추천수·입문자용 해설 JSON) |
| `saved_papers` | 즐겨찾기 논문 (alphaXiv 북마크, 담은 날짜, 해설 JSON) |

`notes/techniques/`, `notes/daily/`, `notes/knowledge/saved/`의 md는 사이트 빌드용으로 DB에서 렌더링한 결과다. 직접 고치지 말고 DB를 고친 뒤 `export`.

- `serve`: 1분마다 확인, 지정 시각 이후 오늘 데일리가 완료 상태가 아니면 생성 (PC를 늦게 켜도 그날 것 생성). 실패 시 10분 후 재시도.
