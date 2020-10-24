
def vigenereCipher(plaintext,key):
    # C = p + k mod 256
    anillo =  len(key)
    key = list(key)
    cipherText = ""
    for indice,letra in enumerate(plaintext):
        cipherText += chr((ord(letra) + ord(key[indice%anillo]))%256)
    return cipherText


def vigenereDecipher(ciphertext,key):
    # p = C + (-k) mod 256
    anillo =  len(key)
    
    key = list(key)
    antiKey = []
    for k in key:
        antiKey.append(chr( 256 - ord(k) ))
    decipherText = ""
    for indice,letra in enumerate(ciphertext):
        decipherText += chr((ord(letra) + ord(antiKey[indice%anillo]))%256)
    return decipherText

