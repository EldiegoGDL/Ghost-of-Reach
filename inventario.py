import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar a la base de datos SQLite en caso de que lo ocupen de que quieran que se conecte 
conn = sqlite3.connect('inventario.db')
c = conn.cursor()

# Crear tabla de productos si no existe o por si lo quieren modificar y cambiarlo por este aca para que jale chido
c.execute('''CREATE TABLE IF NOT EXISTS productos
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
             nombre TEXT,
             precio REAL,
             cantidad INTEGER)''')
conn.commit()

def buscar_productos():
    def buscar():
        nombre = entry_nombre.get()
        c.execute("SELECT * FROM productos WHERE nombre LIKE ?", ('%'+nombre+'%',))
        resultados = c.fetchall()
        resultado_text.delete(1.0, tk.END)
        if resultados:
            for resultado in resultados:
                resultado_text.insert(tk.END, f"ID: {resultado[0]}, Nombre: {resultado[1]}, Precio: {resultado[2]}, Cantidad: {resultado[3]}\n")
        else:
            resultado_text.insert(tk.END, "No se encontraron productos.")

    buscar_window = tk.Toplevel(root)
    buscar_window.title("Buscar Productos")
    buscar_window.geometry("400x300")
    buscar_window.configure(bg="#202020")

    tk.Label(buscar_window, text="Nombre del Producto", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_nombre = tk.Entry(buscar_window, bg="#303030", fg="#00FF00")
    entry_nombre.pack(pady=5)
    
    tk.Button(buscar_window, text="Buscar", command=buscar, bg="#00FF00", fg="#202020").pack(pady=10)

    resultado_text = tk.Text(buscar_window, height=10, width=50, bg="#303030", fg="#FFFFFF")
    resultado_text.pack(pady=10)

def agregar_producto():
    def agregar():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        c.execute("INSERT INTO productos (nombre, precio, cantidad) VALUES (?, ?, ?)",
                  (nombre, precio, cantidad))
        conn.commit()
        messagebox.showinfo("Producto Agregado", "Producto agregado exitosamente")
        agregar_window.destroy()
        
    agregar_window = tk.Toplevel(root)
    agregar_window.title("Agregar Producto")
    agregar_window.geometry("300x250")
    agregar_window.configure(bg="#202020")
    
    tk.Label(agregar_window, text="Nombre", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_nombre = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_nombre.pack(pady=5)
    
    tk.Label(agregar_window, text="Precio", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_precio = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_precio.pack(pady=5)
    
    tk.Label(agregar_window, text="Cantidad", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_cantidad = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_cantidad.pack(pady=5)
    
    tk.Button(agregar_window, text="Agregar", command=agregar, bg="#00FF00", fg="#202020").pack(pady=10)

def ver_detalles():
    def buscar_producto():
        producto_id = entry_id.get()
        c.execute("SELECT * FROM productos WHERE id=?", (producto_id,))
        producto = c.fetchone()
        if producto:
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, f"ID: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nCantidad: {producto[3]}")
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    ver_window = tk.Toplevel(root)
    ver_window.title("Ver Detalles del Producto")
    ver_window.geometry("400x300")
    ver_window.configure(bg="#202020")

    tk.Label(ver_window, text="ID del Producto", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_id = tk.Entry(ver_window, bg="#303030", fg="#00FF00")
    entry_id.pack(pady=5)
    
    tk.Button(ver_window, text="Buscar", command=buscar_producto, bg="#00FF00", fg="#202020").pack(pady=10)

    resultado_text = tk.Text(ver_window, height=10, width=50, bg="#303030", fg="#FFFFFF")
    resultado_text.pack(pady=10)

def editar_producto():
    def buscar_producto():
        producto_id = entry_id.get()
        c.execute("SELECT * FROM productos WHERE id=?", (producto_id,))
        producto = c.fetchone()
        if producto:
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, producto[1])
            entry_precio.delete(0, tk.END)
            entry_precio.insert(0, producto[2])
            entry_cantidad.delete(0, tk.END)
            entry_cantidad.insert(0, producto[3])
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def actualizar_producto():
        producto_id = entry_id.get()
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        cantidad = entry_cantidad.get()
        c.execute("UPDATE productos SET nombre=?, precio=?, cantidad=? WHERE id=?",
                  (nombre, precio, cantidad, producto_id))
        conn.commit()
        messagebox.showinfo("Producto Actualizado", "Producto actualizado exitosamente")
        editar_window.destroy()

    editar_window = tk.Toplevel(root)
    editar_window.title("Editar Producto")
    editar_window.geometry("300x350")
    editar_window.configure(bg="#202020")

    tk.Label(editar_window, text="ID del Producto", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_id = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_id.pack(pady=5)

    tk.Button(editar_window, text="Buscar", command=buscar_producto, bg="#00FF00", fg="#202020").pack(pady=10)

    tk.Label(editar_window, text="Nombre", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_nombre = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_nombre.pack(pady=5)
    
    tk.Label(editar_window, text="Precio", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_precio = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_precio.pack(pady=5)
    
    tk.Label(editar_window, text="Cantidad", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_cantidad = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_cantidad.pack(pady=5)
    
    tk.Button(editar_window, text="Actualizar", command=actualizar_producto, bg="#00FF00", fg="#202020").pack(pady=10)

def eliminar_producto():
    def eliminar():
        producto_id = entry_id.get()
        c.execute("DELETE FROM productos WHERE id=?", (producto_id,))
        conn.commit()
        messagebox.showinfo("Producto Eliminado", "Producto eliminado exitosamente")
        eliminar_window.destroy()

    eliminar_window = tk.Toplevel(root)
    eliminar_window.title("Eliminar Producto")
    eliminar_window.geometry("300x200")
    eliminar_window.configure(bg="#202020")
    
    tk.Label(eliminar_window, text="ID del Producto", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_id = tk.Entry(eliminar_window, bg="#303030", fg="#00FF00")
    entry_id.pack(pady=5)
    
    tk.Button(eliminar_window, text="Eliminar", command=eliminar, bg="#FF0000", fg="#FFFFFF").pack(pady=10)

def main():
    global root
    root = tk.Tk()
    root.title("Gestión de Inventario")
    root.geometry("400x500")
    root.configure(bg="#000000")

    title_label = tk.Label(root, text="Gestión de Inventario", font=("Helvetica", 24, "bold"), fg="#00FF00", bg="#000000")
    title_label.pack(pady=10)

    subtitle_label = tk.Label(root, text="Agrega, busca y administra productos", font=("Helvetica", 14), fg="#FFFFFF", bg="#000000")
    subtitle_label.pack(pady=10)

    buttons = [
        ("Buscar Productos", buscar_productos),
        ("Agregar Producto", agregar_producto),
        ("Ver Detalles", ver_detalles),
        ("Editar Producto", editar_producto),
        ("Eliminar Producto", eliminar_producto),
    ]

    for btn_text, btn_command in buttons:
        button = tk.Button(root, text=btn_text, command=btn_command, bg="#00FF00", fg="#000000", font=("Helvetica", 12), width=20, height=2)
        button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
    conn.close()


#como funciona el codigo en primeras pues le puse lode la base de datos en caso de que lo ocupen 
#al momento de ejecutar el codigo pueden seleccionar la opcion que quierean tienen diferentes funcionalidades
#para saber el id de los productos solo se van a la primera opcion buscan el juego como lo pusieron ya el codigo les asigna un id que es un numero y ya en las pestañas 
#que les pida el id nada mas ponen el numero y ya les aparecen los datos ya si quieren que le agregue algo me
