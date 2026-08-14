# Ejercicio#2.py - Menú HelpDesk EDU
lista_tickets = []
def ejecutar_menu():
    while True:
        print("\n========== MENÚ HELPDESK EDU ==========")
        print("1. Registrar Ticket\n2. Listar Tickets\n3. Buscar\n4. Reporte\n5. Salir")
        try:
            opc = int(input("Seleccione una opción (1-5): "))
        except ValueError:
            continue
