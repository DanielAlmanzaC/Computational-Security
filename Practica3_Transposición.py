print("¡Bienvenido al cifrado de transposición!\n")
mensaje = input("Escribe tu mensaje que quieres cifrar\n")
mensaje = mensaje.lower()
mensaje = mensaje.strip()
n = int(input("¿Cuántas filas quieres?\n"))
m = int(input("¿Cuántas columnas quieres?\n"))
l = len(mensaje)
i = 0
a = 0
pos = -1
message = ""

def cantidad(i):
    i+=1
    return i

def posicion(pos):
    pos+=1
    return pos

def transposicion(mensaje,pos,i):
    row = ""
    for i in range(pos,l,n):
        row += mensaje[i]
    return row

while(a<n):
    a+=1
    cantidad(i)
    pos=posicion(pos)
    message+= transposicion(mensaje,pos,i)

print("Tu mensaje ha sido cifrado con ",n,"filas y ",m,"columnas: ",message)