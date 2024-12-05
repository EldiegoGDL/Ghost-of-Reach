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

def main():
    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("400x500")
    root.configure(bg="#FFD700")

    title_label = tk.Label(root, text="Gestión de Inventario", font=("Helvetica", 24, "bold"), fg="darkmagenta", bg="#FFD700")
    title_label.pack(pady=10)

    subtitle_label = tk.Label(root, text="Agrega, busca y administra productos", font=("Helvetica", 14), fg="darkmagenta", bg="#FFD700")
    subtitle_label.pack(pady=10)

    buttons = [
        ("Buscar Productos", buscar_productos),
        ("Agregar Producto", agregar_producto),
        ("Ver Detalles", ver_detalles),
        ("Editar Producto", editar_producto),
        ("Eliminar Producto", eliminar_producto),
    ]

    for btn_text, btn_command in buttons:
        button = tk.Button(root, text=btn_text, command=btn_command, bg="#F08080", fg="white", font=("Helvetica", 12), width=20, height=2)
        button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()

