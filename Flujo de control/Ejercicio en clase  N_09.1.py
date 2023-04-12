print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("31/03/2023")
#Ejercicio 09 Calificación de exámen.
#Ingrese la puntuación de un exámen. Si está entre 9.5 a 10 equivale a exelente,
#si está ente 8.5 y 9.5 es muy bueno, si esta entre 7.0 y 8.5 es bueno, y si esta
#entre 4.0 a 7 es regular, finalmente si está ente 0.0 a 4.0  es deficiente.
calif=float(input('Ingrese su puntuacion del exámen: ')) #Calif= calificaciones ingresadas.
if calif>=9.5 and calif<=10:
    print('Su calificación es Exelente')
elif calif>=8.5 and calif<9.50:
    print('Su calificación es Muy Buena')
elif calif>7.0 and calif<8.50:
    print('Su calificación es Buena')
elif calif>4.0 and calif<=7:
    print('Su calificación es Regular')
else:
    print('Su calificación es Deficiente')