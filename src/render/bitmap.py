from shape.point import Point

class Bitmap:
    def __init__(self, width: int, height: int, xOffset: int, yOffset: int):
        pixels = width*height
        assert pixels % 8 == 0, "um, please use a resoltion that is an integer multiple of 8"
        self.bitmap = bytearray(int(pixels/8))
        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset

    def set(self, point: Point):
        x = point.x + self.xOffset
        y = point.y + self.yOffset
        if x<0 or y<0 or x>self.width or y>self.height:
            return
        bit = (self.height-1-y)*self.width+x
        byte = int(bit/8)
        bit %= 8
        self.bitmap[byte] |= 0x80>>bit
