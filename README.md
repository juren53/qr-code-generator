# MCIS QR Code Module

A standalone MCIS module that generates QR codes for Museum artifacts, allowing visitors to scan a code displayed beside a physical object and be taken directly to that artifact's record online.

---

## Origin

The idea came from Shelly Franklin at WHM (Whitehead Home Museum): add QR codes to artifacts currently on display with no information label. A visitor scans the code with their phone camera — no app required — and a link appears taking them to an image and description of the artifact on the Internet Archive.

The Internet Archive (archive.org) is free and open source, and is already used by many museums worldwide. It serves as the initial backend target for artifact records.

---

## Prototype

Two test QR codes were generated and linked to placeholder records uploaded to the Internet Archive:

- **Ship's bell** — `QR_ships-bell.png`
- **Bridge clock** — `QR_bridge-clock.png`

An existing example of this approach in action is the [Truman Home music collection](https://archive.org/details/trumanhomemusic) on the Internet Archive — a small portion of Harry Truman's record collection, publicly browsable. Someone stumbling across one piece like that online could be compelled to visit the physical Museum to see what else is there.

**Initial reaction:** The technology has matured to the point where implementation at WHM is very doable with relatively little friction.

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

## Open Questions

### Backend

- Is the Internet Archive the right data store to serve WHM artifact data to the public?
- How should backend artifact data be structured?

### Artifact Numbering

- How do we implement a WHM-specific artifact numbering system?

### Physical Display

- How do we unobtrusively display QR codes in the Museum?
- What is the best display method?
- What is the ideal size for visibility and scannability?

---

## Status

Prototype complete. Lots to talk about and plan before full implementation — it is very doable.
