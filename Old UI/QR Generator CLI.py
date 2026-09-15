import qrcode

data = fill = background = filename = None

while not data:
    data = input("Enter Data: ")

while not fill:
    fill = input("Enter the QR pattern color (dark color): ")

while not background:
    background = input("Enter the QR background color (light color): ")

while not filename:
    filename = input("Enter file name: ")

qr = qrcode.QRCode(version=1,
                   box_size=10,
                   border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color=fill,
                    back_color=background)

img.save(filename + '.png')
print("\nYour QR", filename + ".png", "has been saved.\n")
