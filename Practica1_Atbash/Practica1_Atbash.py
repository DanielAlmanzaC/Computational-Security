mensaje = input("Escribe tu mensaje\n")

original = "abcdefghijklmnopqrstuvwxyz"
clave = "ZYXVUTSRQPONMLKJIHGFEDCBA"
cifrado = ""

for i in mensaje.lower():
    if(i in original):
        cifrado += clave[original.index(i)]

print("Tu mensaje ha sido cifrado: "+cifrado)