#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa 
#anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

def Day(day):
    if day > 0 and day < 32 :
        number = [day]
        for num in number:
            date_day = str(num).rjust(2,'0') #Agregar un 0 en la primera posicion de cualquier numero <10
    else:
        date_day = 0
    return date_day

#date_day = Day(input('Day de nacimiento: '))


def Month(month):
    if month > 0 and month < 13:
        number = [month]
        for num in number:
            date_month = str(num).rjust(2,'0')
    else:
        date_month = 0
    return date_month

#date_month = Month(input('Mes de nacimiento: '))

def Year(year):
    if year > 1950 and year < 2022:
        date_year = year
    else:
        date_year = 0000

    return date_year

#date_year = Year(int(input('Año de nacimiento: ')))

def Date(date_day,date_month,date_year):
    if date_month == 1 and date_day < 31:
        print('/DD: '+str(date_day)+'/MM: '+str(date_month)+'/YYYY: '+str(date_year))
    

Date(Day(int(input('Dia de nacimiento: '))),Month(int(input('Mes de nacimiento: '))),Year(int(input('Año de nacimiento: '))))


