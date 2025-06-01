from circle.bitmap import Bitmap
from circle.circle import Circle
from circle.renderer_text import blit

b = Bitmap(40, 40, 19, 19)
c = Circle(18)

c.draw(b.set)
blit(b)

