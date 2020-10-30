
def vigenereCipher(plaintext,key):
    # C = p + k mod 256
    anillo =  len(key)
    key = list(key)
    cipherText = ""
    alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
  
    plaintext = ' '.join([line.strip() for line in plaintext.strip().splitlines()])
    plaintext = plaintext.replace(" ","")
    
    for indice,letra in enumerate(plaintext):
            cipherText += alfabeto[((alfabeto.index(letra.upper()) + alfabeto.index(key[indice%anillo].upper()))%26)]
    return cipherText


def vigenereDecipher(ciphertext,key):
    # p = C + (-k) mod 256
    anillo =  len(key)
    
    key = list(key)
    antiKey = []
    ciphertext = ciphertext.strip()
    alfabeto=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for k in key:
        if (alfabeto.index(k.upper()) == 0):
            antiKey.append(alfabeto[0])
        else:
            antiKey.append(alfabeto[( 26 - alfabeto.index(k.upper()) )])
            
    decipherText = ""
    for indice,letra in enumerate(ciphertext):
        decipherText += alfabeto[((alfabeto.index(letra.upper()) + alfabeto.index(antiKey[indice%anillo].upper()))%26)]
    return decipherText

