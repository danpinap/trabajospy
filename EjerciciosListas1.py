print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("04/04/2023")
###CURSO DE FUNDAMENTOS DE PYTHON
#1. Crear una lista de numeros del 1 al 5
listnum=[1,2,3,4,5]
#2. Accede al elemto 3 de la lista:
print(listnum.index(3))
#3. Modifica un elemento de la lista:
listnum[4]=6
print(listnum)
#4. Agrega el elemento 9 al final de la lista
listnum.append(9)
print(listnum)
#5. Eliminar el elemento 2 de la lista:
listnum.remove(2)
print(listnum)
#6. Recorrer una lista con un bucle for:
for e in listnum:
    print(e)
#7. Ordenar una lista:
listnum.sort
print(listnum)
listnum.sort(reverse=True) ##este es para ordenar de al reves de mayor a menor.
print(listnum)
#8. Obtener la longitud de una lista:
print(len(listnum))
#9. Comprobar si un elemento está en la lista:
print(9 in listnum)
#otra forma:
if 9 in listnum:
    print('El número 9 está en la lista')
else:
    'El número 9 no está en la lista'

#agregando la solicitud al usuario:
input('Ingrese un número para buscar en la lista: ')
if 9 in listnum:
    print('El número 9 está en la lista')
else:
    'El número 9 no está en la lista'