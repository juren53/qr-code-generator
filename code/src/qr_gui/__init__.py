#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# qr_gui package
#
# PyQt6 GUI front-end for the QR Code Generator. The QMainWindow is composed
# from focused mixins (menu, file ops, view, printing, help) following the
# pattern used by Tag Writer, Audio Tag Writer, and the HSTL Photo Framework.
# -----------------------------------------------------------------------------

from .constants import APP_NAME, APP_VERSION, APP_TIMESTAMP

__all__ = ["APP_NAME", "APP_VERSION", "APP_TIMESTAMP"]
