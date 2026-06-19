#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# help.py
#
# HelpMixin: README / Changelog viewers, issue tracker link, and an About
# dialog. The About dialog uses pyqt-app-info when available (matching the
# sibling apps) and falls back to a plain QMessageBox otherwise.
# -----------------------------------------------------------------------------

from pathlib import Path

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QDesktopServices
from PyQt6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QMessageBox,
    QTextEdit,
    QVBoxLayout,
)

from .constants import (
    APP_DESCRIPTION,
    APP_NAME,
    APP_SHORT_NAME,
    APP_TIMESTAMP,
    APP_VERSION,
    ISSUE_TRACKER_URL,
)


def _find_doc(filename: str):
    """Locate a doc file (README.md / CHANGELOG.md) near the project root."""
    here = Path(__file__).resolve()
    for base in here.parents:
        candidate = base / filename
        if candidate.is_file():
            return candidate
    return None


class HelpMixin:
    def _show_text_file(self, title: str, filename: str):
        path = _find_doc(filename)
        if path is None:
            QMessageBox.information(self, title, f"{filename} was not found.")
            return
        try:
            text = path.read_text(encoding="utf-8")
        except OSError as exc:
            QMessageBox.warning(self, title, f"Could not read {filename}:\n{exc}")
            return

        dialog = QDialog(self)
        dialog.setWindowTitle(title)
        dialog.resize(720, 560)
        layout = QVBoxLayout(dialog)
        viewer = QTextEdit()
        viewer.setReadOnly(True)
        if filename.lower().endswith(".md"):
            viewer.setMarkdown(text)
        else:
            viewer.setPlainText(text)
        layout.addWidget(viewer)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Close)
        buttons.rejected.connect(dialog.reject)
        buttons.accepted.connect(dialog.accept)
        layout.addWidget(buttons)
        dialog.exec()

    def on_readme(self):
        self._show_text_file("README", "README.md")

    def on_changelog(self):
        self._show_text_file("Changelog", "CHANGELOG.md")

    def on_issue_tracker(self):
        QDesktopServices.openUrl(QUrl(ISSUE_TRACKER_URL))
        self.set_status("Opened the issue tracker in your browser.")

    def on_about(self):
        try:
            from pyqt_app_info import AppIdentity, gather_info
            from pyqt_app_info.qt import AboutDialog

            identity = AppIdentity(
                name=APP_NAME,
                short_name=APP_SHORT_NAME,
                version=APP_VERSION,
                commit_date=APP_TIMESTAMP,
                description=APP_DESCRIPTION,
                features=[
                    "Generate QR codes from URLs or arbitrary text",
                    "On-screen PNG preview with zoom / fit-to-window",
                    "Save as PNG and copy to the clipboard",
                    "Print and print-preview via system print services",
                ],
            )
            info = gather_info(identity, caller_file=__file__)
            AboutDialog(info, parent=self).exec()
        except Exception:
            QMessageBox.about(
                self,
                f"About {APP_NAME}",
                f"<b>{APP_NAME}</b> &nbsp; v{APP_VERSION}<br><br>"
                f"{APP_DESCRIPTION}<br><br>"
                f"Built with <b>PyQt6</b>.<br>"
                f"<small>{APP_TIMESTAMP}</small>",
            )
