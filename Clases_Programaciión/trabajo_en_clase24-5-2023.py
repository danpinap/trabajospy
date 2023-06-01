#programa que detemine si una persona es mayor de edad.
#declaro la variable y recibo edad:
edad=int(input('Ingrese su edad: '))
#validar si la edad es mayor o igual que 18:
if edad>=18:
    print('Felicidades eres mayor de edad!!!')#imprimo el mensaje

#si una persona se llama juan:
nombre=input('Ingrese su nombre: ')
#hago la comparación:
if nombre=='juan':
    print('hola juan')
else:
    print('Este programa lo usa solo juan')

#programa para saber si una persona es mayor o menor de edad.
#declaro la variable y recibo edad:
edad=int(input('Ingrese su edad: '))
#validar si la edad es mayor o igual que 18:
if edad>=18:
    print('Ud es mayor de edad')#imprimo el mensaje
else:
    print('Ud no es mayor de edad')

#Calculadora
print('Menú')
print('1. Suma 2. Resta 3. Multiplicación 4. División')
opcion=int(input('Seleccione una opción: '))
if opcion==1:#Compruebo si eligió suma.
    num1=float(input('Ingrese el primer número: '))
    num2=float(input('Ingrese el segundo número: '))
    suma=num1+num2
    print('El resultado de la suma es: ',suma)
elif opcion==2:#Compruebo si eligió resta.
    num1=float(input('Ingrese el primer número: '))
    num2=float(input('Ingrese el segundo número: '))
    resta=num1-num2
    print('El resultado de la resta es: ',resta)
elif opcion==3:#Compruebo si eligió Multiplicación.
    num1=float(input('Ingrese el primer número: '))
    num2=float(input('Ingrese el segundo número: '))
    multiplicación=num1*num2
    print('El resultado de la multiplicación es: ',multiplicación)
elif opcion==1:#Compruebo si eligió división.
    num1=float(input('Ingrese el primer número: '))
    num2=float(input('Ingrese el segundo número: '))
    division=num1+num2
    print('El resultado de la division es: ',division)
else:
    print('La opción ingresada es incorrecta.')

'''Resolver el ejercicio: Los putos que obtienen los alumnos son de 0.0
a 10. Reprobado 0.0 - 5.99, Suficiente 6.0 - 7.99, Bien 8.0 - 9.48 y
sobresaliente 9.5-10. Alumnos con sobresaliente recibirán un incentivo
económico del 65% de un salario básico unificado ($425). Escribir un
programagrama que lea la calificación del alumno e indique su nivel de
rendimiento, y la cantidad de dinero que recibirá (en caso de no recibir
incentivo también indicarlo).'''
#Solicitar nota:
nota=float(input('Ingrese su nota: '))
if nota>=0.00 and nota<6:
    print('Su nivel de rendimiento es Reprobado por tanto no recibirá el incentivo.')
elif nota>=6.00 and nota<8:
    print('Su nivel de rendimiento es Suficiente, pero no recibirá el incentivo.')
elif nota>=8.00 and nota<9.50:
    print('Su nivel de rendimiento esta Bien, pero no recibirá el incentivo.')
elif nota>=9.50 and nota<10:
    incent=425*(65/100)
    print('Su nivel de rendimiento es Sobresaliente, recibirá un incentivo de: ${}'.format(incent))
else:
    print('La nota ingresada es incorrecta!!')
    