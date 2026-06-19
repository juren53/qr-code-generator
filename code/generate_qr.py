#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# generate_qr.py
#
# Generates a QR code from a user-supplied URL and saves it as a PNG image.
# Prompts for the URL and output filename, then renders the URL and filename
# as captions below the QR code.
#
# Version : 0.1.0
# Created : 2026-06-19 03:47:36 CDT
# -----------------------------------------------------------------------------

import qrcode
from PIL import Image, ImageDraw, ImageFont

# Prompt the user for the URL to encode
url = input("Enter the URL to encode: ").strip()

# Prompt the user for the output filename
filename = input("Enter the output filename [qrcode_example.png]: ").strip()
if not filename:
    filename = "qrcode_example.png"
if not filename.lower().endswith(".png"):
    filename += ".png"

# Create the QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data(url)
qr.make(fit=True)

# Create the QR code image
qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

# Build a taller canvas with room for the URL and filename captions below the QR code
caption_lines = [url, filename]
try:
    font = ImageFont.truetype("DejaVuSans.ttf", 20)
except OSError:
    font = ImageFont.load_default()

measure = ImageDraw.Draw(qr_img)
line_metrics = []
for line in caption_lines:
    bbox = measure.textbbox((0, 0), line, font=font)
    line_metrics.append((bbox[2] - bbox[0], bbox[3] - bbox[1]))

margin = 15
line_spacing = 8
total_text_height = sum(h for _, h in line_metrics) + line_spacing * (len(caption_lines) - 1)

canvas = Image.new(
    "RGB",
    (qr_img.width, qr_img.height + total_text_height + 2 * margin),
    "white",
)
canvas.paste(qr_img, (0, 0))

# Draw each caption line centered below the QR code
draw = ImageDraw.Draw(canvas)
text_y = qr_img.height + margin
for line, (text_width, text_height) in zip(caption_lines, line_metrics):
    text_x = (canvas.width - text_width) // 2
    draw.text((text_x, text_y), line, fill="black", font=font)
    text_y += text_height + line_spacing

canvas.save(filename)
print(f"Saved QR code to {filename}")



