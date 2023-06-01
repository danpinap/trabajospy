#PROGRAMA DE ALCANCIA QUE NO PERMITE RETIRAR DINERO
alcancia=float(input("cuanto quiere ahorrar: ")) #aqui recibo cuanto quiere ahorrar en mi alcancia
suma=0 #declaro la variable suma con cero ya que ahi ire sumando(o restando) lo que pongo(o quito) de mi alcancia
ahorro=float(input("ingrese valor a ahorrar: ")) #aqui recibo mi primer valor a guardar en el alcancia
suma = suma + ahorro #modifico la variable suma para saber ahora cuanto tengo en mi alcancia ( podria colocar todo esto dentro de un if validadno que no quiera retirar algo de la alcancia que esta vacia )
while suma<alcancia: #aqui comparo que el valor d e la suma sea menor al total de la alcancia. es decir veo si es necesario seguir pidiendo mas dinero o ya tengo lo que queria ahorrar
   ahorro = float(input("ingrese valor a ahorrar : "))#aqui ya voy a ir recibiendo el valor que voy a ahorrar (esto se mostrara siempre y cuando aun no se logre el objetivo que quiero ahorrar)
   if ahorro >= 0: #con este if voy a verificar que no deba retirar mas  delo que tengo... por lo que coloco suma(lo que tengo en mi alcancia)+(coloco el mas por la lay d elos signos por uqe el retirar es menos y si hago - seria -*-=+)
      # tengo 30+ (-35 que quiere retirar) me quedaria  -5>=0 entonces no entraria y se iria al else
       suma = suma + 0 #hago la suma para saber cuanto tengo ahora en mi alcancia
       #print("suma", suma)
   else:
       print("no puede rerirar hasta que logre objetivo, usted tiene ahorrado: ",suma)
print("usted logo a ahorrar", suma)


#PROGRAMA PARA CALCULO DEL PROMEDIO
x=1     #Declaro variable contadora para la terminación del bucle.
suma=0  #Declaro una variable acumulativa.
while x<=10:    #Establezco la condición de la duración del bucle.
    valor=int(input('ingrese un numero a para promediar: '))    #Solicito ingreso de un número.
    suma=suma+valor    #Realiza la acumulación de los valores ingresados.
    x=x+1              #Realiza el conteo de los números ingresados y permite salir del bucle al llegar a 10.
promedio = suma/10     #Calcula el promedio de todos los números ingresados.
print('La suma es igual a ',suma)   #Imprime la suma de total de los números ingresados.
print('El promedio es ',promedio)   #Imprime el promedio calculado.

#PROGRAMA QUE MUESTRA LA SUMA ACUMULADA DE LOS NÚMEROS
sumtot=0
print('Este programa le mostrará la suma aculmulda de los cantidades que ingrese')
print('Para salir pesione 0')
dato=float(input('Ingrese un número a sumar: '))
sumtot=sumtot+dato
while dato!= 0:
    dato=float(input('Ingrese un número a sumar: '))
    sumtot=sumtot+dato
    print('La suma acumulada de los números ingresados al momento es: ',sumtot)

#pedir al usuario que ingrese numeros el programa debera contar
#cuantos pares e impars en total hay
cantpar=0
cantimpar=0
Print('Este es un contador de números pares e impares')
Print('Presione 0 para salir')
while num!= 0:
    num = int(input('Ingrese un número:')
    if num%2 ==0:
        cantpar = cantpar + 1
    else:
        num%2 != 0:
        cantimpar = cantimpar + 1
print(f'De los números ingresados hay {par} pares y {impar} impares.')