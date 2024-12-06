import tkinter as tk
from tkinter import messagebox
import sqlite3

# Clase de conexión a la base de datos
class BaseDatos:
    def __init__(self, db_name):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def ejecutar(self, query, params=()):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def consultar(self, query, params=()):
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

# Producto
class Producto(BaseDatos):
    def __init__(self, db_name):
        super().__init__(db_name)

    def crear_producto(self, nombre, precio, genero, calificacion, plataforma, cantidad):
        self.ejecutar(''' 
            INSERT INTO producto (nombre_producto, precio, genero, Calificacion, plataforma, cantidad)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, precio, genero, calificacion, plataforma, cantidad))

    def buscar_productos(self, nombre_producto):
        return self.consultar('''
            SELECT * FROM producto WHERE nombre_producto LIKE ?
        ''', ('%' + nombre_producto + '%',))

    def obtener_producto_por_id(self, producto_id):
        return self.consultar('''
            SELECT * FROM producto WHERE id_producto = ?
        ''', (producto_id,))

    def actualizar_producto(self, producto_id, nombre, precio, genero, calificacion, plataforma, cantidad):
        self.ejecutar('''
            UPDATE producto SET nombre_producto=?, precio=?, genero=?, Calificacion=?, plataforma=?, cantidad=? WHERE id_producto=?
        ''', (nombre, precio, genero, calificacion, plataforma, cantidad, producto_id))

    def eliminar_producto(self, producto_id):
        self.ejecutar('''
            DELETE FROM producto WHERE id_producto = ?
        ''', (producto_id,))


# Crear una instancia de la clase Producto
producto_db = Producto('Prueva.db')

# Función para buscar productos
def buscar_productos():
    def buscar():
        nombre = entry_nombre.get()
        productos = producto_db.buscar_productos(nombre)
        resultado_text.delete(1.0, tk.END)
        if productos:
            for resultado in productos:
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

# Función para agregar productos
def agregar_producto():
    def agregar():
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        genero = entry_genero.get()
        calificacion = entry_calificacion.get()
        plataforma = entry_plataforma.get()
        cantidad = entry_cantidad.get()
        producto_db.crear_producto(nombre, precio, genero, calificacion, plataforma, cantidad)
        messagebox.showinfo("Producto Agregado", "Producto agregado exitosamente")
        agregar_window.destroy()
        
    agregar_window = tk.Toplevel(root)
    agregar_window.title("Agregar Producto")
    agregar_window.geometry("300x350")
    agregar_window.configure(bg="#202020")
    
    tk.Label(agregar_window, text="Nombre", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_nombre = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_nombre.pack(pady=5)

    tk.Label(agregar_window, text="Precio", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_precio = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_precio.pack(pady=5)

    tk.Label(agregar_window, text="Género", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_genero = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_genero.pack(pady=5)

    tk.Label(agregar_window, text="Calificación", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_calificacion = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_calificacion.pack(pady=5)

    tk.Label(agregar_window, text="Plataforma", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_plataforma = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_plataforma.pack(pady=5)

    tk.Label(agregar_window, text="Cantidad", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_cantidad = tk.Entry(agregar_window, bg="#303030", fg="#00FF00")
    entry_cantidad.pack(pady=5)

    tk.Button(agregar_window, text="Agregar", command=agregar, bg="#00FF00", fg="#202020").pack(pady=10)

# Función para ver detalles de un producto
def ver_detalles():
    def buscar_producto():
        producto_id = entry_id.get()
        producto = producto_db.obtener_producto_por_id(producto_id)
        if producto:
            resultado_text.delete(1.0, tk.END)
            resultado_text.insert(tk.END, f"ID: {producto[0]}\nNombre: {producto[1]}\nPrecio: {producto[2]}\nGénero: {producto[3]}\nCalificación: {producto[4]}\nPlataforma: {producto[5]}\nCantidad: {producto[6]}")
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

# Función para editar productos
def editar_producto():
    def buscar_producto():
        producto_id = entry_id.get()
        producto = producto_db.obtener_producto_por_id(producto_id)
        if producto:
            entry_nombre.delete(0, tk.END)
            entry_nombre.insert(0, producto[1])
            entry_precio.delete(0, tk.END)
            entry_precio.insert(0, producto[2])
            entry_genero.delete(0, tk.END)
            entry_genero.insert(0, producto[3])
            entry_calificacion.delete(0, tk.END)
            entry_calificacion.insert(0, producto[4])
            entry_plataforma.delete(0, tk.END)
            entry_plataforma.insert(0, producto[5])
            entry_cantidad.delete(0, tk.END)
            entry_cantidad.insert(0, producto[6])
        else:
            messagebox.showerror("Error", "Producto no encontrado")

    def actualizar_producto():
        producto_id = entry_id.get()
        nombre = entry_nombre.get()
        precio = entry_precio.get()
        genero = entry_genero.get()
        calificacion = entry_calificacion.get()
        plataforma = entry_plataforma.get()
        cantidad = entry_cantidad.get()
        producto_db.actualizar_producto(producto_id, nombre, precio, genero, calificacion, plataforma, cantidad)
        messagebox.showinfo("Producto Actualizado", "Producto actualizado exitosamente")
        editar_window.destroy()

    editar_window = tk.Toplevel(root)
    editar_window.title("Editar Producto")
    editar_window.geometry("400x400")
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

    tk.Label(editar_window, text="Género", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_genero = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_genero.pack(pady=5)

    tk.Label(editar_window, text="Calificación", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_calificacion = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_calificacion.pack(pady=5)

    tk.Label(editar_window, text="Plataforma", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_plataforma = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_plataforma.pack(pady=5)

    tk.Label(editar_window, text="Cantidad", bg="#202020", fg="#FFFFFF").pack(pady=5)
    entry_cantidad = tk.Entry(editar_window, bg="#303030", fg="#00FF00")
    entry_cantidad.pack(pady=5)

    tk.Button(editar_window, text="Actualizar", command=actualizar_producto, bg="#00FF00", fg="#202020").pack(pady=10)


# Función principal de la aplicación
root = tk.Tk()
root.title("Gestión de Inventario")
root.geometry("300x200")
root.configure(bg="#202020")

tk.Button(root, text="Agregar Producto", command=agregar_producto, bg="#00FF00", fg="#202020").pack(pady=10)
tk.Button(root, text="Buscar Producto", command=buscar_productos, bg="#00FF00", fg="#202020").pack(pady=10)
tk.Button(root, text="Ver Detalles", command=ver_detalles, bg="#00FF00", fg="#202020").pack(pady=10)
tk.Button(root, text="Editar Producto", command=editar_producto, bg="#00FF00", fg="#202020").pack(pady=10)

root.mainloop()


#como funciona el codigo en primeras pues le puse lode la base de datos en caso de que lo ocupen 
#al momento de ejecutar el codigo pueden seleccionar la opcion que quierean tienen diferentes funcionalidades
#para saber el id de los productos solo se van a la primera opcion buscan el juego como lo pusieron ya el codigo les asigna un id que es un numero y ya en las pestañas 
#que les pida el id nada mas ponen el numero y ya les aparecen los datos ya si quieren que le agregue algo me
