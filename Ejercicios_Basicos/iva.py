#Calcular productos con y sin iva dentro de un ciclo

# Productos con IVA
def ConIva(cantidad):
    i = 1;
    sub = 0;
    while (i<=cantidad):
        producto = input('Producto a comprar: ')
        total = Porciento(
            float(input('Precio de '+producto+': ')),
            float(input('Iva de '+producto+': ' ))
        )
        print('Total de '+producto+': '+str(total))
        sub +=total
        i += 1 
    return sub;

#Productos sin IVA
def SinIva(cantidad):
    i = 1;
    sub = 0;
    while(i<=cantidad):
        producto = input('Producto a comprar : ')
        precio = float(input('Precio de '+producto+': '))
        sub += precio
        i += 1
    return sub;
    
    
#Obtener porcentajes de compra
def Porciento(precio,iva):
    iva_pagar = (iva / 100.0)*precio
    total = precio + iva_pagar
    return total

print('----------------------------WELCOME----------------------------')
accion = int(input('1. Comenzar\n2. Salir\n'))
if (accion == 1):
    bandera = True
    while (bandera ==True):
        accion2 = int(input('1. Obtener productos con IVa\n2. Obtener productos sin Iva\n'))
        if (accion2 == 1):
            total_pagar= ConIva(int(input('Productos a comprar: ')))
            print('El total de su compra es de: '+ str(total_pagar))
            action3 = int(input('1. Continuar?\n2. Salir\n'))
            if (action3 == 1):
                bandera = True
            if (action3 == 2):
                print('----------------------------BYE FRIEND----------------------------')
                bandera = False
            if(action3 >= 3 or action3 <=0):
                print('Error de respuesta')
                print('----------------------------BYE FRIEND----------------------------')
                bandera = False
        if (accion2 == 2):
            total_pagar= SinIva(int(input('Productos a comprar: ')))
            print('El total de su compra es de: '+ str(total_pagar))
            action3 = int(input('1. Continuar?\n2.Salir\n'))
            if (action3 ==1):
                bandera = True
            if (action3 == 2):
                print('----------------------------BYE FRIEND----------------------------')
                bandera = False
            if (action3>=3 or action3<=0) :
                print('Error de respuesta')
                print('----------------------------BYE FRIEND----------------------------')
                bandera = False
        if(accion2 >= 3 or accion2 <= 0) :
            print('Error de respuesta')
            print('----------------------------BYE FRIEND----------------------------')
            bandera = False
if (accion == 2):
        print('----------------------------BYE FRIEND----------------------------')
else :
    print('Error de respuesta')
    print('----------------------------BYE FRIEND----------------------------')

    



