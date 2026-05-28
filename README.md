# QR-CODE-GENERATOR
This is a simple Python project that generates a UPI Payment QR Code using the qrcode library. The generated QR can be scanned using any UPI app like PhonePe, Paytm, or Google Pay.


A simple Python script that generates a dynamic, scan-and-pay UPI QR Code. The generated QR code is universal and can be scanned using any standard Indian UPI application like PhonePe, Paytm, Google Pay, or BHIM.

## Features
- Generates a universal UPI payment deep-link layout.
- Automatically saves the generated QR code as an image (`upi_payment_qr.png`).
- Instantly previews the image upon generation.

## Prerequisites
You need Python installed on your machine along with the `qrcode` library with Pillow support.

```bash
pip install qrcode[pil]
