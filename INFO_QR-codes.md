# QR Code Reference

A quick reference guide for users of the QR Code Generator.

---

## What Is a QR Code?

A **QR code** (Quick Response code) is a two-dimensional barcode that stores data as a grid of black and white squares. Unlike a traditional one-dimensional barcode that can only hold a few dozen characters, a QR code can encode thousands of characters across both axes of the grid.

QR codes are read by any smartphone camera or dedicated scanner app. Three distinctive square markers in the corners let the device orient and locate the code at any angle.

---

## Brief History

QR codes were invented in **1994** by Masahiro Hara at Denso Wave, a Toyota subsidiary in Japan, originally to track automobile parts on assembly lines. The format was published as an open standard, and Denso Wave waived enforcement of its patents, which allowed QR codes to spread freely across industries worldwide. The technology saw explosive consumer adoption in the 2010s and again during the COVID-19 pandemic (2020–2021), when touchless menus and check-ins became standard.

---

## What Can a QR Code Store?

A QR code can encode four types of data:

| Mode | Contents | Max characters |
|------|----------|---------------|
| Numeric | Digits 0–9 only | ~7,000 |
| Alphanumeric | Uppercase letters, digits, and a handful of symbols | ~4,300 |
| Binary/Byte | Full ASCII — lowercase, punctuation, URLs, etc. | ~2,950 |
| Kanji | Japanese characters | ~1,800 |

URLs and plain text use Binary/Byte mode. For everyday use, a QR code comfortably holds a full URL, a vCard contact, a Wi-Fi password, or a paragraph of text.

**Version** refers to the physical size of the code. Version 1 is a 21×21 grid; Version 40 is 177×177. The generator chooses the smallest version that fits your content.

---

## Error Correction

QR codes include redundant data so they can still be decoded even if part of the code is damaged, dirty, or obscured. There are four error correction levels:

| Level | Can recover if this much of the code is lost |
|-------|----------------------------------------------|
| L (Low) | ~7% |
| M (Medium) | ~15% |
| Q (Quartile) | ~25% |
| H (High) | ~30% |

Higher error correction makes codes larger and denser but more resilient. Level M or Q is a good default for printed codes that may get worn or smudged. Level H is used when part of the code will be intentionally covered — for example, when a logo is placed in the center.

---

## Common Uses

**Access and authentication**
- Website URLs and deep links
- Wi-Fi network credentials (SSID + password in one scan)
- Event tickets and boarding passes
- Two-factor login verification

**Commerce and payments**
- Mobile payment apps (widely used in China, India, and increasingly elsewhere)
- Loyalty programs, coupons, and promotions
- Product traceability and authenticity seals

**Information**
- Restaurant and venue menus
- Business cards and contact info (vCard)
- Product manuals and support pages
- Museum and exhibit labels
- Tombstone memorials

---

## Practical Tips for Good QR Codes

**Size matters.** Print QR codes large enough to scan reliably. A minimum of about 2 cm × 2 cm (roughly 1 inch) is a common rule of thumb for codes scanned at arm's length. Codes displayed on-screen or at distance need to be proportionally larger.

**Contrast is critical.** The standard is dark modules on a light background. Reversed codes (light on dark) may not scan reliably on all readers. Avoid placing the code on a busy or patterned background.

**Quiet zone.** QR codes require a blank margin — called the "quiet zone" — around all four sides. Without it, scanners may fail to locate the code. The standard specifies 4 module-widths of margin.

**Test before distributing.** Always scan your generated code with at least one device before printing or publishing. What looks correct to the eye may still fail to scan.

**Keep URLs short.** Shorter content produces a smaller, less dense code that scans faster and more reliably. If you're encoding a long URL, consider using a URL shortener first.

**Captions help users.** Including a short label or the URL as human-readable text below the code lets people know what they're about to scan — which also builds trust.

---

## Security Considerations

QR codes are opaque: you cannot tell where a code will take you by looking at it. This creates some risks to be aware of:

- **Malicious URLs** — A code can link to a phishing site, a malware download, or an unwanted action. Only scan codes from sources you trust.
- **Code tampering** — Stickers with a fraudulent code can be placed over a legitimate one in public spaces (parking meters, restaurant tables, posters). Inspect physical codes for signs of tampering.
- **Automatic actions** — Some readers will automatically open a browser, connect to Wi-Fi, or add a contact without asking. Review your scanner app's settings and prefer apps that show a preview before acting.

As a generator of QR codes: make sure the content you encode is what you intend, and consider adding a visible caption or URL so recipients know where the code leads.

---

## Further Reading

- [QR Code — Wikipedia](https://en.wikipedia.org/wiki/QR_code)
- [ISO/IEC 18004:2015 — QR Code standard](https://www.iso.org/standard/62021.html) (paid)
- [Denso Wave QR Code information](https://www.qrcode.com/en/)
