print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("31/03/2023")
#Ejercicio 14
#Programa para determinar si un número es divisible por 4 y 6
num_usr=int(input('Ingrese el número a verificar: '))
if num_usr%4==0:
    print('El número '+str(num_usr)+' es divisible para 4')
elif num_usr%6==0:
    print(f'El número {num_usr} es divisible para 6')
else:
    print('El dato ingresado no es divisible para 4 ó 6')