#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# view.py
#
# ViewMixin: zoom controls for the QR preview plus theme selection and a
# dark-mode toggle, driven by the ThemeManager module.
# -----------------------------------------------------------------------------

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QApplication, QInputDialog

from .theme import (
    DEFAULT_THEME,
    canvas_color,
    get_fusion_palette,
    get_theme_registry,
    is_dark_theme,
)

_MIN_ZOOM = 0.25
_MAX_ZOOM = 8.0


class ViewMixin:
    def on_zoom_in(self):
        self._apply_zoom(self.zoom_factor * 1.25)

    def on_zoom_out(self):
        self._apply_zoom(self.zoom_factor / 1.25)

    def on_reset_zoom(self):
        self.fit_mode = False
        self._apply_zoom(1.0)

    def _apply_zoom(self, factor):
        if self.current_image is None:
            return
        self.fit_mode = False
        self.zoom_factor = max(_MIN_ZOOM, min(_MAX_ZOOM, factor))
        self.refresh_preview()
        self.set_status(f"Zoom: {round(self.zoom_factor * 100)}%")

    def on_fit_to_window(self):
        if self.current_image is None:
            return
        self.fit_mode = True
        self.refresh_preview()
        self.set_status("Fit to window.")

    # ── Theming ───────────────────────────────────────────────────────────
    def on_select_theme(self):
        registry = get_theme_registry()
        themes = [
            (registry.get_theme(n).display_name, n)
            for n in registry.get_theme_names()
            if registry.get_theme(n) is not None
        ]
        display_names = [d for d, _ in themes]
        current_display = next(
            (d for d, k in themes if k == self.current_theme), display_names[0]
        )
        name, ok = QInputDialog.getItem(
            self, "Select Theme", "Theme:", display_names,
            display_names.index(current_display), editable=False,
        )
        if ok and name:
            self.current_theme = next(k for d, k in themes if d == name)
            self.apply_theme()
            self.set_status(f"Applied {name} theme.")

    def on_toggle_dark_mode(self):
        self.current_theme = DEFAULT_THEME if is_dark_theme(self.current_theme) else "dark"
        self.apply_theme()
        self.set_status(f"Applied {self.current_theme} theme.")

    def apply_theme(self):
        QApplication.instance().setPalette(get_fusion_palette(self.current_theme))
        self.scroll_area.setStyleSheet(
            f"QScrollArea {{ background-color: {canvas_color(self.current_theme)}; }}"
        )
        if hasattr(self, "dark_mode_action"):
            self.dark_mode_action.setChecked(is_dark_theme(self.current_theme))
        QSettings().setValue("theme/current", self.current_theme)
