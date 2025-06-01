from collections.abc import Callable

from .point import Point


class Circle:
    def __init__(self, radius: int) -> None:
        self.r = radius

    def draw(self, func: Callable[[Point], None]) -> None:
        point = Point(self.r, 0)

        while point.y < point.x:
            for p in mirrorPoints(point):
                func(p)

            p1 = Point(point.x, point.y+1)
            p2 = Point(point.x-1, point.y+1)
            if circleDistance(p1, self.r) < circleDistance(p2, self.r):
                point = p1
            else:
                point = p2

def circleDistance(p: Point, r: int) -> int:
    return abs(p.x**2+p.y**2-r**2)

def mirrorPoints(p: Point) -> dict:
    return [
        Point(p.x, p.y),
        Point(-p.x, p.y),
        Point(p.x, -p.y),
        Point(-p.x, -p.y),
        Point(p.y, p.x),
        Point(-p.y, p.x),
        Point(p.y, -p.x),
        Point(-p.y, -p.x),
    ]

