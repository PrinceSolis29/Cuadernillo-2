class Ticket:
    # Atributos de clase
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

    def cambiar_estado(self, nuevo_estado):
        estado_normalizado = self._normalizar(nuevo_estado)
        if estado_normalizado in Ticket.ESTADOS_VALIDOS:
            self.estado = estado_normalizado
            return True
        return False

    def cambiar_prioridad(self, nueva_prioridad):
        prioridad_normalizada = self._normalizar(nueva_prioridad)
        if prioridad_normalizada in Ticket.PRIORIDADES_VALIDAS:
            self.prioridad = prioridad_normalizada
            return True
        return False

    
    # MÉTODO ESPECIAL STR
    
    def __str__(self):
        """Devuelve una representación legible y ordenada del objeto."""
        return f"Ticket #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad} | Estado: {self.estado}"



# PRUEBAS DEL CASO DE USO

if __name__ == "__main__":
    # Creamos el ticket
    mi_ticket = Ticket(104, "Ana Lopez", "media")
    
    # Imprimimos el objeto directamente (invoca automáticamente a __str__)
    print("--- Mostrando representación del objeto ---")
    print(mi_ticket)
    
    # Hacemos un cambio para ver cómo se actualiza la impresión
    mi_ticket.cambiar_estado("en_proceso")
    print("\n--- Después de cambiar el estado ---")
    print(mi_ticket)
