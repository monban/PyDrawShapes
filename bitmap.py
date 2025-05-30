class Bitmap:
    def __init__(self, width, height, xOffset, yOffset):
        pixels = width*height
        assert pixels % 8 == 0, "um, please use a resoltion that is an integer multiple of 8"
        self.bitmap = bytearray(int(pixels/8))
        self.width = width
        self.height = height
        self.xOffset = xOffset
        self.yOffset = yOffset

    def blit(self):
        line = 0
        x = 0
        for byte in self.bitmap:
            if x % (self.width/8) == 0:
                x=0
                print()
                print(f'{line:02d}: ', end='')
                line += 1
            for bit in range(8):
                pass
                if (byte & (0x80>>bit)):
                    print('##', end='')
                else:
                    print('..', end='')
            x += 1
        print()

    def set(self, x, y):
        x += self.xOffset
        y += self.yOffset
        if x<0 or y<0 or x>self.width or y>self.height:
            return
        bit = (self.height-1-y)*self.width+x
        byte = int(bit/8)
        bit %= 8
        self.bitmap[byte] |= 0x80>>bit
