print('INSTITUTO UNIVERSITARIO TECNOLÓGICO DEL AZUAY')
print('PROGRAMACIÓN')
print('Danny Adrián Piña Piña')
print('PORTAFOLIO DE EJERCICIOS UNIDAD 2') 
'''Ejercicio 1.- Crear dos variables de cualquiera de los tipos básicos,
dar un valor a la primera y a continuación asigne la segunda a la primera.
Imprimir por pantlla las dos vriables. Cambiar el valor de la segunda
variable y volver a imprimir las variables por pantallaa. ¿Qué es lo que
ocurre? (Conteste en un comentario en su codigo)'''
#creo dos variables:
var_text=str()
var_num=int()
#dar valor a la primera:
var_text='Que numero tengo'
#asignar la segunda a la primera:
var_text=var_num
#imprimir las dos variables:
print(var_text, var_num)
#cambiar valor de la segunda:
var_num=10
#imprimir las dos variables:
print(var_text, var_num)
'''Como podemos observar, el valor de la variable var_text a pesar de ser 
diferente a la segúda "var_num" terminó asumiendo el mismo valor de la
segunda y se perdió su valor tipo texto original. Para no perder la
información de la variable 1 podíamos haber crado una variable auxiliar y
así mantener para su uso posterior.'''