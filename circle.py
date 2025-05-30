from bitmap import Bitmap
from point import Point

b = Bitmap(40, 40, 20, 20)

r = 16
point = Point(r, 0)

def CircleDistance(p: Point, r: int):
    return abs(p.x**2+p.y**2-r**2)

while point.y < point.x:
    b.set(point)
    b.set(Point(-point.x, point.y))
    b.set(Point(point.x, -point.y))
    b.set(Point(-point.x, -point.y))
    b.set(Point(point.y, point.x))
    b.set(Point(-point.y, point.x))
    b.set(Point(point.y, -point.x))
    b.set(Point(-point.y, -point.x))

    p1 = Point(point.x, point.y+1)
    p2 = Point(point.x-1, point.y+1)
    if CircleDistance(p1, r) < CircleDistance(p2, r):
        point = p1
    else:
        point = p2

b.blit()
