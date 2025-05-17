class ACL:
    def __init__(self, fecha_prestamo, fecha_devolucion=None, estado='entregado'):
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion
        self.estado = estado  # 'entregado', 'por devolver'

    def __str__(self):
        return f"Préstamo: {self.fecha_prestamo} - Devolución: {self.fecha_devolucion} - Estado: {self.estado}"
