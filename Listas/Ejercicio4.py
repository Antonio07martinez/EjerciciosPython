# Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el 
# código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un 
# programa que pregunte por un número de teléfono con este formato y muestre por pantalla el número de 
# teléfono sin el prefijo y la extensión.

tel = input('Escribe el numero telefonico con prefijo y extension: ')
inicio = tel[3:] #Eliminara los tres primeros digitos de la cadena
fin = inicio[:-2] #Eliminara los ultimos dos digitos de la cadena
print('Numero sin prefijo ni extencion: '+fin)

#Ota forma:
tel = input("Introduce un número de teléfono con el formato +xx-xxxxxxxxx-xx: ")
print('El número de teléfono es ', tel[4:-3])