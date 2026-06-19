#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# generate_qr.py
#
# Generates a QR code from a user-supplied URL and saves it as a PNG image.
# Prompts for the URL and output filename, then renders the URL and filename
# as captions below the QR code.
#
# The actual rendering lives in src/qr_gui/qr_core.py, shared with the PyQt6
# GUI front-end (qr_code_gui.py).
#
# Version : 0.2.0
# Created : 2026-06-19 03:47:36 CDT
# -----------------------------------------------------------------------------

import os
import sys

# Make the src/ directory importable so the shared qr_core helper can be found.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from qr_gui.qr_core import normalize_filename, render_qr


def main():
    # Prompt the user for the URL to encode
    url = input("Enter the URL to encode: ").strip()

    # Prompt the user for the output filename
    filename = normalize_filename(input("Enter the output filename [qrcode_example.png]: "))

    # Render the QR code with the URL and filename captioned below it
    canvas = render_qr(url, caption_lines=[url, filename])

    canvas.save(filename)
    print(f"Saved QR code to {filename}")


if __name__ == "__main__":
    main()
