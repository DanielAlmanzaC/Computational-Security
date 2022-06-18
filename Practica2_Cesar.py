print("Este es el algoritmo de cifrado Cesar")
mensaje = input("Escribe tu mensaje para cifrar\n")
cant = int(input("¿Cuántas posiciones quieres avanzar?\n"))
letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def cesar(mensaje):
    cifrado = ""
    for i in mensaje.upper():
        if(i in letras):
            cifrado += letras[letras.index(i)+cant]
    return cifrado

input("El mensaje cifrado es: "+cesar(mensaje))

mensaje2 = input("Escribe el texto cifrado esta vez\n")
cant = int(input("¿Cuántas posiciones está recorrido el mensaje?\n"))
letras2 = "ZYXWVUTSRQPOÑNMLKJIHGFEDCBAZYXWVUTSRQPOÑNMLKJIHGFEDCBA"

def cesarInv(mensaje):
    descifrado = ""
    for i in mensaje.upper():
        if(i in letras2):
            descifrado += letras2[letras2.index(i)+cant]
    return descifrado

input("El mensaje original es: "+cesarInv(mensaje2))

