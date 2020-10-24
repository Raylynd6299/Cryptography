# Python Program - Print ASCII Values
with open ("prueba.txt",'w+') as file:		
	for i in range(1, 255):
		ch = chr(i)
		file.write(f"{i} = {ch}\n")