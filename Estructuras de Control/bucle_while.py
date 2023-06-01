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
def cont_ascend(fin):
    inicio=0
    conteo=inicio+1
    while conteo!=fin: 
        print(conteo)
        conteo+=1
    else:
        print('fin conteo')
#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero
# positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def cont_descend(inicio):
    fin=0
    conteo=inicio-1
    while conteo!=fin: 
        print(conteo)
        conteo-=1
    else:
        print('fin conteo')
#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positi
# vo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese
# número y lo imprima en la pantalla.
def suma_progresiva(fin):
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
def factorial(dato):
    factor=1
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
import random
def adivinar_num(randomizado):
    num=0
    while num!=randomizado:
        num=int(input('Digite un número del 1 al 100: '))
        if num > randomizado:
            print('El número {} es mayor, intente con otro mas bajo'.format(num))
        elif num< randomizado:
            print('El número {} es menor, intente con otro mas alto'.format(num))
        else:
            print('Felicidades adivino el número',num)
#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de cadena
# y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para sim
# plificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def cont_vocales(cadena):
    conteo_vocales = 0
    a = 0 
    while a < len(cadena):
        if cadena[a].lower() in "aeiou":# Si la letra es una vocal, sumamos 1 al contador de vocales
            conteo_vocales+= 1
        a+=1
    return conteo_vocales
#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero
# positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde
# cero hasta ese número y lo imprima en la pantalla.
def suma_pares(num):
    sumatoria=0
    contador=0
    while contador<=num:
        if contador%2==0:
            sumatoria+=contador
        contador+=1
    return sumatoria 
#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros
# positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la
# base elevada al exponente y lo imprima en la pantalla.
def potencia(base,expon):
    respuesta=1
    contador=1
    while contador<= expon:
        respuesta*=base
        contador+=1
    return respuesta
#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números
# y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la panta
# lla.
def promedio(valores):
    sumatoria=0
    contador=0
    while contador<len(valores):
        sumatoria=sumatoria+int(valores[contador])
        contador+=1
    print(sumatoria/len(valores))
#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de 
# cadena y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena.
# Para simplificar el problema, puedes considerar que las palabras están separadas por
# espacios en blanco.

def contador_palabras(cadena):
    contador=0
    indice=0
    if len(cadena)==0:
        contador=0
    else:
        contador>0
    while indice<cadena:
        if cadena[indice]==' ':
            contador+=1
            indice+=1
            print('La cadena de cadena tiene',contador,'de palabras.')
    

#### MI MENÚ DE OPCIONES ####
menu=True ##Bandera es solo un nombre cualquiera de variable
while menu:
    print(('MENÚ DE OPCIONES'))
    print('1. Conteo Ascendente.')
    print('2. Conteo Descendente.')
    print('3. Suma de Números.')
    print('4. Factorial de un Número.')
    print('5. Adivinar un Número ente 1 y 100.')
    print('6. Contador de Vocales.')
    print('7. Suma de Números Pares')
    print('8. Cálculo de Potencias.')
    print('9. Cálculo de Promedio.')
    print('10 Contador de Palabras.')
    print('0. Salir del Menú.')
    opcion=int(input('Digite una opción:'))
    if opcion ==0:
        menú=False
        print('Gracias por interactuar.')
    if opcion ==1:
        fin=int(input('Digite número para comenzar cuenta progresiva: '))
        cont_ascend(fin)
    elif opcion ==2:
        inicio=int(input('Digite número para comenzar cuenta regresiva: '))
        cont_descend(inicio)
    elif opcion ==3:
        fin=int(input('Digite número para suma progresiva: '))
        suma_progresiva(fin)
    elif opcion ==4:
        dato=int(input('Digite número para el factorial: '))
        factorial(dato)
    elif opcion ==5:
        randomizado=random.randint(1,100)
        adivinar_num(randomizado)
    elif opcion ==6:
        cadena = input("Digite un texto solo con letras minúsculas: ")
        print('Su cadena tiene',cont_vocales(cadena),'vocales')
    elif opcion ==7:
        num=int(input('Digite un número: '))
        print('La suma de los números pares es: ',suma_pares(num))
    elif opcion ==8:
        base=int(input('Digite el número que será la base: '))
        expon=int(input('Digite el número de la potencia a la que desea elevar: '))
        print('El número ',base,' elevado al exponente ',expon,' es igual a ',potencia(base,expon))
    elif opcion ==9:
        valores=input('Ingrese los números separados por coma: ').split(',')
        promedio(valores)
    elif opcion ==10:
        cadena=input('Digite su cadena para contar las palabras: ')
        contador_palabras(cadena)
    else:
        print('La opción ingresada es incorrecta. ')
        break