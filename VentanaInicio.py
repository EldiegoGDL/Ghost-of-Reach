import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage
from inventario import Inventario


class VentanaPrincipal:
    def __init__(self, root):
        self.root = root  # Aquí ya recibimos el objeto root
        self.root.geometry("300x500")
        self.root.resizable(0, 0)
        self.root.configure(bg="cornflowerblue")
        self.root.title("Ventana Principal")

        # Texto Ventana
        self.bienvenida = ttk.Label(self.root, text="Bienvenidos", font=("Arial Black", 15))

        # Ubicación del texto
        self.bienvenida.place(x=75, y=10)

        # Estilo para botones
        style = ttk.Style()
        style.configure("TButton",
                        background="#0000FF",  # Color azul para los botones
                        foreground="blue",     # Texto azul en los botones
                        font=("Arial", 10))

        # Botones
        self.inventario = ttk.Button(self.root, text="Inventario", style="TButton", command=self.abrir_inventario)
        self.inventario.place(x=100, y=150)

        compraFisica = ttk.Button(self.root, text="Compra Fisica", style="TButton")
        compraFisica.place(x=95, y=200)

        compraDomicilio = ttk.Button(self.root, text="Compra A Domicilio", style="TButton")
        compraDomicilio.place(x=80, y=250)

    def abrir_inventario(self):
        # Crear una nueva ventana de nivel superior (Toplevel)
        self.new_window = tk.Toplevel(self.root)
        self.inventario = Inventario(self.new_window)  # Asumiendo que Inventario es una clase en otro archivo

# Código principal
if __name__ == "__main__":
    root = tk.Tk()  # Se crea una instancia de Tk()
    ventana_principal = VentanaPrincipal(root)  # Se pasa la instancia de Tk() a la clase VentanaPrincipal
    root.mainloop()
