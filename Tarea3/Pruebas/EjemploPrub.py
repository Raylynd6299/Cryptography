from Crypto.Cipher import DES
from Crypto import Random


key = b"Raymundo"

iv = Random.new().read(DES.block_size)

cipher = DES.new(key=key,mode=DES.MODE_ECB)

plaintext = b"Hola soy Raymundo Pulido"

msg = cipher.encrypt(plaintext)
with open("./thundercats.bmp","rb") as file:
    header = file.read(54)
    plaintext = file.read()
    
msg = cipher.encrypt(plaintext)
#print(msg)

with open("./thundercats_c.bmp","wb") as file:
    file.write(header+msg)
#print(len(plaintext)/8)