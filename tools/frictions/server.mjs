// Throwaway friction picker. Run: node tools/frictions/server.mjs  → http://localhost:4747
// State lives in tools/frictions/frictions.json (seeded from seed.json on first run).
import { createServer } from "node:http";
import { readFileSync, writeFileSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const dir = dirname(fileURLToPath(import.meta.url));
const DATA = join(dir, "frictions.json");
const SEED = join(dir, "seed.json");
const PORT = 4747;

if (!existsSync(DATA)) {
  const seed = JSON.parse(readFileSync(SEED, "utf8"));
  writeFileSync(DATA, JSON.stringify(seed.map((x, i) => ({ id: i + 1, ...x })), null, 1));
}
const load = () => JSON.parse(readFileSync(DATA, "utf8"));
const save = (items) => writeFileSync(DATA, JSON.stringify(items, null, 1));

const html = String.raw`<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Frictions</title>
<style>
:root{--bg:#F3F1E9;--ink:#141412;--soft:#7B776C;--line:#DAD6CA;--card:#fff;--lime:#C8F169;--star:#141412}
@media(prefers-color-scheme:dark){:root{--bg:#161512;--ink:#EAE8E1;--soft:#9B968A;--line:#2E2C26;--card:#1F1E1A}}
*{box-sizing:border-box;margin:0;padding:0}
body{background:var(--bg);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif;padding:28px 20px 80px}
.wrap{max-width:820px;margin:0 auto}
header{display:flex;justify-content:space-between;align-items:baseline;gap:16px;flex-wrap:wrap;margin-bottom:18px}
h1{font-size:22px;letter-spacing:-.01em}
.count{font-size:13px;color:var(--soft)}
.count b{color:var(--ink)}
.bar{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:14px;align-items:center}
.chip{border:1px solid var(--line);background:transparent;color:var(--ink);border-radius:999px;padding:6px 12px;font-size:13px;cursor:pointer}
.chip.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
.spacer{flex:1}
.add{display:flex;gap:8px;margin-bottom:22px}
.add input,.add select{border:1px solid var(--line);background:var(--card);color:var(--ink);border-radius:8px;padding:10px 12px;font:inherit}
.add input{flex:1}
.add button{background:var(--lime);color:#141412;border:0;border-radius:8px;padding:10px 16px;font:inherit;font-weight:600;cursor:pointer}
h2{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin:22px 0 8px}
ul{list-style:none}
li{display:flex;align-items:center;gap:12px;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:10px 12px;margin-bottom:6px}
li.star{border-color:var(--ink)}
.s{width:30px;height:30px;border-radius:50%;border:1px solid var(--line);background:transparent;cursor:pointer;font-size:15px;flex:none;color:var(--ink)}
li.star .s{background:var(--lime);border-color:var(--lime);color:#141412}
.t{flex:1;outline:none;border-radius:4px;padding:2px 4px}
.t:focus{background:var(--bg)}
.v{display:flex;gap:2px;flex:none}
.v button{width:26px;height:26px;border-radius:6px;border:1px solid var(--line);background:transparent;color:var(--soft);cursor:pointer;font-size:12px}
.v button.on{background:var(--ink);color:var(--bg);border-color:var(--ink)}
li.down{opacity:.45}
.x{color:var(--soft);background:none;border:0;cursor:pointer;font-size:16px;opacity:.5}
.x:hover{opacity:1}
.hint{font-size:12px;color:var(--soft);margin-top:30px}
kbd{font-family:inherit;border:1px solid var(--line);border-radius:4px;padding:0 4px}
</style></head><body><div class="wrap">
<header><h1>Frictions</h1><div class="count" id="count"></div></header>
<div class="bar" id="filters"></div>
<form class="add" id="add"><select id="area"><option>everyday</option><option>office</option><option>designer</option><option>developer</option></select>
<input id="text" placeholder="add a friction — short, in the voice…" autocomplete="off"><button>Add</button></form>
<div id="lists"></div>
<p class="hint">Click <kbd>★</kbd> to favorite, <kbd>▲</kbd> keep / <kbd>▼</kbd> cut. Click text to edit inline (blur to save). Everything writes to <code>tools/frictions/frictions.json</code>.</p>
</div>
<script>
const AREAS=["everyday","office","designer","developer"];
let items=[],filter="all";
const $=s=>document.querySelector(s);
async function api(m,b){const r=await fetch("/api",{method:m,headers:{"content-type":"application/json"},body:b?JSON.stringify(b):undefined});return r.json()}
async function load(){items=await api("GET");render()}
function render(){
  const stars=items.filter(i=>i.star).length;
  const up=items.filter(i=>i.vote>0).length,dn=items.filter(i=>i.vote<0).length;
  $("#count").innerHTML='<b>'+stars+'</b> favorites · <b>'+up+'</b> ▲ · <b>'+dn+'</b> ▼ · '+items.length+' total';
  $("#filters").innerHTML=['all','★','▲','▼',...AREAS].map(a=>'<button class="chip'+(filter===a?' on':'')+'" data-f="'+a+'">'+a+'</button>').join('');
  $("#filters").querySelectorAll(".chip").forEach(b=>b.onclick=()=>{filter=b.dataset.f;render()});
  const groups=filter==='★'?[['★ favorites',items.filter(i=>i.star)]]:filter==='▲'?[['▲ upvoted',items.filter(i=>i.vote>0)]]:filter==='▼'?[['▼ downvoted',items.filter(i=>i.vote<0)]]:AREAS.filter(a=>filter==='all'||filter===a).map(a=>[a,items.filter(i=>i.area===a)]);
  $("#lists").innerHTML=groups.map(([g,list])=>'<h2>'+g+' · '+list.length+'</h2><ul>'+list.map(i=>
    '<li class="'+(i.star?'star':'')+(i.vote<0?' down':'')+'" data-id="'+i.id+'"><button class="s" title="favorite">'+(i.star?'★':'☆')+'</button><span class="t" contenteditable spellcheck="false">'+esc(i.text)+'</span><span class="v"><button class="up'+(i.vote>0?' on':'')+'" title="keep">▲</button><button class="dn'+(i.vote<0?' on':'')+'" title="cut">▼</button></span><button class="x" title="delete">×</button></li>').join('')+'</ul>').join('');
  $("#lists").querySelectorAll("li").forEach(li=>{
    const id=+li.dataset.id;
    li.querySelector(".s").onclick=async()=>{items=await api("PATCH",{id,toggle:true});render()};
    li.querySelector(".up").onclick=async()=>{const cur=items.find(i=>i.id===id);items=await api("PATCH",{id,vote:cur.vote>0?0:1});render()};
    li.querySelector(".dn").onclick=async()=>{const cur=items.find(i=>i.id===id);items=await api("PATCH",{id,vote:cur.vote<0?0:-1});render()};
    li.querySelector(".x").onclick=async()=>{items=await api("DELETE",{id});render()};
    const t=li.querySelector(".t");
    t.onblur=async()=>{const text=t.textContent.trim();const cur=items.find(i=>i.id===id);if(text&&text!==cur.text){items=await api("PATCH",{id,text});render()}};
    t.onkeydown=e=>{if(e.key==="Enter"){e.preventDefault();t.blur()}};
  });
}
function esc(s){return s.replace(/[&<>]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;'}[c]))}
$("#add").onsubmit=async e=>{e.preventDefault();const text=$("#text").value.trim();if(!text)return;items=await api("POST",{area:$("#area").value,text});$("#text").value="";render()};
load();
</script></body></html>`;

createServer((req, res) => {
  const send = (code, body, type = "application/json") => { res.writeHead(code, { "content-type": type }); res.end(body); };
  if (req.url === "/" && req.method === "GET") return send(200, html, "text/html; charset=utf-8");
  if (req.url !== "/api") return send(404, "{}");
  let raw = ""; req.on("data", (c) => (raw += c)); req.on("end", () => {
    let items = load(); const b = raw ? JSON.parse(raw) : {};
    if (req.method === "POST") { const id = Math.max(0, ...items.map((i) => i.id)) + 1; items.push({ id, area: b.area, text: b.text, star: true, vote: 0 }); }
    if (req.method === "PATCH") { const it = items.find((i) => i.id === b.id); if (it) { if (b.toggle) it.star = !it.star; if (typeof b.text === "string") it.text = b.text; if (typeof b.vote === "number") it.vote = b.vote; } }
    if (req.method === "DELETE") items = items.filter((i) => i.id !== b.id);
    if (req.method !== "GET") save(items);
    send(200, JSON.stringify(items));
  });
}).listen(PORT, () => console.log(`Frictions → http://localhost:${PORT}`));
