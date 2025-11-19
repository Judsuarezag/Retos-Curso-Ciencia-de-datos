# Este es el código en Pythpon para el Reto 2 del Curso de Ciencia de datos

# Hecho por Judsuarezag

# 1. Escribe un programa en Python que pregunte el nombre del usuario, su edad y su correo electrónico y luego imprima el siguiente mensaje en pantalla:
#  Input: Digite su nombre: Pedro
#  Digite su edad: 30
#  Digite su correo electrónico: p3dr1t0_12345@gmail.com
#  Output: Bienvenido al sistema Pedro, su correo electrónico es p3dr1t0_12345@gmail.com y tiene 30 años de edad

Nombre = input("Digite su nombre: ")
Edad = input("Digite su edad: ")
Correo = input("Digite su correo electrónico: ")

print(f"Bienvenido al sistema {Nombre}, su correo electrónico es {Correo} y tiene {Edad} años de edad")

# 2. Utilizando Python, dado un número n calcula la siguiente operación ((n^2+2n)/2) e imprime en pantalla el resultado:
# Output: El resultado de la operación es

n = int(input("Digite un número: "))
resultado = (n**2 + 2*n) / 2
print(f"El resultado de la operación es {resultado}")

# 3.	Escribe un programa que imprima en pantalla el largo de una cadena de texto:
# Input: Ingrese una cadena de texto: ¡Hola mundo!
# Output: La cadena de texto tiene 12 caracteres

cadena = input("Ingrese una cadena de texto: ")
largo = len(cadena)
print(f"La cadena de texto tiene {largo} caracteres")

# 4. Escribe un programa que elimine los primeros tres caracteres de una cadena de texto:
# Input: Ingrese una cadena de texto: Hola mundo
# Output: a mundo

cadena2 = input("Ingrese una cadena de texto: ")
nueva_cadena = cadena2[3:]
print(nueva_cadena)

# 5.	Escribe un programa que elimine los primeros dos y los últimos dos caracteres de una cadena de texto:
# Input: Ingrese una cadena de texto: Hola mundo
# Output: la mun

cadena3 = input("Ingrese una cadena de texto: ")
nueva_cadena2 = cadena3[2:-2]
print(nueva_cadena2)

# 6.	Si tienes una panadería que vende el mismo tipo de pan a $2500 10 veces al día, ¿cuánto venderá en una semana?
precio_pan = 2500
ventas_diarias = 10
total_semanal = precio_pan * ventas_diarias * 7
print(f"La panadería venderá ${total_semanal} en una semana")