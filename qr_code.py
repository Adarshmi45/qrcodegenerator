import qrcode as qr

#Qr code link or message
img=qr.make("https://adarshmi45.github.io/portfolio/")
img.save("Portfolio.png")