import bitmap

b = bitmap.Bitmap(40, 40, 20, 20)

r = 16
y = 0
x = r


while y<x:
    b.set(x,y)
    b.set(y,x)
    b.set(-x,y)
    b.set(-y,x)
    b.set(x,-y)
    b.set(y,-x)
    b.set(-x,-y)
    b.set(-y,-x)
    x1 = x
    y1 = y+1
    x2 = x-1
    y2 = y+1
    d1 = abs((x1)**2+(y1)**2-r**2)
    d2 = abs((x2)**2+(y2)**2-r**2)
    if d1 < d2:
        x=x1
        y=y1
    else:
        x=x2
        y=y2

b.blit()
