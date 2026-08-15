#Ejercicio 13: Clase GestorTickets que encapsula la coleccion
class Ticket:
    PRIORIDADES_VALIDAS = ("BAJA", "MEDIA", "ALTA")
    ESTADOS_VALIDOS = ("ABIERTO", "EN_PROCESO", "RESUELTO")

    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"
        
        prioridad_normalizada = self._normalizar(prioridad)
        if prioridad_normalizada not in Ticket.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        self.prioridad = prioridad_normalizada

    def _normalizar(self, valor):
        return valor.strip().upper()

    def __str__(self):
        return f" Ticket #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad}"


# ========================================================
# EJERCICIO 13: CLASE GESTOR DE TICKETS
# ========================================================
class GestorTickets:
    def __init__(self):
        # Atributo interno encapsulado que inicia vacío
        self._tickets = []

    def agregar_ticket(self, ticket):
        """Agrega un objeto Ticket a la lista interna usando append()."""
        self._tickets.append(ticket)

    def buscar_por_id(self, ticket_id):
        """Busca un ticket por su ID. Devuelve None si no existe."""
        for t in self._tickets:
            if t.ticket_id == ticket_id:
                return t
        return None

    def listar_tickets(self):
        """Muestra todas las instancias guardadas en el gestor."""
        for t in self._tickets:
            print(t)


# ========================================================
# CASOS DE PRUEBA OFICIALES
# ========================================================
if __name__ == "__main__":
    # Creamos el gestor del sistema
    gestor = GestorTickets()

    # Caso de prueba 1: Agregar un ticket y luego buscar por ID
    print("--- CASO DE PRUEBA 1 ---")
    nuevo_ticket = Ticket(501, "Esteban Quito", "MEDIA")
    gestor.agregar_ticket(nuevo_ticket)
    
    print("Entrada: Buscar ID 501 tras haber sido agregado.")
    ticket_encontrado = gestor.buscar_por_id(501)
    print(f"Salida esperada: {ticket_encontrado}")

    # Caso de prueba 2: Buscar por un ID inexistente
    print("\n--- CASO DE PRUEBA 2 ---")
    print("Entrada: Buscar ID 999 (Inexistente).")
    ticket_fantasma = gestor.buscar_por_id(999)
    print(f"Salida esperada: {ticket_fantasma}")