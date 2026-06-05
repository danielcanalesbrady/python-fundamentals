#El bucle "for" se usa para iterar (recorrer) una secuencia: una lista, una cadena, un rango, etc.

#Ejemplo 1: recorrer una lista
""" frutas = ["manzana","pera","uva"]
for fruta in frutas:
    print(fruta) """

#Ejemplo 2: recorrer un string(carácter por carácter)
""" for letra in "Python":
    print(letra) """

#Ejemplo 3: usar range() para repetir un número de veces
""" for i in range(5):
    print(i) """

#Ejemplo 4: range(inicio, fin, paso)
""" for i in range(2,10,2):
    print(i)  """

#1 Escribe un bucle for que imprima los números del 1 al 10 (incluido).

""" for i in range(1,11,1):
    print(i) """

#2 Dada una lista colores = ["rojo", "verde","azul","amarillo"]
""" colores =["rojo", "verde","azul","amarillo"] 

for color in colores:
    longitud = len(color)
    print(f"{color} -> {longitud}") """

#3 Usando range() imprime todos los números pares entre 2 y 20 (inclusive).
""" for i in range(2,21,2):
    print(i) """

#4 Pide al usuario un número entero n. Luego usa un bucle for para imprimir la tabla de multiplicar de ese número (del 1 al 10).

""" usuarios = ["Daniel","peo","s"]
x,y,z = usuarios

print(x)
print(y)
print(z) """


