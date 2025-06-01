from .bitmap import Bitmap


def blit(bitmap: Bitmap) -> None:
    line = 0
    x = 0
    for byte in bitmap.bitmap:
        if x % (bitmap.width / 8) == 0:
            x = 0
            print()
            print(f"{line:02d}: ", end="")
            line += 1
        for bit in range(8):
            if byte & (0x80 >> bit):
                print("##", end="")
            else:
                print("..", end="")
        x += 1
    print()
