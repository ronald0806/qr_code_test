import qrcode

# website Link
music_link = 'https://www.youtube.com/watch?v=QJQNLpzJJDA'

# actual qr code
qr = qrcode.QRCode(version =1, box_size = 10, border = 10)

# data added to the qr code from music_link
qr.add_data(music_link)
qr.make()

# makes image of qr code
img = qr.make_image(fill_color = 'black', back_color = 'white')

img.save('youtube_qr.png')