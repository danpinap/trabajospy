print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("04/04/2023")
#CURSO DE FUNDAMENTOS DE PYTHON
#EJERCICIOS DE LISTAS A RESOLVER
#Crea una lista vacía llamada numeros e introduce los números del 1 al 5. Luego, muestra la lista por pantalla.
numeros=[1,2,3,4,5]
print(numeros)
#Crea una lista con los nombres de tus amigos y muestra por pantalla el primer elemento de la lista.
nombres=['ismael', 'byron', 'vinicio', 'silvana', 'mayra']
print(nombres[0])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números pares.
listnum=[1,2,3,4,5,6,7,8,9,10]
for e in listnum:
    if e%2==0:
        print(e)
    else:
        print('No es par')
#Crea una lista con los nombres de tus amigos y muestra por pantalla el último elemento de la lista.
nombres=['ismael', 'byron', 'vinicio', 'silvana', 'mayra']
print(nombres[4])
print(nombres[len(nombres)-1]) #Segunda forma de mostrar último elemento de la lista.
#Crea una lista con los números del 1 al 10 y muestra por pantalla el último elemento de la lista.
listnum=[1,2,3,4,5,6,7,8,9,10]
print(listnum[-1])
#Crea una lista con los números del 1 al 10 y muestra por pantalla los números impares.
listnum=[1,2,3,4,5,6,7,8,9,10]
for e in listnum:
    if e%2!=0:
        print(e)
    else:
        print('Es igual')
#Crea una lista con los nombres de tus amigos y añade un nuevo amigo a la lista. Luego, muestra la lista por pantalla.
nombres=['ismael', 'byron', 'vinicio', 'silvana', 'mayra']
nombres.append('marco')
print(nombres)
nombres.insert(2,'Marco') #El método insert permite seleccionar la posición en este caso la 2 y luego de coma el nombre o dato a ingresar.
print(nombres)
#Crea una lista con los números del 1 al 10 y muestra por pantalla el primer y el último elemento de la lista.
listnum=[1,2,3,4,5,6,7,8,9,10]
print(listnum[0]),
print(listnum[-1])
#Crea una lista con los nombres de tus amigos y muestra por pantalla el número de elementos de la lista.
nombres=['ismael', 'byron', 'vinicio', 'silvana', 'mayra','marco']
print(len(nombres))
#Crea una lista con los números del 1 al 10 y muestra por pantalla la suma de todos los elementos de la lista.
listnum=[1,2,3,4,5,6,7,8,9,10]
print(sum(listnum))
listnum1=[1,2,3,4,5,6,7,8,9,10] ## Este es otra forma sin función suma(sum)
suma=0
for e in listnum1:
    suma=suma+e
    print(suma)
#tabién se puede platear de otra manera:
listnum2=[1,2,3,4,5,6,7,8,9,10]
suma1=0
for e in listnum2:
    suma1+=e
    print(suma1)