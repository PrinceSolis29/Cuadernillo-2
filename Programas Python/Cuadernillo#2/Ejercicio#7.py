#Ejercicio 7: atributos de clase compartidos
class Ticket:
   #class ticket 
    PRIORIDADES_VALIDAS = ("BAJA", "MEDIA", "ALTA")
    ESTADOS_VALIDOS = ("ABIERTO", "EN_PROCESO", "RESUELTO")

    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"
        
        # Validación usando el atributo de clase 
        prioridad_normalizada = prioridad.strip().upper()
        if prioridad_normalizada not in Ticket.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridad inválida: {prioridad}")
        self.prioridad = prioridad_normalizada
#if
if __name__ == "__main__":
    # Acceso directo desde la clase, sin crear ningún objeto Ticket
    print(Ticket.ESTADOS_VALIDOS)
    
    
