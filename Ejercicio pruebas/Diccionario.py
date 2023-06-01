cursos = {
    "Pedro": ["Matemáticas", "Biología", "Historia"],
    "María": ["Física", "Química", "Literatura"]
}
###Imprime las materias en las que está inscrito Pedro.
print(cursos["Pedro"])
###Agrega una materia más a la lista de materias de María: "Programación".
cursos["María"].append('Programación')
print(cursos["María"])
###Crea un nuevo diccionario con los estudiantes que están inscritos en la materia de Biología.
dicbiol={}
for k,w in cursos.items():
     if 'Biología' in w:
         dicbiol[k]=w
print(dicbiol)
