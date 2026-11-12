// [섭노트 custom] 사이드바 열기/닫기 버튼과 드래그 너비 조절.
// 상태는 localStorage에 저장하고, 초기 적용은 sidebar-init.inline.ts가 담당한다.
// SPA 이동 시 micromorph가 body를 다시 맞추면서 추가한 요소가 지워지므로 "nav"마다 다시 붙인다.

type Side = "left" | "right"

const SIDES: Side[] = ["left", "right"]
const MIN_W = 200
const MAX_W = 600
const DEFAULT_W = 320
const root = document.documentElement

const store = {
  get(key: string): string | null {
    try {
      return localStorage.getItem(key)
    } catch {
      return null
    }
  },
  set(key: string, value: string) {
    try {
      localStorage.setItem(key, value)
    } catch {
      // 저장 실패 시 이번 방문 동안만 유지
    }
  },
}

const LABEL: Record<Side, string> = { left: "왼쪽 사이드바", right: "오른쪽 사이드바" }

function panelIcon(side: Side): string {
  const x = side === "left" ? 9 : 15
  return `<svg xmlns="http://www.w3.org/2000/svg" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><line x1="${x}" y1="3" x2="${x}" y2="21"/></svg>`
}

function isCollapsed(side: Side): boolean {
  return root.classList.contains(`sb-${side}-collapsed`)
}

function updateButton(side: Side) {
  const btn = document.getElementById(`sb-toggle-${side}`)
  if (!btn) return
  const collapsed = isCollapsed(side)
  const label = `${LABEL[side]} ${collapsed ? "열기" : "닫기"}`
  btn.setAttribute("aria-label", label)
  btn.setAttribute("title", label)
  btn.setAttribute("aria-expanded", String(!collapsed))
}

function setCollapsed(side: Side, collapsed: boolean) {
  root.classList.toggle(`sb-${side}-collapsed`, collapsed)
  store.set(`sb-${side}-collapsed`, collapsed ? "1" : "0")
  updateButton(side)
}

function clampWidth(px: number): number {
  return Math.round(Math.min(MAX_W, Math.max(MIN_W, px)))
}

function applyWidth(side: Side, px: number): number {
  const w = clampWidth(px)
  root.style.setProperty(`--sb-${side}-w`, `${w}px`)
  return w
}

function ensureToggle(side: Side) {
  if (document.getElementById(`sb-toggle-${side}`)) return
  const btn = document.createElement("button")
  btn.id = `sb-toggle-${side}`
  btn.type = "button"
  btn.className = `sb-toggle sb-toggle-${side}`
  btn.innerHTML = panelIcon(side)
  btn.addEventListener("click", () => setCollapsed(side, !isCollapsed(side)))
  document.body.appendChild(btn)
  updateButton(side)
}

function ensureResizer(side: Side) {
  const sidebar = document.querySelector<HTMLElement>(`.page[data-frame="default"] .sidebar.${side}`)
  if (!sidebar || sidebar.querySelector(":scope > .sb-resizer")) return

  const handle = document.createElement("div")
  handle.className = "sb-resizer"
  handle.setAttribute("role", "separator")
  handle.setAttribute("aria-orientation", "vertical")
  handle.setAttribute("title", "드래그: 너비 조절 · 더블클릭: 기본 너비")

  handle.addEventListener("pointerdown", (e: PointerEvent) => {
    if (e.button !== 0) return
    e.preventDefault()
    const rect = sidebar.getBoundingClientRect()
    let width = rect.width
    handle.setPointerCapture(e.pointerId)
    root.classList.add("sb-resizing")

    const onMove = (ev: PointerEvent) => {
      const raw = side === "left" ? ev.clientX - rect.left : rect.right - ev.clientX
      width = applyWidth(side, raw)
    }
    const onUp = (ev: PointerEvent) => {
      if (handle.hasPointerCapture(ev.pointerId)) handle.releasePointerCapture(ev.pointerId)
      handle.removeEventListener("pointermove", onMove)
      handle.removeEventListener("pointerup", onUp)
      handle.removeEventListener("pointercancel", onUp)
      root.classList.remove("sb-resizing")
      store.set(`sb-${side}-w`, String(Math.round(width)))
    }
    handle.addEventListener("pointermove", onMove)
    handle.addEventListener("pointerup", onUp)
    handle.addEventListener("pointercancel", onUp)
  })

  handle.addEventListener("dblclick", () => {
    applyWidth(side, DEFAULT_W)
    store.set(`sb-${side}-w`, String(DEFAULT_W))
  })

  sidebar.appendChild(handle)
}

function setupSidebarControls() {
  // 기본 3단 레이아웃 페이지에서만 동작 (404 등 사이드바 없는 프레임 제외)
  if (!document.querySelector('.page[data-frame="default"]')) return
  for (const side of SIDES) {
    ensureToggle(side)
    ensureResizer(side)
  }
}

document.addEventListener("nav", setupSidebarControls)
document.addEventListener("render", setupSidebarControls)
