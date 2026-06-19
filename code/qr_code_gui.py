#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# qr_code_gui.py
#
# PyQt6 GUI front-end for the QR Code Generator.
#
# Thin launcher that defers to the modular implementation in src/qr_gui/.
# Enter a URL or any text, preview the rendered PNG on screen, save it as a
# PNG, copy it to the clipboard, or print it via the system print services.
#
# Version : 0.2.0
# Created : 2026-06-19 04:23 CDT
# -----------------------------------------------------------------------------

import os
import sys

# Make the src/ directory importable so the qr_gui package can be found.
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "src"))

from qr_gui.main import main

if __name__ == "__main__":
    sys.exit(main())
