print('INSTITUTO UNIVERSITARIO TECNOLÓGICO DEL AZUAY')
print('PROGRAMACIÓN')
print('Danny Adrián Piña Piña')
print('Recuperación 26-5-2023 UNIDAD 3')

'''Ejercicio 2: Conversor de unidades de almacenamiento.  Realizar un conversor de unidades de almacenamiento
por ejemplo convertir de Bytes a Kilobytes, de Kilobytes a megabytes y de Megabytes a Gigabytes.'''
### Conversor de Unidades de Almacenamiento ###
print('  CONVERSOR DE UNIDADES DE ALMACENAMIENTO\n 1. bits a Bytes\n 2. Bytes a Kilobytes\n 3. Kilobytes a Megabytes\n 4. Megabytes a Gigabyts\n 5. Gigabytes a Terabytes')
opcion=int(input('Digite el número de la operación que desea realizar: '))
if opcion==1:
    num1=float(input('Ingrese valor en bits: '))
    B=num1/8
    print('Los {} bits equivalen a {} Bytes'.format(num1,B))
elif opcion==2:
    num1=float(input('Ingrese valor en byts: '))
    KB=num1/1024
    print('Los {} byts equivalen a {} Kilobytes'.format(num1,KB))
elif opcion==3:
    num1=float(input('Ingrese valor en byts: '))
    MB=num1/1024
    print('Los {} KB equivalen a {} MB'.format(num1,MB))
elif opcion==4:
    num1=float(input('Ingrese valor en byts: '))
    GB=num1/1024
    print('Los {} MB equivalen a {} GB'.format(num1,GB))
elif opcion==5:
    num1=float(input('Ingrese valor en byts: '))
    TB=num1/1024
    print('Los {} GB equivalen a {} TB'.format(num1,TB))
else:
    print('La opción ingresada no es la correcta!!!')