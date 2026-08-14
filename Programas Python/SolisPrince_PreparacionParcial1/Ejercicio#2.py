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
#        if opc == 5:
#            print("Saliendo del programa...")
        if opc == 1:
            print("\n--- REGISTRAR TICKET ---")
            try:
                id_t = int(input("ID: "))
                sol = input("Solicitante: ").strip()
                tit = input("Título: ").strip()
                prio = input("Prioridad (Low/Medium/High/Critical): ").strip()
                
                if not sol or not tit:
                    print("Error: Campos obligatorios vacíos.")
                    continue
                    
                lista_tickets.append({"id": id_t, "solicitante": sol, "titulo": tit, "prioridad": prio, "status": "Open"})
                print("Ticket agregado con éxito.")
            except ValueError:
                print("ID inválido.")
