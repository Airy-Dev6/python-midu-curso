###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí

nombre = 'Airy'
ciudad = 'CDMX'

print(f"Mi nombre es {nombre}\nMi cuidad es {ciudad}")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(f'{a} = {type(a)}\n{b} = {type(b)}\n{c} = {type(c)}\n{d} = {type(d)}\n{e} = {type(e)}')

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

numeroStr = '12345'

print(f"{int(numeroStr)} type = {type(int(numeroStr))}\n{numeroStr} a float = {float(numeroStr)}{type(float(numeroStr))}")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

my_nombre = 'Airy'
age = 24
height = 1.75

print(f"Mi nombre es {my_nombre} tengo {age} y mido {height}")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = int(round(3.1416)/2)

print('El valor de PI es:', 3.1416)
print('El valor de round(pi) es:', round(3.1416))
print('El valot de round(PI)/2 es = ', resultado    )