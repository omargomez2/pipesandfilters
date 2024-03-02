#---------------------------------
# Author: Omar S. Gómez
# Date: February 2024
# Description: Software filter that add a watermark text over an image
#---------------------------------
from PIL import Image, ImageDraw, ImageFont

def watermark(img, texto, tamanio_fuente):
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", tamanio_fuente)
    draw.text((5, 5), texto, fill=(255, 255, 255), font=font)
    return img


