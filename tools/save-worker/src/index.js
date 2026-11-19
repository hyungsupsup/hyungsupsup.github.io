// 섭웨이 ☆ 담기 버튼 → alphaXiv 북마크 중계 (Cloudflare Worker)
// 비밀 값(wrangler secret): ALPHAXIV_API_KEY, SAVE_TOKEN
// POST /ping  — 비밀번호 확인
// POST /save  {"id": "2611.18359"} — alphaXiv 'Want to read' 폴더에 저장

const ALLOWED_ORIGINS = ["https://hyungsupsup.github.io", "http://localhost:8080"]
const ARXIV_ID = /^\d{4}\.\d{4,5}(v\d+)?$/

function cors(origin) {
  const o = ALLOWED_ORIGINS.includes(origin) ? origin : ALLOWED_ORIGINS[0]
  return {
    "Access-Control-Allow-Origin": o,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Authorization, Content-Type",
    "Access-Control-Max-Age": "86400",
    Vary: "Origin",
  }
}

function json(body, status, origin) {
  return new Response(JSON.stringify(body), {
    status,
    headers: { "Content-Type": "application/json", ...cors(origin) },
  })
}

// 길이가 같을 때만 비교하고, 내용은 일정 시간 비교
function safeEqual(a, b) {
  if (typeof a !== "string" || typeof b !== "string" || a.length !== b.length) return false
  let r = 0
  for (let i = 0; i < a.length; i++) r |= a.charCodeAt(i) ^ b.charCodeAt(i)
  return r === 0
}

async function alphaxiv(env, tool, args) {
  const res = await fetch("https://api.alphaxiv.org/mcp/v1", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json, text/event-stream",
      Authorization: `Bearer ${env.ALPHAXIV_API_KEY}`,
    },
    body: JSON.stringify({ jsonrpc: "2.0", id: 1, method: "tools/call", params: { name: tool, arguments: args } }),
  })
  const text = await res.text()
  const line = text.split("\n").find((l) => l.startsWith("data:"))
  const msg = JSON.parse(line ? line.slice(5) : text)
  if (msg.error || msg.result?.isError) {
    throw new Error(JSON.stringify(msg.error || msg.result?.content || "alphaXiv error").slice(0, 300))
  }
  return msg.result
}

export default {
  async fetch(request, env) {
    const origin = request.headers.get("Origin") || ""
    if (request.method === "OPTIONS") return new Response(null, { status: 204, headers: cors(origin) })
    if (request.method !== "POST") return json({ error: "method" }, 405, origin)
    if (!ALLOWED_ORIGINS.includes(origin)) return json({ error: "origin" }, 403, origin)

    const auth = (request.headers.get("Authorization") || "").replace(/^Bearer\s+/i, "")
    if (!env.SAVE_TOKEN || !safeEqual(auth, env.SAVE_TOKEN)) return json({ error: "auth" }, 401, origin)

    const path = new URL(request.url).pathname
    if (path === "/ping") return json({ ok: true }, 200, origin)
    if (path !== "/save") return json({ error: "not found" }, 404, origin)

    let id = ""
    try {
      id = String((await request.json()).id || "").trim()
    } catch {}
    if (!ARXIV_ID.test(id)) return json({ error: "bad id" }, 400, origin)

    try {
      await alphaxiv(env, "save_papers_to_folder", { paper_ids_or_urls: [id] })
      return json({ ok: true, id }, 200, origin)
    } catch (e) {
      return json({ error: "alphaxiv", detail: String(e.message || e) }, 502, origin)
    }
  },
}
