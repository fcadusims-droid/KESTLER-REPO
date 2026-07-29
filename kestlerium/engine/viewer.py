"""A janela do terrário.

Gera uma página estática a partir do estado do mundo. Sem servidor, sem engine,
sem assets: SVG desenhado na hora e dados embutidos no HTML.

**O que a visualização precisa mostrar é o invisível.** Onde cada um está é
trivial — a planta baixa resolve em quinze pontos. O que prende é o que não se
vê olhando: que alguém acredita numa versão errada do que aconteceu, que outro
está há semanas sem entender como o mundo funciona, que uma tensão vem
crescendo numa aresta há um mês. Por isso o mapa é pequeno e os painéis são
grandes.
"""

from __future__ import annotations

import json
import sqlite3

from . import clock as clockmod


def snapshot(conn: sqlite3.Connection, tick: int, world_name: str) -> dict:
    """O estado do mundo neste instante, pequeno o bastante para versionar."""
    agents = {r["id"]: dict(r) for r in conn.execute("SELECT * FROM agent")}
    locations = [dict(r) for r in conn.execute("SELECT * FROM location")]
    edges = [dict(r) for r in conn.execute("SELECT * FROM location_edge")]

    estado = [
        dict(r) for r in conn.execute(
            "SELECT agent_id, location_id, activity FROM agent_state WHERE tick = ?",
            (tick,),
        )
    ]

    facts = {r["id"]: dict(r) for r in conn.execute("SELECT * FROM fact")}
    beliefs = [dict(r) for r in conn.execute("SELECT * FROM belief")]
    relations = [dict(r) for r in conn.execute("SELECT * FROM relation")]
    knowledge = [
        dict(r) for r in conn.execute(
            "SELECT agent_id, concept, grasp, taught_by FROM knowledge")
    ]

    # Quem sabe o quê, na versão de cada um — o coração do que se quer ver.
    cabecas = {}
    for b in beliefs:
        f = facts.get(b["fact_id"])
        if not f:
            continue
        cabecas.setdefault(b["agent_id"], []).append({
            "sujeito": f["subject"],
            "predicado": f["predicate"],
            "acredita": b["distorted_object"] or f["object"],
            "verdade": f["object"],
            "fiel": b["distortion"] == 0,
            "confianca": round(b["confidence"], 2),
            "fonte": b["source_agent_id"],
        })

    sabedoria = {}
    for k in knowledge:
        sabedoria.setdefault(k["agent_id"], []).append(
            {"conceito": k["concept"], "dominio": round(k["grasp"], 2),
             "ensinou": k["taught_by"]}
        )

    # Os fios de história — Fase 8. A planta baixa mostra onde as pessoas
    # estão; o fio mostra o que está acontecendo com elas ao longo de semanas,
    # que é a única coisa que um instante não consegue mostrar.
    fios = []
    for r in conn.execute(
            "SELECT * FROM thread ORDER BY status, opened_day DESC LIMIT 12"):
        entradas = [dict(e) for e in conn.execute(
            "SELECT day, kind, text FROM thread_entry WHERE thread_id = ?"
            " ORDER BY day, id", (r["id"],))]
        fios.append({"titulo": r["title"], "estado": r["status"],
                     "abriu": r["opened_day"],
                     "entradas": entradas[-4:]})

    return {
        "mundo": world_name,
        "fios": fios,
        "tick": tick,
        "quando": clockmod.label(tick),
        "noite": clockmod.is_night(tick),
        "agentes": {a: {"nome": r["name"], "origem": r["origin"]}
                    for a, r in agents.items()},
        "locais": [
            {"id": l["id"], "nome": l["name"], "x": l["x"], "y": l["y"],
             "tipo": l["kind"]} for l in locations
        ],
        "arestas": [[e["from_id"], e["to_id"]] for e in edges
                    if e["from_id"] < e["to_id"]],
        "estado": estado,
        "cabecas": cabecas,
        "conhecimento": sabedoria,
        "relacoes": [
            {"a": r["agent_a"], "b": r["agent_b"],
             "afeto": round(r["affect"], 2), "confianca": round(r["trust"], 2),
             "tensao": round(r["tension"], 2)}
            for r in relations
            if abs(r["affect"]) > 0.05 or r["tension"] > 0.15
        ],
    }


