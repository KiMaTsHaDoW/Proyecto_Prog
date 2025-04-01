from datetime import datetime
from clases.constantes import *


class ACL:
    def __init__(self, FechaPrestamo:datetime, FechaDevolucion:datetime, estado: ENTREGADO | DEVOLVER):
        self.FechaPrestamo = FechaPrestamo
        self.FechaDevolucion = FechaDevolucion
        self.Estado = estado