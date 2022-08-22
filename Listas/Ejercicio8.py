#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de 
#céntimos del precio introducido.

import math

def Precio(costo):
    decimal, entero = math.modf(costo)
    print('Entero: {}, Decimal: {}'.format(int(entero),round(decimal,2)))
    
def Stop():
    print('Gracias por participar')
    
i = 0
quest = input('Quieres empezar? ')
if quest == 'si':
    i = 1
    while i == 1:
        Precio(float(input('Introduce el precio del producto: ')))
        quest2 = input('Quieres continuar? ')
        if quest2 == 'si':
            i = 1
        else:
            Stop()
            i = 0
else: 
    Stop()
    i = 0
    