#Ejercicio 1: registro de un ticket por consola
# Ejercicio#1.py - Registro de Ticket HelpDesk EDU

def registrar_ticket():
    print("--- REGISTRO DE TICKET (HelpDesk EDU) ---")
    
    categorias_validas = ["General", "Hardware", "Software", "Network"]
    prioridades_validas = ["Low", "Medium", "High", "Critical"]
    
    # Validar el Número de Ticket (Entero)
    try:
        id_ticket = int(input("Ingrese el número de ticket: ").strip())
    except ValueError:
        print("Error: El ID del ticket debe ser un número entero.")
        return
