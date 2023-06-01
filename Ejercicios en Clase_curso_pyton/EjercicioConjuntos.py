print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("10/04/2023")
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE CONJUNTOS
#Crear un conjunto con los números del 1 al 10 e imprimirlo en pantalla.
numeros={1,2,3,4,5,6,7,8,9,10}
print(type(numeros))
print(numeros)
#Crear dos conjuntos, uno con los números pares del 1 al 10 y otro con los impares del 1 al 10. Luego, imprimir los conjuntos y la intersección entre ellos.
pares=set()
impares=set()
for p in numeros:
    if p%2==0:
        pares.add(p)
    elif p%2!=0:
        impares.add(p)
    else:
        print('error')
print(pares, impares)
print(pares.intersection(impares))
#Crear un conjunto con los elementos "manzana", "banana" y "naranja". Luego, pedirle al usuario que ingrese un elemento y determinar si ese elemento se encuentra en el conjunto o no.
frutas={'manzana','banana','naranja'}
elemento=set()
dato=input('Ingrese el un elemento que desea comprobar\n''si se encuentra detro del conjunto frutas: ')
elemento.add(dato)
if elemento.issubset(frutas)==True:
    print('El elemento {}, está dentro del conjunto frutas'.format(dato))
else:
    print('El elemento {}, no está dentro del conjunto frutas'.format(dato))
#Crear un conjunto con los números del 1 al 5 y otro con los números del 4 al 8. Luego, unir los conjuntos y eliminar los elementos repetidos. Finalmente, imprimir el conjunto resultante.
a={1,2,3,4,5}
b={4,5,6,7,8}
c=a|b #uso del operador de union.
#c1=set()
#a.union(b)==c1#uso metodo union.
d=(a.intersection(b))
for e in d:
    c.discard(e)
print(c)
#Crear un conjunto con los elementos "leche", "pan", "huevos" y "azúcar". Luego, eliminar el elemento "azúcar" del conjunto y agregar el elemento "harina". Finalmente, imprimir el conjunto resultante.
alimentos={'leche','pan','huevos','azucar'}
alimentos.discard('azucar')
alimentos.add('harina')
print(alimentos)
#Crear un conjunto con los nombres "Juan", "María", "Pedro" y "Luisa". Luego, imprimir el número de elementos del conjunto.
nombres={'Juan','María','Pedro','Luisa'}
print(len(nombres))
#Crear dos conjuntos, uno con los números del 1 al 5 y otro con los números del 4 al 8. Luego, imprimir los conjuntos y la diferencia simétrica entre ellos.
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a, b, a.symmetric_difference(b))
#Crear un conjunto con los números del 1 al 10 y otro con los números del 5 al 15. Luego, imprimir los conjuntos y la unión entre ellos.
num1={1,2,3,4,5,6,7,8,9,10}
num2={5,6,7,8,9,10,11,12,13,14,15}
print(num1, num2, num1.union(num2))
#Crear un conjunto con los elementos "manzana", "banana", "naranja" y "pera". Luego, imprimir los elementos del conjunto en orden alfabético.
frutas0={'manzana','banana','naranja','pera'}
frutas1=sorted(frutas0)
print(frutas1)
#Crear un conjunto con los números del 1 al 10 y otro con los números del 6 al 15. Luego, imprimir los conjuntos y la intersección entre ellos.
num3={1,2,3,4,5,6,7,8,9,10}
num4={6,7,8,9,10,11,12,13,14,15}
print(num3, num4, num3.intersection(num4))