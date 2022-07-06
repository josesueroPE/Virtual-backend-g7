from email import message


edad_roberta = 28

if edad_roberta >= 18 :
    print('si puede entrar a la discoteca')
else:
    print('no peudes entrar, anda al cine')


edad_martin = 8

if edad_martin >= 65:
    print('esa persona esta jubilada')
elif edad_martin >= 18:
    print('esa persona es mayor de edad')
elif edad_martin >= 0:
    print ('esa persona es menor de edad')
else:
    print ('edad imposible')

#recordar que ELIF deopende de que si el anterior no se ha cumpluiod, si ya se cumplio entonces no se considere.



print ('hola')
#esto de abajo es para meter data, para ingresas valores al programa desde consola
# data = int(input("hola, ingresa tu edad:" )) - esto hara que reconozca el input como entero

talla = input("hola, ingresa tu talla de polo:")
print(type(talla))

# Dependiendo de la talla del polo podriamos hacer lo siguiente: si es XL entonces indicar que llegara
# para fines de mes, si es L o M solicitar el color del polo, y si es 
# talla S indicar que solo hay en color morado

if talla == 'xl':
    print('el polo recien llegra a fin de mes')
elif talla == 'l' or talla == 'm' : 
    input('ingresa el color del polo')
elif talla == 's' :
    print('solo hay en color morado')
else:
    print ('talla incorrecta')

#ahroa vamos a cambiar un poco 

if talla == 'l' or talla == 'm' : 
    input('ingresa el color del polo')
elif talla == 's' :
    print('solo hay en color morado')
elif talla == 'xl' :
    print('el polo recien llegra a fin de mes')
else:
    print ('talla incorrecta')


#Recordemos que a veces la gente en el input va meterle mayuscula o minuscula entoinces hacemos un pequeño
# truco, sera ponerle en el input de la talla .lower eso hara que todo lo que se ingrese el sistema 
# lo va a convertir en miniscula asi de la siguietne manera y tambien hay otros metodos 
# como por ejemplo capitalize, etc. 
if talla.lower() == 'xl':
    print('el polo recien llegra a fin de mes')



