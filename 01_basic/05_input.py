###
# 07 - Entrada de usuario (input()) - Versión simplificada
# La función input() permite obtener datos del usuario a través de la consola
###


nombre  = input('hola, ¿Cómo te llamas?\n')
print(f'Hola {nombre}, encantado de conocerte')

age = int(input('¿Cuántos años tienes?\n'))

print(f'Tienes {age} años')
print(f'Dentro de 20 años tendras {age + 20}')


print('Obten multiples valores a la vez')
country, city = input('¿En qué país y ciudad vives?\n').split()

print(f'Vives en {country}, {city}')
