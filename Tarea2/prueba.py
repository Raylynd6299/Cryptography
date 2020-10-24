Texto = ""
with open("TextoPrub","r") as file:
    Texto = file.read()

with open("Respuesta.txt","w+") as filee:
    for letra in Texto:
        filee.write(f"{ord(letra)} \n")