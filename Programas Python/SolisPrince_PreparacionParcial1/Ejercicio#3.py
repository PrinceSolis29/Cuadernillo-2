#ejercicio 3: Modelo orientado a objetos

#clase Usuario para representar a los usuarios del sistema
class Usuario:
    def __init__(self, id_usuario, nombre, email, rol):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol  # Puede ser 'student' o 'technician'
    #definir el método __str__ para representar al usuario como una cadena legible
    def __str__(self):
        return f"Usuario [{self.rol.upper()}]: {self.nombre} (Email: {self.email})"
#clase Ticket para representar los tickets de soporte
class Ticket:
    def __init__(self, id_ticket, titulo, categoria, prioridad, solicitante):
        self.id_ticket = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante  # Guarda un objeto de tipo Usuario
        self.tecnico_asignado = None   # Inicia vacio (asociacion opcional)
        self._status = "Open"          # Atributo encapsulado interno
    #definir propiedades para acceder y modificar el estado del ticket
    def asignar_tecnico(self, tecnico):
        #if rol del tecnico
        if tecnico.rol.lower() == "technician":
            self.tecnico_asignado = tecnico
            print(f"Técnico {tecnico.nombre} asignado con éxito al Ticket #{self.id_ticket}.")
        else:
            print(f"Error de Asignación: El usuario {tecnico.nombre} no tiene el rol de 'technician'.")
    def cambiar_estado(self, nuevo_estado):
        estados_validos = ["Open", "In Progress", "Resolved", "Closed", "Cancelled"]
        if nuevo_estado in estados_validos:
            self._status = nuevo_estado
            print(f"Estado del Ticket #{self.id_ticket} cambiado a: {nuevo_estado}")
        else:
            print(f"Error: '{nuevo_estado}' no es un estado válido.")

    def __str__(self):
        tec_nombre = self.tecnico_asignado.nombre if self.tecnico_asignado else "Ninguno"
        return f"Ticket #{self.id_ticket} - Título: {self.titulo} | Estado: {self._status} | Técnico: {tec_nombre}"

if __name__ == "__main__":
    print("--- DEMOSTRACIÓN DE POO HELPDESK EDU ---")
    # Instanciar usuarios reales
    alumno = Usuario(1, "Carlos Gómez", "cgomez@miumg.edu.gt", "student")
    ingeniero = Usuario(2, "Ing. Marta Ruiz", "mruiz@miumg.edu.gt", "technician")
    
    # Crear e interactuar con el Ticket
    ticket_prueba = Ticket(101, "Error de acceso a Blackboard", "Software", "High", alumno)
    print(ticket_prueba)
    
    ticket_prueba.asignar_tecnico(ingeniero)
    ticket_prueba.cambiar_estado("In Progress")
    print(ticket_prueba)
