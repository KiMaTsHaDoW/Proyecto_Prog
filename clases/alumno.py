class Alumno:
    def __init__(self, Nombre:str, Apellidos:str, TramoConcedido:str, Seccion):
        self.Nombre = Nombre
        self.Apellidos = Apellidos
        self.TramoConcedido = TramoConcedido
        self.Seccion = Seccion

    def __str__(self):
        return f'{self.Nombre}:{self.Apellidos}:{self.TramoConcedido}:{self.Seccion}'
