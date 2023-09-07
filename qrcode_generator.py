import qrcode
features=qrcode.QRCode(version=2,box_size=6,border=9)
features.make(fit=True)
img=qrcode.make("https://www.linkedin.com/in/shushrutha-a-528a71253")
img.save("qr.png") 
