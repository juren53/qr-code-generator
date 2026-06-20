# Changelog - QR Code Module

All notable changes to the QR Code Module project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

> **Note for maintainers:** Every version header **must** include a date, a 4-digit 24-hour time, and the timezone label.
> Correct format: `## QRG [X.Y.Z] - YYYY-MM-DD HHMM CDT`
> Example: `## QRG [0.1.0] - 2026-06-19 0352 CDT`

## QRG [0.2.3] - 2026-06-20 0915 CDT

### Added

- **Label field for printed output** — a new optional "Label" text field appears below the URL input in the GUI
  - When captioning is enabled and a label is provided, the label prints centered below the QR code at full font size (20pt), with the URL printed below it at a reduced font size (14pt), making long URLs more likely to fit the printed output
  - When no label is entered, behavior is unchanged: the URL caption renders at full size as before
  - **Files Modified**: `code/src/qr_gui/main.py`, `code/src/qr_gui/file_ops.py`, `code/src/qr_gui/qr_core.py`

---

## QRG [0.2.2] - 2026-06-19 1131 CDT

### Changed

- **ThemeManager module integration** — replaced the self-contained `theme.py` palette/stylesheet system with the shared ThemeManager module (v2.0), following the same pattern as the earlier Icon Manager Module migration
  - Gains 6 themes (Dark, Light, Solarized Light, Solarized Dark, Dracula, GitHub) vs the previous 4; theme selection now persists across sessions via `QSettings`
  - `apply_theme()` switches from CSS `setStyleSheet()` to `QPalette`-based `setPalette(get_fusion_palette(...))` for proper Fusion style integration
  - `on_select_theme()` displays proper theme display names and maps them back to internal registry keys
  - `on_toggle_dark_mode()` targets `"light"` / `"dark"` internal keys; `_DARK_THEMES` set (`dark`, `solarized_dark`, `dracula`) drives the `is_dark_theme()` helper
  - `MainWindow` loads the persisted theme from `QSettings` on startup, validated against the registry; falls back to `"light"` if the stored key is stale or unrecognized
  - `os.path.expanduser()` detects the ThemeManager path at `~/Projects/ThemeManager/`; self-contained fallback if the module is unavailable is not provided — ThemeManager is a required dependency
  - **Files Modified**: `code/src/qr_gui/theme.py`, `code/src/qr_gui/view.py`, `code/src/qr_gui/main.py`, `code/src/qr_gui/menu.py`

---

## QRG [0.2.1] - 2026-06-19 0902 CDT

### Fixed

- **Windows taskbar showing Python's default icon** — the app icon now appears correctly in the taskbar, Alt-Tab switcher, and all other Windows icon consumers
  - Root cause: `main.py` used the Icon Manager Module only as a last-resort fallback (after loading the raw `ICON_QR-code-gen.png`), so `_init_win32()` never fired; Windows grouped the process under Python's own AppUserModelID and displayed Python's icon
  - Fix: IMM is now imported at module level — before `QApplication` is created — so `SetCurrentProcessExplicitAppUserModelID("SynchroSoft.QRG")` runs at startup; `set_taskbar_icon()` is called after `window.show()` to also set the per-window COM property and `WM_SETICON`

### Added

- **`resources/icons/` icon set** — generated from `ICON_QR-code-gen.png` using `generate_icons.py` from the Icon Manager Module
  - `app.ico` — multi-resolution Windows icon (16 × 16 through 256 × 256)
  - `app.icns` — macOS icon bundle
  - `app.png`, `app_16x16.png` through `app_256x256.png` — individual PNGs for Linux and Qt fallback
  - **Files Added**: `code/resources/icons/app.ico`, `code/resources/icons/app.icns`, `code/resources/icons/app.png`, `code/resources/icons/app_{16,24,32,48,64,128,256}x{N}.png`

### Changed

- **`main.py` icon loading** — replaced the ad-hoc `get_app_icon()` / `_load_imm()` helpers with a module-level `IconLoader` instance pointing at `code/resources/icons/`; `get_app_icon()` is now a one-liner delegation to `_app_icons.app_icon()`
- **`.gitignore`** — added `!resources/icons/*.png` negation rule so the icon PNGs are tracked despite the top-level `*.png` exclusion that suppresses generated QR output files
  - **Files Modified**: `code/src/qr_gui/main.py`, `code/.gitignore`

---

## QRG [0.2.0] - 2026-06-19 0423 CDT

### Added

