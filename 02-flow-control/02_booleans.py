###
# 02 - Booleanos
# Fundamentales para el control de flujo y la logica en programación
###

import os
os.system('clear')

# Los booleanos representan valores de verdad: True o False

print('\nValores de booleanos básicos:')
print(True)
print(False)

# Operadores de comparación: devuelven un valor Booleano

print('\nOperadores de comparación')
print('5 > 3', 5 > 3)     # True
print('5 < 3', 5 < 3)     # False 
print('5 == 5', 5 == 5)   # True (igualdad)
print('5 != 3', 5 != 3)   # True (Desigualdad)
print('5 >= 5', 5 <= 5)   # True (Mayor o igual que)
print('5 <= 3', 5 <= 3)   # False(Menor o igual que)

print('\nComparación de cadenas.')

print('Manzana < pera', 'Manzana' < 'Pera') # True
print('Hola == hola', 'Hola' == 'hola') # False

# Operadore logicos: and, or, not 

print('\nOperadores Logicos')
print('True and True:', True and True)      # True 
print('True and False:', True and False)    # False 
print('False and False: ', False and False) # False
print('True or False: ', True or False)     # True
print('False or False: ', False or False)   # False
print('not True: ', not True)               # False
print('not False: ', not False)             # True 

