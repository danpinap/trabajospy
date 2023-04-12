print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("01/04/2023")
#Ejercicio 20
#Escribir un programa que pregunte al usuario una cantidad de días
#y muestre por pantalla cuantas horas, minutos y segundos hay en
#dicha cantidad de días.
dias=int(input('Ingrese la cantidad de días que desee transformar en:\n'
+'horas, minutos y segundos.\n'))
horas=dias*24
minutos=horas*60
segundos=minutos*60
print(f'La cantidad de días {dias} que ingresó son equivalentes a:\n')
print('{} horas, {} minutos y {} segundos'.format(horas,minutos,segundos))