from PIL import Image, ImageDraw
 
def make(size, path, maskable=False):
    img = Image.new("RGB", (size, size), "#1f3a5f")
    d = ImageDraw.Draw(img)
    pad = size * (0.22 if maskable else 0.14)
    w = size - 2 * pad
    h = w * 0.72
    x0, y0 = pad, (size - h) / 2
    # libro abierto: dos páginas
    d.rounded_rectangle([x0, y0, x0 + w / 2 - size * 0.01, y0 + h], radius=size * 0.03, fill="#f6f3ec")
    d.rounded_rectangle([x0 + w / 2 + size * 0.01, y0, x0 + w, y0 + h], radius=size * 0.03, fill="#f6f3ec")
    # renglones de texto
    for i in range(4):
        yy = y0 + h * (0.22 + i * 0.17)
        d.line([x0 + w * 0.07, yy, x0 + w * 0.43, yy], fill="#1f3a5f", width=max(2, int(size * 0.012)))
        d.line([x0 + w * 0.57, yy, x0 + w * 0.93, yy], fill="#1f3a5f", width=max(2, int(size * 0.012)))
    # cruz dorada sobre el libro
    cx, cy = size / 2, y0 - size * 0.02
    d.rectangle([cx - size * 0.012, cy - size * 0.09, cx + size * 0.012, cy + size * 0.02], fill="#f2c14e")
    d.rectangle([cx - size * 0.045, cy - size * 0.06, cx + size * 0.045, cy - size * 0.036], fill="#f2c14e")
    img.save(path)
 
make(192, "icons/icon-192.png")
make(512, "icons/icon-512.png")
make(512, "icons/icon-maskable-512.png", maskable=True)
print("Íconos creados en icons/")