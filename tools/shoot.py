import sys
from playwright.sync_api import sync_playwright
import os
OUT=os.environ.get('SHOTS','screenshots/')
os.makedirs(OUT,exist_ok=True)
pages=sys.argv[1].split(',')
mode=sys.argv[2] if len(sys.argv)>2 else 'desk'
with sync_playwright() as p:
    b=p.chromium.launch()
    vp={'width':1440,'height':900} if mode in ('desk','dark') else {'width':390,'height':844}
    ctx=b.new_context(viewport=vp,device_scale_factor=1, color_scheme=('dark' if mode=='dark' else 'light'))
    errs=[]
    for pth in pages:
        pg=ctx.new_page(); pg.on('pageerror',lambda e:errs.append(str(e))); pg.on('console',lambda m: errs.append(m.text) if m.type=='error' else None)
        pg.goto('http://localhost:8765/'+pth); pg.wait_for_timeout(2200)
        name=pth.replace('/','_').replace('.html','')+'_'+mode
        pg.screenshot(path=OUT+name+'.png',full_page=True)
        sw=pg.evaluate('document.documentElement.scrollWidth'); h=pg.evaluate('document.body.scrollHeight')
        print(pth,mode,'scrollW',sw,'H',h)
        pg.close()
    print('errors',errs[:10])
    b.close()
