print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("11/04/2023")
###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le 
# permitira seleccionar al usuario que ejercicios ejecutar.
#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero 
# positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada
# número en la pantalla.
fin=int(input('Ingrese número para comenzar cuenta progresiva: '))
inicio=0
conteo=inicio+1
while conteo!=fin: 
    print(conteo)
    conteo+=1
else:
    print('fin conteo')
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero
# positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
fin=0
inicio=int(input('Ingrese número para comenzar cuenta regresiva: '))
conteo=inicio-1
while conteo!=fin: 
    print(conteo)
    conteo-=1
else:
    print('fin conteo')
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positi
# vo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese
# número y lo imprima en la pantalla.
fin=int(input('Ingrese número para suma progresiva: '))
inicio=0
conteo=inicio+1
suma=0
while conteo!=fin:
    conteo+=1
    if conteo>0 and conteo<=fin:
        suma+=suma+1
        print(suma)
else:
    print('fin conteo')
#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y,
# utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla.
# El factorial de un número n se define como el producto de todos los números enteros desde
# 1 hasta n.
factor=1
dato=int(input('Ingrese número para el factorial: '))
while dato!=0:
    factor=factor*dato
    dato=dato-1
print('La respuesta es ',factor)
#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1
# y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al
# número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario
# ingresa un número menor al número generado, el programa debe imprimir "El número que buscas
# es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones,
# adivinaste el número!" y terminar.

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto
# y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para sim
# plificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.

#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero
# positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde
# cero hasta ese número y lo imprima en la pantalla.

#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros
# positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la
# base elevada al exponente y lo imprima en la pantalla.

#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números
# y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la panta
# lla.

#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de 
# texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena.
# Para simplificar el problema, puedes considerar que las palabras están separadas por
# espacios en blanco.
cadena=input('Ingrese su texto para contar las palabras: ')
def contador_palabras(cadena):
    contador=0
    indice=0
    if len(cadena)==0:
        contador=0
    else:
        contador=1
    while indice<cadena:
        if cadena[indice]==' ':
            contador+=1
            indice+=1
    print(contador)