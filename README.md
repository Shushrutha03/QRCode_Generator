# QRCode_Generator

**Description**
This Python script generates QR codes from input data, such as URLs or text, using the qrcode library. It's a simple tool that allows you to create QR codes for various purposes.

**How to Use**

1.Install the required library:
Before using the script, you need to install the qrcode library if you haven't already. You can install it using pip:
   pip install qrcode

2.Customize the input data:
Edit the script and replace the URL or text you want to encode into the QR code. You can do this by modifying the following line:
img = qrcode.make("https://www.linkedin.com/in/shushrutha-a-528a71253")

3.Run the script:
Execute the script, and it will generate a QR code based on the input data and save it as an image file named "qr.png" in the same directory as the script.

**Example:**
In the provided code, a QR code for the LinkedIn profile generated and saved as "qr.png."

**Acknowledgments**
This script uses the qrcode library for QR code generation. Thanks to the developers of the qrcode library for creating this useful tool.

Feel free to use this script to generate QR codes for your own URLs or text data.

For more information about the qrcode library, visit: qrcode library on GitHub

