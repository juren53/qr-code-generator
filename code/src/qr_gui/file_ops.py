#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# file_ops.py
#
# FileOpsMixin: QR generation, saving to PNG, and clipboard operations.
# -----------------------------------------------------------------------------

import os

from PyQt6.QtGui import QGuiApplication, QImage, QPixmap
from PyQt6.QtWidgets import QFileDialog, QMessageBox

from .qr_core import normalize_filename, render_qr


def pil_to_qimage(pil_img) -> QImage:
    """Convert a PIL image to a QImage (deep-copied to own its buffer)."""
    img = pil_img.convert("RGB")
    data = img.tobytes("raw", "RGB")
    qimg = QImage(data, img.width, img.height, img.width * 3, QImage.Format.Format_RGB888)
    return qimg.copy()


class FileOpsMixin:
    def on_generate(self):
        text = self.url_edit.text().strip()
        if not text:
            self.set_status("Enter a URL or text to encode first.")
            self.url_edit.setFocus()
            return

        caption_lines = [text] if self.caption_check.isChecked() else None
        try:
            self.current_image = render_qr(text, caption_lines)
        except Exception as exc:  # pragma: no cover - defensive
            QMessageBox.critical(self, "QR Generation Failed", str(exc))
            self.set_status("QR generation failed.")
            return

        self.base_pixmap = QPixmap.fromImage(pil_to_qimage(self.current_image))
        self.zoom_factor = 1.0
        self.fit_mode = True
        self.refresh_preview()
        self.update_action_states()
        self.set_status(
            f"Generated QR code ({self.current_image.width}×{self.current_image.height} px)."
        )

    def on_save_as(self):
        if self.current_image is None:
            self.set_status("Nothing to save — generate a QR code first.")
            return

        suggested = normalize_filename(self.url_edit.text().strip() or "qrcode")
        # Strip characters that are awkward in filenames from a URL-derived name.
        suggested = suggested.replace("/", "_").replace(":", "_").replace("?", "_")
        start_path = os.path.join(os.path.expanduser("~"), suggested)

        path, _ = QFileDialog.getSaveFileName(
            self, "Save QR Code", start_path, "PNG Image (*.png);;All Files (*)"
        )
        if not path:
            return
        path = normalize_filename(path)

        try:
            self.current_image.save(path)
        except Exception as exc:
            QMessageBox.critical(self, "Save Failed", str(exc))
            self.set_status("Save failed.")
            return

        self.last_saved_path = path
        self.set_status(f"Saved QR code to {path}")

    def on_paste_url(self):
        text = QGuiApplication.clipboard().text().strip()
        if text:
            self.url_edit.setText(text)
            self.set_status("Pasted text from clipboard.")
        else:
            self.set_status("Clipboard is empty.")

    def on_copy_image(self):
        if self.current_image is None:
            self.set_status("Nothing to copy — generate a QR code first.")
            return
        QGuiApplication.clipboard().setImage(pil_to_qimage(self.current_image))
        self.set_status("Copied QR code image to the clipboard.")

    def on_clear(self):
        self.url_edit.clear()
        self.current_image = None
        self.base_pixmap = None
        self.last_saved_path = None
        self.refresh_preview()
        self.update_action_states()
        self.url_edit.setFocus()
        self.set_status("Cleared.")
