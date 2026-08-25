#Ejercicio 19: Encapsulamiento del historial de comentarios
class Usuario:
    def __init__(self, nom, mail, tipo):
        self.nom = nom
        self.mail = mail
        self.tipo = tipo

    def datos_contacto(self):
        return f"{self.nom} ({self.mail})"


class Ticket:
    total_creados = 0
    prioridades = ["BAJA", "MEDIA", "ALTA"]

    def __init__(self, u, prioridad):
        p = prioridad.strip().upper()
        if p not in self.prioridades:
            raise ValueError("La prioridad no es valida")
        
        Ticket.total_creados += 1
        self.id = Ticket.total_creados
        self.usr = u
        self.prioridad = p
        self.estado = "ABIERTO"
        
        # Lista interna con guion bajo para encapsular (ocultar) los comentarios
        self._coms = []

    def agregar_comentario(self, autor, texto):
        # Si el texto esta vacio o solo tiene espacios, lo rechaza
        if not texto.strip():
            return False
            
        self._coms.append(f"[{autor}]: {texto.strip()}")
        return True

    def cantidad_comentarios(self):
        return len(self._coms)

    def obtener_comentarios(self):
        # Retorna una copia exacta (.copy()) para que nadie pueda alterar la original desde fuera
        return self._coms.copy()

    def __str__(self):
        info_usr = self.usr.datos_contacto()
        return f"#{self.id} - {info_usr} - {self.prioridad} - {self.estado}"


u1 = Usuario("Ana Lopez", "ana@umg.edu.gt", "solicitante")
t = Ticket(u1, "alta")

# Prueba 1: Meter un comentario bueno
ok1 = t.agregar_comentario("Luis Perez", "Equipo revisado")
print("comentario 1 guardado?:", ok1, "| total:", t.cantidad_comentarios())

# Prueba 2: Intentar meter uno vacio
ok2 = t.agregar_comentario("Luis Perez", "   ")
print("comentario 2 guardado?:", ok2, "| total:", t.cantidad_comentarios())

# Prueba 3: Intentar romper el encapsulamiento
lista_afuera = t.obtener_comentarios()
lista_afuera.clear() # Intentamos borrar los comentarios desde afuera

print("total despues del soborno de lista:", t.cantidad_comentarios()) # Sigue siendo 1
print("comentarios reales:", t.obtener_comentarios())
