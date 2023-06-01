print('INSTITUTO UNIVERSITARIO TECNOLÓGICO DEL AZUAY')
print('PROGRAMACIÓN')
print('Danny Adrián Piña Piña')
print('Recuperación 26-5-2023 UNIDAD 3')

'''Ejercicio1.- Calculadora de operaciones básicas. Realizar una calculadora que permita realizar operaciones básicas.
Suma, Resta, Multiplicación y División.  Realice las comprobaciones necesarias para realizar las operaciones, por
ejemplo: para dividir dos numero debo considerar que el divisor sea diferente de cero.'''
### Calculadora de operaciones básicas ###
print('  CALCULADORA DE OPERACIONES BÁSICAS\n 1. Suma\n 2. Resta\n 3. Multiplicación\n 4. División\n')
opcion=int(input('Digite el número de la operación que desea realizar: '))

if opcion==1:
    num1=float(input('Digite cantidad uno: '))
    num2=float(input('Digite cantidad dos: '))
    suma=num1+num2
    print('El resultado de la suma de los números {} y {} es {}'.format(num1,num2,suma))
elif opcion==2:
    num1=float(input('Digite cantidad uno: '))
    num2=float(input('Digite cantidad dos: '))
    resta=num1-num2
    print('El resultado de la resta de los números {} y {} es {}'.format(num1,num2,resta))
elif opcion==3:
    num1=float(input('Digite cantidad uno: '))
    num2=float(input('Digite cantidad dos: '))
    multiplic=num1*num2
    print('El resultado de la multiplicación de los números {} y {} es {}'.format(num1,num2,multiplic))
elif opcion==4:
    num1=float(input('Digite cantidad uno: '))
    num2=float(input('Digite cantidad dos: '))
    if num1>num2:
        divis=num1/num2
        print('El resultado de la división de los números {} y {} es {}'.format(num1,num2,divis))
    else:
        print(f'El número {num1} no se puede dividir para el número {num2}')
else:
    print('La opción ingresada no es la correcta!!!')