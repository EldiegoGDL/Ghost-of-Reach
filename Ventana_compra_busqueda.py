import tkinter as tk
from tkinter import Listbox, ttk, messagebox
from sqlite3 import IntegrityError
import datetime
import os
import sys

# Agregar la ruta al archivo base_De_Datos_Y_Consultas.py
ruta_base_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_base_datos)

# Importar clases necesarias
from base_De_Datos_Y_Consultas import Producto, Cliente, Transaccion

# Base de datos
DB_NAME = "Prueva.db"
producto_db = Producto(DB_NAME)
cliente_db = Cliente(DB_NAME)
transaccion_db = Transaccion(DB_NAME)


def actualizar_lista(listbox, productos):
    """Actualiza los elementos del Listbox con una nueva lista de productos."""
    listbox.delete(0, tk.END)  # Limpia el Listbox
    for producto in productos:
        listbox.insert(tk.END, producto)  # Agrega cada producto al Listbox


def buscar_en_lista(event, entrada, listbox):
    """Filtra los productos según el texto ingresado."""
    termino = entrada.get().strip().lower()
    productos = producto_db.consultar("SELECT nombre_producto FROM producto WHERE cantidad > 0")
    lista_filtrada = [producto[0] for producto in productos if termino in producto[0].lower()]
    actualizar_lista(listbox, lista_filtrada)


def actualizar_lista_desde_bd(listbox):
    """Carga todos los productos disponibles desde la base de datos."""
    productos = producto_db.consultar("SELECT nombre_producto FROM producto WHERE cantidad > 0")
    lista_productos = [producto[0] for producto in productos]
    actualizar_lista(listbox, lista_productos)


def buscar_elemento(listbox):
    """Muestra detalles del producto seleccionado."""
    try:
        seleccionado = listbox.get(listbox.curselection())
        detalles = producto_db.consultar("SELECT * FROM producto WHERE nombre_producto = ?", (seleccionado,))
        if detalles:
            abrir_nueva_ventana(detalles[0],listbox)
        else:
            messagebox.showinfo("No disponible", f"El producto '{seleccionado}' no está disponible.")
    except tk.TclError:
        messagebox.showwarning("Selección vacía", "Por favor, selecciona un producto para buscar.")


def abrir_nueva_ventana(detalles_producto,listbox):
    """Abre una nueva ventana con información del producto."""
    nueva_ventana = tk.Toplevel()
    nueva_ventana.geometry("300x400")
    nueva_ventana.title(f"Detalles de {detalles_producto[1]}")
    nueva_ventana.config(bg="#c8c8c8")
    nueva_ventana.resizable(0, 0)

    info = (
        f"Producto: {detalles_producto[1]}\n"
        f"Precio: {detalles_producto[2]}\n"
        f"Género: {detalles_producto[3]}\n"
        f"Calificación: {detalles_producto[4]}\n"
        f"Plataforma: {detalles_producto[5]}\n"
        f"Cantidad disponible: {detalles_producto[6]}"
    )
    ttk.Label(nueva_ventana, text=info, font=("Times New Roman", 12), background="#c8c8c8").pack(pady=10)

    metodo_pago = tk.StringVar(value="efectivo")
    ttk.Radiobutton(nueva_ventana, text="Efectivo", variable=metodo_pago, value="efectivo").pack(pady=10)
    ttk.Radiobutton(nueva_ventana, text="Tarjeta", variable=metodo_pago, value="tarjeta").pack(pady=10)

    ttk.Button(
        nueva_ventana, text="Comprar",
        command=lambda: confirmar_compra(detalles_producto, metodo_pago, nueva_ventana, listbox)
    ).pack(pady=20)

    ttk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack(pady=20)


def confirmar_compra(detalles_producto, metodo_pago, ventana, listbox):
    """Registra la compra de un producto."""
    ventana.destroy()
    fecha_actual = datetime.date.today()
    try:
        seleccion = metodo_pago.get()
        transaccion_db.crear_transaccion(
            id_empleado=1, id_cliente=1, id_producto=detalles_producto[0],
            monto=detalles_producto[2], direccion="local",
            fecha_inicio=None, fecha_final=None, tarifa_envio=0,
            fecha_compra=fecha_actual, tipo_transaccion=seleccion
        )
        producto_db.ejecutar(
            "UPDATE producto SET cantidad = cantidad - ? WHERE id_producto = ?",
            (1, detalles_producto[0])
        )
        actualizar_lista_desde_bd(listbox)
        messagebox.showinfo("Compra realizada", f"Has comprado el producto: {detalles_producto[1]}")
    except IntegrityError as e:
        messagebox.showerror("Error", f"No se pudo registrar la transacción: {e}")


def mostrar_ventana():
    """Crea y muestra la ventana principal."""
    ventana = tk.Tk()
    ventana.geometry('600x400')
    ventana.title("Gestión de Productos")
    ventana.config(bg="#c8c8c8")

    # Widgets
    etiqueta = ttk.Label(ventana, text="Buscar producto:", font=("Times New Roman", 15), background="#c8c8c8")
    etiqueta.pack(pady=10, anchor="w", padx=20)

    entrada = ttk.Entry(ventana, width=50)
    entrada.pack(pady=5, padx=20, anchor="w")

    listbox_frame = ttk.Frame(ventana)
    listbox_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    scrollbar = ttk.Scrollbar(listbox_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(listbox_frame, font=("Times New Roman", 12), yscrollcommand=scrollbar.set)
    listbox.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=listbox.yview)

    boton_buscar = ttk.Button(ventana, text="Ver Detalles", command=lambda: buscar_elemento(listbox))
    boton_buscar.pack(pady=10)

    # Vinculación del evento
    entrada.bind("<KeyRelease>", lambda event: buscar_en_lista(event, entrada, listbox))

    # Cargar productos al iniciar
    actualizar_lista_desde_bd(listbox)

    ventana.mainloop()




