# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

QR Code Generator is a PyQt6 desktop application for generating QR codes from a URL or any text string. It renders a preview of the QR PNG on screen and supports save, clipboard copy, and print via system print services. An optional caption prints a short label centered below the code at full font size and the URL below that in a smaller font. Print output can be scaled 10–100% of the page. Current version: v0.2.4.

A standalone CLI tool (`code/generate_qr.py`) and a legacy web-based version (`code/qr-code-generator-library.html`) also live in the repo.

## Development Commands

### Running the Application
```bash
python code/qr_code_gui.py

# Pre-fill with a URL from the command line
python code/qr_code_gui.py https://example.com
```

### Dependencies
```bash
pip install PyQt6 qrcode Pillow
```

## Critical Project Rules

### Timezone Convention
**ALL timestamps MUST use Central Time USA (CST/CDT), NEVER UTC.**

This applies to:
- Changelog entries
- Version labels (APP_TIMESTAMP in `code/src/qr_gui/constants.py`)
- Documentation timestamps

### Version Numbering
- Production releases: `v0.X.Y` (e.g., v0.2.0)
- Point releases/patches: `v0.X.Ya`, `v0.X.Yb` (e.g., v0.2.2a)
- Update version in: `code/src/qr_gui/constants.py` (APP_VERSION, APP_TIMESTAMP), `code/qr_code_gui.py` (header comment), `CHANGELOG.md`

## Architecture

### Modular Package Structure

The application uses a mixin-based architecture under `code/src/qr_gui/`. The root launcher `code/qr_code_gui.py` is a thin wrapper that adds `code/src/` to the path and calls `main()`.

```python
# MainWindow composition in code/src/qr_gui/main.py
class MainWindow(MenuMixin, FileOpsMixin, ViewMixin, PrintMixin, HelpMixin, QMainWindow):
```

### Module Dependency Flow
constants → qr_core → theme → mixins (menu, file_ops, view, printing, help) → main

**Do not introduce circular imports.**

### Key Modules

| Module | Purpose |
|--------|---------|
| `constants.py` | APP_NAME, APP_VERSION, APP_TIMESTAMP, GITHUB_REPO |
| `qr_core.py` | Qt-free QR rendering — PIL image with optional caption; first caption line uses `font_size` (20pt), subsequent lines use `secondary_font_size` (14pt); shared by GUI and CLI |
| `theme.py` | ThemeManager integration |
| `menu.py` | MenuMixin — menu bar and actions |
| `file_ops.py` | FileOpsMixin — QR generation, save PNG, copy to clipboard; builds caption from optional label + URL |
| `view.py` | ViewMixin — zoom, fit-to-window, scroll area |
| `printing.py` | PrintMixin — system print dialog and print preview; respects `print_scale_spin` for scaled output |
| `help.py` | HelpMixin — About dialog, issue log |
| `main.py` | MainWindow + main() entry point; hosts `url_edit`, `label_edit`, `caption_check`, `print_scale_spin` |

### UI Input Fields (on MainWindow)

| Attribute | Widget | Purpose |
|-----------|--------|---------|
| `url_edit` | `QLineEdit` | URL or text to encode |
| `label_edit` | `QLineEdit` | Optional short label printed above the URL in the caption |
| `caption_check` | `QCheckBox` | Toggles caption rendering on/off |
| `print_scale_spin` | `QSpinBox` | Print scale 10–100% (step 5%); persisted via `QSettings("print/scale")` |

### Shared Modules (external)
- **Icon Manager Module** (`~/Projects/Icon_Manager_Module`) — icon loading, Windows taskbar AUMID
- **ThemeManager** (`~/Projects/ThemeManager`) — built-in themes

### qr_core Design Note
`qr_core.py` is intentionally free of any PyQt6 import so the CLI (`generate_qr.py`) can use it without a GUI toolkit installed.

## Directory Structure

```
QR-codes/
├── code/
│   ├── qr_code_gui.py          # Thin launcher wrapper
│   ├── generate_qr.py          # Standalone CLI QR generator
│   ├── src/
│   │   └── qr_gui/             # Package (9 modules)
│   │       ├── constants.py
│   │       ├── main.py
│   │       ├── menu.py
│   │       ├── file_ops.py
│   │       ├── view.py
│   │       ├── printing.py
│   │       ├── help.py
│   │       ├── theme.py
│   │       └── qr_core.py
│   ├── QR_steamboat-bell.png   # Sample generated QR codes
│   ├── QR_steamboat-clock.png
│   └── qr-code-generator-library.html  # Legacy web-based version
├── docs/                       # Planning docs and library notes
├── notes/                      # Reference notes
├── CHANGELOG.md
└── CLAUDE.md
```

## Common Issues

**Icon not loading**: Ensure `~/Projects/Icon_Manager_Module` exists. The app falls back to a blank icon gracefully if IMM is unavailable.

**`qrcode` module not found**: Run `pip install qrcode[pil]` — the `[pil]` extra is required for PNG rendering.
