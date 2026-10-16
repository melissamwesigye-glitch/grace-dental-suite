"""Rebuilds the Grace Dental Suite logo as a clean SVG: Antic Didone wordmark (outlined) + traced brushstroke heart."""
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.boundsPen import BoundsPen
import sys
FONT='site/assets/fonts/antic-didone-400.woff2'
f=TTFont(FONT); gs=f.getGlyphSet(); cmap=f.getBestCmap(); upm=f['head'].unitsPerEm
cap=f['OS/2'].sCapHeight or 700
# target lines in source-logo coordinates (from measurement): (text, top, height, left, width)
LINES=[('GRACE',101,41,88,146),('DENTAL',156,39,68,172),('SUITE',209,41,99,123)]
def line_path(text, top, h, left, width, ink='#1F161A'):
    # build glyph run in font units
    x=0; parts=[]
    for ch in text:
        gn=cmap[ord(ch)]; parts.append((gn,x)); x+=gs[gn].width
    # measure ink bounds
    bp=BoundsPen(gs)
    for gn,ox in parts:
        tp=TransformPen(bp,(1,0,0,1,ox,0)); gs[gn].draw(tp)
    xmin,ymin,xmax,ymax=bp.bounds
    sy=h/(ymax-ymin); sx=width/(xmax-xmin)
    sp=SVGPathPen(gs)
    for gn,ox in parts:
        # font y-up -> svg y-down
        tp=TransformPen(sp,(sx,0,0,-sy,left+(ox-xmin)*sx, top+ymax*sy)); gs[gn].draw(tp)
    return sp.getCommands(), sx/sy
heart_w,heart_h,heart_d=None,None,None
hw,hh=open('tools/heart_path.txt').readline().split()
heart_d=open('tools/heart_path.txt').read().split('\n',1)[1]
S=6.0
HX,HY=199.17,90.0
def svg(text_fill, heart_fill, name):
    out=[]
    for t,top,h,left,w in LINES:
        d,ratio=line_path(t,top,h,left,w); out.append(d)
    vb=(62,84,326,172)
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb[0]} {vb[1]} {vb[2]} {vb[3]}" role="img" aria-label="Grace Dental Suite">'
    s+=f'<path fill="{heart_fill}" transform="translate({HX} {HY}) scale({1/S})" d="{heart_d}"/>'
    s+=f'<path fill="{text_fill}" d="{"".join(out)}"/></svg>'
    open(name,'w').write(s); print(name,len(s), 'x/y ratio', round(ratio,3))
if __name__=='__main__':
    out=sys.argv[1]
    svg('#1F161A','#F2B6CF',out+'/logo.svg')
    svg('#FAF0F3','#E79BBA',out+'/logo-on-dark.svg')
    # heart only (favicon / decorative)
    s=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {float(hw)/S:.1f} {float(hh)/S:.1f}"><path fill="#C9607F" fill-rule="evenodd" transform="scale({1/S})" d="{heart_d}"/></svg>'
    open(out+'/heart.svg','w').write(s)
