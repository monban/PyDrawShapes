from shape.circle import Circle
from render.bitmap import Bitmap
from render.text import blit

b = Bitmap(40, 40, 19, 19)
c = Circle(18)

c.draw(b.set)
blit(b)

