print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print('07/04/2023')
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla de números enteros y calcular su suma y promedio.
nument=(31,37,8,4,19,23,24)
print(type(nument))
suma=0
promedio=0
for t in nument:
    suma+=t
    promedio=suma/len(nument)
print('La suma es: {} y el promedio es: {}'.format(suma,promedio))
#Crear dos tuplas de la misma longitud y crear una nueva tupla que contenga la suma de los elementos correspondientes de ambas tuplas.
tup1=(31,37,8,4,19,23,24)
tup2=(1,12,17,21,30,35,42)
tup1_2=tup1+tup2
print(tup1_2)
#Crear una tupla de nombres y ordenarla alfabéticamente.
tupnom=('Mayra','Valentina','Adrián','Danny')
listupnom=list(tupnom)
listupnom.sort()
tupnomord=tuple(listupnom)
print(type(tupnomord))
print(tupnomord)
#Crear una tupla de números y encontrar el valor mínimo y máximo.
tup1_2=(31, 37, 8, 4, 19, 23, 24, 1, 12, 17, 21, 30, 35, 42)
valmin=min(tup1_2)
print(valmin)
valmax=max(tup1_2)
print(valmax)
#Crear una tupla de números y convertirla en una lista.
nument1=(31, 8, 4, 19, 23, 24, 12, 17, 21, 35)
print(type(nument1))
nument1alist=list(nument1)
print(type(nument1alist))
#Crear una tupla con los días de la semana y mostrar el tercer elemento.
dias=('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
print(dias[2])
#Crear una tupla con números enteros y mostrar aquellos que son pares.
nument2=(31, 8, 4, 19, 23, 24, 12, 17, 21, 35)
for n in nument2:
    if n%2==0:
        print(n)
#Crear una tupla con los meses del año y mostrar aquellos que tienen más de cinco letras.
meses=('enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre')
for l in meses:
    if len(l)>=5:
        print(l)
#Crear una tupla con las edades de varias personas y mostrar la cantidad de personas mayores de 18 años.
edades=(31, 8, 4, 19, 23, 12, 17, 21, 35)
for e in edades:
    if e>18:
        print(e)
#Crear una tupla de tuplas que contienen información de libros y mostrar el título del tercer libro.
libros=(('El Quijote','La Odisea','La Ilíada'),('La Divina Comedia','Hamlet','La Biblia','La Eneida'),('En Busca del tiempo perdido','Ensayos','Madame Bovary'))
print(type(libros))
print((libros[0][2]))