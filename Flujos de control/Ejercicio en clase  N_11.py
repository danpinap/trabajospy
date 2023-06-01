print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 11 Determinar el mayor de tres números.
print('Ingrese 3 dígitos a comparar a continuación:')
num1=int(input('1° número: '))
num2=int(input('2° número: '))
num3=int(input('3° número: '))
if num1>num2>num3:
    print(f'El número {num1} es mayor')
elif num1>num3>num2:
    print(f'El número {num1} es mayor')
elif num3>num2>num1:
    print(f'El número {num3} es mayor')
elif num3>num1>num2:
    print(f'El número {num3} es mayor')
elif num2>num1>num3:
    print(f'El número {num2} es mayor')
elif num2>num3>num1:
    print(f'El número {num2} es mayor')