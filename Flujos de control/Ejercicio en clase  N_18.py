print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("01/04/2023")
#Ejercicio 18
#Escribir un programa que pida al usuario una frase y determine si
#es un palíndromo. Ignorar espacios en blanco y mayúsculas/minúsculas
#al determinar si la frase es un palíndromo o no.
frase=input('Ingrese una frase para testear a continuación:\n')
frase=frase.lower().replace(' ','')
if frase==frase[::-1]:
    print('La frase que ingresó es un palíndromo.')
else:
    print('La frase que ingresó NO es un palíndromo')