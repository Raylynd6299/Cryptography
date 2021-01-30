from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto import Hash
import rsa


def Cifrar(pathDir,pathLlave):
    
    key = get_random_bytes(16)
    
    cipher = AES.new(key=key,mode=AES.MODE_CBC)
        
    with open(pathDir,"rb") as file:
        plaintext = file.read()
    
    encrypText = cipher.encrypt(pad(plaintext,AES.block_size))
    
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
     
    with open(pathLlave,mode="rb") as publicFile:
            keydata = publicFile.read()
            
    llaveCifrada = ""
    try:
        publicKey = rsa.PublicKey.load_pkcs1(keydata)
    
        llaveCifrada = rsa.encrypt(key,publicKey)
    except :
        return False
    
    with open(f"{nomarch[0]}_C.{nomarch[1]}","wb") as file:
        file.write(llaveCifrada+cipher.iv+encrypText)
    
    return True
    
def DesCifrar(pathDir,pathLlave):
    with open(pathDir,"rb") as file:
        llaveCifrada = file.read(256)
        iv = file.read(16)
        encrypText = file.read()    
    keydata=""
    with open(pathLlave,mode="rb") as privateFile:
            keydata = privateFile.read()
    
    key = ""
    try:
        privateKey = rsa.PrivateKey.load_pkcs1(keydata)
        key = rsa.decrypt(llaveCifrada,privateKey)
    except:
        return False
    
    cipher = AES.new(key=key,mode=AES.MODE_CBC,IV=iv)
    
    plaintext = cipher.decrypt(encrypText)
    
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    
    with open(f"{nomarch[0]}_D.{nomarch[1]}","wb") as file:
        file.write(plaintext)
    return True

def FirmaDigital(pathDir,pathLlave):
    with open(pathLlave,mode="rb") as privateFile:
        keydata = privateFile.read()
    try:
        privateKey = RSA.importKey(keydata)
    except :
        return False
    with open(pathDir,mode="rb") as DataFile:
        Data = DataFile.read()
        
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    if len(nomarch) == 2: 
        try:
            msg_hasher =  Hash.SHA1.new(Data)
            signer = pkcs1_15.new(privateKey)
            
            signature = signer.sign(msg_hasher)
        except :
            return False        
        with open(f"{nomarch[0]}_F.{nomarch[1]}",mode="wb") as SignatureFile:
            SignatureFile.write(signature)
            SignatureFile.write(Data)
    return True

def Verificacion(pathDir,pathLlave):
    with open(pathLlave,mode="rb") as publicFile:
        keydata = publicFile.read()
    try:
        publicKey = RSA.importKey(keydata)
    except :
        return False                
    with open(pathDir,mode="rb") as SignatureFile:
        signature = SignatureFile.read(256)
        Data = SignatureFile.read()
    
    msg_hasher =  Hash.SHA1.new(Data)
    
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    
    try:
        pkcs1_15.new(publicKey).verify(msg_hasher, signature)
        with open(f"{nomarch[0]}_V.{nomarch[1]}",mode="wb") as SignatureFile:
            SignatureFile.write(Data)
        return True
    except:
        return False   

def Emisor(pathDir,pathLlaveE,pathLlaveR ):
       
    key = get_random_bytes(16)
    
    cipher = AES.new(key=key,mode=AES.MODE_CBC)
        
    with open(pathDir,"rb") as file:
        plaintext = file.read()
    
    encrypText = cipher.encrypt(pad(plaintext,AES.block_size))
    
    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    
     
    with open(pathLlaveR,mode="rb") as publicFile:
            keydata = publicFile.read()
            
    llaveCifrada = ""
    try:
        publicKey = rsa.PublicKey.load_pkcs1(keydata)
    
        llaveCifrada = rsa.encrypt(key,publicKey)
    except :
        return False,1
    
    
    with open(pathLlaveE,mode="rb") as privateFile:
        keydata = privateFile.read()
    try:
        privateKey = RSA.importKey(keydata)
    except :
        return False,2
    
    
    try:
        msg_hasher =  Hash.SHA1.new(pad(plaintext,AES.block_size))
        signer = pkcs1_15.new(privateKey)
        signature = signer.sign(msg_hasher)
    except :
        return False,3    
        
    with open(f"{nomarch[0]}_E.{nomarch[1]}","wb") as file:
        file.write(signature+llaveCifrada+cipher.iv+encrypText)
    
    return True,0

def Receptor(pathDir,pathLlaveE,pathLlaveR ):
    with open(pathDir,"rb") as file:
        signature = file.read(256)
        llaveCifrada = file.read(256)
        iv = file.read(16)
        encrypText = file.read()  

    with open(pathLlaveR,mode="rb") as privateFile:
            keydata = privateFile.read()
    
    key = ""
    try:
        privateKey = rsa.PrivateKey.load_pkcs1(keydata)
        key = rsa.decrypt(llaveCifrada,privateKey)
    except:
        return False,1
    
    cipher = AES.new(key=key,mode=AES.MODE_CBC,IV=iv)
    
    plaintext = cipher.decrypt(encrypText)
        
    
    with open(pathLlaveE,mode="rb") as publicFile:
        keydata = publicFile.read()
    try:
        publicKey = RSA.importKey(keydata)
    except :
        return False,2 
                   
        
    msg_hasher =  Hash.SHA1.new(plaintext)
        
    try:
        pkcs1_15.new(publicKey).verify(msg_hasher, signature)
    except:
        return False,3

    archivo = pathDir.strip().split("/")[-1]
    
    nomarch = archivo.split(".")
    
    with open(f"{nomarch[0]}_R.{nomarch[1]}","wb") as file:
        file.write(plaintext)
    return True,0
