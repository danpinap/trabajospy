print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 03
#Escribir un programa que almacene la cadena de caracteres
#contraseña en una variable, pregunte al usuario la contraseña
#e imprima por la pantalla si la contraseña introducida por el
#en la variable sin tener en cuenta mayusculas y minúsculas.
contraseña='mypass123'
contra=input('Por favor digite una contraseña: ')
if contra.lower()==contraseña:
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')
