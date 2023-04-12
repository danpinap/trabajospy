print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("11/04/2023")
###CURSO DE FUNDAMENTOS DE PYTHON
#Trabajar los ejercicios con funciones, para llamarlos deberá de crear un menu en el que le permitira seleccionar al usuario que ejercicios ejecutar.
#1. Suma de elementos de una lista: Dada una lista de números, escribe un programa que calcule la suma de todos los elementos de la lista usando un bucle for.
element=[1,2,3,4,5,6,7,8,9,10]
suma=0
for n in element:
    suma+=n
print('La suma de los elemento es: ',+suma)
#2. Contar elementos en una lista: Dada una lista de elementos, escribe un programa que cuente cuántos elementos hay en la lista usando un bucle for.
element1=['mesa','silla','mueble','aparador','butaca']
suma1=0
for e in element1:
    ocurrencia=element1.count(e)
    suma1=suma1+ocurrencia
    print(suma1)
#3. Imprimir elementos de una lista: Dada una lista de elementos, escribe un programa que imprima cada elemento de la lista en una línea separada usando un bucle for.
element2=['mesa','silla','mueble','aparador','butaca']
for e in element2:
    print(e)
#4. Contar caracteres en una cadena: Dada una cadena de caracteres, escribe un programa que cuente cuántos caracteres hay en la cadena usando un bucle for.
element3=['mesa','silla','mueble','aparador','butaca']
totcarac=0
for c in element3:
    totcarac+=len(c)
print(totcarac)
#5. Imprimir caracteres de una cadena: Dada una cadena de caracteres, escribe un programa que imprima cada carácter de la cadena en una línea separada usando un bucle for.
caract=('¡Que viva Cuenca!')
for c in caract:
    print(c)
#6. Imprimir los primeros N números naturales: Dado un número entero N, escribe un programa que imprima los primeros N números naturales usando un bucle for.
for n in range(0,999):
    if n<=10:
        print(n)
#7. Imprimir los primeros N números pares: Dado un número entero N, escribe un programa que imprima los primeros N números pares usando un bucle for.
for n in range(0,11):
    if n%2==0:
        print(n)
#8. Imprimir los primeros N números impares: Dado un número entero N, escribe un programa que imprima los primeros N números impares usando un bucle for.
for n in range(0,11):
    if n%2==1:
        print(n)
#9. Imprimir la tabla de multiplicar de un número: Dado un número entero N, escribe un programa que imprima la tabla de multiplicar de N usando un bucle for.
dato=int(2)
for m in range(0,11):
    multip=m*dato
    print(f'El {m} x el {dato} es gual a: {multip}')
#10. Imprimir los primeros N números de la serie de Fibonacci: Dado un número entero N, escribe un programa que imprima los primeros N números de la serie de Fibonacci usando un bucle for.
def fibonacci_iter(d):
    n1=1
    n2=1
    if d==1:
        print('0')
    elif d==2:
        print('0','1')
    else:
        print('0')
        print(n1)
        print(n2)
        for i in range(n-3):
            total=n1+n2
            n2=n1
            n1= total
            print(total)
         
fibonacci_iter(8)