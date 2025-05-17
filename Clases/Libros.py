class Libro:
    def __init__(self, titulo, autor, isbn, numero_ejemplares):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.numero_ejemplares = numero_ejemplares

    def __str__(self):
        return f"{self.titulo} by {self.autor} - ISBN: {self.isbn} - Ejemplares: {self.numero_ejemplares}"
