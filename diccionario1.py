print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("07/04/2023")
#CURSO DE FUNDAMENTOS DE PYTHON 
#EJERCICIOS DE DICCIONARIOS
#Crear un diccionario vacío:
dicvacio={}
alumnos=dict()
#Agregar elementos a un diccionario:
alumnos['0106663792']= 'Juan Bravo'
alumnos['1105050775']= 'Veronica Chimbo'
alumnos['0107050270']= 'Antoni Mejia'
alumnos['1501095408']= 'Pizango Jhordan'
alumnos['0105410211']= 'Christian Preciado'
alumnos['0106605017']= 'Astudullo Carlos'
alumnos['0106767007']= 'Bruce Willis'
alumnos['0105737365']= 'Stallin Barbecho'
alumnos['0954337572']= 'Torres Eudyn'
alumnos['0106637150']= 'Paredes Jennifer'
alumnos['0150564078']= 'Danny Alex'
alumnos['0105041982']= 'Adrian Piña'
alumnos['0106399041']= 'Jacqueline Tenesaca'
alumnos['0150474021']= 'David Ñauta'
alumnos['0107270282']= 'Edwin Arroyo'
alumnos['0107416927']= 'José Muñoz'
alumnos['0150578094']= 'Nayeli Gallegos'
alumnos['1105050775']= 'Gabriela Lopez'
print(alumnos)
#Acceder a un valor en un diccionario:
print(alumnos['1105050775'])
#Verificar si una llave existe en un diccionario:
print(alumnos.get('0106767007'))
#Eliminar un elemento de un diccionario:

#Imprimir las llaves de un diccionario:
print(alumnos.keys())
#Imprimir los valores de un diccionario:
print(alumnos.values())
#Imprimir las llaves y valores de un diccionario:
for c,v in alumnos.items():
    print(c,v) 