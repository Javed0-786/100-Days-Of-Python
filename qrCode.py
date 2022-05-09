# Import Library
import qrcode
# Generate QR Code
img = qrcode.make('Kya hal hai loudu')
img.save('hello.png')
