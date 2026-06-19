#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# menu.py
#
# MenuMixin: builds the standard File / Edit / View / Help menu bar. Follows
# the ampersand-mnemonic + keyboard-shortcut convention used across the
# sibling PyQt6 apps (Tag Writer, Audio Tag Writer, HSTL Photo Framework).
# -----------------------------------------------------------------------------

from PyQt6.QtGui import QAction, QKeySequence


class MenuMixin:
    def create_menu_bar(self):
        mb = self.menuBar()

        # ── File ──────────────────────────────────────────────────────────
        file_menu = mb.addMenu("&File")

        generate_act = QAction("&Generate QR Code", self)
        generate_act.setShortcut("Ctrl+G")
        generate_act.setStatusTip("Render a QR code from the current text")
        generate_act.triggered.connect(self.on_generate)
        file_menu.addAction(generate_act)

        self.save_action = QAction("Save &As…", self)
        self.save_action.setShortcut(QKeySequence.StandardKey.SaveAs)
        self.save_action.setStatusTip("Save the QR code as a PNG image")
        self.save_action.triggered.connect(self.on_save_as)
        file_menu.addAction(self.save_action)

        file_menu.addSeparator()

        self.print_action = QAction("&Print…", self)
        self.print_action.setShortcut(QKeySequence.StandardKey.Print)
        self.print_action.setStatusTip("Print the QR code to a system printer")
        self.print_action.triggered.connect(self.on_print)
        file_menu.addAction(self.print_action)

        self.print_preview_action = QAction("Print Pre&view…", self)
        self.print_preview_action.setStatusTip("Preview the printed page before printing")
        self.print_preview_action.triggered.connect(self.on_print_preview)
        file_menu.addAction(self.print_preview_action)

        file_menu.addSeparator()

        quit_act = QAction("&Quit", self)
        quit_act.setShortcut("Ctrl+Q")
        quit_act.setStatusTip("Exit the application")
        quit_act.triggered.connect(self.close)
        file_menu.addAction(quit_act)

        # ── Edit ──────────────────────────────────────────────────────────
        edit_menu = mb.addMenu("&Edit")

        paste_act = QAction("&Paste URL from Clipboard", self)
        paste_act.setShortcut("Ctrl+V")
        paste_act.setStatusTip("Paste clipboard text into the URL field")
        paste_act.triggered.connect(self.on_paste_url)
        edit_menu.addAction(paste_act)

        self.copy_action = QAction("&Copy QR Image", self)
        self.copy_action.setShortcut("Ctrl+C")
        self.copy_action.setStatusTip("Copy the rendered QR code to the clipboard")
        self.copy_action.triggered.connect(self.on_copy_image)
        edit_menu.addAction(self.copy_action)

        edit_menu.addSeparator()

        clear_act = QAction("C&lear", self)
        clear_act.setShortcut("Ctrl+L")
        clear_act.setStatusTip("Clear the input fields and preview")
        clear_act.triggered.connect(self.on_clear)
        edit_menu.addAction(clear_act)

        # ── View ──────────────────────────────────────────────────────────
        view_menu = mb.addMenu("&View")

        zoom_in_act = QAction("Zoom &In", self)
        zoom_in_act.setShortcut("Ctrl++")
        zoom_in_act.triggered.connect(self.on_zoom_in)
        view_menu.addAction(zoom_in_act)

        # Alternate Ctrl+= shortcut (so the user need not press Shift).
        zoom_in_alt = QAction(self)
        zoom_in_alt.setShortcut("Ctrl+=")
        zoom_in_alt.triggered.connect(self.on_zoom_in)
        self.addAction(zoom_in_alt)

        zoom_out_act = QAction("Zoom &Out", self)
        zoom_out_act.setShortcut("Ctrl+-")
        zoom_out_act.triggered.connect(self.on_zoom_out)
        view_menu.addAction(zoom_out_act)

        reset_zoom_act = QAction("&Reset Zoom", self)
        reset_zoom_act.setShortcut("Ctrl+0")
        reset_zoom_act.triggered.connect(self.on_reset_zoom)
        view_menu.addAction(reset_zoom_act)

        fit_act = QAction("&Fit to Window", self)
        fit_act.setShortcut("Ctrl+F")
        fit_act.triggered.connect(self.on_fit_to_window)
        view_menu.addAction(fit_act)

        view_menu.addSeparator()

        theme_act = QAction("Select &Theme…", self)
        theme_act.setStatusTip("Choose a color theme")
        theme_act.triggered.connect(self.on_select_theme)
        view_menu.addAction(theme_act)

        self.dark_mode_action = QAction("Toggle &Dark Mode", self)
        self.dark_mode_action.setShortcut("Ctrl+D")
        self.dark_mode_action.setCheckable(True)
        self.dark_mode_action.setChecked(self.theme_manager.is_dark_theme(self.current_theme))
        self.dark_mode_action.triggered.connect(self.on_toggle_dark_mode)
        view_menu.addAction(self.dark_mode_action)

        # ── Help ──────────────────────────────────────────────────────────
        help_menu = mb.addMenu("&Help")

        readme_act = QAction("&README…", self)
        readme_act.setShortcut("F1")
        readme_act.triggered.connect(self.on_readme)
        help_menu.addAction(readme_act)

        changelog_act = QAction("&Changelog…", self)
        changelog_act.triggered.connect(self.on_changelog)
        help_menu.addAction(changelog_act)

        issue_act = QAction("&Issue Tracker", self)
        issue_act.setStatusTip("Open the GitHub issue tracker in your browser")
        issue_act.triggered.connect(self.on_issue_tracker)
        help_menu.addAction(issue_act)

        help_menu.addSeparator()

        about_act = QAction("&About…", self)
        about_act.triggered.connect(self.on_about)
        help_menu.addAction(about_act)
