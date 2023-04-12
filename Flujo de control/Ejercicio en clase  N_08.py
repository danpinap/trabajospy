print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 08
#Escriba un programa que solicite al usuario una letra y, si es una
#vocal, muestre el mensaje "Es vocal". Verificar si el usuario ingre
#só un string de más de un carácter y, en ese caso, informarle que
#no se puede procesar el dato.
letra=input('Ingrese una letra: ')
if len(letra) != 1:
    print("No se puede procesar el dato. Debe ingresar una sola letra")
elif letra in 'aeiouAEIOU':
    print('Es una vocal')
else:
    print('No es una vocal')