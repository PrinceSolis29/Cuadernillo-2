#ejercicio 3: Modelo orientado a objetos
# Ejercicio#3.py - Modelos POO HelpDesk EDU

class Usuario:
    def __init__(self, id_usuario, nombre, email, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol  # Puede ser 'student' o 'technician'

    def __str__(self):
        return f"Usuario [{self.rol.upper()}]: {self.nombre} (Email: {self.email})"
