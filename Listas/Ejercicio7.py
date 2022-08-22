#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte 
#delante de la arroba @) pero con dominio ceu.es.

def Correo(email):
    print(email[:email.find('@')] + '@ceu.es')
      
Correo(input("Introduce tu correo electrónico: "))