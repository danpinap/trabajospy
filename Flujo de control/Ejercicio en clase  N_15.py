print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("31/03/2023")
#Ejercicio 15
#Programa para imprimir el día de la semanaa correspondiente a un
#número del 1 al 7.
numseman=input('Seleccione un número del 1 al 7 para visualizar el día de\n'+'la semana correspondiente: ')
if len(numseman)!=1:
    print('El número ingresado no es de un dígito')
elif numseman=='1':
    print('Lunes')
elif numseman=='2':
    print('Martes')
elif numseman=='3':
    print('Miércoles')
elif numseman=='4':
    print('Jueves')
elif numseman=='5':
    print('Viernes')
elif numseman=='6':
    print('Sábado')
elif numseman=='7':
    print('Domingo')
else:
    print('El dato ingresado es incorrecto')