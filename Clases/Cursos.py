class Curso:
    def __init__(self, anio, nivel):
        self.anio = anio
        self.nivel = nivel

    def __str__(self):
        return f"Año: {self.anio} - Nivel: {self.nivel}"
