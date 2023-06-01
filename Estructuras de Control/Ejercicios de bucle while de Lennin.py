print('CURSO DE FUNDAMENTOS DE PYTHON')
print('NOMBRE:LENIN CASTRO')
print('Fecha:10/04/2023 ')




#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1.Contador ascendente: # Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde cero hasta ese número, imprimiendo cada número en la pantalla.

def ascendente(num):
    cont=0
    while cont<= num:
        print(cont)
        cont+=1

#2.Contador descendente: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, cuente desde ese número hasta cero, imprimiendo cada número en la pantalla.
def descendente(num):
    while num>=0:
        print(num)
        num-=1


#3.Suma de números: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números desde cero hasta ese número y lo imprima en la pantalla.
def suma(numero):
    sumatoria=0
    cont=0
    while cont<=numero:
        sumatoria+=cont
        cont+=1
    return sumatoria  


#4.Factorial: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule el factorial de ese número y lo imprima en la pantalla. El factorial de un número n se define como el producto de todos los números enteros desde 1 hasta n.
def factorial(num):
    if num < 0:
        print("No existe el factorial de un numero negativo.")
        return 1
    elif num == 0:
        return 1
    else:
        fact = 1
        while(num > 1):
            fact *= num
            num -= 1
        return fact


#5.Adivinar un número: Escribe un programa en Python que genere un número aleatorio entre 1 y 100, y pida al usuario que adivine ese número. Si el usuario ingresa un número mayor al número generado, el programa debe imprimir "El número que buscas es menor". Si el usuario ingresa un número menor al número generado, el programa debe imprimir "El número que buscas es mayor". Si el usuario adivina el número, el programa debe imprimir "¡Felicitaciones, adivinaste el número!" y terminar.
import random
def adivinar(aleatorio):
    numero=0
    while numero!=aleatorio:
        numero=int(input('Ingrese un número del 1 al 10: '))
        if numero > aleatorio:
            print('El numero buscado es mayor al numero a adivinar')
        elif numero< aleatorio:
            print('El numero buscado es menor al numero a adivinar')
        else:
            print('Felicidades adivino el número',numero)

#6.Contador de vocales: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de vocales que tiene esa cadena. Para simplificar el problema, puedes considerar que la cadena solo contiene letras minúsculas.
def vocales(texto):
    contador_vocales = 0
    i = 0 
    while i < len(texto):
        if texto[i].lower() in "aeiou":# Si la letra es una vocal, sumamos 1 al contador de vocales
            contador_vocales+= 1
        i+=1
    return contador_vocales

#7.Suma de números pares: Escribe un programa en Python que pida al usuario un número entero positivo y, utilizando un bucle while, calcule la suma de todos los números pares desde cero hasta ese número y lo imprima en la pantalla.
def suma_pares(numero):
    sumatoria=0
    contador=0
    while contador<=numero:
        if contador%2==0:
            sumatoria+=contador
        contador+=1
    return sumatoria 


#8.Cálculo de potencia: Escribe un programa en Python que pida al usuario dos números enteros positivos: una base y un exponente. Utilizando un bucle while, calcule la potencia de la base elevada al exponente y lo imprima en la pantalla.
def potencia(numero,exponente):
    resultado=1
    contador=1
    while contador<= exponente:
        resultado*=numero
        contador+=1
    return resultado
numero=int(input('Ingrese la base es decir un numero: '))
exponente=int(input('Ingrese el exponente al que va a elevar su base: '))
print('Su base',numero,'elevado al exponente',exponente,'=',potencia(numero,exponente))






#9.Cálculo de promedio: Escribe un programa en Python que pida al usuario una lista de números y, utilizando un bucle while, calcule el promedio de esos números y lo imprima en la pantalla.
def promedio(valores):
    sumatoria=0
    contador=0
    while contador<len(valores):
        sumatoria=sumatoria+int(valores[contador])
        contador+=1
    print(sumatoria/len(valores))



#10.Contador de palabras: Escribe un programa en Python que pida al usuario una cadena de texto y, utilizando un bucle while, cuente la cantidad de palabras que tiene esa cadena. Para simplificar el problema, puedes considerar que las palabras están separadas por espacios en blanco.
def palabras(cadena):
    contador=0
    indice=0
#Si la cadena esta vacía, no hay palabra que contar
    if len(cadena)==0:
        contador=0
    else:
#Si no esta vacia el contador incrementa en uno.
        contador+=1
    while indice<len(cadena):
        if cadena[indice]==' ':
            contador+=1
        indice+=1
    print('La cadena de texto tiene',contador,'palabras')
cadena=input('Ingrese una cadena de texto separados por espacios: ')
palabras(cadena)









opcion=1
while opcion>0 and opcion<=10:
    print('\tMenú de Opciones\n1.Contador Ascendente\n2.Contador Descendente\n3.Suma de numeros\n4.Factorial\n5.Adivinar un número\n6.Contador de vocales\n7.Suma de números pares\n8.Cálculo de Potencia\n9.Cálculo de promedio\n10.Contador de palabras\n0.Salir')
    opcion=int(input('Ingrese una de las opciones del menú: '))
    if opcion==0:
        print('Gracias por su tiempo')
        break
    elif opcion==1:
        print('Contador Ascendente')
        num=int(input('Ingrese un número porfavor: '))
        ascendente(num)
    elif opcion==2:
        print('Contador Descendente')
        num=int(input('Ingrese un número porfavor: '))
        descendente(num)
    elif opcion==3:
        print('Suma de numeros')
        numero=int(input('Ingrese un número: '))
        print('La suma total de su numero es',suma(numero))
    elif opcion==4:
        print('Factorial')
        numero=int(input('Ingrese un numero para calcular el factorial: '))
        print(factorial(numero))
    elif opcion==5:
        print('Adivinar un número')
        aleatorio=random.randint(1,10)
        adivinar(aleatorio)
    elif opcion==6:
        print('Contador de vocales')
        texto = input("Ingresa una cadena de texto en minúsculas: ")
        print('Su texto tiene',vocales(texto),'vocales')
    elif opcion==7:
        print('Suma de números pares')
        numero=int(input('Ingrese un número: '))
        print('De el número',numero,'que ingreso solo se sumo los pares =',suma_pares(numero))
    elif opcion==8:
        print('Cálculo de potencia')  
    elif opcion==9:
        print('Cálculo de promedio')
        valores=input('Ingrese los números separados por coma: ').split(',')
        promedio(valores)
    elif opcion==10:
        print('Contador de palabras')
    

