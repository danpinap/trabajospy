print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("31/03/2023")
#Ejercicio 08.1
#Escribir un programa que pida un número del 0 al 9 y coprobar si es número del 1 al 9.
dato_us=input('Ingrese un número de 0 a 9: ')
if len(dato_us)!=1:
    print('El dato ingresado no es de un dígito.')
elif dato_us in '0123456789':
    print('El número {} ingresado se encuentra dentro del rango.'.format(dato_us))
else:
    print(f'El dato {dato_us} no es un número')