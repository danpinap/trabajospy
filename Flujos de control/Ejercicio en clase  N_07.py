print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 07
#Escribir un programa que pregunte al usuario si quiere una pizza
#vegetariana (pimiento o tofu)o no(peroni, jamon o salmón), y en funcion de su respuesta le muestre un menú
#con los ingredientes disponibles para que elija. Solo puede elegir
#un ingrediente ademas de la mozzarella y tomate que estan den to
#das las pizzas. Al final mostrar en pantalla la pizza elegida y 
#los ingredientes.

ingbase=('Mozzarella, tomate')
p='pimiento'
t='tofu'
r='peperoni'
j='jamón'
s='salmón'
print('Pizzeria Napoli le saluda')
tipo_pizza=input('Presione "v" para una pizza vegetariana \n'
                 'Presione "n" para una pizza No vegetariana \n')
if tipo_pizza=='v':
    print('Los ingredientes son:\n' + ingbase + ' mas un ingrediente adicional:\n'
          +p+' '+'ó'+' '+t)
    inexv=input('Para seleccionar su ingrediente extra\n'
            'Digite "1" para pimiento.\n'
            'Digite "2" para tofu \n')
    if inexv=='1':
        print('Ud. ha seleccionado una pizza vegetariana con:\n', ingbase, 'más', p)
    elif inexv=='2':
        print('Ud. ha seleccionado una pizza vegetariana con:\n', ingbase, 'más', t)
    else:
        print('Opción incorrecta')
    
if tipo_pizza=='n':
    print('Los ingredientes son:\n' + ingbase + 'mas un ingrediente adicional:\n'
          +r+' '+j+' ó '+ s)
    inexv=input('Para seleccionar su ingrediente extra\n'
                'Pulse "1" para peperoni\n'
                'Pulse "2" para jamon\n'
                'Pulse "3" para salmón\n')
    if inexv=='1':
        print('Ud. ha seleccionado una pizza no vegetariana con:\n', ingbase, 'más', r)
    elif inexv=='2':
        print('Ud. ha seleccionado una pizza no vegetariana con:\n', ingbase, 'más', j)
    elif inexv=='3':
        print('Ud. ha seleccionado una pizza no vegetariana con:\n', ingbase, 'más', s)
    else:
        print('Opción incorrecta')
else:
    print('El valor ingresado no corresponde al menú')
    