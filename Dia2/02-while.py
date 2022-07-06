#WHILE
numero = 10
# es un bucle que se realizara de manera automatica hasta que las c
while numero > 0:
    print('numero positivo')
    print(numero)
    numero -= 1

# DO WHILE > n oexiste en python solo existe el WHILE

# solicitar 5 digitos para la loteria pero estos no pueden ser mayor 
# que 100 ni numeros negativos 

contador_numeros = 1
while contador_numeros < 6 :
    numero = int(input('ingresa el numero de la loteria: '))
    if (numero < 100 and numero > 0):
        contador_numeros += 1
        continue
    print('numero ingresado es invalido')
        

    