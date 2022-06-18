# Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde.

def Pagar():
    horas = float(input('Horas trabajadas: '))
    coste = float(input('Coste x hora: '))
    total = horas * coste
    print('Total a pagar es: $'+str(total))

def Obtener():
    pagar = float(input('Total a pagar: '))
    coste = float(input('Coste x hora: '))
    obtener = pagar / coste
    print('Total de horas trabajadas: '+str(obtener))

i=True

while (i):
    res = int(input('Que quieres hacer?\n1. Pagar horas\n2. Saber horas Trabajadas\n3. Salir\n'))
    if res == 1:
        Pagar()
        res2 = int(input('1. Seguir\n2. Salir\n'))
        if res2 == 1:
            i=True
        if res2 == 2:
            print('Gracias...')
            i=False
        if res2 <= 0 or res2 >=3 :
            print('Gracias...')
            i=False

    if res == 2:
        Obtener()
        res2 = int(input('1. Seguir\n2. Salir\n'))
        if res2 == 1:
            i=True
        if res2 == 2:
            print('Gracias...')
            i=False
        if res2 <= 0 or res2 >=3 :
            print('Gracias...')
            i=False

    if res <=0 or res >=3:
        print('Gracias...')
        i=False
        
