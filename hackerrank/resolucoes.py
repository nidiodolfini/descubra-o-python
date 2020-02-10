import pyqrcode
from pyqrcode import QRCode

s = 'https://nidio.dev'

url = pyqrcode.create(s)

url.svg('myqr.svg', scale=8)