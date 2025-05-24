import os 
TAREAS_FILE = "tareas.txt"

def cargar_tareas():
    if not os.path.exists(TAREAS_FILE):
        return []
    with open(TAREAS_FILE, "r") as archivo:
        return [linea.strip() for linea in archivo.readlines()]

def guardar_tareas(tareas):
    with open (TAREAS_FILE, "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

            def mostrar_tareas(tareas):
                if not tareas:
                    print("No hay tareas pendientes.")
                else:
                    for i, tareas in enumerate(tareas, 1): 
                        print(f"{i}. {tarea}")
def agregar_tarea(tareas):
    tarea = input ("Escribe la nueva tarea: ")
    tareas.append(tarea)
    guardar_tareas(tareas)
    print("Tarea agregada. ")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        numero = int(input("Número de la tarea a eliminar: "))
        if 1 <= numero <= len(tareas):
            tareas.pop(numero - 1)
            guardar_tareas(tareas)
            print("Tarea eliminada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Por favor, escribe un número")
def menu():
  tareas = cargar_tareas()  
def menu():
    tareas = cargar_tareas()
    while True:
        print("\n--- Gestor de Tareas---")
        print("1. ver tareas")
        print("2. agregar tarea")
        print("3. eliminar tarea")
        print("4. salir")
        opcion = input("elige una opción: ")

        if opcion == "1":
            mostrar_tareas(tareas) # type: ignore

        elif opcion == "2":
            agregar_tarea(tareas)

        elif opcion == "3":
            eliminar_tarea(tareas)

        elif opcion == "4":
            print("¡Hasta luego! :)")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    menu
