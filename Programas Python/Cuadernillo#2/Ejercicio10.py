#Ejercicio 10: comparar dos ticket por atributo
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
        return f"🎫 Ticket #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad}"

    # ========================================================
    # EJERCICIO 10: COMPARACIÓN POR EL ATRIBUTO SOLICITANTE
    # ========================================================
    def __eq__(self, otro):
        """Compara si dos tickets son iguales según su solicitante."""
        if not isinstance(otro, Ticket):
            return False
        return self.solicitante == otro.solicitante


# ========================================================
# CASOS DE PRUEBA: COMPARACIÓN POR SOLICITANTE
# ========================================================
if __name__ == "__main__":
    print("--- CASOS DE PRUEBA: COMPARACIÓN POR SOLICITANTE ---")

    # Creamos instancias de prueba
    ticket_1 = Ticket(101, "Sofía Castro", "ALTA")
    ticket_2 = Ticket(102, "Sofía Castro", "BAJA")   # Mismo solicitante, diferente ID
    ticket_3 = Ticket(103, "Carlos Mendoza", "ALTA") # Diferente solicitante

    # Prueba 1: Mismo solicitante
    print(f"\n[Prueba 1] ¿ticket_1 tiene el mismo solicitante que ticket_2?:")
    print(f"Resultado: {ticket_1 == ticket_2}")  # Imprime: True

    # Prueba 2: Distinto solicitante
    print(f"\n[Prueba 2] ¿ticket_1 tiene el mismo solicitante que ticket_3?:")
    print(f"Resultado: {ticket_1 == ticket_3}")  # Imprime: False
