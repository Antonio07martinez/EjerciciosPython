# Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y después 
# muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

def Palabra_Vocal(palabra,vocal):
    mayus = vocal.upper()
    if mayus == 'A' or mayus == 'E' or mayus == 'I' or mayus == 'O' or mayus == 'U':
        print('Palabra: '+palabra+'\nVocal: '+mayus)
        print('*********************************************')
    else:
        print('Error, no selecciono una vocal')

Palabra_Vocal(
    input('Escribe una palabra: '),
    input('Escribe una vocal: ')
)