#Ejercicio17: Contador de tickets con atributo de clase mutable
class Ticket:
    # Atributos de clase
    total_creados = 0  # Contador global compartido por todas las instancias
    PRIORIDADES_VALIDAS = ["BAJA", "MEDIA", "ALTA"]
    ESTADOS_VALIDOS = ["ABIERTO", "EN_PROCESO", "RESUELTO"]

    def __init__(self, solicitante, prioridad):
        # 1. Validar y normalizar primero
        prioridad_norm = self._normalizar(prioridad)
        if prioridad_norm not in self.PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridad inválida. Debe ser una de: {self.PRIORIDADES_VALIDAS}")
        
        # 2. Modificar el atributo de clase e identificar la instancia SOLO si es válido
        Ticket.total_creados += 1
        self.ticket_id = Ticket.total_creados
        
        # 3. Asignación de atributos de instancia
        self.solicitante = solicitante
        self.prioridad = prioridad_norm
        self.estado = "ABIERTO"

    def _normalizar(self, valor):
        return valor.strip().upper()

    def __str__(self):
        return f"#{self.ticket_id} | {self.solicitante} | {self.prioridad} | {self.estado}"


# Bloque de pruebas (Casos de prueba del cuadernillo)
if __name__ == "__main__":
    print("--- CASO DE PRUEBA 1: Creación de tickets válidos ---")
    try:
        t1 = Ticket("Ana Lopez", "alta")
        t2 = Ticket("Carlos Gómez", "media")
        t3 = Ticket("Mario Ruiz", "baja")
        
        print(t1)
        print(t2)
        print(t3)
        print(f"Total de tickets creados exitosamente: {Ticket.total_creados}") # Esperado: 3
    except ValueError as e:
        print(f"Error inesperado: {e}")

    print("\nPrueba 2: Intento con prioridad inválida")
    try:
        t4 = Ticket("Luis Perez", "urgente")  # Debe lanzar ValueError
    except ValueError as e:
        print(f"Capturado correctamente el error esperado: {e}")
    
    # Comprobación final de que el contador no se movió tras el fallo
    print(f"Contador final no cambia: {Ticket.total_creados}") # Esperado: 3
