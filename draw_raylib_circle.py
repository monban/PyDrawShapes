from render.bitmap import Bitmap
from render.raylib import blit
from shape.circle import Circle
import pyray

# Use raylib to display the shapes
# this uses the slow draw_pixel function and also recalculates the shapes
# every frame. it would be much faster / better to write once to a texture
# and then just draw the texture in the raylib loop, but I haven't figured
# out how to initialize a raylib struct Image in Python yet.
# stilk, it gives a good example of the flexibility of the shapes to use
# any arbitrary display mechanism that can call the "draw" method
c = Circle(400)

pyray.init_window(800, 450, "Hello")
while not pyray.window_should_close():
    pyray.begin_drawing()
    pyray.clear_background(pyray.WHITE)
    c.draw(lambda p: pyray.draw_pixel(p.x, p.y, pyray.BLACK))
    pyray.draw_text("Hello world", 190, 200, 20, pyray.VIOLET)
    pyray.end_drawing()
pyray.close_window()


