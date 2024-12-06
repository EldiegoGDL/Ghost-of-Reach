import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime  # Importar el módulo datetime
import sys 
import os
# Agregar la ruta al directorio donde está el archivo base_De_Datos_Y_Consultas.py
ruta_base_datos = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(ruta_base_datos)
# Importar las clases necesarias desde el archivo externo
from base_De_Datos_Y_Consultas import Producto, Cliente, Transaccion

def mostrar_agregar_direccion(telefono):
    
    nueva_ventana = tk.Toplevel()   # Crear una nueva ventana
    nueva_ventana.title("Agregar Dirección")
    nueva_ventana.geometry("600x600")
    nueva_ventana.config(bg="gray")

    # Conectar con la base de datos y obtener el nombre del cliente
    cliente_db = Cliente("prueva.db")  # Asegúrate de usar la ruta correcta para tu base de datos

    resultado_nom = cliente_db.consultar('''
        SELECT nombre_cliente FROM cliente WHERE telefono = ?
    ''', (telefono,))

    resultado_num = cliente_db.consultar('''
        SELECT telefono FROM cliente WHERE telefono = ?
    ''', (telefono,))

    if resultado_nom:
        nombre_cliente = resultado_nom[0][0]  # Obtener el primer resultado de la consulta
    else:
        nombre_cliente = "Cliente no encontrado" 

    if resultado_num:
        numero_cliente = resultado_num[0][0]  # Obtener el primer resultado de la consulta
    else:
        numero_cliente = "Cliente no encontrado" 


    miFrame = tk.Frame(nueva_ventana, width=500, height=500, bg="#c8c8c8")
    miFrame.pack()

    # Funciones de validación
    def validar_entrada_letras(input):
        # Permite letras, espacios y vacío, pero no caracteres especiales
        if all(c.isalpha() or c == " " for c in input) or input == "":
            return True
        return False

    def validar_entrada_numeros(input):
        # Permite números, espacios y vacío, pero no caracteres especiales
        if all(c.isdigit() or c == " " for c in input) or input == "":
            return True
        return False

    # Creación de las etiquetas y campos con validaciones
    tk.Label(miFrame, text="Nombre").place(x=50, y=50)
    nombreText = tk.Entry(miFrame, validate="key", textvariable=tk.StringVar(value=nombre_cliente), validatecommand=(nueva_ventana.register(validar_entrada_letras), "%P"))
    nombreText.place(x=110, y=50)

    tk.Label(miFrame, text="Número de Teléfono").place(x=250, y=50)
    numeroText = tk.Entry(miFrame, validate="key", textvariable=tk.StringVar(value=numero_cliente), validatecommand=(nueva_ventana.register(validar_entrada_letras), "%P"))
    numeroText.place(x=380, y=50)

    tk.Label(miFrame, text="Calle").place(x=50, y=100)
    calleText = tk.Entry(miFrame)
    calleText.place(x=100, y=100)

    tk.Label(miFrame, text="N. Exterior").place(x=250, y=100)
    numExtText = tk.Entry(miFrame)
    numExtText.place(x=320, y=100)

    tk.Label(miFrame, text="Colonia").place(x=50, y=150)
    coloniaText = tk.Entry(miFrame)
    coloniaText.place(x=100, y=150)

    tk.Label(miFrame, text="Código Postal").place(x=250, y=150)
    codPostText = tk.Entry(miFrame, validate="key", validatecommand=(nueva_ventana.register(validar_entrada_numeros), "%P"))
    codPostText.place(x=350, y=150)

    tk.Label(miFrame, text="Referencia").place(x=50, y=200)
    referenciaText = tk.Entry(miFrame)
    referenciaText.place(x=120, y=200, width=300)

    def validar_campos():
        if not (nombreText.get() and numeroText.get() and calleText.get() and numExtText.get() and
                coloniaText.get() and codPostText.get() and referenciaText.get()):
            messagebox.showwarning("Campos Vacíos", "Por favor, rellene todos los campos.")
        else:
            mostrar_buscar_videojuegos(nombreText.get(), calleText.get())

    # Botones
    tk.Button(miFrame, text="Confirmar", bg="green", fg="white", command=validar_campos).place(x=300, y=450)
    tk.Button(miFrame, text="Atrás", bg="red", fg="white", command=nueva_ventana.destroy).place(x=100, y=450)

