# QR Code Module

A standalone module that generates QR codes for Museum artifacts, allowing visitors to scan a code displayed beside a physical object and be taken directly to that artifact's record online.

---

## Origin

A visitor scans the code with their phone camera — no app required — and a link appears taking them to an image and description of the artifact on the Internet Archive.

The Internet Archive (archive.org) is free and open source, and is already used by many museums worldwide. It serves as the initial backend target for artifact records.

---

## Prototype

Two test QR codes were generated and linked to placeholder records uploaded to the Internet Archive:

- **Steamboat bell** — `QR_steamboat-bell.png`
- **Steamboat clock** — `QR_steamboat-clock.png`

| Steamboat Bell | Steamboat Clock |
| :---: | :---: |
| <img src="codes/QR_steamboat-bell.png" width="250"> | <img src="codes/QR_steamboat-clock.png" width="250"> |

**Initial reaction:** The technology has matured to the point where implementation at virtually any size institution is straightforward and easy to implement.

---

## Testing Findings

When the test QR codes were printed, they scanned noticeably faster than codes displayed on a computer screen. They were successfully scanned at under 2 cm (~0.75 inches), though more thorough testing in the Museum environment is needed to determine the ideal size and display options.

Key trade-offs identified so far:

| Variable | Notes |
| :--- | :--- |
| QR code size | Smaller is less intrusive but harder to scan at a distance |
| Lighting conditions | Museum lighting varies and affects scan reliability |
| Phone age | Older devices may be slower to recognize codes |
| OS version | Scanner behaviour differs across iOS and Android versions |
| Camera resolution | Lower resolution reduces reliability at small sizes |

---

## Creating and Implementing QR Codes for Your Museum

1. **Publish an item to the Internet Archive.**

2. **Generate a QR Code** for the item published in the Internet Archive.

3. **Display the printed QR code** next to the artifact.

---

## Open Questions

### Backend

- Is the Internet Archive the right data store to serve your museum artifact data to the public?
- How should backend artifact data be structured?

### Artifact Numbering

- What artifact numbering system can be used?

### Physical Display

- How can QR codes be unobtrusively displayed in a museum?
- What is the best display method?
- What is the ideal size for visibility and scannability?

---

## Status

Prototype complete. Lots to talk about and plan before full implementation — it is very doable.
