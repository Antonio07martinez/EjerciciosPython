# Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e imprima por pantalla en líneas distintas el 
# nombre del usuario tantas veces como el número introducido.

def Consola(nombre,veces):
    i = 0;
    while i < veces:
        print('Nombre: '+nombre)
        i += 1
    print('**********************************************')

Consola(
    input('Escribe el nombre: '),
    int(input('Cantidad de veces a escribir: '))
)


#Otro metodo:
#nombre = input("¿Cómo te llamas? ")
#n = input("Introduce un número entero: ")
#print((nombre + "\n") * int(n))