# QR Code Generator Library

## Introduction

This project aims to be the best, clearest library for generating QR Codes. The primary goals are flexible options and absolute correctness. Secondary goals are compact implementation size and good documentation comments.

This work is an independent implementation based on reading the official ISO specification documents. The library has a more intuitive API and shorter code length than competing libraries. The library is designed first in Java and then ported to TypeScript, Python, Rust, C++, and C. It is open source under the MIT License. For each language, the codebase is roughly 1000 lines of code and has no dependencies other than the respective language's standard library.

## Live Demo (JavaScript)

You can generate QR Code symbols conveniently on a web page, powered by the TypeScript port of this library.

### Parameters for QR Code Generation:

- **Text string:** Enter your text to be put into the QR Code
- **Error correction level:**
  - Low
  - Medium
  - Quartile
  - High
- **Output format:**
  - Bitmap
  - Vector
- **Border:** Number of modules (default: 4)
- **Scale:** Pixels per module (default: 8)
- **Colors:**
  - Light: #FFFFFF (white)
  - Dark: #000000 (black)
- **Version range:**
  - Minimum: 1
  - Maximum: 40
- **Mask pattern:**
  - -1 for automatic
  - 0 to 7 for manual
- **Boost ECC:** Option to increase error correction code level within same version

## Features

### Core features:

- Available in 6 programming languages, all with nearly equal functionality: Java, Java (fast), TypeScript/JavaScript, Python, Rust, Rust (no heap), C++, C
- Significantly shorter code but more documentation comments compared to competing libraries
- Supports encoding all 40 versions (sizes) and all 4 error correction levels, as per the QR Code Model 2 standard
- Output format: Raw modules/pixels of the QR symbol
- Detects finder-like penalty patterns more accurately than other implementations
- Encodes numeric and special-alphanumeric text in less space than general text
- Open-source code under the permissive MIT License

### Manual parameters:

- User can specify minimum and maximum version numbers allowed, then library will automatically choose smallest version in the range that fits the data
- User can specify mask pattern manually, otherwise library will automatically evaluate all 8 masks and select the optimal one
- User can specify absolute error correction level, or allow the library to boost it if it doesn't increase the version number
- User can create a list of data segments manually and add ECI segments

### Optional advanced features (Java only):

- Encodes Japanese Unicode text in kanji mode to save a lot of space compared to UTF-8 bytes
- Computes optimal segment mode switching for text with mixed numeric/alphanumeric/general/kanji parts

## Source Code

This library is designed with essentially the same API structure and naming in multiple languages for your convenience: Java, TypeScript, Python, Rust, C++, C. Each language port is pure and doesn't use foreign function calls. Regardless of the language used, the generated results are guaranteed to be identical because the algorithms are translated faithfully.

Git repositories:
- Primary: https://github.com/nayuki/QR-Code-generator
- Mirror: https://gitlab.com/Nayuki/QR-Code-generator

## Language Implementations

### Java

The Java implementation (SE 7+) includes:
- QrCode.java, QrSegment.java, BitBuffer.java
- Optional advanced logic (SE 8+): QrSegmentAdvanced.java
- Runnable demo program: QrCodeGeneratorDemo.java

Available as a package on Maven Central: io.nayuki:qrcodegen

### Java, fast

For heavy-duty use, this alternate Java implementation achieves a speed-up of about 1.5 to 10 times compared to the reference Java library.

### TypeScript

The TypeScript implementation includes:
- qrcodegen.ts
- Demo matching all other languages: qrcodegen-output-demo.ts
- Interactive demo: qrcodegen-input-demo.ts

### JavaScript

The JavaScript port can be found in the releases section on GitHub, with versions compatible with ECMAScript 5 (for IE11) or ES6/2015 (for modern browsers).

### Python

The Python implementation (Python 3+) includes:
- qrcodegen.py
- Runnable demo program: qrcodegen-demo.py

Available as a package on PyPI: `pip install qrcodegen`

### Rust

The Rust implementation includes:
- lib.rs
- Runnable demo program: qrcodegen-demo.rs

Available as a package on Crates.io: qrcodegen

### Rust, no heap

This implementation combines the object-oriented organization of the other Rust port and the complete lack of heap allocation of the C port, suitable for constrained environments.

### C++

The C++ implementation (C++11 and above) includes:
- qrcodegen.hpp, qrcodegen.cpp
- Runnable demo program: QrCodeGeneratorDemo.cpp

### C

The C implementation (C99 and above) includes:
- qrcodegen.h, qrcodegen.c
- Runnable demo program: qrcodegen-demo.c

This C port is designed specifically for constrained environments like microcontrollers.

## More Information

- [Wikipedia: QR code](https://en.wikipedia.org/wiki/QR_code)
- [QRcode.com by Denso Wave](https://www.qrcode.com/en/)
- [Thonky.com: QR Code Tutorial](https://www.thonky.com/qr-code-tutorial/)

---

Source: [Project Nayuki - QR Code Generator Library](https://www.nayuki.io/page/qr-code-generator-library)

