import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/HarshChauhan19')
qr.make(fit=True)

img = qr.make_image(fill_color="aqua", back_color="yellow")

type(img)

img.save("img4.png")