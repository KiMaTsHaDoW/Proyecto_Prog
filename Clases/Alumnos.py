class Alumno:
    def __init__(self, nombre, apellidos, tramo_concedido, seccion):
        self.nombre = nombre
        self.apellidos = apellidos
        self.tramo_concedido = tramo_concedido
        self.seccion = seccion

    def __str__(self):
        return f"{self.nombre} {self.apellidos} - Tramo: {self.tramo_concedido} - Sección: {self.seccion}"
