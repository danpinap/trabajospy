#Conjunto a
a=set()
a.add(1)
a.add(3)
a.add(6)
a.add(5)
a.add(4)
#Conjunto b
b=set()
b.add(3)
b.add(10)
b.add(5)
b.add(6)
b.add(4)
b.add(8)
b.discard(8)
#Conjunto c
c=set()
c.add(3)
c.add(5)
c.add(9)
print('Los conuntos son: ',a,b,c)
b.discard(8)
print('Conjunto',b)
d=a.copy()
print('Conjunto D',d)
c.clear()
print('Conjunto C',c)
c=b.copy()
print('Conjunto C',c)
#Verificar si es disyunto entre c y a.
print(c.isdisjoint(a))
#Verificar si es disyunto entre c y b.
print(c.isdisjoint(b))
#Creamos un nuevo conjunto
e=set()
e.add(3)
e.add(4)
#Verificar si es un subconjunto
print(e.issubset(b))
print(e.issubset(a))
print(e.issubset(d))
print(b.issubset(d))
#Verificar si es e contiente a a
print(e.issuperset(a))
f=c.union(b)
print('Conjunto F',f)
#Unir un conjunto a otro en el propio conjunto
f=a.update(b)
print('Conjunto A',a)
#Ver elementos no comunes
print(a.difference(b))
#Diferencia que se guarda en los elementos no comunes entre dos conjuntos
a.difference_update(b)
print('Conjunto A',a)
#Verificar la intersección de conjuntos
print(c.intersection(d))
#Ahora interseccion con update
c.intersection_update(d)
print('Conjunto c',c)
print('Conjunto A',a)
print('Conjunto A',b)
print('Conjunto A',c)
print('Conjunto A',d)
print('Conjunto A',e)
print('Conjunto A',f)
print(e.symmetric_difference(d))
