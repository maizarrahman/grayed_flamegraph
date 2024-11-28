import random

def parse(svg):
    color = ('207','195','199','203','191','179','183','187')
    p2 = 1
    while p2 < len(svg)-50:
        p1 = svg.find('<g>', p2) + 3
        p2 = svg.find('</g>', p1)
    
        pt1 = svg.find('<title>', p1) + 7
        pt2 = svg.find('</title>', pt1)
        title = svg[pt1:pt2]
        if pt2 > p2:
            print('title "%s" may be wrong. parse failed.'%title)
            break
    
        pr1 = svg.find('"rgb(', pt2) + 5
        pr2 = svg.find(')"', pr1)
        rgb = svg[pr1:pr2]
        if pr2 > p2:
            print('rgb "%s" may be wrong. parse failed.'%rgb)
            break        
    
        if 'dym' in title:
            rgb = '250,127,0'    
        else:
            r = random.choice(color)
            rgb = '%s,%s,%s'%(r,r,r)
        svg = svg[:pr1] + rgb + svg[pr2:]

    return svg


with open("Documents/Odoo/dess/flamegraph/flamegraph_20241118_0045.svg", 'r') as f:
    s = f.read()

with open("flamegraph_20241118_0045.svg", 'w') as f:
    f.write(parse(s))