# Pantalla de buscar videojuegos
def mostrar_buscar_videojuegos(nombreText, calleText):
    
    ventana = tk.Toplevel()  
    ventana.title("Buscar Videojuegos")
    ventana.geometry('600x400')
    ventana.config(bg="#c8c8c8")

    DB_NAME = "Prueva.db"
    producto_db = Producto(DB_NAME)

    # Función para actualizar la lista desde la base de datos
    def actualizar_lista_desde_bd():
        productos = producto_db.consultar("SELECT nombre_producto FROM producto WHERE cantidad > 0")
        lista_productos = [producto[0] for producto in productos]  # Extraer nombres de productos
        actualizar_lista(lista_productos)

    def actualizar_lista(productos):
        """Actualiza los elementos del Listbox con una nueva lista de productos."""
        listbox.delete(0, tk.END)  # Limpia el Listbox
        for producto in productos:
            listbox.insert(tk.END, producto)  # Agrega cada producto al Listbox

    def buscar_en_lista(event=None):
        """Filtra los productos según el texto ingresado."""
        termino = entrada.get().lower()
        productos = producto_db.consultar("SELECT nombre_producto FROM producto WHERE cantidad > 0")
        lista_filtrada = [producto[0] for producto in productos if termino in producto[0].lower()]
        actualizar_lista(lista_filtrada)


    def buscar_elemento():
        """Muestra detalles del producto seleccionado."""
        try:
            seleccionado = listbox.get(listbox.curselection())
            detalles = producto_db.consultar("SELECT * FROM producto WHERE nombre_producto = ?", (seleccionado,))
            if detalles:
                abrir_ventana_compra(detalles[0])
            else:
                messagebox.showinfo("No disponible", f"El producto '{seleccionado}' no está disponible.")
        except tk.TclError:
            messagebox.showwarning("Selección vacía", "Por favor, selecciona un producto para buscar.")

    def abrir_ventana_compra(detalles_producto):
        """Abre una nueva ventana con la información detallada del videojuego seleccionado."""
        nueva_ventana = tk.Toplevel(ventana)
        nueva_ventana.geometry("350x450")
        nueva_ventana.title(f"Detalles de {detalles_producto[1]}")
        nueva_ventana.config(bg="#f9f9f9")

        info = f"Producto: {detalles_producto[1]}\n"
        info += f"Precio: {detalles_producto[2]}\n"
        info += f"Género: {detalles_producto[3]}\n"
        info += f"Calificación: {detalles_producto[4]}\n"
        info += f"Plataforma: {detalles_producto[5]}\n"
        info += f"Cantidad disponible: {detalles_producto[6]}"

        # Título del videojuego
        ttk.Label(nueva_ventana, text=f"{detalles_producto[1]}", font=("Times New Roman", 14, "bold"), background="#f9f9f9").pack(pady=10)

        # Plataforma
        ttk.Label(nueva_ventana, text=f"Plataforma: {detalles_producto[5]}", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)

        # Costo de envío
        ttk.Label(nueva_ventana, text="Costo de envío:", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)
        envio_entry = ttk.Entry(nueva_ventana,  width=10, justify="center")
        envio_entry.pack(pady=5)

        # Total
        ttk.Label(nueva_ventana, text="costo del juego:", font=("Times New Roman", 12, "bold"), background="#f9f9f9").pack(pady=5)
        total_label = ttk.Label(nueva_ventana, text=f"$ {detalles_producto[2]}", font=("Times New Roman", 12), background="#f9f9f9")
        total_label.pack(pady=5)
        

        # Tipo de transacción
        ttk.Label(nueva_ventana, text="tipo de pago:", font=("Times New Roman", 12, "bold"), background="#f9f9f9").pack(pady=5)
        metodo_pago = tk.StringVar()  # Elimina el valor predeterminado inicial
        combobox_metodo_pago = ttk.Combobox(nueva_ventana, textvariable=metodo_pago, state="readonly", values=["Tarjeta", "Efectivo"])
        combobox_metodo_pago.pack(pady=5)
        metodo_pago = combobox_metodo_pago

        # Botones de Confirmar y Cancelar
        botones_frame = ttk.Frame(nueva_ventana)
        botones_frame.pack(pady=20)

        cancelar_btn = ttk.Button(botones_frame, text="Cancelar", command=ventana.destroy)
        cancelar_btn.grid(row=0, column=0, padx=10)

        confirmar_btn = ttk.Button(botones_frame, text="Confirmar", command=lambda: compra_exitosa(detalles_producto[1], metodo_pago.get(), envio_entry.get(), detalles_producto[2], detalles_producto[0]))
        confirmar_btn.grid(row=0, column=1, padx=10)

    def compra_exitosa(videojuego, metodo_pago, costo_envio, precio_unitario, id_productos ):
        if metodo_pago == "seleccione un metodo de pago" or not metodo_pago:
            messagebox.showwarning("Método de pago", "Por favor, selecciona un método de pago.")
            return
        
        fecha_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        fecha_final = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        direccion = f"{nombreText}, {calleText}"

        transaccion = Transaccion('Prueva.db')
        transaccion.crear_transaccion(
            id_empleado=1,  # Sustituye con el ID real
            id_cliente=1,
            id_producto=id_productos,
            monto = precio_unitario,
            direccion=direccion,
            fecha_inicio=fecha_inicio,
            fecha_final=fecha_final,
            tarifa_envio=costo_envio,
            fecha_compra=datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            tipo_transaccion=metodo_pago
        )
        producto_db.ejecutar('''
        UPDATE producto
        SET cantidad = cantidad - ?
        WHERE id_producto = ?
        ''', (1, id_productos))

        actualizar_lista_desde_bd()

        messagebox.showinfo("Compra Exitosa", f"Has comprado '{videojuego}' con éxito.\nMétodo de pago: {metodo_pago}\n"
                                            f"Nombre: {nombreText}\nCalle: {calleText}")



    tk.Label(ventana, text="Buscar:", font=("Arial", 15), bg="#c8c8c8").pack(pady=10, anchor="w", padx=20)
    entrada = tk.Entry(ventana, width=50)
    entrada.pack(pady=5, padx=20, anchor="w")
    entrada.bind("<KeyRelease>", buscar_en_lista)

    listbox_frame = tk.Frame(ventana)
    listbox_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    listbox = tk.Listbox(listbox_frame, font=("Arial", 12))
    listbox.pack(fill=tk.BOTH, expand=True)

    tk.Button(ventana, text="Atrás", command=ventana.destroy).pack(pady=10)
    tk.Button(ventana, text="Buscar", command=buscar_elemento).pack()

    actualizar_lista_desde_bd()


