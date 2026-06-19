#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# printing.py
#
# PrintMixin: send the rendered QR code to a system printer via the standard
# Qt print services, with both a direct Print dialog and a Print Preview.
# -----------------------------------------------------------------------------

from PyQt6.QtCore import QRect, Qt
from PyQt6.QtGui import QPainter
from PyQt6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class PrintMixin:
    def _render_to_printer(self, printer):
        """Paint the QR pixmap centered on the page, preserving aspect ratio."""
        if self.base_pixmap is None or self.base_pixmap.isNull():
            return
        painter = QPainter(printer)
        try:
            page = painter.viewport()
            scaled = self.base_pixmap.size()
            scaled.scale(page.size(), Qt.AspectRatioMode.KeepAspectRatio)
            x = page.x() + (page.width() - scaled.width()) // 2
            y = page.y() + (page.height() - scaled.height()) // 2
            target = QRect(x, y, scaled.width(), scaled.height())
            painter.drawPixmap(target, self.base_pixmap)
        finally:
            painter.end()

    def on_print(self):
        if self.base_pixmap is None or self.base_pixmap.isNull():
            self.set_status("Nothing to print — generate a QR code first.")
            return
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintDialog(printer, self)
        dialog.setWindowTitle("Print QR Code")
        if dialog.exec() == QPrintDialog.DialogCode.Accepted:
            self._render_to_printer(printer)
            self.set_status("Sent QR code to printer.")
        else:
            self.set_status("Print canceled.")

    def on_print_preview(self):
        if self.base_pixmap is None or self.base_pixmap.isNull():
            self.set_status("Nothing to preview — generate a QR code first.")
            return
        printer = QPrinter(QPrinter.PrinterMode.HighResolution)
        dialog = QPrintPreviewDialog(printer, self)
        dialog.setWindowTitle("Print Preview")
        dialog.paintRequested.connect(self._render_to_printer)
        dialog.exec()
