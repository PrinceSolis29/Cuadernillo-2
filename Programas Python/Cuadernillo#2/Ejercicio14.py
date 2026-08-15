#Ejercicio 14: Estadisticas dentro de GestorTickets
class Ticket:
    PRIORIDADES_VALIDAS = ("BAJA", "MEDIA", "ALTA")

    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad.strip().upper()

    def __str__(self):
        return f"🎫 Ticket #{self.ticket_id} ({self.prioridad})"


class GestorTickets:
    def __init__(self):
        self._tickets = []

    def agregar_ticket(self, ticket):
        self._tickets.append(ticket)

    #MÉTODO DE ESTADÍSTICAS
  
    def estadisticas_por_prioridad(self):
        """Devuelve un diccionario con el conteo por cada prioridad."""
        # Se inicializan en 0 para cumplir el requisito de gestor vacío
        conteo = {"BAJA": 0, "MEDIA": 0, "ALTA": 0}
        
        for t in self._tickets:
            if t.prioridad in conteo:
                conteo[t.prioridad] += 1
                
        return conteo


#PRUEBAS
if __name__ == "__main__":
    print("--- EJECUTANDO CASOS DE PRUEBA DEL EJERCICIO 14 ---")

   
    # Caso 2: Entrada - Gestor Vacío
   
    print("\n[Caso 2] Entrada: Gestor vacío")
    gestor_vacio = GestorTickets()
    resultado_vacio = gestor_vacio.estadisticas_por_prioridad()
    print(f"Salida esperada: {resultado_vacio}") 
    # Debe imprimir: {'BAJA': 0, 'MEDIA': 0, 'ALTA': 0}

  
    # Caso 1: Entrada - Gestor con Tickets Cargados
   
    print("\n[Caso 1] Entrada: Gestor con tickets cargados")
    gestor_lleno = GestorTickets()
    
    # Cargamos datos de prueba con diferentes prioridades
    gestor_lleno.agregar_ticket(Ticket(101, "Sofía Castro", "ALTA"))
    gestor_lleno.agregar_ticket(Ticket(102, "Diego Ruiz", "BAJA"))
    gestor_lleno.agregar_ticket(Ticket(103, "Ana López", "MEDIA"))
    gestor_lleno.agregar_ticket(Ticket(104, "Carlos Mendoza", "ALTA"))

    resultado_lleno = gestor_lleno.estadisticas_por_prioridad()
    print(f"Salida esperada: {resultado_lleno}")
    # Debe imprimir: {'BAJA': 1, 'MEDIA': 1, 'ALTA': 2}
