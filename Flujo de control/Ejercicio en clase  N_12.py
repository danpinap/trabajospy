print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 12
#Programa para deteminar si un número es positivo, negativo o cero
dato_base=int(input('Ingrese un número entero, puede elegir entre positivo, negativo o cero: '))
if dato_base<0:
    print('El número {} es un número negativo'.format(dato_base))
if dato_base==0:
    print('EL número {} es cero'.format(dato_base))
if dato_base>0:
    print('EL número {} es positivo'.format(dato_base))