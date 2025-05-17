class Curso:
    def __init__(self, ano, nivel):
        self.ano = ano
        self.nivel = nivel

    def __str__(self):
        return f"Año: {self.ano} - Nivel: {self.nivel}"