def verificar_telefono_existe(telefono):
    # Crear una instancia de la clase Cliente para acceder a la base de datos
    cliente_db = Cliente('Prueva.db')

    # Ejecutar una consulta para buscar el teléfono en la base de datos
    resultado = cliente_db.consultar('''
        SELECT telefono FROM cliente WHERE telefono = ?
    ''', (telefono,))

    # Si el resultado no está vacío, significa que el teléfono ya existe
    if resultado:
        return True  # El teléfono ya existe
    else:
        return False  # El teléfono no existe


# Función para mostrar la ventana para agregar cliente
def mostrar_agregar_cliente():
    ventana2 = tk.Tk()
    ventana2.title("Agregar Cliente")
    ventana2.geometry("400x300")
    
    tk.Label(ventana2, text="Ingrese los datos del cliente para agregar:").pack(pady=10)
    
    # Campos de entrada para agregar un cliente (por ejemplo, nombre, teléfono)
    nombre_label = tk.Label(ventana2, text="Nombre:")
    nombre_label.pack(pady=5)
    nombre_text = tk.Entry(ventana2)
    nombre_text.pack(pady=5)
    
    telefono_label = tk.Label(ventana2, text="Teléfono:")
    telefono_label.pack(pady=5)
    telefono_text = tk.Entry(ventana2)
    telefono_text.pack(pady=5)
    
    def agregar_cliente():
        nombre = nombre_text.get()
        telefono = telefono_text.get()
        if nombre == "" or telefono == "":
            messagebox.showwarning("Campos Vacíos", "Por favor, complete todos los campos.")
        else:
            
            # Crear la transacción y agregarla a la base de datos
            agrCliente = Cliente('Prueva.db')  # Asegúrate de que la ruta a la base de datos sea correcta
            agrCliente.crear_cliente(nombre, telefono)

            messagebox.showinfo("Cliente agregado", f"Cliente {nombre} con teléfono {telefono} agregado.")
            ventana2.destroy()  # Cierra la ventana actual

    tk.Button(ventana2, text="Agregar Cliente", bg="green", fg="white", command=agregar_cliente).pack(pady=10)
    

# Función para mostrar la ventana principal
def mostrar_ventana_principal():
    
    ventana = tk.Tk()  # Ventana principal
    ventana.title("Verificar Cliente")
    ventana.geometry("400x200")
    ventana.config(bg="gray")

    miFrame = tk.Frame(ventana, width=400, height=200, bg="#c8c8c8")
    miFrame.pack()

    tk.Label(miFrame, text="Ingrese el número de teléfono del cliente:").pack(pady=10)
    telefonoText = tk.Entry(miFrame)
    telefonoText.pack(pady=5)

    def continuar():
        telefono = telefonoText.get()
        if telefono == "":
            messagebox.showwarning("Campos Vacíos", "Por favor, ingrese el número de teléfono.")
        else:
            if verificar_telefono_existe(telefono):
                messagebox.showinfo("Cliente encontrado", "Cliente encontrado en la base de datos.")
                
                mostrar_agregar_direccion(telefono)
            else:
                messagebox.showinfo("error", "cliente no encontrado")

    tk.Button(miFrame, text="Continuar", bg="green", fg="white", command=continuar).pack(pady=10)
    tk.Button(miFrame, text="Agregar Cliente", bg="blue", fg="white", command=mostrar_agregar_cliente).pack(pady=10)
    ventana.mainloop()

<<<<<<< HEAD



=======
>>>>>>> cf0d2947ba95f413d8a49c00400c0a2eb95d7a8b
