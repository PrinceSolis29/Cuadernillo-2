#ejercicio#6: metodo cambiar prioridad con validacion
class Ticket:
    # Atributos de clase (Catálogos compartidos)
    PRIORIDADES_VALIDAS = ("BAJA", "MEDIA", "ALTA")
    ESTADOS_VALIDOS = ("ABIERTO", "EN_PROCESO", "RESUELTO")

    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"  # Estado inicial automático
        
        # Validación inicial en el constructor 
        prioridad_normalizada = prioridad.strip().upper()
        if prioridad_normalizada not in Ticket.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        self.prioridad = prioridad_normalizada

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del ticket si es válido (Ejercicio 5)."""
        estado_normalizado = nuevo_estado.strip().upper()
        if estado_normalizado in Ticket.ESTADOS_VALIDOS:
            self.estado = estado_normalizado
            return True
        return False

    def cambiar_prioridad(self, nueva_prioridad):
        """Cambia la prioridad del ticket si pertenece al catálogo """
        prioridad_normalizada = nueva_prioridad.strip().upper()
        if prioridad_normalizada in Ticket.PRIORIDADES_VALIDAS:
            self.prioridad = prioridad_normalizada
            return True
        return False

# PRUEBAS DE LOS CASOS DE USO
if __name__ == "__main__":
    # Creamos un ticket inicial válido (Prioridad ALTA)
    mi_ticket = Ticket(1, "Ana Lopez", "alta")
    print(f"Ticket creado -> Prioridad actual: {mi_ticket.prioridad}")

    # Caso de prueba 1: Cambiar a una prioridad válida
    resultado1 = mi_ticket.cambiar_prioridad("media")
    print(f"¿Cambio exitoso ('media')?: {resultado1} | Nueva prioridad: {mi_ticket.prioridad}")

    # Caso de prueba 2: Intentar cambiar a una prioridad inválida
    resultado2 = mi_ticket.cambiar_prioridad("urgente")
    print(f"¿Cambio exitoso ('urgente')?: {resultado2} | Prioridad se mantiene: {mi_ticket.prioridad}")
