cadena=input('Ingrese una cadena de texto: ')
def cont_vocales(cadena):
    conteo_vocales = 0
    a = 0 
    while a < len(cadena):
        if cadena[a].lower() in "aeiou":# Si la letra es una vocal, sumamos 1 al contador de vocales
            conteo_vocales+= 1
        a+=1
    return conteo_vocales
print(cont_vocales(cadena))