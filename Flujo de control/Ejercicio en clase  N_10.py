print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 10 Determinar si un año es bisiesto.
#Es divisible entre 4, pero no es divisible entre 100. Es divisible entre 400.
añobis=int(input('Ingrese el año a evaluar: '))
if añobis%4==0:
    print('El año {} es bisiesto'.format(añobis))
else:
    print(f'El año {añobis} no es un año bisiesto')