#Ejercicio 18: un ticket que contiene un objeto usuario
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

    def __str__(self):
        info_usr = self.usr.datos_contacto()
        return f"#{self.id} - {info_usr} - {self.prioridad} - {self.estado}"


if __name__ == "__main__":
    # creando datos de prueba basicos
    u1 = Usuario("Ana Lopez", "ana@umg.edu.gt", "solicitante")
    
    t1 = Ticket(u1, "alta")
    t2 = Ticket(u1, "media")
    
    print("ticket 1:", t1)
    print("ticket 2:", t2)
    print("mismo usuario?:", t1.usr is t2.usr)
