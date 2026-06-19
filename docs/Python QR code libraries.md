There are several excellent Python QR code libraries that are well-maintained and feature-rich. 

Here are few:

### Python QR Code Libraries

1. **qrcode**
   - The most popular and well-maintained Python QR code library
   - Simple API but highly customizable (size, error correction, border)
   - Can generate QR codes as PIL images, SVG, or ASCII art
   - Supports custom colors and logos embedded in QR codes
   - Installation: `pip install qrcode[pil]`

2. **segno**
   - Very fast and lightweight library
   - Produces highly optimized QR codes
   - Supports Micro QR codes (smaller variant of QR)
   - Can output as PNG, SVG, EPS, PDF, etc.
   - Installation: `pip install segno`

3. **PyQRCode**
   - Pure Python QR code generator
   - Multiple output formats (PNG, SVG, EPS, terminal)
   - Simple and straightforward API
   - Installation: `pip install pyqrcode pypng` (with PNG support)

4. **python-barcode**
   - More comprehensive - does QR codes plus many other barcode formats
   - Good if you might need other barcode types in the future
   - Installation: `pip install python-barcode`

Here's a quick example using the popular `qrcode` library:

```python
import qrcode
from PIL import Image

def create_museum_qr(url, exhibit_id, save_path):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image
    img.save(f"{save_path}/exhibit_{exhibit_id}_qr.png")
    
    return f"QR code for exhibit {exhibit_id} created successfully!"

# Example usage
create_museum_qr("https://museum.org/exhibits/dinosaur-fossils", "dino01", "./qr_codes")
```

Would you like me to go into more detail on any of these libraries or show more advanced examples?
