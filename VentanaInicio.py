import tkinter as tk
from tkinter import ttk






# Funciones para los botones
def compra_fisica():
    import Ventana_compra_busqueda
    try:
        Ventana_compra_busqueda.mostrar_ventana()
    except AttributeError:
        print("No se pudo encontrar la función 'mostrar_ventana' en Ventana_compra_busqueda.")

def venta_en_linea():
    import ServicioADomicilio
    try:
        ServicioADomicilio.mostrar_ventana_principal()
    except AttributeError:
        print("No se pudo encontrar la función 'mostrar_ventana' en ServicioADomicilio.")

<<<<<<< HEAD
def Inventario():
=======
def inventario():
    import inventario
>>>>>>> cf0d2947ba95f413d8a49c00400c0a2eb95d7a8b
    try:
        inventario.mostrar_ventana()
    except AttributeError:
        print("No se pudo encontrar la función 'mostrar_ventana' en inventario.")
        
def agregar():
    import Agregar
    try:
        Agregar.mostrar_ventana()
    except AttributeError:
        print("No se pudo encontrar la función 'mostrar_ventana' en Agregar.")


# Ventana principal
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ventana Principal")
ventana.config(bg="black")  # Fondo negro

# Estilo de los botones
style = ttk.Style()
style.theme_use("clam")  # Cambia al tema clam para personalizar colores
style.configure("Boton.TButton",
                font=("Helvetica", 12),
                background="green",
                foreground="white")
style.map("Boton.TButton", background=[('active', 'dark green')])

# Botón 1: Compra física
boton_compra_fisica = ttk.Button(ventana, text="Compra Física", style="Boton.TButton", command=compra_fisica)
boton_compra_fisica.pack(pady=20, fill=tk.X, padx=50)

# Botón 2: Venta en línea
boton_venta_en_linea = ttk.Button(ventana, text="Venta en Línea", style="Boton.TButton", command=venta_en_linea)
boton_venta_en_linea.pack(pady=20, fill=tk.X, padx=50)

# Botón 3: Inventario
boton_inventario = ttk.Button(ventana, text="Inventario", style="Boton.TButton", command=Inventario)
boton_inventario.pack(pady=20, fill=tk.X, padx=50)

# Botón 4: Agregar cliente y empleado
boton_agregar = ttk.Button(ventana, text="Agregar", style="Boton.TButton", command=agregar)
boton_agregar.pack(pady=20, fill=tk.X, padx=50)

# Ejecutar la ventana
ventana.mainloop()