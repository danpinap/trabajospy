#Ejemplo 1.- imprimir los numeros del 1 a 3.
x=1
while x<=3:
    print(x)
    x=x+1 # tambén se puede poner x=+1
print('fin del programa')

#Ejemplo 2.- Pedir un número positivo una y otra vez hasta que ingrese correctamente.
num=int(input('Ingrese un número positivo: '))
while num<0:
    print('número incorrecto')
    num=int(input('Ingrese un número positivo: '))
print('gracias')

#Ejemplo 3.- Escriba SI para continuar

x=input('Escriba si, si desea seguir ejecutando el programa: ')
while x=='si':
    print('¿Desea seguir ejecutando el programa? ')
    x=input('Escriba si, si desea seguir ejecutando el programa: ')
print('Ha decidido salir...\n Hasta la vista!!!')

#
contraseña=input('Ingrese la constraseña: ')
repite_contraseña=input('Ingrese la contraseña otra vez: ')
while contraseña!=repite_contraseña:
    repite_contraseña=input('Ingrese la contraseña otra vez: ')
print('Las contraseñas son iguales')