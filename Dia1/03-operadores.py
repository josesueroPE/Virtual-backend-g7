#operadores aritmeticos
from datetime import datetime


edad_juan = 40
edad_maria = 34

#suma
print(edad_juan + edad_maria)

# resta
print(edad_juan - edad_maria)

# multiplicacion
print(edad_juan * edad_maria)

# division
print(edad_juan / edad_maria)

# modulo = Resultado del Entero de la division
print(edad_juan % edad_maria)

# cociente
print(edad_juan // edad_maria)

#POTENCIA
print(edad_juan ** 2)


# en el caso de los caracaters strins cuando hacemos una sumatorio e nlso string se hara una concatenmacion

mes = 'junio'
temporada = 'invierno'
print(mes + temporada)

#y si hacemos yuso de la multipliacion hara que se repita   N casntidad de veces

print(mes * 5)

#operadores de asignacion

print ("""
{}""".format(mes)*5)

#Operadores de comparacion

Edad_luis = 15
edad_martha = 30

#mayor que
print(Edad_luis < edad_martha)

#menor que
print(Edad_luis > edad_martha)

#igual que
print(Edad_luis == edad_martha)

# != diferente que
print(Edad_luis != edad_martha)

# >=mayor o igual que
print(Edad_luis >= edad_martha)

# <= menor o igual que
print(Edad_luis <= edad_martha)


#OPERADORES LOGICOS
edad_luis = 15
edad_martha = 30

# and "y"  -- Tienen que cumplirse ambos para que sean verdadero, basta que uno sea falso y 
# todo se malogra todo se vuelve falso
print(edad_luis > 18 and edad_luis > edad_martha)

# Or "O" --  Basta con que al menos 1 de las dos condicionmes sea verdadero o cumpla la 
# condicion para qeu todos sean verdaderos
print(edad_luis > 18 or edad_luis > edad_martha)

# not "NO" --Iniverte el resultado, si es V lo mando falso y si es falso lo manda a V
print(not edad_luis > 50)


#EJERCICIOS
edad_eduardo = 18
edad_renato = 26
edad_laura =35


# como saber si eduardo es mayor de edad
print(edad_eduardo >= 18)

# como saber si eduardo es mayor que laura
print(edad_eduardo > edad_laura)

#como saber si renato es menor que laura pero mayor qeu eduardo
print(edad_eduardo < edad_laura and edad_renato > edad_eduardo )

# como saber si laura puede ser mayor que renato o menor que eduardo
print(edad_laura > edad_renato or edad_laura < edad_eduardo)



#OPERADORES DE ASIGNACION
# = Asignacion 
edad = 50

# Incremento (esto es para sumarle una unidad, 51, luego 52, etc)
edad += 1

# Decremento (esto es para sumarle una unidad, 51, luego 52, etc)
edad -= 1

# *= Multiplicador - puedes pner que multipli8que x1 o x2 etc
edad *= 1

# /= division 
edad /= 1

# hay mas como poer ejemplo potencia, cociente, etc























