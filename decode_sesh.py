import base64
import zlib

def decode(session):
    s = str(session) + '==='
    d = zlib.decompress(base64.urlsafe_b64decode(s))
    print(d)


decode('eJwNyUEKgCAQRuG7_GsXLayFl5FJpQRxQieDpLs3qwffmwhcR2qdJHP1XUgS3FQtcKtB40f7GVx06EA4SWDQQ6rUMqu8cbAU2ln84q2-u6fmc4Tb7PcDKa4gCQ')
