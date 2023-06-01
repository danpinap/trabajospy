print('INSTITUTO UNIVERSITARIO TECNOLÓGICO DEL AZUAY')
print('PROGRAMACIÓN')
print('Danny Adrián Piña Piña')
print('PORTAFOLIO DE EJERCICIOS UNIDAD 2') 
'''Ejercicio 4.- Juan es un vendedor en una tienda de tecnología en donde
tiene un sueldo base y se lleva una comisión del 10% de las ventas que
realice. Pedir por teclado el sueldo base del comerciante y el valor total
de las ventas realizadas. Calcular y mostrar por pantalla el sueldo que
recibirá Juean al final del mes'''
#pedir sueldo:}
var_sueld=float(input('Ingrese el vaor de su sueldo: '))
#pedir valor de total ventas:
var_ventot=float(input('Digite el valor total de las ventas realizadas: '))
#calcular 10% de comision:
var_comisión=(var_ventot*(10/100))
#calculo sueldo total:
var_totsuel=var_sueld+var_comisión
#imprimo por pantalla:
print('El sueldo total a recibir es de: $', round(var_totsuel, 2))
#En el print empleo la función round para redondear a dos decimales.
