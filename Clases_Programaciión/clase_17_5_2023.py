a=5
b=2
#Suma.
print(f'El resultado de sumar, a {a} + {b} es: ',a+b)
#Resta.
print(f'El resultado de restar, a {a} - {b} es: ',a-b)
#Multiplicación.
print(f'El resultado de multiplicar, a {a} * {b} es: ',a*b)
#División.
print(f'El resultado de dividir, a {a} / {b} es: ',a/b)
#División valor exacto.
print(f'El resultado con valor entero de dividir, a {a} / {b} es: ',a//b)
#Residuo de la División.
print(f'El residuo de dividir, a {a} / {b} es: ',a%b)
#Potencia
print(f'El resultado de elevar, a {a} a la {b} es: ',a**b)

#---Operadores de Comparación.
#Mayor que.
print(f'{a} es < que {b}: ',a<b)
#Menor que.
print(f'{a} es > que {b}: ',a>b)
#Igualdad.
print(f'{a} es = que {b}: ',a==b)
#Diferente.
print(f'{a} es diferente que {b}: ',a!=b)
#Mayor o igual.
print(f'{a} es mayor o igual que {b}: ',a>=b)
#Menor o igual.
print(f'{a} es menor o igual que {b}: ',a<=b)
#and
print(a==b and b==a)
#and
print(a==5 or 5==b)

#---Operadores de asignación
#a=a+b
a+=b
print(a)
#a=a/b
a/=b
print(a)
#Concatenar cadenas
d='hola'
c=' mundo'
cadena=d + c
print(cadena)