# LISTAS
alumnos = ['JAVIER', 'ALEJANDRO', 'ALEXANDRA', 'JENNY']

#las listas estan representadas por CORCHETES! >> []

# son colecciones de datos ordenadas (posiciones), las poisciones
#siempre empiezan en cero

print(alumnos[0])

variados = [10, [1,2,3]]
print(variados[1][1])

# cuando usamos 2 punto : al momento de definitr la posiconm de una listam, le 
# estaremos indicando que que queremos una sublitsta de esa lista 
# siendo el primera valor la posicion inicial y el segundo valor hasta 
# qye posicion tiene que llegar (menor que)
print(alumnos[1:3])
#destructuracion de una lista, osea extraer los elementos internos 
print(alumnos[:])
#cuando usamos posiciones negativas en uina lista, PY lo invierte,
#ahora la posicion -1 sera el ultimo elemento de la lista y asi
# sucesivamente
print(alumnos[-1])


#sentido de pertenencia, en el cual podemos consultar si un valor
#determinado exciste en una lista asi de esta manera:
for alumno in alumnos:
    if alumno == "JENNY":
        print('si esta')
        break

#sentido de pertenencia, en el cual podemos consultar si un valor
#determinado exciste en una lista asi de esta manera:
print('jenny' in alumnos)
print(10 in alumnos)

#las listas son colecciones de datos EDITABLES
alumnos[0] = 'MARTIN'
print(alumnos)

#APPEND sirve para agregar una valor a la lista pero AL FINAL de ella
alumnos.append('IVANOV')
print(alumnos)

#EXTEND combina las 2 listas en una sola
alumnos.extend(['LUIS', 'LILY', 'JORDAN'])


#otra forma de combinar es 'concatenando' las listas
alumnos += ['YORDY', ' JAVIER', 'RUBEN']
print(alumnos)

# Eliminar un elemento de la lista

#primera forma de eliminar por el metodo DEL
del alumnos[1:3]
print(alumnos)

#s2da forma por POP, lo que hace elimina el contenido de esa posicion
#pero se puede almacenar el contenido en otra variable
alumno_eliminado = alumnos.pop(2)

print(alumnos)
print(alumno_eliminado)

# tercera forma
alumnos.clear()
print (alumnos)