# Escribir un programa que leea un entero n, introducido por el usuario y después muestre en pantalla la suma
# de todos los enteros desde 1 hasta n, la suma de los n primeros enteros positivos puede ser calculada de la
# siguiente forma: suma=((n(n+1))/2)

#Funciones
def Suma(n):
    res = n*(n+1)
    return res

suma = Suma(float(input('Escribe un numero: ')))

print('El resultado final es: '+str(suma/2))