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
#elif opc == 2:
        elif opc == 2:
            # Listar Tickets
            print("\n--- LISTADO DE TICKETS ---")
            if not lista_tickets:
                print("No hay tickets registrados.")
                #for t in lista_tickets: para mostrar los tickets
            for t in lista_tickets:
                print(f"ID: {t['id']} | Solicitante: {t['solicitante']} | Estado: {t['status']}")
        #opc == 3: para buscar por solicitante
        elif opc == 3:
            print("\n--- BUSCAR POR SOLICITANTE ---")
            buscar = input("Nombre a buscar: ").strip().lower()
            for t in lista_tickets:
                if buscar in t['solicitante'].lower():
                    print(f"Encontrado -> ID: {t['id']} | Título: {t['titulo']}")
           #opc == 4: para mostrar resumen por prioridad         
        elif opc == 4:
            print("\n--- RESUMEN POR PRIORIDAD ---")
            conteos = {"Low": 0, "Medium": 0, "High": 0, "Critical": 0}
            for t in lista_tickets:
                if t['prioridad'] in conteos:
                    conteos[t['prioridad']] += 1
            print(conteos)
        elif opc == 5:
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción fuera de rango.")

if __name__ == "__main__":
    ejecutar_menu()
