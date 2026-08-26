#Ejercicio 2: Metodo __str__ para comentario
class Comentario:
    def __init__(self, autor, texto):
        if not texto or texto.strip() == "":
            raise ValueError("El texto del comentario no puede estar vacío")
            
        self._autor = autor
        self._texto = texto.strip()

    #entra el ejercicio 2
    def __str__(self):
        # Concatenamos el nombre del autor y el texto del comentario
        return f"{self._autor.nombre}: {self._texto}"
#imprimir en consola
if __name__ == "__main__":
    # Creamos un usuario
    class UsuarioDummy:
        def __init__(self, nombre):
            self.nombre = nombre

    usuario_ana = UsuarioDummy("Ana Lopez")
    
    # Creamos el comentario
    mi_comentario = Comentario(usuario_ana, "Se revisó el equipo")
    
    print("Prueba __str__ ---")
    # Al imprimir el objeto, Python llama automáticamente a __str__
    print(mi_comentario) 
