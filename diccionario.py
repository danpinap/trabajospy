print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("04/04/2023")
alumnos={'Nombre': 'Juan',
         'Apellido': 'Pérez',
         'Cédula': '1105050775',
         'Dirección': 'Cuenca',
         'E-mail': 'juan@gmail.com'}
print(alumnos)
print(alumnos['Cédula'])
print(alumnos['E-mail'])
alumnos['Cédula']= 1105050772
alumnos['Género']= 'Masculino'
print(alumnos)
instituto={'Carreras': ['Programación', 'BigData', 'Infraestructura', 'DesarrolloAPP', 'Mecatrónica', 'Ciberseguridad'],
           'Materias': ['RedesDatos1', 'LenguageyComunicación', 'Metodología', 'SistemasOperativos', 'ArquitecturadeComputadoras', 'LaboratoriodeInfraestructura', 'SoporteHardwareyAPP.'],
           'Profesores': ['Williams Treslles', 'Hans Ochoa', 'Ana Piedra', 'Adriana Reinoso', 'Mónica Galarza', 'MaBelén Toledo'],
           'Notas': [84, 92, 88, 82, 94, 86]}
print(instituto['Carreras'])
print(instituto['Materias'])
print(instituto['Profesores'])
print(instituto['Notas'])
promedio=0
suma=0
for e in instituto['Notas']:
    suma=suma+e
promedio=suma/len(instituto['Notas'])
print(promedio)
#otra forma de hacer...
print(sum(instituto['Notas'])/len(instituto['Notas']))
#otro metodo para hacer....
suma=0
for e in instituto['Notas']:
    suma+=float(e)
print(suma/len(instituto['Notas']))
###Para redondear decimales le podemos agregar el operador round previo la operacion.
print(round(suma/len(instituto['Notas']),2))
#usar el min y max para obtener minimo y maximo valor dentro de una lista.
notaminima=min(instituto['Notas'])
posicion=instituto['Notas'].index(notaminima)
print('La nota mínima es ',notaminima, 'en la materia de ',instituto['Materias'][posicion],' con la docente ',instituto['Profesores'][posicion])