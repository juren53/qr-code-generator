# Python QR Code Libraries

There are several excellent, mature Python libraries available for generating QR codes. Here are the most popular options, depending on your specific needs.

---

## 1. `qrcode` — The Standard Choice

This is the most widely used library. It is robust, simple, and integrates perfectly with Pillow (PIL) to generate images. It also supports rendering QR codes directly in the terminal as text.

- **Best for:** General use, standard image generation (PNG, JPEG), and quick scripts.
- **Installation:** `pip install qrcode[pil]`

**Basic Example:**

```python
import qrcode

# Create the QR code object
qr = qrcode.QRCode(version=1, box_size=10, border=4)
qr.add_data("https://www.example.com")
qr.make(fit=True)

# Create and save the image
img = qr.make_image(fill_color="black", back_color="white")
img.save("qrcode_example.png")
```

---

## 2. `segno` — No Heavy Dependencies

`segno` is a pure-Python library, meaning it doesn't require extra C-libraries or heavy image packages like Pillow to function out of the box. It can export to SVG, PNG, PDF, and even animated GIFs.

- **Best for:** Lightweight applications, AWS Lambda functions (where package size matters), and native SVG generation.
- **Installation:** `pip install segno`

**Basic Example:**

```python
import segno

qrcode = segno.make_qr("https://www.example.com")
qrcode.save("segno_qr.svg", scale=10)  # Saves as a scalable vector graphic
```

---

## 3. `amzqr` — Amazing QR

If you want to make your QR codes visually striking, `amzqr` allows you to embed images (static or animated GIFs) into the background of the QR code.

- **Best for:** Marketing, artistic, or stylized QR codes.
- **Installation:** `pip install amzqr`

**Basic Example:**

```python
from amzqr import amzqr

version, level, qr_name = amzqr.run(
    words="https://www.example.com",
    version=1,
    level='H',
    picture="background_image.png",  # Path to your background image
    colorized=True,
    save_name="artistic_qr.png"
)
```

---

## Summary Recommendation

| If you need to... | Use this library |
| :--- | :--- |
| Generate standard PNG/JPEG images quickly | `qrcode` |
| Create scalable vector graphics (SVG) without heavy dependencies | `segno` |
| Blend the QR code with a custom background image or animated GIF | `amzqr` |
