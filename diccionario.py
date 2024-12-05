# Solución
alumno = {
    "nombre": "Juan",
    "edad": 20,
    "curso": "Matemáticas"
}

# Imprimir el diccionario
print(alumno)

# Solución
print(alumno["nombre"])  # Imprime: Juan

# Solución
alumno["nota"] = 8.5
print(alumno)

# Solución
del alumno["curso"]
print(alumno)

# Solución
for clave, valor in alumno.items():
    print(clave, ":", valor)
            
# Solución
clase = {
    "alumno1": {"nombre": "Ana", "edad": 21, "nota": 9.0},
    "alumno2": {"nombre": "Carlos", "edad": 22, "nota": 7.5}
}

# Imprimir el diccionario completo
print(clase)

# Solución
clase["alumno1"]["nota"] = 9.5
print(clase["alumno1"])
