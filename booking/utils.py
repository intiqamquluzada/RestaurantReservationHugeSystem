from pyqrcode import create


def embed_QR(url_input, name):
    embedded_qr = create(url_input)
    embedded_qr.png(name, scale=7)

