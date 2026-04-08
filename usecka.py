from PIL import Image

obrazok = Image.new("RGB", (100, 100), "white")
pixels = obrazok.load()

a1 = int(input("Zadaj suradnicu prvého bodu (x): "))
a2 = int(input("Zadaj suradnicu prveho bodu (y): "))
b1 = int(input("Zadaj suradnicu druhého bodu (x): "))
b2 = int(input("Zadaj suradnicu druhého bodu (y): "))

x = 0
y = 0

if a1 == b1:
    for i in range(min(a2, b2), max(a2, b2) + 1):
        pixels[a1, i] = (0, 0, 0)
else:
    if a1 != b1:
        a = (a2 - b2) / (a1 - b1) 
        b = a2 - a1 * ((a2 - b2) / (a1 - b1))
   
if abs(a1 - b1) >= abs(a2 - b2):
    for i in range(a1, b1):
        y = int(a * i + b)
        pixels[i, y] = (0, 0, 0)
        for i in range(a2, b2):
            x = int(round((i - b) / a))
            if 0 <= x < obrazok.width and 0 <= i < obrazok.height:
                pixels[x, i] = (0, 0, 0)

obrazok.show()
