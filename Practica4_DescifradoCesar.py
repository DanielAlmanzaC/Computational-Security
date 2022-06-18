print("Este es el algoritmo de descifrado Cesar")
# mensaje = "ZAMXAMNFADYQZFQEMTNEFNMCGQMYGQDNMNFADYQZFNXQMTNEFNMCGQMHUHN" 
#el mensaje 1 está desplazado 13 lugares
mensaje = "UJSKRSDWLRIM REMDIMSDRSDSN LRIM IMWRSDSN LRUJSKRSDWL"
#el mensaje 2 está desplazado 19 posiciones y está en latín
#mensaje = "IAÑJWOXSÑRSÑ WZÑYWZC SHFCGÑS DWSNOÑQCAÑSZÑDFW SFÑDOGC"
cant = int(input("¿Cuántas posiciones está recorrido el mensaje?\n"))
#el mensaje 3 está desplazado 15 posiciones
letras = "ZYXWVUTSRQPOÑNMLKJIHGFEDCBA ZYXWVUTSRQPOÑNMLKJIHGFEDCBA"

def cesarInv(mensaje):
    descifrado = ""
    for i in mensaje.upper():
        if(i in letras):
            descifrado += letras[letras.index(i)+cant]
    return descifrado

input("El mensaje original es: "+cesarInv(mensaje))

