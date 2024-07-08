import qrcode
import qrcode.main
import random
import time

counter = 0
while True:
    data = ["Random","Good","Bad","Ugly","Sad"]
    rand = random.choice(data)
    
    qr = qrcode.main.QRCode(version=1,box_size=20,border=1)
    
    qr.add_data(rand)
    
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="white",back_color="black")
    
    img.save("qrcode.png")
    
    time.sleep(10)
    
    counter += 1
    
    print(f'{counter} : QRSaved')