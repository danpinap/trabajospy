print('INSTITUTO TECNOLÓGICO DEL AZUAY')
print('CURSO DE PYTHON')
print('Danny Adrián Piña Piña')
print("30/03/2023")
#Ejercicio 05
#Los tramos impositivos para la declaración de la renta en un determinado
#país son los siguientes (vertabla en ejercicio en clase). Realizar
#un programa que pueda decir el % de impuestos que una persona deba pagar
#según su sueldo.
sueldo=float(input('Ingrese el valor de su sueldo: '))
rango1=(sueldo*0.05)                                           
rango2=(sueldo*0.15)
rango3=(sueldo*0.25)
rango4=(sueldo*0.30)
rango5=(sueldo*0.45)
if sueldo<10000:
    print('Ud. debe pagar el 5% ' + 'que equivale a: ' + str(rango1) + 'USD.')
    print('El salario neto a recibir es:\n', sueldo-rango1)
elif sueldo>=10000 and sueldo<20000:
    print(f'Ud. debe pagar el 15% que equivalente a: {rango2} USD.')
    print('El salario neto a recibir es:\n', sueldo-rango2)
elif sueldo>=20000 and sueldo<35000:
    print('Ud. debe pagar el 25% que equivale a: {} USD.'.format(rango3))
    print('El salario neto a recibir es:\n', sueldo-rango3)
elif sueldo>=35000 and sueldo<60000:
    print('Ud. debe pagar el 30% que equivale a:', rango4, 'USD')
    print('El salario neto a recibir es:\n', sueldo-rango4)
elif sueldo>=60000:
    print('Ud. debe pagar el 45% que equivale a: ' + str(rango5) + 'USD')
    print('El salario neto a recibir es:\n', sueldo-rango5)
else:
    print('El salario ingresado es incorrecto')