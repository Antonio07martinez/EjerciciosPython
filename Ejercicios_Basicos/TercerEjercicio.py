#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario 
# lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!, donde <nombre> es el nombre que el 
# usuario haya introducido.

# Fuction
def people(name,last_name,age,favorite_sport):
    print('---------------------------WELCOME---------------------------')
    print('Hello '+name+' '+last_name)
    print('You are '+str(age)+' and your favorite sport is '+favorite_sport)
    print('------------------------BYE MY FRIEND------------------------')

people(
    input('What is your name?: '),
    input('What is your last name?: '),
    int(input('How are you?: ')),
    input('What is your favorite sport?: '))
