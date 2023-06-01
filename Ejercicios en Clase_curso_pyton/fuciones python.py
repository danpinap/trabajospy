#Imprimir los números del 0 al 100 con la función range:
for numeros in range (101): ##Se coloca el 101 porque si se deja en 100 nos presenta hasta el 99.
    print(f'Los números son:{numeros}')
#Para imprimir números pares
for numerosp in range (0,101,2): ##Agregamos el inicio, fin y la itineracia de la lista.
    print('Los números son:{}'.format(numerosp))

def mayorEdad(edad):
    bandera=False
    if edad>=17:
        bandera=True
    return bandera

while True:
    dato=int(input('Ingrese la edad'))
    if mayorEdad(dato)==True:
        print('Es mayor de edad')
        break
    else:
        print('Es menor de edad')