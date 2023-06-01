# para comentar 1 línea
''' para comenta más de una linea'''

print('Hola Adrián')
suma=1+2
print('El resultado de la suma es: ')
#También se puede poner junto:
print('El resultado de la suma es: ',suma)
#Asignar a la variable 'a' el valor de 1
a=1
print(a)
#Asignar  a la varible 'a' el valor de 4*3
a=4*3
print(a)
a=8
#Solicitar 5 valores de A hasta B y luego hasignar cumplir
#las condiciones de igualdad descritas en el ejercicio.
A=int(input('Escriva valor varible 1: '))
B=int(input('Escriva valor varible 2: '))
C=int(input('Escriva valor varible 3: '))
D=int(input('Escriva valor varible 4: '))
E=int(input('Escriva valor varible 5: '))
print(A,B,C,D,E) #imprimir los valores originales ingresados.
aux=A
A=E
E=C
C=B
B=D
D=aux
#imprime los cambios de variables
print(A,B,C,D,E)
#Literales
a=int(3)
a=int(input('escriba el valor: '))

b=float(4.5)
b=float(input('escriba el valor: '))

c=input('Escriba algo: ')
c=str(input('escriba algo: '))

d=True
d=False