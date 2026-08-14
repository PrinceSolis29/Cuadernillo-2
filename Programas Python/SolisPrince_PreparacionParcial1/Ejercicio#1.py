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
    # Capturar campos de texto obligatorios
    solicitante = input("Ingrese el nombre del solicitante: ").strip()
    titulo = input("Ingrese el título del ticket: ").strip()
    descripcion = input("Ingrese la descripción: ").strip()
    
    if not solicitante or not titulo or not descripcion:
        print("Error: El solicitante, título y descripción son obligatorios.")
        return
    # 3. Solicitar y validar categoría contra coleccion permitida
    print(f"Categorías válidas: {categorias_validas}")
    categoria = input("Ingrese la categoría: ").strip()
    if categoria not in categorias_validas:
        print("Error: Categoría no válida.")
        return
    # 4. Solicitar prioridad y estructurar en un diccionario con status inicial Open
    print(f"Prioridades válidas: {prioridades_validas}")
    prioridad = input("Ingrese la prioridad: ").strip()
    if prioridad not in prioridades_validas:
        print("Error: Prioridad no válida.")
        return

    ticket = {
        "id": id_ticket,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    # 5. Mostrar resumen formateado con f-strings
    print("\n=== RESUMEN DEL TICKET REGISTRADO ===")
    print(f"ID Ticket:   {ticket['id']}")
    print(f"Solicitante: {ticket['solicitante']}")
    print(f"Título:      {ticket['titulo']}")
    print(f"Categoría:   {ticket['categoria']}")
    print(f"Prioridad:   {ticket['prioridad']}")
    print(f"Estado:      {ticket['status']}")

if __name__ == "__main__":
    registrar_ticket()
