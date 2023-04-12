print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print('08/04/2023')
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#1.Crea un diccionario vacío y agrega tres elementos de la siguiente forma: 'clave': valor
diccio0=dict()
diccio0['1501095408']='Pizango Jhordan'
diccio0['0105410211']='Christian Preciado'
diccio0['0106605017']='Astudullo Carlos'
print(diccio0)
#2.Dado el siguiente diccionario:
personas={'Juan':28,'María':20,'Pedro':32,'Ana':25}
print(type(personas))
#a) Imprime la edad de Juan.
print(personas['Juan'])
#b) Agrega un nuevo elemento al diccionario con la clave 'Luis' y la edad 18.
personas['Luis']=18
print(personas)
#c) Elimina el elemento con la clave 'Pedro'.
personas.pop('Pedro')
print(personas)
#3.Dado el siguiente diccionario:
ventas = {'manzanas': 10, 'naranjas': 5, 'peras': 8}
#a) Imprime la cantidad de manzanas vendidas.
print(ventas['manzanas'])
#b) Agrega 3 elementos más al diccionario: 'limones': 12, 'sandías': 3, 'melones': 5.
ventas['limones']=12
ventas['sandías']=3
ventas['melones']=5
#c) Imprime las claves del diccionario.
print(ventas.keys())
#4. Dado el siguiente diccionario:
alumnos = {'Juan': {'edad': 22, 'promedio': 8.5}, 'María': {'edad': 20, 'promedio': 9.0}, 'Pedro': {'edad': 25, 'promedio': 7.5}}
#a) Imprime la edad de Juan.
print(alumnos['Juan']['edad'])
#b) Imprime el promedio de María.
print(alumnos['María']['promedio'])
#c) Agrega un nuevo elemento al diccionario con la clave 'Ana' y los valores 'edad': 19 y 'promedio': 8.0.
alumnos['Ana']={'edad':19, 'promedio':8.0}
print(alumnos)
#5. Dado el siguiente diccionario:
empleados = {'Juan': {'departamento': 'Ventas', 'sueldo': 1500}, 'María': {'departamento': 'Contabilidad', 'sueldo': 1800}, 'Pedro': {'departamento': 'Ventas', 'sueldo': 1700}, 'Ana': {'departamento': 'Recursos Humanos', 'sueldo': 1900}}
#a) Imprime el sueldo de Pedro.
print(empleados['Pedro']['sueldo'])
#b) Cambia el sueldo de Ana a 2000.
empleados['Ana']={'departamento': 'Recursos Humanos', 'sueldo': 2000}
print(empleados['Ana']['sueldo'])
#c) Crea un nuevo diccionario con los empleados del departamento de Ventas.
dicventas=dict()
for c,v in empleados.items():
    for a,b in v.items():
        if b=='Ventas':
            dicventas[c]={a:b}
print(dicventas)
#6.Dado el siguiente diccionario:
cursos = {
    'Pedro': ['Matemáticas', 'Biología', 'Historia'],
    'María': ['Física', 'Química', 'Literatura']
}
#a) Imprime las materias en las que está inscrito Pedro.
print(cursos['Pedro'])
#b) Agrega una materia más a la lista de materias de María: 'Programación'.
cursos['María'].append('Programación')
print(cursos['María'])
#c) Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
dicbiol={}
for k,w in cursos.items():
     if 'Biología' in w:
         dicbiol[k]=w
print(dicbiol)
#7. Dado el siguiente diccionario:
productos = {'manzanas': 2.99, 'naranjas': 1.99, 'peras': 3.99, 'uvas': 4.99, 'kiwis': 0.99, 'duraznos': 2.49}
stock = {'manzanas': 100, 'naranjas': 50, 'peras': 25, 'uvas': 75, 'kiwis': 200, 'duraznos': 60}
#a) Imprime el precio de las naranjas.
print(productos['naranjas'])
#b) Cambia el stock de peras a 12.
stock.update({'peras': 12})
print(stock)
#c) Crea una función que calcule el valor total de los productos en el diccionario.
sumprecio=0
sumcant=0
for f,p in productos.items():
    sumprecio+=p
for n,o in stock.items():
    sumcant+=o
total=sumprecio*sumcant
print(f'El valor total de los productos es: {total}')
