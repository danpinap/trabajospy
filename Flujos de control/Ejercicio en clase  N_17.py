print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("31/03/2023")
#Ejercicio 17
#Escribir un programa que pida al usuario una nota del 0 al 10 y
#muestre por pantalla la calificación según la siguiente tabla.
#ver tabla documento fundamento pyton.
nota=float(input('Ingrese su calificación de 1 a 10 a continuación\n'))
if nota>=0 and nota<=2:
    print('Su calificación es Muy deficiente')
elif nota>=3 and nota<=4:
    print('Su calificación es Insuficiente')
elif nota>=5 and nota<=6:
    print('Su calificación es Suficiente')
elif nota==7:
    print('Su calificación es Buena')
elif nota>=8 and nota<=9:
    print('Su calificación es Notable')
elif nota==10:
    print('Su calificación es Sobresaliente')
else:
    print('Error en dato ingresdo')