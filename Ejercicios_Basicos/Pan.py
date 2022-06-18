# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
# Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el 
# programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser 
# fresca y el coste final total.

def VentaPan(piezas):
    cantidad = piezas * 3.49
    descuento = cantidad * 0.60
    print('Total de piezas: '+str(piezas)+'\nPrecio a pagar: $'+str(cantidad)+'\nTotal por no ser fresco: $'+str(descuento))

VentaPan(int(input('Cantidad de piezas de pan a comprar: ')))
