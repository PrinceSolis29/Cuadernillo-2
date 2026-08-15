#Ejercicio 12: filtrar objetos por atributo
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
        return f" Ticket #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad} | Estado: {self.estado}"

#FUNCIÓN DE FILTRADO

def tickets_por_prioridad(tickets, prioridad):
    """Filtra y devuelve una nueva lista con los tickets de la prioridad dada."""
    lista_filtrada = []
    
    # Recorremos la lista y seleccionamos según la condición
    for ticket in tickets:
        if ticket.prioridad == prioridad.strip().upper():
            lista_filtrada.append(ticket)
            
    return lista_filtrada


#Pruebas
if __name__ == "__main__":
    print("--- CASO DE PRUEBA 1: FILTRAR TICKETS ---")

    # Lista de objetos Ticket ya creada (Entrada del problema)
    tickets_originales = [
        Ticket(101, "Sofía Castro", "ALTA"),
        Ticket(102, "Diego Ruiz", "BAJA"),
        Ticket(103, "Ana López", "MEDIA"),
        Ticket(104, "Carlos Mendoza", "ALTA")
    ]

    print("--- Ejecutando función de filtrado ---")
    # Invocamos la función con el parámetro requerido "ALTA"
    tickets_altas = tickets_por_prioridad(tickets_originales, "ALTA")

    print("\nSalida esperada (Lista con prioridad ALTA):")
    print("----------------------------------------------------------------")
    for t in tickets_altas:
        print(t)
    print("----------------------------------------------------------------")
    
    # Verificación extra para demostrar que la lista original no cambió
    print(f"\nVerificación de requisitos: Cantidad original sigue siendo {len(tickets_originales)}")
