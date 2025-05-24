import tkinter as tk
from tkinter import messagebox

TAREAS_FILE = "tareas.txt"

def cargar_tareas():
    try:
        with open(TAREAS_FILE, "r") as archivo:
            return [linea.strip() for linea in archivo.readlines()]
    except FileNotFoundError:
        return []

def guardar_tareas(tareas):
    with open(TAREAS_FILE, "w") as archivo:
        for tarea in tareas:
            archivo.write(tarea + "\n")

def actualizar_lista():
    lista_tareas.delete(0, tk.END)
    for tarea in tareas:
        lista_tareas.insert(tk.END, tarea)

def agregar_tarea():
    texto = entrada.get()
    if texto:
        tarea = "[ ] " + texto
        tareas.append(tarea)
        guardar_tareas(tareas)
        entrada.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Atención", "Escribe una tarea antes de agregar.")

def marcar_como_hecha():
    seleccion = lista_tareas.curselection()
    if seleccion:
        i = seleccion[0]
        if tareas[i].startswith("[ ]"):
            tareas[i] = tareas[i].replace("[ ]", "[x]", 1)
            guardar_tareas(tareas)
            actualizar_lista()
        else:
            messagebox.showinfo("Ya hecha", "Esa tarea ya está marcada como hecha.")
    else:
        messagebox.showwarning("Atención", "Selecciona una tarea.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        i = seleccion[0]
        tareas.pop(i)
        guardar_tareas(tareas)
        actualizar_lista()
    else:
        messagebox.showwarning("Atención", "Selecciona una tarea para eliminar.")

# --- Interfaz ---
ventana = tk.Tk()
ventana.title("Gestor de Tareas")

tareas = cargar_tareas()

entrada = tk.Entry(ventana, width=40)
entrada.pack(pady=10)

boton_agregar = tk.Button(ventana, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack()

lista_tareas = tk.Listbox(ventana, width=50)
lista_tareas.pack(pady=10)
actualizar_lista()

boton_hecha = tk.Button(ventana, text="Marcar como Hecha", command=marcar_como_hecha)
boton_hecha.pack(pady=5)

boton_eliminar = tk.Button(ventana, text="Eliminar Tarea", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

ventana.mainloop()
