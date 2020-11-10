plainText =[ [151,151,47]]


K = [[1,2,3],[4,5,6],[11,9,8]]

def Multi(A,B):
	C=[]
	print(len(A))
	print(len(B))
	for fila in range(len(A)):
		C.append([])
		for columna in range(len(B[0])):
			re = 0
			for indice in range(len(A[0])):
				re +=(A[fila][indice] *B[indice][columna])
				
			C[fila].append(re)

	return C
def operacionesMatriciales(Matriz,funcion):
	for fila in range(len(Matriz)):
		for columna in range(len(Matriz[fila])):
			Matriz[fila][columna] = funcion(Matriz[fila][columna])
	return Matriz		

RES = Multi(plainText,K)
ope = lambda valor:valor%256

Ress = operacionesMatriciales(RES,ope)
print(RES)
