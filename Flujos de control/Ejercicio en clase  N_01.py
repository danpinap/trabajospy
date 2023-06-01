#Programa para decidir cruzar la calle o no según el color del semaforo.
print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")

semaforo=input("Digite un color del semaforo en minusculas a continuación: ")

if(semaforo=='rojo'):
    print('Ud. no debe cruzar')
elif semaforo=="amarillo":
    print('Ud. preparece para cruzar')
elif semaforo=='verde':
    print('Ud. puede cruzar')
else:
    print('El dato ingresado no es correcto')