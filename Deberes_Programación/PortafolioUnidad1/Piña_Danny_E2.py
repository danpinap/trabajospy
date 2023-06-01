print('INSTITUTO UNIVERSITARIO TECNOLÓGICO DEL AZUAY')
print('PROGRAMACIÓN')
print('Danny Adrián Piña Piña')
print('PORTAFOLIO DE EJERCICIOS UNIDAD 2') 
'''Ejercicio 2.- Solicite al usuario ingresar el precio de una laptop,
calcule el valor del IVA e indicar el valor que pagará el usuario. El
IVA será una constante(declarar) que será 12%. ¿El precio de la laptop
como que tipo de dato debería ser declarado y por qué (conteste en un
comentario en su codigo)'''
#Solicitar precio:
var_precio=float(input('Ingrese el precio: '))
#Declarar variable iva:
var_iva12=(12/100)
#Calcular iva:
var_calciva=var_precio*var_iva12
#Calcular el precio total a pagar:
var_total=var_precio+var_calciva
#Imprimir por pantalla:
print('Ud deberá cancelar el valor de {}, incluído el iva.'.format(var_total))

'''El precio de la laptop debería ser declarado como una variale "float"
puesto que puede tomar valores decimales.'''