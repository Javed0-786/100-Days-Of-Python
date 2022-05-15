# Import Library
import qrcode
# Generate QR Code
img = qrcode.make('aur abhishek bhai kya haal hai')
img.save('hello.png')
