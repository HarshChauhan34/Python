import qrcode

img = qrcode.make('https://github.com/HarshChauhan19')

type(img)

img.save("img1.png")