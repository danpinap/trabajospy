print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 06
#Realiar un programa que lea dos números por teclado y permita elegir
#entre 3 opciones en un menú.
print('Digite dos números a continuación: \n')
num1=int(input('Primer número: '))
num2=int(input('Segundo número: '))
opcionmenu=input('Pulse "s" para realizar una suma \n'
          'Pulse "r" para realizar una resta \n'
          'Pulse "m" para realizar una multiplicación:\n'
          )
if opcionmenu=='s':
    print('La respuesta es: ',num1+num2)
elif opcionmenu=='r':
    print('La respuesta es: ',num1-num2)
elif(opcionmenu=='m'):
    print('La respuesta es: ',num1*num2)
else:
    print('Opción seleccionada inválida')