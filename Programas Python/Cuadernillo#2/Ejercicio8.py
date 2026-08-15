class Ticket:
    # Atributos de clase (Ejercicio 7)
    PRIORIDADES_VALIDAS = ("BAJA", "MEDIA", "ALTA")
    ESTADOS_VALIDOS = ("ABIERTO", "EN_PROCESO", "RESUELTO")

    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"
        
        # Usamos la normalización desde el constructor
        prioridad_normalizada = self._normalizar(prioridad)
        if prioridad_normalizada not in Ticket.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        self.prioridad = prioridad_normalizada

    # MÉTODO PRIVADO
    def _normalizar(self, valor):
        """Aplica limpieza de espacios y convierte a mayúsculas."""
        return valor.strip().upper()

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado reutilizando el método privado."""
        estado_normalizado = self._normalizar(nuevo_estado)
        if estado_normalizado in Ticket.ESTADOS_VALIDOS:
            self.estado = estado_normalizado
            return True
        return False

    def cambiar_prioridad(self, nueva_prioridad):
        """Cambia la prioridad reutilizando el método privado."""
        prioridad_normalizada = self._normalizar(nueva_prioridad)
        if prioridad_normalizada in Ticket.PRIORIDADES_VALIDAS:
            self.prioridad = prioridad_normalizada
            return True
        return False
    
# PRUEBAS DEL CASO DE USO
if __name__ == "__main__":
    mi_ticket = Ticket(1, "Ana Lopez", "alta")
    
    # Probando la normalización indirecta con espacios y minúsculas
    print("¿Test _normalizar en estado?:", mi_ticket.cambiar_estado("   en_proceso   "))
    print("Estado actual:", mi_ticket.estado)
    
    print("¿Test _normalizar en prioridad?:", mi_ticket.cambiar_prioridad("   baja   "))
    print("Prioridad actual:", mi_ticket.prioridad)
    print("fin del programa")
