#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el 
# capital obtenido en la inversión.

def Operacion(cantidad,interes,años):
    porcentaje = interes * 0.01
    anual = porcentaje * cantidad
    total = cantidad - (anual * años)
    print('\n-------------------------------------------------------------- WELCOME ------------------------------------------')
    print('Inversion de: $'+str(cantidad)+'\nInteres anual: '+str(interes)+'%\nDescuento por año: -$'+str(anual)+'\nTotal de: $'+str(total))
    print('\n---------------------------------------------------------------- BYE --------------------------------------------')

Operacion(
    float(input('Cantidad a invertir: $')),
    int(input('Porcentaje de interes anual: %')),
    int(input('Total de años a usar: ')),
)

