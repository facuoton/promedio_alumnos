class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

alumnos = [Alumno('Juan', 10), Alumno('Maria', 8), Alumno('Pedro', 9)]

def calcular_promedio(alumnos):
    suma = 0
    for alumno in alumnos:
        suma += alumno.nota
    return suma / len(alumnos)

print(f"El promedio de notas es: {calcular_promedio(alumnos)}")
