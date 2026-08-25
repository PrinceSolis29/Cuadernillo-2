#Ejercicio 20: Cierre integrador: asignación de técnicos y reporte de carga
class Usuario:
    def __init__(self, nom, mail, tipo):
        self.nom = nom
        self.mail = mail
        self.tipo = tipo

    def datos_contacto(self):
        return f"{self.nom} ({self.mail})"


class Ticket:
    total_creados = 0
    prioridades = ["BAJA", "MEDIA", "ALTA"]

    def __init__(self, u, prioridad):
        p = prioridad.strip().upper()
        if p not in self.prioridades:
            raise ValueError("La prioridad no es valida")
        
        Ticket.total_creados += 1
        self.id = Ticket.total_creados
        self.usr = u
        self.prioridad = p
        self.estado = "ABIERTO"
        self._coms = []
        
        # Propiedad del ejercicio 20
        self.tecnico = None

    def asignar_tecnico(self, u_tecnico):
        if u_tecnico.tipo == "tecnico":
            self.tecnico = u_tecnico
            return True
        return False

    def __str__(self):
        info_usr = self.usr.datos_contacto()
        tec_nom = self.tecnico.nom if self.tecnico else "Sin asignar"
        return f"#{self.id} - {info_usr} - {self.prioridad} - Encargado: {tec_nom}"


class GestorTickets:
    def __init__(self):
        self._tickets = []

    def agregar_ticket(self, t):
        self._tickets.append(t)

    def carga_por_tecnico(self):
        carga = {}
        for t in self._tickets:
            if t.tecnico is not None:
                nom_tec = t.tecnico.nom
                if nom_tec in carga:
                    carga[nom_tec] += 1
                else:
                    carga[nom_tec] = 1
        return carga

    def tickets_sin_asignar(self):
        sin_asignar = []
        for t in self._tickets:
            if t.tecnico is None:
                sin_asignar.append(t)
        return sin_asignar


# --- PRUEBAS DEL CIERRE INTEGRADOR (Ejecución Directa) ---
# Usuarios base
usr_ana = Usuario("Ana Lopez", "ana@umg.edu.gt", "solicitante")
tec_luis = Usuario("Luis Perez", "luis@umg.edu.gt", "tecnico")

# Creamos el gestor y 3 tickets
gestor = GestorTickets()
t1 = Ticket(usr_ana, "alta")
t2 = Ticket(usr_ana, "media")
t3 = Ticket(usr_ana, "baja")

gestor.agregar_ticket(t1)
gestor.agregar_ticket(t2)
gestor.agregar_ticket(t3)

print("--- ejecutando casos de prueba ---")

# Caso 1: Intentar asignar a un solicitante (Debe dar False)
ok_c1 = t1.asignar_tecnico(usr_ana)
print("¿Asignado a Ana (solicitante)?:", ok_c1)

# Caso 2: Asignar a un tecnico real (Debe dar True)
ok_c2 = t1.asignar_tecnico(tec_luis)
print("¿Asignado a Luis (tecnico)?:", ok_c2)

# Caso 3: Asignar un segundo ticket a Luis para cumplir la prueba de carga (2 para Luis, 1 libre)
t2.asignar_tecnico(tec_luis)

print("\n--- reporte final del gestor ---")
print("carga por tecnico:", gestor.carga_por_tecnico())

pendientes = gestor.tickets_sin_asignar()
print(f"tickets sin asignar ({len(pendientes)} pendientes):")
for p in pendientes:
    print("  *", p)
