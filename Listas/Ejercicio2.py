# Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por
# pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra con todas 
# las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en mayúscula. El 
# usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

#name = input('Write your name: ')
#last_name = input('Write your last name: ')
#print('Name with Upper: '+name.upper()+' '+last_name.upper())
#print('Name with Lower: '+name.lower()+' '+last_name.lower())
#print('Name: '+name.capitalize()+' '+last_name.capitalize())
#print('********************************************************************')

#Otro metodo
name = input("¿Cómo te llamas? ")
print(name.lower())
print(name.upper())
print(name.title()) #Para convertir un texto a formato titulo utiliza el metodo title(). title() convierte
# la primera letra de cada palabra de una cadena a mayusculas
