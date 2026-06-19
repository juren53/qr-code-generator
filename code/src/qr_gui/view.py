#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# view.py
#
# ViewMixin: zoom controls for the QR preview plus theme selection and a
# dark-mode toggle, driven by the local ThemeManager.
# -----------------------------------------------------------------------------

from PyQt6.QtWidgets import QApplication, QInputDialog

from .theme import DEFAULT_THEME

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
        names = self.theme_manager.get_theme_names()
        current_index = names.index(self.current_theme) if self.current_theme in names else 0
        name, ok = QInputDialog.getItem(
            self, "Select Theme", "Theme:", names, current_index, editable=False
        )
        if ok and name:
            self.current_theme = name
            self.apply_theme()
            self.set_status(f"Applied {name} theme.")

    def on_toggle_dark_mode(self):
        if self.theme_manager.is_dark_theme(self.current_theme):
            self.current_theme = DEFAULT_THEME
        else:
            self.current_theme = "Dark"
        self.apply_theme()
        self.set_status(f"Applied {self.current_theme} theme.")

    def apply_theme(self):
        QApplication.instance().setStyleSheet(
            self.theme_manager.generate_stylesheet(self.current_theme)
        )
        # Keep the preview backdrop in step with the theme.
        self.scroll_area.setStyleSheet(
            f"QScrollArea {{ background-color: {self.theme_manager.canvas_color(self.current_theme)}; }}"
        )
        if hasattr(self, "dark_mode_action"):
            self.dark_mode_action.setChecked(
                self.theme_manager.is_dark_theme(self.current_theme)
            )
