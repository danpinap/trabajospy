#---Ejercicios de Tipos de Datos Simples
#Ejercicio 1.- Escriba un progarama que muestre por pantalla la cadena  ¡Hola Mundo!

print('Hola Mundo')

"""Ejercicio 2.- Escriba un progarama que almacene la cadena ¡Hola Mundo! en una variable
y luego muestre por pantalla el contenido"""

saludo='¡Hola Mundo!'
print(saludo)

"""Ejercicio 3.- Escriba un progarama que pregunte el nombre al usuario en la consola y
después de que el usuario lo introduzca muestre por pantalla la cadena ¡Hola <nombre>!,
donde <nombre> es el nombre que el usuario haya introducido"""

nombre=str(input('Ingrese su nombre: '))
print('¡Hola', nombre+'!')

nombre=input('Ingrese su nombre: ')
print(f'¡Hola, {nombre} !' )
"""Ejercicio 4.- Escriba un progarama que muestre por pantalla el resultado de la siguiente
operación aritmética"""

a=16
b=12

#Suma.
print(f'El resultado de sumar, a {a} + {b} es: ',a+b)
#Resta.
print(f'El resultado de restar, a {a} - {b} es: ',a-b)
#Multiplicación.
print(f'El resultado de multiplicar, a {a} * {b} es: ',a*b)
#División.
print(f'El resultado de dividir, a {a} / {b} es: ',a/b)
"""Ejercicio 4.- Escriba un progarama que pregunte al usuario por el número de horas trabajadas
y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

horas=int(input('Ingrese el número de horas trabajadas: '))
val_hora=float(input('Ingrese el coste por hora: '))
paga=horas*val_hora
print('Le corresponde un pago de: ',paga)