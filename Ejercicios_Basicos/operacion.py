#Escribir un programa que mueste por pantalla el resultado de la siguiente operacion aritmetica ((3+2)/(2.5))^2

#Funciones
#Primer metodo

#def Suma(num1,num2):
#    resultado_suma=num1+num2
#    return resultado_suma

#def Multiplicacion(num3,num4):
#    resultado_multiplicacion=num3*num4
#    return resultado_multiplicacion

#def Division(suma,multiplicacion):
#    resultado_division=suma/multiplicacion
#    return resultado_division

#def Total(division):
#    resultado = division * division
#    print('El total es: '+str(resultado))


#suma = Suma(
#    float(input('Primer valor de Suma: ')),
#    float(input('Segundo valor de Suma: ')))

#multiplicacion = Multiplicacion(
#    float(input('Primer valor de Multiplicacion: ')),
#    float(input('Segundo valor de Multiplicacion: ')))

#division = Division(suma,multiplicacion)
#total = Total(division)

#Segundo metodo

total = (float(input('Num de Suma 1: ')) +  float(input('Num de Suma 2: '))) / (float(input('Num de Multiplicacion 1: ')) *  float(input('Num de Multiplicion 2: ')))
resultado = total * total;
print('El resultado de la operacion es: '+str(resultado))




