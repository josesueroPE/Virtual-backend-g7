# bucle FOR
numeros = [10, 20, 30, 40, 50, 60]

for numero in numeros:
    print(numero)

frase_motivadora= 'al que madruga encuentra todo cerrado'

# contador o flag (bandera), va a contar cierto numero de vueltas, ciertas cosas repetidas etc
contador = 0
for caracter in frase_motivadora:
    #print(caracter)
    #cuentame cuantas letras n hay en esa frase
    if caracter == 'n':
        print('hay una n')
        #contador = contador +1
        contador += 1 
print("hay {} veces repetida la letra n". format(contador))


for valor in range(10):
    #emepzar desde el numero 0 hasta el < 10 e incrementara de 1 en 1
    print (valor)

for valor in range (3, 7):
    #el primer parametro sera el numero en e lcual va a empezar
    #y el segundo hasta que numero debe llegar incremenatose de 1 en 1 
    print(valor)

for valor in range (4, 7, 2):
    #el primer parametro sera el numero en e lcual va a empezar
    #y el segundo hasta que numero debe llegar incremenatose de 1 en 1 
    #y el 3er parametro sera de cuento en cuanto debe alterar el contador
    print(valor)


#EJERCICIO:
#cuanto de esos digitos son numeros pares y cuantos son multiplos de 3
# hay __ numeros pares y hay __ multiplos de tres
# HINT: usar for con condicionales
numeros=[10,30,12,17,24,67]

contador_numeros_pares = 0
contador_multiplos_tres =0

for numero in numeros:
    if numero % 2 == 0:
        contador_numeros_pares += 1
    
    if numero % 3 == 0:
        contador_multiplos_tres += 1

print ("hay {} numeros pares y hay {} multiplos de tres".format(contador_numeros_pares, contador_multiplos_tres))

#supongamos que los 10K sion los usuarios en un sistema y queremos encontrar al usuario con un determiando nombre
#no necesitamos recorrer los 19k usuarios, xq ese es el numero 600 por ejemplo
for valor in range(0,10000):
    print(valor)
    if(valor == 600):
        print('el usuario fue encontrado')
        break
        #el break sirve para finalziar de manera prematura un bucle (for, while)
for valor in range(0,20):
    if(valor == 5):
        print('el usuario fue encontrado')
        continue
    #de esta manera continue > sirve para que el codigo que viene a continacion n ose ejectute
    print(valor)

for valor in range(0,20):
    pass 
    #PASS es la palrba clave paraque evitara que nos lance error python


alumnos = ['EDUARDO', 'LILY', 'JOSE', 'RAFAEL']

for alumno in alumnos:
    if alumno == 'EDUARDO':
        pass
        print('hola')
else:
    print ('no se encontra el alumno a buscar')
#el ELSE ingresa una vez que haya terminado de iterar el FOR












