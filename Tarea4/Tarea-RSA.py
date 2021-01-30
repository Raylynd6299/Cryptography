from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto import Hash
import argparse
import rsa


parser = argparse.ArgumentParser()
parser.add_argument("-GK","--GenKeys",help="Genera la llave privada y publica del numero de bits enviado, Tipos: 512,1024,2048,3072,4096",type=int)
parser.add_argument("-N","--Name",help="Indica el nombre de los archivos")
parser.add_argument("-K","--Key",help="Indica el nombre del archivo de la llave")
parser.add_argument("-M","--Message",help="Indica el nombre del archivo que tiene el mensaje")
parser.add_argument("-nt","--numberThreads",help="Indica el numero de procesos para crear las llaves",type=int)
parser.add_argument("-C", help="Cifrar", action="store_true")
parser.add_argument("-D", help="Descifrar",action="store_true")
parser.add_argument("-S", help="Generar Firma Digital", action="store_true")
parser.add_argument("-F","--Func",help="Indica la funcion Hash a usar, Tipo: ‘MD5’, ‘SHA-1’, ‘SHA-224’, SHA-256’, ‘SHA-384’ , ‘SHA-512’.")
parser.add_argument("-V", help="Verificar Firma Digital",action="store_true")
parser.add_argument("-s", help="Archivo con la Firma Digital")
parser.add_argument("--Steps", help="Firma o Verificacion a mano",action="store_true")

args = parser.parse_args()

if args.GenKeys and args.Name:
    if args.numberThreads:
        (publicKey,privateKey) = rsa.newkeys(args.GenKeys,poolsize=args.numberThreads)
    else:
        (publicKey,privateKey) = rsa.newkeys(args.GenKeys)
           
    with open(f"{args.Name}_PubKey.key",mode="wb") as publicFile:
        publicFile.write(publicKey.save_pkcs1())
    with open(f"{args.Name}_PrivKey.key",mode="wb") as privateFile:
        privateFile.write(privateKey.save_pkcs1())
elif args.C and args.Key and args.Message:
    if "PubKey.key" in args.Key:
        with open(args.Key,mode="rb") as publicFile:
            keydata = publicFile.read()
        publicKey = rsa.PublicKey.load_pkcs1(keydata)
        
        with open(args.Message,mode="rb") as DataFile:
            Data = DataFile.read()
        name = args.Message
        name = name.strip().split(".")
        if len(name) == 2: 
            Cifrado = rsa.encrypt(Data,publicKey)
            with open(f"{name[0]}_C.{name[1]}",mode="wb") as CiferFile:
                CiferFile.write(Cifrado)
    else:
        print("Ingrese la llave Publica")                   
elif args.D and args.Key and args.Message:
    if "PrivKey.key" in args.Key:
        with open(args.Key,mode="rb") as privateFile:
            keydata = privateFile.read()
        privateKey = rsa.PrivateKey.load_pkcs1(keydata)
        
        with open(args.Message,mode="rb") as DataFile:
            Data = DataFile.read()
        name = args.Message
        name = name.strip().split(".")
        if len(name) == 2: 
            try:
                Decifrado = rsa.decrypt(Data,privateKey)
                with open(f"{name[0]}_D.{name[1]}",mode="wb") as DeciferFile:
                    DeciferFile.write(Decifrado)
            except:
                print("Error al Descifrar, el archivo fue modificado")
    else:
        print("Ingrese la llave Privada")
elif args.Steps and args.S and args.Key and args.Message :
    if "PrivKey.key" in args.Key:
        with open(args.Key,mode="rb") as privateFile:
            keydata = privateFile.read()
        privateKey = RSA.importKey(keydata)
       
        with open(args.Message,mode="rb") as DataFile:
            Data = DataFile.read()
            
        name = args.Message
        name = name.strip().split(".")
        if len(name) == 2: 
            msg_hasher =  Hash.SHA1.new(Data)
            signer = pkcs1_15.new(privateKey)
            
            signature = signer.sign(msg_hasher)
                        
            with open(f"{name[0]}.{name[1]}",mode="wb") as SignatureFile:
                SignatureFile.write(signature)
                SignatureFile.write(Data)
            
        else:
            print("Ingrese un nombre de archivo valido")
    else:
        print("Ingrese la llave Privada Correcta")     
elif args.Steps and args.V and args.Key and args.s:
    if "PubKey.key" in args.Key:
        with open(args.Key,mode="rb") as publicFile:
            keydata = publicFile.read()
        publicKey = RSA.importKey(keydata)
                        
        with open(args.s,mode="rb") as SignatureFile:
            signature = SignatureFile.read(256)
            Data = SignatureFile.read()
        #print(Data)
        msg_hasher =  Hash.SHA1.new(Data)
        
        name = args.s
        name = name.strip().split(".")
        try:
            pkcs1_15.new(publicKey).verify(msg_hasher, signature)
            with open(f"{name[0]}.{name[1]}",mode="wb") as SignatureFile:
                SignatureFile.write(Data)
            print("El archivo no fue modificado, Firma valida, Verificado!!!")
        except:
            print("El archivo fue modificado, Error Firma INVALIDA")     
                    
    else:
        print("Ingrese la llave Publica Correcta")
elif args.S and args.Key and args.Message and args.Func:
    
    ## Falta Terminarlo
    if "PrivKey.key" in args.Key:
        with open(args.Key,mode="rb") as privateFile:
            keydata = privateFile.read()
        privateKey = rsa.PrivateKey.load_pkcs1(keydata)
        
        with open(args.Message,mode="rb") as DataFile:
            Data = DataFile.read()
            
        name = args.Message
        name = name.strip().split(".")
        if len(name) == 2: 
            if args.Func in ["MD5","SHA-1","SHA-224","SHA-256","SHA-384","SHA-512"]:
                signature = rsa.sign(Data,privateKey,args.Func)
                with open(f"{name[0]}.sig",mode="wb") as SignatureFile:
                    SignatureFile.write(signature)
            else:
                print("Ingrese una Funcion Hash valida")
        else:
            print("Ingrese un nombre de archivo valido")
    else:
        print("Ingrese la llave Privada Correcta")     
elif args.V and args.Key and args.Message and args.s:
    if "PubKey.key" in args.Key:
        if ".sig" in args.s:
            with open(args.Key,mode="rb") as publicFile:
                keydata = publicFile.read()
            publicKey = rsa.PublicKey.load_pkcs1(keydata)
            
            with open(args.Message,mode="rb") as DataFile:
                Data = DataFile.read()
                
            with open(args.s,mode="rb") as SignatureFile:
                signature = SignatureFile.read()
            try:
                verify = rsa.verify(Data, signature, publicKey)
                if verify:
                    print("El archivo no fue modificado, Verificado!!!")
                else:
                    print("El archivo fue modificado, Error")
            except:
                print("El archivo fue modificado, Error")     
                        
        else:
            print("Ingrese una firma digital valida")
    else:
        print("Ingrese la llave Publica Correcta")
