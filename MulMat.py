C0 =[ [9,99,11]]
Plain = [[16,3,8]]

K = [[1,2,3],[4,5,6],[11,9,8]]

def Multi(A,B):
	C=[]
	#print(len(A))
	#print(len(B))
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
def XorArray(A,B):
	C = []
	if len(A[0]) == len(B[0]) :
		for ind in range(len(A[0])):
			C.append ( A[0][ind] ^ B[0][ind])
	return C	

RES = Multi(C0,K)
ope = lambda valor:valor%256
operacionesMatriciales(RES,ope)
num = int(input("Numero"))
for ite in range(num):
	RES = Multi(RES,K)
	operacionesMatriciales(RES,ope)
C = XorArray(Plain,RES)
print(RES)
print(C)
