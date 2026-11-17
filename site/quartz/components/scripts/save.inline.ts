// 데일리 카드의 ☆ 담기 → Cloudflare Worker(tools/save-worker) → alphaXiv 북마크
// 비밀번호는 기기마다 처음 한 번 입력하고 localStorage에 기억한다. 없으면 기존처럼 alphaXiv 페이지로 이동.
const WORKER_URL = "https://supnote-save.hyungsupsup.workers.dev"
const TOKEN_KEY = "sn-save-token"
const SAVED_KEY = "sn-saved-ids"

function store(key: string, value?: string): string | null {
  try {
    if (value === undefined) return localStorage.getItem(key)
    if (value === "") localStorage.removeItem(key)
    else localStorage.setItem(key, value)
  } catch {}
  return null
}

function savedIds(): Set<string> {
  try {
    return new Set(JSON.parse(store(SAVED_KEY) || "[]"))
  } catch {
    return new Set()
  }
}

function markSaved(a: HTMLElement) {
  a.textContent = "⭐ 담음"
  a.classList.add("on")
  a.removeAttribute("href")
}

async function call(path: string, token: string, body?: object): Promise<Response> {
  return fetch(WORKER_URL + path, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}`, "Content-Type": "application/json" },
    body: JSON.stringify(body || {}),
  })
}

async function ensureToken(): Promise<string | null> {
  const t = store(TOKEN_KEY)
  if (t) return t
  const entered = window.prompt("담기 비밀번호 (이 기기에서 한 번만 입력)\n취소하면 alphaXiv 페이지로 이동합니다.")
  if (!entered) return null
  const r = await call("/ping", entered).catch(() => null)
  if (!r || !r.ok) {
    window.alert(r && r.status === 401 ? "비밀번호가 틀렸어요." : "저장 서버에 연결하지 못했어요.")
    return null
  }
  store(TOKEN_KEY, entered)
  return entered
}

async function onClick(e: MouseEvent) {
  const a = (e.target as HTMLElement).closest("a.dp-star") as HTMLAnchorElement | null
  if (!a || a.classList.contains("on") || a.dataset.busy) return
  const id = (a.href.match(/abs\/([\d.v]+)/) || [])[1]
  if (!id) return
  e.preventDefault()
  a.dataset.busy = "1"
  const original = a.textContent
  try {
    const token = await ensureToken()
    if (!token) {
      window.open(a.href, "_blank", "noopener")
      return
    }
    a.textContent = "담는 중…"
    const r = await call("/save", token, { id })
    if (r.status === 401) {
      store(TOKEN_KEY, "")
      window.alert("비밀번호가 바뀌었어요. 다시 눌러서 입력해 주세요.")
      a.textContent = original
      return
    }
    if (!r.ok) throw new Error(String(r.status))
    const ids = savedIds()
    ids.add(id)
    store(SAVED_KEY, JSON.stringify([...ids]))
    markSaved(a)
  } catch {
    a.textContent = original
    window.alert("담기에 실패했어요. 잠시 후 다시 시도해 주세요.")
  } finally {
    delete a.dataset.busy
  }
}

function init() {
  const ids = savedIds()
  document.querySelectorAll<HTMLAnchorElement>("a.dp-star").forEach((a) => {
    const id = (a.href.match(/abs\/([\d.v]+)/) || [])[1]
    if (id && ids.has(id)) markSaved(a)
  })
}

document.addEventListener("click", onClick)
document.addEventListener("nav", init)
init()
