# Affine Cipher has the next structure to Cipher
# C = A * p + B mod n
# p = A^-1 ( C + (-B) ) mod n

# To this exercise n = 256

import random

def verifyKey(A,n):
    x = A
    y = n
    while ( y > 0):
        r = x%y
        x = y
        y = r
    if (x == 1 ):
        return True,x
    else:
        return False,x

def xgcd(a, b):
    """
    a = anillo
    b = alpha
    MCD(a,b) = c
    c = a * u0 + b * v0
    return (c,u0,v0,bm1)
    """
    anillo = a
    if b == 0:
        return 0,1,0
 
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1
 
    while b != 0:
        q = a//b
        r = a - b * q
        u = u0 - q * u1
        v = v0 - q * v1
        #Update a,b
        a = b
        b = r
        #Update for next iteration
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v
    bm1 = v0
    if v0 < 0:
        bm1 = anillo + v0

    return  a, u0, v0, bm1
    
def AffineCipher(alpha,beta,anillo,plainText):
    """"
        Ya entran validados (alpha,beta,anillo)
    """
    cipherText = ""
    for letter in plainText:
        CipherLetter =  chr(((alpha * ord(letter)) + beta)% anillo)
        cipherText += CipherLetter
    return cipherText

def AffineDecipher(alpha,beta,anillo,cipherText):
    """"
        Ya entran validados (alpha,beta,anillo)
    """
    deciphetText = ""
    
    _,_,_,alphaNeg =  xgcd(anillo,alpha)

    betaNeg = anillo - beta
    
    for letter in cipherText:   
        DecipherLetter =  chr(((alphaNeg * ord(letter)) + (alphaNeg * betaNeg)%anillo )% anillo)
        deciphetText += DecipherLetter
    return deciphetText
        
def GenKey(anilloN):
    pruebas = []
    a = random.randint(1, anilloN)
    while verifyKey(a,anilloN) != (True,1):
        pruebas.append(a)
        while a in pruebas:
            a = random.randint(1, anilloN)
    return a,random.randint(1, anilloN)

if __name__ == '__main__':
    print(GenKey(256))
    print(verifyKey(7,25))
    