import qrcode
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://github.com/HarshChauhan19")
qr.make(fit=True)

img=qr.make_image(fill_color="(123, 211, 234)", back_color="(246, 214, 214)")

type(img)

img.save("img2.png")