PAGE = """<!doctype html>
<html lang="pt-BR"><head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Kestlerium</title>
<style>
:root{--bg:#0e0e12;--panel:#16161d;--line:#26262f;--txt:#e6e6ea;--dim:#8b8b96;
      --accent:#a78bfa;--warn:#f59e0b;--ok:#10b981}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--txt);
     font:15px/1.6 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif}
.wrap{max-width:1180px;margin:0 auto;padding:clamp(1rem,4vw,2.5rem)}
header{margin-bottom:1.6rem}
h1{font-size:.8rem;letter-spacing:.3em;text-transform:uppercase;color:var(--accent);
   margin:0 0 .5rem;font-weight:600}
.quando{font-size:clamp(1.4rem,4vw,2rem);font-weight:700;letter-spacing:-.02em;margin:0}
.sub{color:var(--dim);font-size:.9rem;margin:.3rem 0 0}
.grid{display:grid;gap:1.2rem;grid-template-columns:1fr}
@media(min-width:900px){.grid{grid-template-columns:1.1fr .9fr}}
.card{background:var(--panel);border:1px solid var(--line);border-radius:12px;padding:1.1rem 1.2rem}
.card h2{font-size:.72rem;letter-spacing:.18em;text-transform:uppercase;color:var(--dim);
         margin:0 0 .9rem;font-weight:600}
svg{width:100%;height:auto;display:block}
.loc{fill:#1d1d26;stroke:#2f2f3b}
.loc-lbl{fill:#6f6f7d;font-size:2.6px;text-anchor:middle}
.pes{fill:var(--accent)}
.pes-lbl{fill:#cfcfd8;font-size:2.4px;text-anchor:middle}
.via{stroke:#232330;stroke-width:.4}
table{width:100%;border-collapse:collapse;font-size:.85rem}
td{padding:.32rem 0;border-bottom:1px solid #1e1e27;vertical-align:top}
td:first-child{color:var(--dim);white-space:nowrap;padding-right:.9rem}
.tag{font-size:.68rem;padding:.1rem .4rem;border-radius:99px;background:#22222c;color:var(--dim)}
.errado{color:var(--warn)}
.certo{color:var(--ok)}
.vazio{color:var(--dim);font-size:.85rem}
#porta{min-height:72vh;display:flex;flex-direction:column;align-items:center;
       justify-content:center;text-align:center;gap:.2rem}
/* display:flex vence o atributo `hidden` — sem isto a porta nunca some. */
[hidden]{display:none!important}
#porta h1{font-size:.85rem}
.lede{font-size:clamp(1.5rem,4.5vw,2.3rem);font-weight:700;letter-spacing:-.02em;
      max-width:20ch;line-height:1.2;margin:.4rem 0 1rem}
.resumo{color:var(--dim);font-size:.95rem;margin:0 0 2rem}
#entrar{font:inherit;font-weight:600;font-size:1rem;color:#fff;background:var(--accent);
        border:0;border-radius:999px;padding:.85rem 2.2rem;cursor:pointer;
        transition:transform .15s ease,background .15s ease}
#entrar:hover{background:#8b5cf6;transform:translateY(-2px)}
#entrar:focus-visible{outline:2px solid var(--accent);outline-offset:4px}
.aviso{color:var(--dim);font-size:.8rem;max-width:44ch;margin:1.8rem 0 0;line-height:1.7}
.fio{padding:.9rem 0;border-bottom:1px solid #1e1e27}
.fio:last-child{border-bottom:0}
.fio h3{font-size:.95rem;margin:0 0 .5rem;font-weight:600}
.fio p{margin:.35rem 0;font-size:.86rem;color:#c4c4cf}
.dia{color:var(--dim)}
footer{margin-top:2rem;color:var(--dim);font-size:.78rem;line-height:1.7}
</style></head><body><div class="wrap">

<section id="porta">
  <h1>Kestlerium</h1>
  <p class="lede">Um lugar que continua acontecendo quando ninguém está olhando.</p>
  <p class="resumo" id="resumo"></p>
  <button id="entrar" type="button">Entrar no Kestlerium</button>
  <p class="aviso">O mundo anda no horário de Brasília. O que você vai ver é o instante em que ele está agora — não uma gravação, não uma simulação que começa quando você chega.</p>
</section>

<section id="mundo" hidden>
<header>
  <h1>Kestlerium</h1>
  <p class="quando" id="quando"></p>
  <p class="sub" id="sub"></p>
</header>
<div class="grid">
  <div>
    <div class="card"><h2>A vila agora</h2><div id="mapa"></div></div>
    <div class="card" style="margin-top:1.2rem"><h2>Onde cada um está</h2><div id="onde"></div></div>
  </div>
  <div>
    <div class="card"><h2>O que se acredita — e o que é verdade</h2><div id="cabecas"></div></div>
    <div class="card" style="margin-top:1.2rem"><h2>Quem ainda não entende o mundo</h2><div id="saber"></div></div>
    <div class="card" style="margin-top:1.2rem"><h2>Entre as pessoas</h2><div id="rel"></div></div>
  </div>
</div>
<div class="grid" style="margin-top:1.2rem;grid-template-columns:1fr">
  <div>
    <div class="card"><h2>Os fios de história</h2><div id="fios"></div></div>
  </div>
</div>
<footer id="rodape"></footer>
</section>
</div>
<script id="dados" type="application/json">__DADOS__</script>
<script>
const D = JSON.parse(document.getElementById('dados').textContent);
const nome = id => (D.agentes[id]||{}).nome || id;

// A porta: ninguém cai dentro do terrário, entra quem quer.
document.getElementById('resumo').textContent =
  D.quando + ' · ' + (D.noite ? 'noite' : 'dia') + ' · ' +
  Object.keys(D.agentes).length + ' moradores';
document.getElementById('entrar').addEventListener('click', () => {
  document.getElementById('porta').hidden = true;
  document.getElementById('mundo').hidden = false;
  window.scrollTo({top: 0});
});

document.getElementById('quando').textContent = D.quando;
document.getElementById('sub').textContent =
  (D.noite ? 'noite' : 'dia') + ' · horário de Brasília · ' +
  Object.keys(D.agentes).length + ' moradores';

// --- planta baixa ---
const porLocal = {};
D.estado.forEach(e => { if(e.location_id) (porLocal[e.location_id] ||= []).push(e); });
const loc = Object.fromEntries(D.locais.map(l => [l.id, l]));
let svg = '<svg viewBox="0 0 100 92" role="img" aria-label="Planta da vila">';
D.arestas.forEach(([a,b]) => {
  const A = loc[a], B = loc[b];
  if(A && B) svg += `<line class="via" x1="${A.x}" y1="${A.y}" x2="${B.x}" y2="${B.y}"/>`;
});
D.locais.forEach(l => {
  const gente = porLocal[l.id] || [];
  const r = 5 + Math.min(4, gente.length);
  svg += `<circle class="loc" cx="${l.x}" cy="${l.y}" r="${r}" stroke-width=".4"/>`;
  svg += `<text class="loc-lbl" x="${l.x}" y="${l.y + r + 3}">${l.nome}</text>`;
  gente.forEach((g, i) => {
    const ang = (i / Math.max(1,gente.length)) * Math.PI * 2 - Math.PI/2;
    const px = l.x + Math.cos(ang) * (r - 2.2), py = l.y + Math.sin(ang) * (r - 2.2);
    svg += `<circle class="pes" cx="${px}" cy="${py}" r="1.1"><title>${nome(g.agent_id)} — ${g.activity}</title></circle>`;
  });
});
svg += '</svg>';
document.getElementById('mapa').innerHTML = svg;

// --- onde cada um está ---
const emTransito = D.estado.filter(e => !e.location_id);
let linhas = D.estado.filter(e => e.location_id)
  .sort((a,b)=> nome(a.agent_id).localeCompare(nome(b.agent_id)))
  .map(e => `<tr><td>${nome(e.agent_id)}</td><td>${(loc[e.location_id]||{}).nome||e.location_id}
             <span class="tag">${e.activity}</span></td></tr>`).join('');
linhas += emTransito.map(e => `<tr><td>${nome(e.agent_id)}</td><td class="vazio">a caminho</td></tr>`).join('');
document.getElementById('onde').innerHTML = linhas ? `<table>${linhas}</table>`
  : '<p class="vazio">Ninguém registrado neste instante.</p>';

// --- crenças: o coração do que se quer ver ---
let cb = [];
Object.entries(D.cabecas).forEach(([quem, itens]) => {
  itens.filter(i => !i.fiel || i.confianca < 0.95).forEach(i => {
    cb.push(`<tr><td>${nome(quem)}</td><td>
      <em>${i.sujeito}</em> ${i.predicado}
      <strong class="${i.fiel?'certo':'errado'}">${i.acredita ?? '—'}</strong>
      ${i.fiel ? '' : `<span class="tag">na verdade: ${i.verdade ?? '—'}</span>`}
      <span class="tag">conf ${i.confianca}</span>
      ${i.fonte ? `<span class="tag">ouviu de ${nome(i.fonte)}</span>` : ''}
    </td></tr>`);
  });
});
document.getElementById('cabecas').innerHTML = cb.length ? `<table>${cb.slice(0,18).join('')}</table>`
  : '<p class="vazio">Todo mundo sabe o que aconteceu, e sabe direito. Ainda não há versão torta circulando.</p>';

// --- conhecimento ---
const total = 10;
let sb = Object.entries(D.conhecimento).map(([quem, cs]) => {
  const dominados = cs.filter(c => c.dominio >= 0.55).length;
  return {quem, dominados, faltam: cs.filter(c=>c.dominio<0.55).map(c=>c.conceito)};
}).filter(x => x.faltam.length).sort((a,b)=>a.dominados-b.dominados);
document.getElementById('saber').innerHTML = sb.length
  ? `<table>${sb.slice(0,10).map(x=>`<tr><td>${nome(x.quem)}</td><td>
       ainda não sabe: ${x.faltam.slice(0,4).join(', ')}</td></tr>`).join('')}</table>`
  : '<p class="vazio">Todos aqui sabem como o mundo funciona. É a vila da base: eles moram aqui desde o começo.</p>';

// --- relações ---
const rel = D.relacoes.slice().sort((a,b)=> b.tensao - a.tensao).slice(0,10);
document.getElementById('rel').innerHTML = rel.length
  ? `<table>${rel.map(r=>`<tr><td>${nome(r.a)} · ${nome(r.b)}</td><td>
      <span class="tag">afeto ${r.afeto}</span>
      <span class="tag">confiança ${r.confianca}</span>
      <span class="tag">tensão ${r.tensao}</span></td></tr>`).join('')}</table>`
  : '<p class="vazio">Nada marcante entre as pessoas ainda.</p>';

// --- fios (Fase 8): o que um instante não mostra ---
const fios = D.fios || [];
document.getElementById('fios').innerHTML = fios.length
  ? fios.map(f => `<div class="fio">
      <h3>${f.titulo} <span class="tag">${f.estado}</span></h3>
      ${f.entradas.map(e=>`<p><span class="dia">Dia ${e.day}.</span> ${e.text}</p>`).join('')}
    </div>`).join('')
  : '<p class="vazio">Ainda não há fio de história aqui. Um fio nasce de um fato que volta a importar — e a vila da base não guarda segredo nenhum.</p>';

document.getElementById('rodape').textContent =
  'O Kestlerium anda no horário de Brasília e não para quando ninguém está olhando. ' +
  'Esta página é um registro do instante — o mundo já seguiu.';
</script></body></html>
"""


def render(snap: dict) -> str:
    return PAGE.replace("__DADOS__", json.dumps(snap, ensure_ascii=False))
