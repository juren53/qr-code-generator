#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# main.py
#
# MainWindow + application entry point for the QR Code Generator GUI.
#
# The window is composed from focused mixins — MenuMixin, FileOpsMixin,
# ViewMixin, PrintMixin, HelpMixin — following the structure used by Tag
# Writer, Audio Tag Writer, and the HSTL Photo Framework. The central widget
# holds a small input form on top and a scrollable, zoomable preview of the
# rendered QR PNG below it. Printing goes through the standard Qt system
# print services (see printing.py).
# -----------------------------------------------------------------------------

import os
import pathlib
import sys

from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication,
    QCheckBox,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QScrollArea,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

from .constants import APP_NAME, APP_ORGANIZATION, APP_SHORT_NAME, APP_TIMESTAMP, APP_VERSION
from .file_ops import FileOpsMixin
from .help import HelpMixin
from .menu import MenuMixin
from .printing import PrintMixin
from .theme import DEFAULT_THEME, get_theme_registry
from .view import ViewMixin

_PLACEHOLDER = "No QR code yet — enter a URL or text and press Generate (Ctrl+G)."

# IMM setup at module level so _init_win32() fires before QApplication is created.
_IMM_PATH = os.path.expanduser("~/Projects/Icon_Manager_Module")
if os.path.isdir(_IMM_PATH) and _IMM_PATH not in sys.path:
    sys.path.insert(0, _IMM_PATH)

_app_icons = None
try:
    from icon_loader import IconLoader  # side-effect: _init_win32() on Windows
    _app_icons = IconLoader(
        base_path=pathlib.Path(__file__).resolve().parents[2] / "resources" / "icons"
    )
except Exception:
    pass


def get_app_icon() -> QIcon:
    if _app_icons is not None:
        return _app_icons.app_icon()
    return QIcon()


class MainWindow(MenuMixin, FileOpsMixin, ViewMixin, PrintMixin, HelpMixin, QMainWindow):
    """Main application window composed from mixins."""

    def __init__(self):
        super().__init__()

        # State
        saved = QSettings().value("theme/current", DEFAULT_THEME)
        self.current_theme = saved if get_theme_registry().get_theme(saved) else DEFAULT_THEME
        self.current_image = None          # PIL.Image of the rendered QR
        self.base_pixmap = None            # full-resolution QPixmap
        self.zoom_factor = 1.0
        self.fit_mode = True
        self.last_saved_path = None

        self.setWindowTitle(APP_NAME)
        self.resize(640, 720)
        self.setWindowIcon(get_app_icon())

        self._build_central()
        self.create_menu_bar()
        self._build_status_bar()

        self.apply_theme()
        self.update_action_states()
        self.refresh_preview()
        self.url_edit.setFocus()

    # ── UI construction ────────────────────────────────────────────────────
    def _build_central(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(8, 8, 8, 8)

        # Input row
        form_row = QHBoxLayout()
        form_row.addWidget(QLabel("URL / Text:"))
        self.url_edit = QLineEdit()
        self.url_edit.setPlaceholderText("https://example.com")
        self.url_edit.returnPressed.connect(self.on_generate)
        form_row.addWidget(self.url_edit, 1)
        self.generate_btn = QPushButton("Generate")
        self.generate_btn.setDefault(True)
        self.generate_btn.clicked.connect(self.on_generate)
        form_row.addWidget(self.generate_btn)
        layout.addLayout(form_row)

        # Options row
        options_row = QHBoxLayout()
        self.caption_check = QCheckBox("Caption the code with the text below it")
        self.caption_check.setChecked(True)
        options_row.addWidget(self.caption_check)
        options_row.addStretch(1)
        layout.addLayout(options_row)

        # Preview area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(False)
        self.scroll_area.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.preview_label = QLabel(_PLACEHOLDER)
        self.preview_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scroll_area.setWidget(self.preview_label)
        layout.addWidget(self.scroll_area, 1)

    def _build_status_bar(self):
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Ready")
        version_label = QLabel(f"v{APP_VERSION}  ({APP_TIMESTAMP})")
        version_label.setStyleSheet("color: gray;")
        self.status_bar.addPermanentWidget(version_label)

    # ── Shared helpers used across mixins ───────────────────────────────────
    def set_status(self, message: str):
        self.status_bar.showMessage(message)

    def update_action_states(self):
        has_image = self.current_image is not None
        for attr in ("save_action", "print_action", "print_preview_action", "copy_action"):
            action = getattr(self, attr, None)
            if action is not None:
                action.setEnabled(has_image)

    def refresh_preview(self):
        if self.base_pixmap is None or self.base_pixmap.isNull():
            self.preview_label.setPixmap(QIcon().pixmap(0, 0))  # clear any pixmap
            self.preview_label.clear()
            self.preview_label.setText(_PLACEHOLDER)
            self.preview_label.resize(self.scroll_area.viewport().size())
            return

        if self.fit_mode:
            target = self.scroll_area.viewport().size()
            target.setWidth(max(1, target.width() - 4))
            target.setHeight(max(1, target.height() - 4))
            scaled = self.base_pixmap.scaled(
                target,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        else:
            base = self.base_pixmap.size()
            scaled = self.base_pixmap.scaled(
                int(base.width() * self.zoom_factor),
                int(base.height() * self.zoom_factor),
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        self.preview_label.setPixmap(scaled)
        self.preview_label.resize(scaled.size())

    def resizeEvent(self, event):
        super().resizeEvent(event)
        if self.fit_mode and self.base_pixmap is not None:
            self.refresh_preview()


def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setOrganizationName(APP_ORGANIZATION)
    app.setApplicationVersion(APP_VERSION)
    app.setStyle("Fusion")
    app.setWindowIcon(get_app_icon())

    window = MainWindow()
    window.show()

    if _app_icons is not None:
        _app_icons.set_taskbar_icon(window, f"{APP_ORGANIZATION}.{APP_SHORT_NAME}")

    # Pre-fill from a command-line argument, if provided.
    if len(sys.argv) > 1 and sys.argv[1].strip():
        window.url_edit.setText(sys.argv[1].strip())
        window.on_generate()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
