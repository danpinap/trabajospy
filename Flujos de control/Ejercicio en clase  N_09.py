print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 09 Calificación de exámen.
#Ingrese la puntuación de un exámen. Si es >= 90 la calificacion
#es A, si es >= 80 la calificación es B, si la calificación es
#>= 70 la calificación es C, si >= 60 la calificación es D, sino
# la calificaciión es F.
calif=int(input('Ingrese su puntuacion del exámen: '))
if calif>= 90:
    print('Su calificación es A')
elif calif>= 80:
    print('Su calificación es B')
elif calif>= 70:
    print('Su calificación es C')
elif calif>= 60:
    print('Su calificación es D')
else:
    print('Su calificación es F')
    