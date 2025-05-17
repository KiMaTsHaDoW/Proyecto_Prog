class Materia:
    def __init__(self, nombre, departamento):
        self.nombre = nombre
        self.departamento = departamento

    def __str__(self):
        return f"{self.nombre} - Departamento: {self.departamento}"
