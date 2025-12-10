# 1.	Escribe un programa en Python que muestre la tabla de multiplicar del número 4, desde 4×1 hasta 4×10. El programa debe utilizar un bucle for y mostrar cada operación con su resultado.

print("Tabla del 4 - Multiplicacion")
for i in range(1, 11):
  resultado = 4 * i
  print(f"4 x {i} = {resultado}")

# 2.	Define una función que reciba cuatro números enteros como parámetros y determine cuál de ellos es el menor. No se permite usar funciones como min(), sino que debe hacerse mediante comparaciones con condicionales if.
def numero_menor(a, b, c, d):
  menor = a
  if b < menor:
    menor = b
  if c < menor:
    menor = c
  if d < menor:
    menor = d
  return print(f"El numero menor es {menor}")

numero_menor(2,4,6,8)

# 3.	Crea una función que reciba una lista de números enteros y devuelva una nueva lista que contenga solo los números pares de la lista original. Debe usarse un bucle y el operador módulo (%) para identificar si un número es par.

def filtrar_pares(lista):
  pares = []
  for numero in lista:
    if numero % 2 == 0:
      pares.append(numero)
  return pares

print(filtrar_pares([1,2,6,7,8,10]))

# 4.	Implementa una función que reciba una lista de valores numéricos y retorne su promedio. En caso de recibir una lista vacía, la función debe retornar 0 para evitar errores de división entre cero. La suma debe calcularse manualmente con un bucle.
def promedio_numero(lista):
  # Para evitar alguna division entre 0
  if len(lista) == 0:
    return 0
  #####################
  suma = 0
  for numero in lista:
    suma += numero
  return suma / len(lista)

print(promedio_numero([15,20,14,18]))

#5.	Desarrolla una función que recorra una lista utilizando un bucle while y determine si existe al menos un número par dentro de ella. La función debe regresar True al encontrar uno, y False si no hay ninguno.

def tiene_par(lista):
  i = 0
  while i < len(lista):
    if lista[i] % 2 == 0:
      return True
    i += 1    # i = i + 1
  return False

lista1 = [1,5,9,3]
lista2 = [1,4,9,3]

print(tiene_par(lista2))


# 6.	Dado un diccionario donde las llaves representan colores y los valores representan números, escribe un programa que recorra el diccionario usando un bucle for e imprima cada par clave–valor en pantalla.
# Diccionario -> clave : valor
colores = {
  "azul": 1,
  "verde": 3,
  "amarillo": 2
}

for color in colores:
  print(color, "->", colores[color])