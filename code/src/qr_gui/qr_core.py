#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# qr_core.py
#
# Qt-free QR rendering helper shared by the CLI (generate_qr.py) and the
# PyQt6 GUI (qr_code_gui.py). Produces a PIL RGB image of a QR code with an
# optional set of caption lines drawn below it.
#
# Keeping this module free of any PyQt6 import means the command-line tool
# can render QR codes without a GUI toolkit installed.
# -----------------------------------------------------------------------------

from __future__ import annotations

import qrcode
from PIL import Image, ImageDraw, ImageFont


def normalize_filename(filename: str, default: str = "qrcode_example.png") -> str:
    """Return a sensible .png filename, applying the default when blank."""
    filename = (filename or "").strip()
    if not filename:
        filename = default
    if not filename.lower().endswith(".png"):
        filename += ".png"
    return filename


def _load_caption_font(size: int = 20) -> ImageFont.ImageFont:
    """Load DejaVuSans at the requested size, falling back to the PIL default."""
    try:
        return ImageFont.truetype("DejaVuSans.ttf", size)
    except OSError:
        return ImageFont.load_default()


def render_qr(
    data: str,
    caption_lines: list[str] | None = None,
    *,
    box_size: int = 10,
    border: int = 4,
    fill_color: str = "black",
    back_color: str = "white",
    font_size: int = 20,
    secondary_font_size: int = 14,
) -> Image.Image:
    """Render *data* as a QR code and return a PIL RGB image.

    If *caption_lines* is provided, each line is drawn centered on a white
    strip below the QR code. The first line uses *font_size*; subsequent lines
    use *secondary_font_size* so a short label can sit above a long URL.
    """
    qr = qrcode.QRCode(version=1, box_size=box_size, border=border)
    qr.add_data(data)
    qr.make(fit=True)

    qr_img = qr.make_image(fill_color=fill_color, back_color=back_color).convert("RGB")

    caption_lines = [line for line in (caption_lines or []) if line]
    if not caption_lines:
        return qr_img

    fonts = [
        _load_caption_font(font_size if i == 0 else secondary_font_size)
        for i in range(len(caption_lines))
    ]

    measure = ImageDraw.Draw(qr_img)
    line_metrics = []
    for line, font in zip(caption_lines, fonts):
        bbox = measure.textbbox((0, 0), line, font=font)
        line_metrics.append((bbox[2] - bbox[0], bbox[3] - bbox[1]))

    margin = 15
    line_spacing = 8
    total_text_height = (
        sum(h for _, h in line_metrics) + line_spacing * (len(caption_lines) - 1)
    )

    canvas = Image.new(
        "RGB",
        (qr_img.width, qr_img.height + total_text_height + 2 * margin),
        back_color,
    )
    canvas.paste(qr_img, (0, 0))

    draw = ImageDraw.Draw(canvas)
    text_y = qr_img.height + margin
    for line, (text_width, text_height), font in zip(caption_lines, line_metrics, fonts):
        text_x = (canvas.width - text_width) // 2
        draw.text((text_x, text_y), line, fill=fill_color, font=font)
        text_y += text_height + line_spacing

    return canvas
