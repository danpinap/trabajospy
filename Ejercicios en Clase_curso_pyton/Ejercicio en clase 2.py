numero1=int(input("Ingrese el primer numero a comparar: "))
numero2=int(input("Ingrese el segundo número a comparar: "))
igual=(numero1==numero2)
diferente=(numero1!=numero2)
mayor=(numero1>numero2)
menor=(numero1<numero2)
mayor_igual=(numero2>=numero1)
#Opción uno para representar la salida de información.
print("Los números " + str(numero1) +" y " +str(numero2) +" son iguales? " +str(igual))
print("Los números " + str(numero1) +" y " +str(numero2) +" son diferentes? " +str(diferente))
print("El número " + str(numero1), "es mayor? " + str(mayor))
print("El número " + str(numero1), "es menor? " + str(menor))
print("El número " + str(numero2), "es mayor o igual al número" +str(numero1) +" ? "+ str(mayor_igual)+"\n")
#Opcidon dos para representar la salida de información.
print(f"Los números: {numero1} y {numero2} son iguales?: {igual}")
print(f"Los números: {numero1} y {numero2} son diferentes?: {diferente}")
print(f"El número: {numero1} es mayor?: {mayor}")
print(f"El número: {numero1} es menor?: {menor}")
print(f"El número {numero2} es mayor o igual al número {numero1}? {mayor_igual}\n")
#Opción tres para representar la salida de información.
print("Los números: {} y {} son iguales? {}". format(numero1, numero2, igual))
print("Los números: {} y {} son diferentes? {}". format(numero1, numero2, diferente))
print("EL número: {} es mayor? {}". format(numero1, mayor))
print("EL número: {} es menor? {}". format(numero1, menor))
print("EL número: {} es mayor o igual al número {} {}\n". format(numero2, numero1, mayor_igual))
#Opción cuatro para representar la salida de informaión
print('Los números: ', numero1,' y ', numero2,' son iguales? ', igual)
print('Los números: ', numero1,' y ', numero2,' son diferentes? ', diferente)
print('El número: ', numero1,'es mayor?', mayor)
print('El número: ', numero1,'es menor?', menor)
print('El número: ', numero2,'es mayor o igual al', numero1,' ? ', mayor_igual)