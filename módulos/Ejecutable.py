from funciones import*
#####MENÚ DE OPCIONES#####
opcion=0
while opcion>=0 and opcion>=10:
    print('MENÚ DE OPCIONES')
    print('1.Suma')
    print('2.Resta')
    print('3.Multiplicación')
    print('4.División')
    print('0.Salir')
    opcion=int(input('Ingrese una opción: '))
    if opcion==0:
        print('Ha seleccionado la opción salir')
        break
    elif opcion==1:
        a=int(input('Ingrese el primer número: '))
        b=int(input('Ingrese el segundo número_: '))
        print('El resultado de la suma es: ',suma(a,b))