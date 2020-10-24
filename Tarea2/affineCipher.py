# Affine Cipher has the next structure to Cipher
# C = A * p + B mod n
# p = A^-1 ( C + (-B) ) mod n

# To this exercise n = 256

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
    
# if __name__ == '__main__':
#     print(verifyKey(13,256))
#     print(xgcd(173,83))
    