#tuplas son colecciones de datos ordenadas pero no editables
#una vez creada no hay forma de modificarla
#generalmente sirve para guardar valores o datos que no lo vamos a modificar 
#en todo el programa, como variables, secretos, conexion a la BD, 
#conexion a una libreria ExternalClashErro
#ralgo que no queramos modificar de manera accidental
# se representa con PARENTESIS, recordar que los cochetes son listas

profesores = ('EDUARDO', 'OSMAR')

print(profesores[0])

data = (1,True, 'junio', 14.5, [1,2,3,4])

print(data[1:4])

#se puede eliminar toda la variable pero no se puede eliminar
#parte del contenido de la tupla 

del data

notas = (10,15,15,18,10,5,7,14)
#count > sirve para contar las veces que se repirte cierto valor
print(notas.count(10))
print(notas.count(20))

# index >si existe ese valor en la tupla se retornara la posicion en
#la que se encuentre, sino exuiste se emitira error
print(notas.index(15))

#muestra las posiciones en la que esta 1 y 2
