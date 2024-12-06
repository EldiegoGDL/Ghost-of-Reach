import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage





# Función para los botones
def compra_fisica():
    import Ventana_compra_busqueda

def venta_en_linea():
    import ServicioADomicilio
    

def Inventario():
    import inventario

# Ventana principal
ventana = tk.Tk()
ventana.geometry("400x300")  # Tamaño de la ventana
ventana.title("Ventana principal")
ventana.config(bg="black")  # Fondo negro

# Botón 1: Compra física
boton_compra_fisica = ttk.Button(ventana, text="Compra Física", command=compra_fisica)
boton_compra_fisica.pack(pady=20, fill=tk.X, padx=50)

# Botón 2: Venta en línea
boton_venta_en_linea = ttk.Button(ventana, text="Venta en Línea",command=venta_en_linea )
boton_venta_en_linea.pack(pady=20, fill=tk.X, padx=50)

# Botón 3: Inventario
boton_inventario = ttk.Button(ventana, text="Inventario", command=Inventario)
boton_inventario.pack(pady=20, fill=tk.X, padx=50)

# Modificar el color de fondo de los botones para que sean verdes
boton_compra_fisica.config(style="Boton.TButton")
boton_venta_en_linea.config(style="Boton.TButton")
boton_inventario.config(style="Boton.TButton")

# Estilo de los botones
style = ttk.Style()
style.configure("Boton.TButton", font=("Helvetica", 12), background="black", foreground="green")

# Ejecutar la ventana
ventana.mainloop()



