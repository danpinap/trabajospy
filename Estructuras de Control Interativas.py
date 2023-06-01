def suma(num1,num2):
    return num1+num2
def resta(num1,num2):
    return num1-num2
def multiplicación(num1,num2):
    return num1*num2
def división(num1,num2):
    return num1/num2
def saludo():
    print('Hola Adrián')
def formateo(nombre,apellido):
    print(nombre, apellido)
bandera=True ##Bandera es solo un nombre cualquiera de variable
while bandera:
    print(('MENÚ DE OPCIONES'))
    print('1 Suma')
    print('2 Resta')
    print('3 Multiplicación')
    print('4 División')
    print('5 Saludo')
    print('6 Fomato')
    print('7 Salir')
    opción=int(input('Digite una opción:'))
    if opción!=5:
        num1=int(input('Ingrese primer número: '))
        num2=int(input('Ingrese segundo número: '))
        if opción ==1:
            print('La suma es igual a: ',suma(num1,num2))
        elif opción ==2:
            print('La resta es igual a: ',resta(num1,num2)) #cuando se trabaja sin función se puede agregar un break con el cual al realizar la operación se corta también el bucle.
        elif opción ==3:
            print('La multiplicación es igual a: ',multiplicación(num1,num2))
        elif opción ==4:
            print('La división es igual a: ',división(num1,num2))
        elif opción ==5:
            saludo()
        else:
            opción ==6:
            formateo()
    else:
        bandera=False
        print('Fin de ciclo')
print('Nueva linea')