- **PyQt6 GUI front-end** — `code/qr_code_gui.py` plus the `code/src/qr_gui/` package add a graphical interface alongside the CLI, following the structure used by Tag Writer, Audio Tag Writer, and the HSTL Photo Framework
  - Composed `MainWindow` built from focused mixins: `MenuMixin`, `FileOpsMixin`, `ViewMixin`, `PrintMixin`, `HelpMixin`
  - Enter a URL or arbitrary text, press **Generate** (or Enter), and the rendered PNG is displayed on screen for review in a scrollable preview area
  - Standard **File / Edit / View / Help** pull-down menus with `&`-mnemonics, keyboard shortcuts, and status tips
    - File: Generate (Ctrl+G), Save As… (Ctrl+Shift+S), Print… (Ctrl+P), Print Preview…, Quit (Ctrl+Q)
    - Edit: Paste URL from Clipboard (Ctrl+V), Copy QR Image (Ctrl+C), Clear (Ctrl+L)
    - View: Zoom In/Out/Reset, Fit to Window, Select Theme…, Toggle Dark Mode (Ctrl+D)
    - Help: README, Changelog, Issue Tracker, About
  - **Printing to standard system print services** via `QtPrintSupport` — `Print…` (`QPrintDialog`) and `Print Preview…` (`QPrintPreviewDialog`), painting the QR code centered on the page with aspect ratio preserved
  - Save the result as a PNG (`QFileDialog`) and copy it to the system clipboard
  - On-screen preview with zoom and fit-to-window, plus a status bar carrying a permanent version label
  - Shared-module integration with graceful fallback: **pyqt-app-info** for the About dialog (falls back to `QMessageBox`), and the **Icon Manager Module** for the app icon (falls back to a null icon)
  - Self-contained `ThemeManager` (Default Light, Dark, Solarized Light/Dark) matching the sibling apps' `get_theme_names()` / `generate_stylesheet()` API
  - **Files Added**: `code/qr_code_gui.py`, `code/src/qr_gui/__init__.py`, `code/src/qr_gui/constants.py`, `code/src/qr_gui/qr_core.py`, `code/src/qr_gui/theme.py`, `code/src/qr_gui/menu.py`, `code/src/qr_gui/file_ops.py`, `code/src/qr_gui/view.py`, `code/src/qr_gui/printing.py`, `code/src/qr_gui/help.py`, `code/src/qr_gui/main.py`

### Changed

- **Shared rendering core** — extracted the QR-rendering logic into `code/src/qr_gui/qr_core.py` (`render_qr()` and `normalize_filename()`), a Qt-free helper now used by both the CLI and the GUI
  - `code/generate_qr.py` refactored to call `qr_core.render_qr()`; its interactive command-line behavior and captioned-PNG output are unchanged
  - The CLI remains a fully available, standalone entry point that does not require PyQt6
  - **Files Modified**: `code/generate_qr.py`

## QRG [0.1.0] - 2026-06-19 0352 CDT

### Added

- **Interactive QR code generator** — `code/generate_qr.py` prompts for a URL at the command line and writes the QR code to a PNG image
  - Prompts for the URL to encode and the output filename (defaults to `qrcode_example.png`; auto-appends `.png` when omitted)
  - Renders the URL and filename as centered captions below the QR code using Pillow's `ImageDraw`/`ImageFont` (DejaVuSans 20pt, with a fallback to the PIL default font)
  - Includes a comment header with a brief description, version stamp, and creation datetime
  - Ships with a `#!/usr/bin/env python3` shebang and is marked executable for direct invocation
  - **Files Added**: `code/generate_qr.py`

- **Norton Simon Museum real-world example** — added a photo and writeup of a QR code in active museum use to the README
  - Documents the Brancusi *Bird in Space* exhibit label "READ" code as an example in the wild
  - **Files Added**: `code/PHOTO_QR-code-at-Norton-Simon.jpg`
  - **Files Modified**: `README.md`

- **Repository hygiene** — added `.gitignore` to keep generated artifacts out of version control
  - Ignores `__pycache__/` and generated `*.png` files
  - **Files Added**: `code/.gitignore`

### Fixed

- **Module shadowing on import** — renamed the original `qrcode.py` to `generate_qr.py`
  - Root cause: a script named `qrcode.py` shadowed the installed `qrcode` library, so `import qrcode` re-imported the script itself and raised `AttributeError: partially initialized module 'qrcode' has no attribute 'QRCode'` (circular import)
  - Fix: renamed the file so the library resolves correctly
  - **Files Modified**: `code/qrcode.py` → `code/generate_qr.py`

### Documentation

- **README Usage section** — added a Usage section documenting requirements (`qrcode`, `Pillow`) and how to run `code/generate_qr.py`, including a sample interactive session
  - **Files Modified**: `README.md`

- **README Status update** — noted that the command-line generator is now available
  - **Files Modified**: `README.md`

---

## QRG [0.0.2] - 2026-06-18 2351 CDT

### Added

- **Proof-of-feasibility demo in README** — embedded the prototype QR code images and an implementation-steps section
  - Added the steamboat bell and clock prototype codes as a side-by-side demo table
  - Added a "Creating and Implementing QR Codes for Your Museum" three-step section
  - **Files Modified**: `README.md`

- **QR codes email thread transcript** — captured the May 2025 discussion as a Markdown document under `notes/`
  - **Files Added**: `notes/` transcript

### Changed

- **Project reorganization** — moved project files into `docs/`, `notes/`, and `code/` subdirectories for a cleaner root, and renamed `codes/` to `code/`
  - Updated README image paths to match the new directory layout
  - **Files Modified**: `README.md`

- **README reframing** — reworked the README into a general-purpose QR code module rather than an institution-specific one
  - Rewrote the Origin section as an Overview of museum QR use
  - Broadened the feasibility statement to apply to any size institution and generalized institution-specific language
  - Normalized QR code image display sizes and improved formatting of the Python QR library notes
  - Added a last-updated timestamp
  - **Files Modified**: `README.md`

### Removed

- **Saved Gmail HTML export** — removed the raw HTML email export in favor of the Markdown transcript
  - **Files Removed**: Gmail HTML export of the QR codes email thread

---

## QRG [0.0.1] - 2026-06-17 1238 CDT

### Added

- **Initial project** — established the QR Code Module repository
  - Added the project README describing the museum QR code module concept
  - Added the QR code generator project files, including the `qrcode` library reference page (`code/qr-code-generator-library.html`), prototype QR code images, and supporting assets
  - Reconciled QR code PNG filenames with their linked content
  - **Files Added**: `README.md`, `code/qr-code-generator-library.html`, `code/QR_steamboat-bell.png`, `code/QR_steamboat-clock.png`, `code/index.html`, `code/res/`

---
