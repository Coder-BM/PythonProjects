import qrcode
import random

data = ["Random","Good","Bad","Ugly","Sad"]

rand = random.choice(data)

qr = qrcode.QRCode(version=1,box_size = 10, border=1)
qr.add_data(rand)
qr.make(fit=True)

qr_image = qr.make_image(fill_color = "Green", back_color="Black")

qr_image.save("Details.png")

print("Image Saved!!!!")
