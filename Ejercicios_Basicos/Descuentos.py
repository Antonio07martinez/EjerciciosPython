# Crea el programa que pida el precio de un artículo y el descuento en porcentaje. El
# programa debe mostrar al final el nombre del artículo, le descuento en porcentaje, el
# precio original, el descuento en pesos, el total a pagar.

def Operacion(precio, descuento,producto):
    menos_pagar = (descuento * 0.01)*precio
    pagar = precio - menos_pagar
    print('Precio de '+producto+': $'+str(precio)+' Con descuento de '+str(descuento)+'%')
    print(str(precio)+' - '+str(menos_pagar)+' = '+str(pagar))
    print('---------------------------------------------------------------------------------')

cantidad = (int(input('Cantidad de prendas a comprar: ')))
i=0

while(i<cantidad):
    Operacion(
    float(input('Introduce la cantidad a pagar: $')),
    int(input('Porcentaje de la prenda: ')),
    input('Producto a comprar: '))
    i=i+1
