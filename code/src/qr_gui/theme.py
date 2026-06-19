#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# theme.py
#
# Lightweight, self-contained theme manager for the QR Code Generator GUI.
# Exposes the same public surface used by Tag Writer / Audio Tag Writer
# (get_theme_names() + generate_stylesheet()) so the View menu can offer
# theme selection and a dark-mode toggle without an external dependency.
# -----------------------------------------------------------------------------

from __future__ import annotations

# Each theme is a small palette dict; generate_stylesheet() turns it into a
# Qt stylesheet applied application-wide via QApplication.setStyleSheet().
_THEMES = {
    "Default Light": {
        "dark": False,
        "window": "#f0f0f0",
        "text": "#1e1e1e",
        "base": "#ffffff",
        "border": "#b0b0b0",
        "accent": "#0a64c8",
        "canvas": "#e8e8e8",
    },
    "Dark": {
        "dark": True,
        "window": "#2b2b2b",
        "text": "#e6e6e6",
        "base": "#1e1e1e",
        "border": "#555555",
        "accent": "#3b9dff",
        "canvas": "#232323",
    },
    "Solarized Light": {
        "dark": False,
        "window": "#fdf6e3",
        "text": "#586e75",
        "base": "#ffffff",
        "border": "#93a1a1",
        "accent": "#268bd2",
        "canvas": "#eee8d5",
    },
    "Solarized Dark": {
        "dark": True,
        "window": "#002b36",
        "text": "#93a1a1",
        "base": "#073642",
        "border": "#586e75",
        "accent": "#268bd2",
        "canvas": "#073642",
    },
}

DEFAULT_THEME = "Default Light"


class ThemeManager:
    """Minimal theme registry producing Qt stylesheets."""

    def __init__(self):
        self.current_theme = DEFAULT_THEME

    def get_theme_names(self) -> list[str]:
        return list(_THEMES.keys())

    def is_dark_theme(self, theme_name: str) -> bool:
        return _THEMES.get(theme_name, _THEMES[DEFAULT_THEME])["dark"]

    def canvas_color(self, theme_name: str) -> str:
        """Background color recommended for the QR preview area."""
        return _THEMES.get(theme_name, _THEMES[DEFAULT_THEME])["canvas"]

    def generate_stylesheet(self, theme_name: str) -> str:
        c = _THEMES.get(theme_name, _THEMES[DEFAULT_THEME])
        return f"""
            QMainWindow, QDialog {{ background-color: {c['window']}; }}
            QWidget {{ color: {c['text']}; }}
            QLabel {{ color: {c['text']}; background: transparent; }}
            QLineEdit, QPlainTextEdit, QTextEdit, QSpinBox {{
                background-color: {c['base']};
                color: {c['text']};
                border: 1px solid {c['border']};
                border-radius: 4px;
                padding: 4px;
            }}
            QPushButton {{
                background-color: {c['base']};
                color: {c['text']};
                border: 1px solid {c['border']};
                border-radius: 4px;
                padding: 6px 12px;
            }}
            QPushButton:hover {{ border-color: {c['accent']}; }}
            QPushButton:default {{ border: 1px solid {c['accent']}; }}
            QMenuBar, QMenu {{ background-color: {c['window']}; color: {c['text']}; }}
            QMenu::item:selected, QMenuBar::item:selected {{
                background-color: {c['accent']}; color: #ffffff;
            }}
            QStatusBar {{ background-color: {c['window']}; color: {c['text']}; }}
            QScrollArea {{ border: 1px solid {c['border']}; }}
        """
