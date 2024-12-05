import tkinter as tk
from tkinter import messagebox

def buscar_productos():
    messagebox.showinfo("Buscar Productos", "Ir a la página de búsqueda de productos")

def agregar_producto():
    messagebox.showinfo("Agregar Producto", "Ir a la página de agregar producto")

def ver_detalles():
    messagebox.showinfo("Ver Detalles", "Ir a la página de ver detalles del producto")

def editar_producto():
    messagebox.showinfo("Editar Producto", "Ir a la página de editar producto")

def eliminar_producto():
    messagebox.showinfo("Eliminar Producto", "Ir a la página de eliminar producto")

class Inventario:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Inventario")
        self.root.geometry("400x500")
        self.root.configure(bg="#FFD700")

        # Título de la ventana
        title_label = tk.Label(root, text="Gestión de Inventario", font=("Helvetica", 24, "bold"), fg="darkmagenta", bg="#FFD700")
        title_label.pack(pady=10)

        # Subtítulo
        subtitle_label = tk.Label(root, text="Agrega, busca y administra productos", font=("Helvetica", 14), fg="darkmagenta", bg="#FFD700")
        subtitle_label.pack(pady=10)

        # Lista de botones y sus funciones
        buttons = [
            ("Buscar Productos", buscar_productos),
            ("Agregar Producto", agregar_producto),
            ("Ver Detalles", ver_detalles),
            ("Editar Producto", editar_producto),
            ("Eliminar Producto", eliminar_producto),
        ]

        # Crear los botones y añadirlos a la ventana
        for btn_text, btn_command in buttons:
            button = tk.Button(root, text=btn_text, command=btn_command, bg="#F08080", fg="white", font=("Helvetica", 12), width=20, height=2)
            button.pack(pady=10)

    # Si se desea, se pueden agregar más métodos específicos aquí

# Código principal que inicia la ventana
if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal
    inventario_window = Inventario(root)  # Crear la instancia de la clase Inventario
    root.mainloop()  # Iniciar el ciclo de la aplicación
