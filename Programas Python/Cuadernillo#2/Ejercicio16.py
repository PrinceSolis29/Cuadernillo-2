class Ticket:
    def __init__(self, ticket_id, solicitante, prioridad):
        self.ticket_id = ticket_id
        self.solicitante = solicitante
        self.prioridad = prioridad.strip().upper()
        self.estado = "ABIERTO"

    def mismos_datos(self, otro):
        #Devuelve True si los atributos clave coinciden, aunque sean objetos distintos
        if not isinstance(otro, Ticket):
            return False
        return (self.ticket_id == otro.ticket_id and 
                self.solicitante == otro.solicitante and 
                self.prioridad == otro.prioridad)


# Demostración del comportamiento de Identidad vs Igualdad
if __name__ == "__main__":
    print("Ejemplos de identidad Vs Igualdad")
    
    # Caso 1: Dos objetos independientes con idéntica información
    t1 = Ticket(1, "Ana Lopez", "ALTA")
    t2 = Ticket(1, "Ana Lopez", "ALTA")
    
    # Caso 2: Una variable que apunta al primer objeto (Referencia)
    t3 = t1

    # Mostrando sus direcciones en memoria
    print(f"Dirección de memoria de t1: {id(t1)}")
    print(f"Dirección de memoria de t2: {id(t2)}")
    print(f"Dirección de memoria de t3: {id(t3)}\n")

    print("Ejemplos de operados y metodos")
    # t1 y t2 no son el mismo objeto en memoria
    print(f"¿t1 is t2? (¿Misma identidad?): {t1 is t2}")  # Esperado: False
    
    # t1 y t2 sí contienen la misma información interna
    print(f"¿t1.mismos_datos(t2)? (¿Mismo contenido?): {t1.mismos_datos(t2)}")  # Esperado: True
    
    # t1 y t3 apuntan exactamente a la misma celda de memoria
    print(f"¿t1 is t3? (¿Misma identidad por alias?): {t1 is t3}")  # Esperado: True
