from PIL import Image, ImageDraw
obrazok = Image.new("RGB", (401, 401), "white")
pixels = obrazok.load()

#ohranicenie
ImageDraw.Draw(obrazok).rectangle([(0, 0), (400, 400)], outline="black")
ImageDraw.Draw(obrazok).line([(200, 200), (400, 200)], fill="black")
ImageDraw.Draw(obrazok).line([(200, 200), (200, 400)], fill="black")

#Mriezka
for x in range(0, 201, 20):
    for y in range(0, 201, 20):
        ImageDraw.Draw(obrazok).line([(x, 20), (x, y)], fill="black")
        ImageDraw.Draw(obrazok).line([(20, y), (x, y)], fill="black")

#schody
for i in range (0, 201, 20):
    ImageDraw.Draw(obrazok).line([(i, 200+i), (i, 220+i)], fill="black")
    ImageDraw.Draw(obrazok).line([(i, i + 220), (i + 20, i + 220)], fill="black")

#kriz
ImageDraw.Draw(obrazok).line([(201, 201), (400, 400)], fill="black")
ImageDraw.Draw(obrazok).line([(400, 201), (201, 400)], fill="black")

#sikme ciary
for i in range(200, 401, 20):
    ImageDraw.Draw(obrazok).line([(i, 0), (200, i-200)], fill="black")

obrazok.show()