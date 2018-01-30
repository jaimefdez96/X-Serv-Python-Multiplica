#!/usr/bin/python3
#Tablas de multiplicar

Numeros = list(range(1,11))
for Numero in Numeros:
    print ('Tabla del ', Numero)
    print('..............')
    for Operando in Numeros:
    	Resultado = Numero * Operando;
    	print(Numero, 'por', Operando, 'es', Resultado)
    print(' ')
