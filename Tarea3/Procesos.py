from Crypto.Cipher import DES
from Crypto import Random

#iv = Random.new().read(DES.block_size)
iv = b'\xa3my\x12\xb5\xc3\xc3W'
def Encriptar(llave,tipo,pathDir):
    global iv
    llave_tr = ""
    if len(llave) != 8:
        return False
    else:
        llave_tr = str.encode(llave)
    
    if(tipo == DES.MODE_CBC):
        cadFin = "cbc"
    elif(tipo == DES.MODE_CFB):
        cadFin = "cfb"
    elif(tipo == DES.MODE_OFB):
        cadFin = "ofb"
    elif(tipo == DES.MODE_ECB):
        cadFin = "ecb"
    else:
        return False
        
    if tipo == DES.MODE_ECB :
        cipher = DES.new(key=llave_tr,mode=DES.MODE_ECB)
    else :
        cipher = DES.new(key=llave_tr,mode=tipo,IV=iv)
    
    
    
    with open(pathDir,"rb") as file:
        header = file.read(54)
        plaintext = file.read()
    
    encrypText = cipher.encrypt(plaintext)
    
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    
    with open(f"{nomarch[0]}_{cadFin}.{nomarch[1]}","wb") as file:
        file.write(header+encrypText)
    return True
    
def Desencriptar(llave,tipo,pathDir):
    global iv
    llave_tr = ""
    if len(llave) != 8:
        return False
    else:
        llave_tr = str.encode(llave)
        
    if(tipo == DES.MODE_CBC):
        cadFin = "cbc"
    elif(tipo == DES.MODE_CFB):
        cadFin = "cfb"
    elif(tipo == DES.MODE_OFB):
        cadFin = "ofb"
    elif(tipo == DES.MODE_ECB):
        cadFin = "ecb"
    else:
        return False
    
    if tipo == DES.MODE_ECB :
        cipher = DES.new(key=llave_tr,mode=DES.MODE_ECB)
    else :
        cipher = DES.new(key=llave_tr,mode=tipo,IV=iv)
    
    
    with open(pathDir,"rb") as file:
        header = file.read(54)
        plaintext = file.read()
    
    encrypText = cipher.decrypt(plaintext)
    
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    
    with open(f"{nomarch[0]}_D_{cadFin}.{nomarch[1]}","wb") as file:
        file.write(header+encrypText)
    return True
    
    
# if __name__ == '__main__':
#     Encriptar("Raymundo",DES.MODE_OFB,"./thundercats.bmp")
#     Desencriptar("Raymundo",DES.MODE_OFB,"./thundercats_ofb.bmp")
    