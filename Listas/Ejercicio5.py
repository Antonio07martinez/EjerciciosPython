# Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla 
# la frase invertida.

#Primer metodo
def Palabra(palabra):
    sinEspacios = palabra.replace(' ','')
    minusculas = sinEspacios.lower()
    invertida = minusculas[::-1] #Con 4 puntos altera el orden de la palabra, mientras que con dos puntos solo elimina el caracter
    print('La palabra invertida es '+invertida)
    if invertida == minusculas:
        print('La palabra es palindromo')
    else:
        print('No tiene parentesco')

def Palabra2(palabra):
    inversa = ''
    for i in palabra:
        inversa = i + inversa
        print(inversa)


Palabra(input('Escribe una palabra: '))

