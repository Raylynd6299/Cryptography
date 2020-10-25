
def vigenereCipher(plaintext,key,anilloN):
    # C = p + k mod 256
    anillo =  len(key)
    key = list(key)
    cipherText = ""
    for indice,letra in enumerate(plaintext):
        cipherText += chr((ord(letra) + ord(key[indice%anillo]))%anilloN)
    return cipherText


def vigenereDecipher(ciphertext,key,anilloN):
    # p = C + (-k) mod 256
    anillo =  len(key)
    
    key = list(key)
    antiKey = []
    for k in key:
        antiKey.append(chr( anilloN - ord(k) ))
    decipherText = ""
    for indice,letra in enumerate(ciphertext):
        decipherText += chr((ord(letra) + ord(antiKey[indice%anillo]))%anilloN)
    return decipherText

