# --- CLASE DEL EJERCICIO 1 ---
class Comentario:
    def __init__(self, autor, texto):
        if not texto or texto.strip() == "":
            raise ValueError("El texto del comentario no puede estar vacío")
            
        self._autor = autor
        self._texto = texto.strip()

if __name__ == "__main__":
    # Creamos un objeto de usuario simulado para la prueba
    class UsuarioDummy:
        def __init__(self):
            self.nombre = "Ana Lopez"
            
    usuario_de_prueba = UsuarioDummy()


    # CASO 1: Entrada con texto válido
    print("\nEjecutando Caso 1...")
    try:
        comentario1 = Comentario(usuario_de_prueba, "Se revisó el equipo")
        print("Resultado: Se creó sin error")
    except ValueError as e:
        print(f"Resultado incorrecto: {e}")

    # CASO 2: Entrada con espacios vacíos
    print("\nEjecutando Caso 2...")
    try:
        comentario2 = Comentario(usuario_de_prueba, "			")
        print("Resultado incorrecto: Se creó el comentario pero debía fallar.")
    except ValueError as e:
        print("Resultado: Se lanzó ValueError")
