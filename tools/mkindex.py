import json,os,sys,html
root=sys.argv[1]
base='https://zeir1x.github.io/rycerz-overlays/'
members=[]
for d in sorted(os.listdir(root)):
    f=os.path.join(root,d,'piezas.json')
    if os.path.isfile(f): members.append((d,json.load(open(f))))
GROUPS={'oficial':'Overlay oficial','juego':'Para jugar en directo','pantalla':'Pantallas de escena'}
cards=[]
for slug,m in members:
    rows=[]
    for g,gl in GROUPS.items():
        ps=[p for p in m['pieces'] if p['group']==g]
        if not ps: continue
        rows.append(f'<h3>{gl}</h3><ul>')
        for p in ps:
            url=f"{base}{slug}/{p['id']}.html"
            rows.append(f'<li><div><strong>{html.escape(p["label"])}</strong><small>{p["w"]} × {p["h"]}</small></div><code>{url}</code><span class="b"><button data-u="{url}">Copiar link</button><a href="{slug}/{p["id"]}.html" target="_blank" rel="noopener">Abrir</a></span></li>')
        rows.append('</ul>')
    cards.append(f'<section><header><h2>{html.escape(m["name"])}</h2><span>{html.escape(m["role"])}</span></header>{"".join(rows)}</section>')
page=f'''<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>RYCERZ Overlays</title><meta name="robots" content="noindex">
<style>:root{{--v:#7b2ff2;--l:#a879ff;--bg:#06070f;--card:#0d0f1f;--t:#f3f2f8;--m:#9aa0b8}}*{{box-sizing:border-box}}body{{margin:0;background:radial-gradient(900px 500px at 10% -10%,#7b2ff233,transparent),var(--bg);color:var(--t);font:15px/1.5 system-ui,Segoe UI,Arial,sans-serif}}main{{max-width:1000px;margin:0 auto;padding:40px 16px 80px}}h1{{font-size:34px;letter-spacing:.04em;margin:0}}h1 b{{color:var(--l)}}.lead{{color:var(--m);margin:6px 0 28px}}section{{background:var(--card);border:1px solid #ffffff14;border-radius:18px;padding:22px;margin-bottom:22px}}header{{display:flex;align-items:baseline;gap:12px}}h2{{margin:0;font-size:24px;text-transform:uppercase;letter-spacing:.05em}}header span{{color:var(--l);font-size:13px;text-transform:uppercase;letter-spacing:.2em}}h3{{font-size:12px;letter-spacing:.24em;text-transform:uppercase;color:var(--m);margin:22px 0 8px}}ul{{list-style:none;margin:0;padding:0}}li{{display:grid;grid-template-columns:minmax(180px,1fr) minmax(0,2fr) auto;gap:12px;align-items:center;padding:10px 0;border-top:1px solid #ffffff0d}}li small{{display:block;color:var(--m);font-size:12px}}code{{font-size:12px;color:#cbbfff;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}}.b{{display:flex;gap:8px}}button,a{{font:600 13px system-ui;padding:8px 12px;border-radius:10px;border:1px solid #ffffff1f;background:#ffffff0a;color:var(--t);text-decoration:none;cursor:pointer;white-space:nowrap}}button{{background:var(--v);border-color:var(--v)}}button.ok{{background:#1f9d55;border-color:#1f9d55}}.tip{{color:var(--m);font-size:13px;margin-top:-10px;margin-bottom:24px}}@media(max-width:700px){{li{{grid-template-columns:1fr}}}}</style></head>
<body><main><h1>RYCERZ <b>OVERLAYS</b></h1><p class="lead">Links de los overlays de cada integrante para TikTok LIVE Studio, OBS o Streamlabs.</p>
<p class="tip">En TikTok LIVE Studio: Agregar fuente → Enlace / Link, pega el link y pon el tamaño que dice cada overlay. En OBS: fuente de Navegador → URL.</p>
{"".join(cards)}</main>
<script>document.querySelectorAll('button[data-u]').forEach(b=>b.addEventListener('click',async()=>{{try{{await navigator.clipboard.writeText(b.dataset.u);}}catch(e){{const t=document.createElement('textarea');t.value=b.dataset.u;document.body.append(t);t.select();document.execCommand('copy');t.remove();}}b.textContent='¡Copiado!';b.classList.add('ok');setTimeout(()=>{{b.textContent='Copiar link';b.classList.remove('ok')}},1600);}}));</script></body></html>'''
open(os.path.join(root,'index.html'),'w').write(page)
open(os.path.join(root,'.nojekyll'),'w').write('')
print(len(members))
