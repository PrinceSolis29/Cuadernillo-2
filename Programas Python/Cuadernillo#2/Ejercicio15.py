#Ejercicio 15: Mini proyecto integrado
class Ticket:
    PRIORIDADES_VALIDAS = ("BAJA", "MEDIA", "ALTA")

    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.estado = "ABIERTO"
        
        # Validación estricta que lanza ValueError si no pertenece al catálogo
        prioridad_normalizada = prioridad.strip().upper()
        if prioridad_normalizada not in Ticket.PRIORIDADES_VALIDAS:
            raise ValueError(f"La prioridad '{prioridad}' no es válida.")
        self.prioridad = prioridad_normalizada

    def __str__(self):
        return f"Ticket #{self.ticket_id} | Solicitante: {self.solicitante} | Prioridad: {self.prioridad} | Estado: {self.estado}"


class GestorTickets:
    def __init__(self):
        self._tickets = []

    def agregar_ticket(self, ticket):
        self._tickets.append(ticket)

    def buscar_por_id(self, ticket_id):
        for t in self._tickets:
            if t.ticket_id == ticket_id:
                return t
        return None

    def listar_tickets(self):
        if not self._tickets:
            print("No hay tickets registrados en el sistema.")
            return
        for t in self._tickets:
            print(t)

    def estadisticas_por_prioridad(self):
        conteo = {"BAJA": 0, "MEDIA": 0, "ALTA": 0}
        for t in self._tickets:
            if t.prioridad in conteo:
                conteo[t.prioridad] += 1
        return conteo
    
# PROYECTO INTEGRADOR: MENÚ INTERACTIVO PRINCIPAL

if __name__ == "__main__":
    gestor = GestorTickets()
    
    while True:
        print("\n--- HelpDesk EDU - Sistema de Tickets O.O. ---")
        print("1. Registrar ticket")
        print("2. Listar tickets")
        print("3. Buscar por ID")
        print("4. Ver estadísticas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción (1-5): ").strip()
        
        if opcion == "1":
            print("\n[Registro de Nuevo Ticket]")
            try:
                t_id = int(input("Ingrese el ID numérico del ticket: "))
                solicitante = input("Ingrese el nombre del solicitante: ")
                prioridad = input("Ingrese la prioridad (BAJA, MEDIA, ALTA): ")
                
                # REQUISITO: Bloque try/except para evitar que se caiga el programa
                nuevo_ticket = Ticket(t_id, solicitante, prioridad)
                gestor.agregar_ticket(nuevo_ticket)
                print("¡Ticket registrado exitosamente!")
                
            except ValueError as e:
                print(f"Error de Validación: {e} El ticket no fue registrado.")
                
        elif opcion == "2":
            print("\n[Listado General de Tickets]")
            gestor.listar_tickets()
            
        elif opcion == "3":
            print("\n[Búsqueda de Ticket]")
            try:
                id_buscar = int(input("Ingrese el ID del ticket a buscar: "))
                resultado = gestor.buscar_por_id(id_buscar)
                if resultado:
                    print(f"Encontrado -> {resultado}")
                else:
                    print("No se encontró ningún ticket con ese ID.")
            except ValueError:
                print("Por favor, ingrese un ID numérico válido.")
                
        elif opcion == "4":
            print("\n[Estadísticas de Carga de Trabajo]")
            resumen = gestor.estadisticas_por_prioridad()
            for prio, cant in resumen.items():
                print(f"• Prioridad {prio}: {cant} ticket(s)")
                
        elif opcion == "5":
            print("\n¡Gracias por utilizar HelpDesk EDU! Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo con un número del 1 al 5.")
