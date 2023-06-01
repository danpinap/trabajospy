print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print('07/04/2023')
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE TUPLAS
#Crear una tupla vacía:
tupvacia=()
print(type(tupvacia))
tupvacia1=tuple
print(tupvacia1)
#Crear una tupla con algunos elementos:
elementos=('La Divina Comedia','Hamlet','La Biblia','La Eneida')
#Acceder a un elemento de la tupla:
print(elementos[2])
#Intentar modificar un elemento de la tupla (esto producirá un error ya que las tuplas son inmutables):
elementos[2]='Necromicón'
#Concatenar dos tuplas:
elementos=('La Divina Comedia','Hamlet','La Biblia','La Eneida')
edades=(31, 8, 4, 19, 23, 12, 17, 21, 35)
elemyedad=elementos+edades
print(elemyedad)
#Obtener la longitud de una tupla:
edades=(31, 8, 4, 19, 23, 12, 17, 21, 35)
print(len(edades))
#Convertir una tupla en una lista:
elementos=('La Divina Comedia','Hamlet','La Biblia','La Eneida')
print(type(elementos))
elementoslist=list(elementos)
print(type(elementoslist))
#Convertir una lista en una tupla:
print(elementoslist)
elemtup=tuple(elementoslist)
print(type(elemtup))
