###
# 03 - Listas
# Secuencais mutables de elementos
# Pueden contener elementos de diferentes tipos
###

import os
os.system('clear')

# Creación de listas 

print('\nCrear listas')
lista1 = [1,2,3,4,5] # lista de enteros
lista2 = ['manzana', 'peras', 'platanos'] # lista de cadenas
lista3: list[str | int | bool] = [1, 'hola', 3.14, True] # lista de tipos mixtos 

lista_vacia = []
lista_de_listas = [[1,2], [3,4]]
matrix = [[1,2], [2,3], [3,4]]


print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceder a elementos por indice

print('\nAcceder a elementos por índice')
print(lista2[0]) # Manzana
print(lista2[-1]) # Platanos
print(lista2[-2]) # peras

print(lista_de_listas[1][0])

# Cambio de elementos

# Slicing (rebanado) de listas

# lista1 = [1,2,3,4,5] 

print(lista1[1:-1]) # [2,3,4]
print(lista1[:3])   # [1,2,3]
print(lista1[3:])   # [3,4,5] del 3ro al final 
print(lista1[:])    # Esto te hace una copia 


# HAY MAS MAGIA

lista1 = [1,2,3,4,5,6,7,8]
# print(lista1[desde:hasta:paso])
print(lista1[1::2])  # Para devolver indices pares
print(lista1[:2:-1]) # Para devolver indices invertidos


# Modificar una lista 

lista1[0] = 20
print(lista1)

# Añadir elementos a una lista 

lista1 = [1,2,3]

lista1 += [4,5,6]

print(lista1)