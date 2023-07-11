import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=15,border=4)
qr.add_data("https://adarshmi45.github.io/portfolio/")
qr.make(fit=True)
img=qr.make_image(fill_color="white",back_color="blue")
img.save("Adarsh Portfolio.png")