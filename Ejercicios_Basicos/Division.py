# Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> 
# da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, y <c> 
# y <r> son el cociente y el resto de la división entera respectivamente.

def Division(n,m):
    c = m / n
    r = m - (n * int(c)) #Se le agrego int a cada variable para convertir de un posible valor float a int
    print('Divisor = '+str(n)+'\nDiviendo = '+str(m)+'\nCociente = '+str(int (c))+'\nResto = '+str(r))

Division(
    int(input('Ingresa el divisor: ')),
    int(input('Ingresa el dividiendo: ')))

