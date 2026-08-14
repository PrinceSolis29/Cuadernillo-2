# Ejercicio#2.py - Menú HelpDesk EDU

lista_tickets = []  # Lista global en memoria

def ejecutar_menu():
    while True:
        print("\n========== MENÚ HELPDESK EDU ==========")
        print("1. Registrar Ticket")
        print("2. Listar Tickets")
        print("3. Buscar por Solicitante")
        print("4. Resumen por Prioridad")
        print("5. Salir")
        
        try:
            opc = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            print("Opción inválida.")
            continue

