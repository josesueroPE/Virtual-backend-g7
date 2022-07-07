# conjunto (set)
#es una coleccion de datos desordebada (no lleva orden en los indices)
#sirve para guardar valores que solamente podremos comprobar si 
#hay o no hay en ese conjunto

meses = {'enero', 'febrero', 'marzo', 'abril'}
print (meses)
print('enero' in meses)
print('agosto' in meses)


#tambien se puede agregar valores
meses.add('mayo')
meses.add('diciembre')

print(meses)

#tnb se puede agregar un conjunto de nuevos elementos
meses.update(['julio', 'setiembre' ])
print(meses)

#el metodo discard elimina todos los valores que coinciden con ese contenido
meses.discard('junio')
print(meses)


meses.remove('julio')
print(meses)