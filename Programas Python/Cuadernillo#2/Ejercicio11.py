#Ejercicio 11: Lista de objetos ticket
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
        return f"Ticket #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad} | Estado: {self.estado}"

if __name__ == "__main__":
    print("--- CASO DE PRUEBA 1: LISTA DE OBJETOS TICKET ---")

    # 1. Crear y almacenar múltiples objetos de la misma clase en una lista
    lista_tickets = []
    
    lista_tickets.append(Ticket(101, "Sofía Castro", "alta"))
    lista_tickets.append(Ticket(102, "Diego Ruiz", "baja"))
    lista_tickets.append(Ticket(103, "Ana López", "media"))
    lista_tickets.append(Ticket(104, "Carlos Mendoza", "alta"))

    print(f"Entrada: {len(lista_tickets)} tickets creados y guardados en la colección.\n")
    print("Salida esperada:")
    print("----------------------------------------------------------------")
    
    # 2. Recorrer la lista con un ciclo for y mostrar el resumen usando print(ticket)
    for ticket in lista_tickets:
        print(ticket)
        
    print("----------------------------------------------------------------")
