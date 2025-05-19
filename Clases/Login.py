from Clases.constantes import USER, PASSWORD

class Login:
    @staticmethod
    def iniciar_sesion():
        print('-' * 5, 'Inicio Sesion', '-' * 5)
        user = input('Usuario: ')
        password = input('Contraseña: ')
        if user == USER and password == PASSWORD :
            return True
        else:
            return False # 'Credenciales incorrectas'