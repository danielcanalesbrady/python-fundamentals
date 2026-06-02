# Ejercicio de Variables y Tipos de Datos

# 1. Números (enteros y decimales)
edad = 25
altura = 1.75
precio = 99.90 

print("--- NÚMEROS ---")
print("Edad (entero):", edad, "-> Tipo:", type(edad))
print("Altura (float):", altura, "-> Tipo:", type(altura))
print("Precio (float):", precio, "-> Tipo:", type(precio))

# 2. Texto (strings)
nombre = "María"
ciudad = "Buenos Aires"
print("\n--- TEXTO ---")
print("Nombre:", nombre, "-> Tipo:", type(nombre))
print("Ciudad:", ciudad, "-> Tipo:", type(ciudad))

# 3. Booleanos (Verdadero/Falso)
es_estudiante = True
tiene_trabajo = False
print("\n--- BOOLEANOS ---")
print("¿Es estudiante?", es_estudiante, "-> Tipo:", type(es_estudiante))
print("¿Tiene trabajo?", tiene_trabajo, "-> Tipo:", type(tiene_trabajo))

# 4. Operaciones con diferentes tipos
print("\n--- OPERACIONES ---")
print("Edad + 5:", edad + 5)
print("Altura + 0.25:", altura + 0.25)
print("Nombre + ' Pérez':", nombre + " Pérez")
print("¿Es mayor de edad?", edad >= 18)