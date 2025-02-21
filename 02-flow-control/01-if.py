###
# 01 - Sentencias condiconales (if, elif, else)
# Permite ejecutar bloques de codigo solo si se cumplen ciertas condiciones
###

import os
os.system('clear')

print ('\nSentencia simple condicional')

edad = 18

if edad >=18:
  print('Eres mayor de edad')
  print('Felicidades\n')

print('Sentencia condiconal con else')
edad = 15

if edad >= 18:
  print('Eres menor de edead')
else: 
  print('Eres menor de edad')

print('\nSentencia condicional con elif')
nota = 7
if nota >= 9:
  print('¡Sobresaliente')
elif nota >= 7:
  print('Notable')
elif nota >= 5: 
  print('Aprovado')
else:
  print('No esta calificado')

print('\nCondicones multiples')

edad = 18
tiene_carnet = True

if edad >= 18 and tiene_carnet:
  print('Puedes condicir  🚗')
else:
  print('Policia!!!!🚓'  )

# 🇻🇪 un pueblo deIsla Margarita

if edad >= 18 or tiene_carnet:
  print('Puedes conducir en la Isla Margarita')
else:
  print('Paga al policia y te deja ir')

es_fin_de_semana = False

if not es_fin_de_semana:
  print('¡Airy, venga que tenemos que trabajar')


print('Anidar Condicionales')

edad = 20 
tiene_dinero = True

if edad >= 18:
  if tiene_dinero:
    print('Puedes ir a la discoteca')
  else:
    print('Quedate en casa')
else: 
  print('No puedes entrar a la disco')


numero = 5

if numero: 
  print('El número no es 0')

nombre = 'Juan'

if nombre:
  print('El nombre no es vacío')


print('\nLa condición ternaria')

# Es una forma concisa de if-else en una linea de código
# [código si cumple la condición] if [condición] else [codigo si no cumple]

edad = 17 
mensaje = 'Es mayor de edad' if edad >= 18 else 'Es menor de edad'
print(mensaje)

# Ejercicios prácticos
# Ejercicio 1: Determinar el mayor de dos números

# Pide al usuario que introduzca dos números y muestra un mensaje indicando cuál es mayor o si son iguales.
# a = int(input('Valor A: '))
# b = int(input('Valor B: '))

# if a > b:
#   print('A es mayor que B')
# elif a == b:
#   print('A y B son iguales')
# else:
#   print('B es mayor que A')

# Ejercicio 2: Calculadora simple

# Pide al usuario dos números y una operación (+, -, *, /). Realiza la operación y muestra el resultado (maneja la división entre cero).

# a = int(input('Primer número: '))
# b = int(input('Segundo Número: '))

# operacion = input('Selecciona operación \n(+, -, *, /):  ')

# if operacion == '+':
#   print(f'{a} + {b} = {a+b}')
# elif operacion == '-':
#   print(f'{a} - {b} = {a-b}')
# elif operacion == '*':
#   print(f'{a} * {b} = {a*b}')
# elif operacion == '/':
#   if b == 0:
#     print(f'{a} / {b} = Error')
#   else:
#     print(f'{a} / {b} = {int(a/b)}')

# Ejercicio 3: Año bisiesto

# Pide al usuario que introduzca un año y determina si es bisiesto:

# Es divisible por 4.
# Excepto si es divisible por 100, pero no por 400.

# print('Evaluación de año Biciesto\n')
# year = int(input('Introduce un año: '))

# if year % 100 == 0 and year % 400 == 0:
#   print(f'{year} Si es año biciesto')
# elif year % 100 == 0:
#   print(f'{year} No es biciesto')
# elif year % 4 == 0:
#   print(f'{year} Si es año biciesto')





# Ejercicio 4: Categorizar edades

# Clasifica una edad ingresada por el usuario en:

# Bebé (0-2 años)
# Niño (3-12 años)
# Adolescente (13-17 años)
# Adulto (18-64 años)
# Adulto mayor (65 años o más)


# edad = int(input('Introduce una edad: '))

# if edad <= 2:
#   print(f'{edad}: Bebé')
# elif edad <= 12:
#   print(f'{edad}: Niño')
# elif edad <= 17:
#   print(f'{edad}: Adolecente')
# elif edad <= 64:
#   print(f'{edad}: Adulto')
# else:
#   print(f'{edad}: Adulto mayor')
