import os
from PIL import Image

def show_logo(name, output_width=100):
    base_path = os.path.dirname(__file__)

    if name == "Arasaka":
        image_path = os.path.join(base_path, "Arasaka.png")
    elif name == "Militech":
        image_path = os.path.join(base_path, "Militech.png")
    elif name == "Kiroshi":
        image_path = os.path.join(base_path, "Kiroshi.png")
    elif name == "Biotech":
        image_path = os.path.join(base_path, "Biotech.png")
    elif name == "Zetatech":
        image_path = os.path.join(base_path, "Zetatech.png")
    else:
        raise ValueError("Logo desconhecido.")

    img = Image.open(image_path).convert("RGBA")
    background = Image.new("RGB", img.size, (255, 255, 255))
    background.paste(img, mask=img.split()[3])  # Usa o canal alfa como máscara
    img = background

    aspect_ratio = img.height / img.width
    output_height = int(aspect_ratio * output_width * 0.5)
    img = img.resize((output_width, output_height))

    ascii_chars = "@%#*+=-:. "
    ascii_image = ""

    for y in range(output_height):
        for x in range(output_width):
            r, g, b = img.getpixel((x, y))
            intensity = (r + g + b) / 3
            ascii_char = ascii_chars[int(intensity / 255 * (len(ascii_chars) - 1))]
            ascii_image += f"\033[38;2;{r};{g};{b}m{ascii_char}\033[0m"
        ascii_image += "\n"

    print(ascii_image)
