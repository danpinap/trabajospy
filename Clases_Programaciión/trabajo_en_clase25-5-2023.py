#Ejercicio # 1
print('Ingrese dos números a verificar divisibilidad: ')
num1=int(input('Número 1: '))
num2=int(input('Número 2: '))
if num1>num2:
    if num1%num2==0:
        print(f'El número {num1} es divisible para el {num2}')
    else:
        print(f'El número {num1} es no es divisible para el {num2}')
else:
    print(f'El número {num1} no se puede dividir para el número {num2}')

#Ejercicio # 2

print('MENU PIZZAS \n1. Vegetariana\n2. No Vegetariana\n')
ingbase=('mozzarella, tomate y ')
opcmen1=int(input('Digite la opción 1 o 2: '))
men_veg=()
men_noveg=()
if opcmen1==1:
    print('MENU iNGREDEITE ADICIONAL \n1. Pimiento\n2. Tofu\n3. Champiñones\n4. Soya\n')
    men_veg=int(input('Digite la opción 1, 2, 3 o 4: '))
    if men_veg==1:
        print('Su pizza es vegetariana con los siguientes ingredientes: {},pimiento'.format(ingbase))
    elif men_veg==2:
        print('Su pizza es vegetariana con los siguientes ingredientes: {}tofu'.format(ingbase))
    elif men_veg==3:
        print('Su pizza es vegetariana con los siguientes ingredientes: {}champiñones'.format(ingbase))
    elif men_veg==4:
        print('Su pizza es vegetariana con los siguientes ingredientes: {}soya'.format(ingbase))
    else:
        print('La opción ingresada es incorrecta!!!')
elif opcmen1==2:
    print('MENU iNGREDEITE ADICIONAL \n1. Peperoni\n2. Jamón\n3. Salámi\n2.')
    men_noveg=int(input('Digite la opción 1, 2 o 3: '))
    if men_noveg==1:
        print('Su pizza es NO vegetariana con los siguientes ingredientes: {}peperoni\n'.format(ingbase))
    elif men_noveg==2:
        print('Su pizza es NO vegetariana con los siguientes ingredientes: {}jamón\n'.format(ingbase))
    elif men_noveg==3:
        print('Su pizza es NO vegetariana con los siguientes ingredientes: {}salámi\n'.format(ingbase))
    else:
        print('La opción ingresada es incorrecta!!!')
else:
    print('La opción ingresada es incorrecta!!!')