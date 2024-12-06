import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3 as sql
from datetime import datetime  # Importar el módulo datetime

def mostrar_agregar_direccion():
   
    ventana.title("Agregar Dirección")
    ventana.geometry("600x600")
    ventana.config(bg="gray")

    miFrame = tk.Frame(ventana, width=500, height=500, bg="#c8c8c8")
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
    nombreText = tk.Entry(miFrame, validate="key", validatecommand=(ventana.register(validar_entrada_letras), "%P"))
    nombreText.place(x=110, y=50)

    tk.Label(miFrame, text="Número de Teléfono").place(x=250, y=50)
    numeroText = tk.Entry(miFrame, validate="key", validatecommand=(ventana.register(validar_entrada_numeros), "%P"))
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
    codPostText = tk.Entry(miFrame, validate="key", validatecommand=(ventana.register(validar_entrada_numeros), "%P"))
    codPostText.place(x=350, y=150)

    tk.Label(miFrame, text="Referencia").place(x=50, y=200)
    referenciaText = tk.Entry(miFrame)
    referenciaText.place(x=120, y=200, width=300)

    # Función de validación de campos vacíos
    def validar_campos():
        if not (nombreText.get() and numeroText.get() and calleText.get() and numExtText.get() and
                coloniaText.get() and codPostText.get() and referenciaText.get()):
            messagebox.showwarning("Campos Vacíos", "Por favor, rellene todos los campos.")
        else:
            # Aquí puedes agregar la lógica para procesar los datos
            mostrar_buscar_videojuegos(nombreText.get(), calleText.get())

    # Botones
    tk.Button(miFrame, text="Confirmar", bg="green", fg="white", command=validar_campos).place(x=300, y=450)
    tk.Button(miFrame, text="Atrás", bg="red", fg="white", command=ventana.destroy).place(x=100, y=450)

# Pantalla de buscar videojuegos
def mostrar_buscar_videojuegos(nombreText, calleText):
    for widget in ventana.winfo_children():
        widget.destroy()

    ventana.title("Buscar Videojuegos")
    ventana.geometry('600x400')
    ventana.config(bg="#c8c8c8")

    def buscar_en_lista(event=None):
        termino = entrada.get().lower()
        lista_filtrada = [item for item in videojuegos if termino in item.lower()]
        actualizar_lista(lista_filtrada)

    def actualizar_lista(lista_filtrada):
        listbox.delete(0, tk.END)
        for item in lista_filtrada:
            listbox.insert(tk.END, item)

    def buscar_elemento():
        try:
            seleccionado = listbox.get(listbox.curselection())
            if seleccionado in videojuegos_disponibles:
                abrir_ventana_compra(seleccionado)
            else:
                messagebox.showinfo("No disponible", f"El videojuego '{seleccionado}' no está disponible.")
        except tk.TclError:
            messagebox.showwarning("Selección vacía", "Por favor, selecciona un videojuego para buscar.")

    def abrir_ventana_compra(videojuego):
        """Abre una nueva ventana con la información detallada del videojuego seleccionado."""
        nueva_ventana = tk.Toplevel(ventana)
        nueva_ventana.geometry("350x450")
        nueva_ventana.title(f"Detalles de {videojuego}")
        nueva_ventana.config(bg="#f9f9f9")

        plataforma = plataformas[videojuego]
        precio_unitario = 1200  # Precio fijo por videojuego (puedes cambiarlo según tu lógica)
        cantidad = 1  # Cantidad fija no editable
        costo_envio = tk.DoubleVar(value=30.0)  # Variable para el costo de envío
        metodo_pago = tk.StringVar(value="seleccione un metodo de pago")  # Método de pago seleccionado (default)

        def calcular_total():
            """Calcula el total basado en la cantidad y el costo de envío."""
            try:
                envio = costo_envio.get()
                total = (precio_unitario * cantidad) + envio
                total_label.config(text=f"$ {total:.2f}")
            except tk.TclError:
                total_label.config(text="Error en los valores")

        # Título del videojuego
        ttk.Label(nueva_ventana, text=f"{videojuego}", font=("Times New Roman", 14, "bold"), background="#f9f9f9").pack(pady=10)

        # Plataforma
        ttk.Label(nueva_ventana, text=f"Plataforma: {plataforma}", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)

        # Cantidad
        ttk.Label(nueva_ventana, text="Cantidad:", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)
        cantidad_label = ttk.Label(nueva_ventana, text=int(cantidad), anchor="center", font=("Times New Roman", 12),background="#f9f9f9", width=10)
        cantidad_label.pack(pady=5)

        # Costo de envío
        ttk.Label(nueva_ventana, text="Costo de envío:", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)
        envio_entry = ttk.Entry(nueva_ventana, textvariable=costo_envio, width=10, justify="center")
        envio_entry.pack(pady=5)
        costo_envio.trace("w", lambda *args: calcular_total())  # Actualizar total al cambiar el costo de envío

        # Total
        ttk.Label(nueva_ventana, text="Total:", font=("Times New Roman", 12, "bold"), background="#f9f9f9").pack(pady=5)
        total_label = ttk.Label(nueva_ventana, text=f"$ {precio_unitario + costo_envio.get():.2f}", font=("Times New Roman", 12), background="#f9f9f9")
        total_label.pack(pady=5)

        # Tipo de transacción
        ttk.Label(nueva_ventana, text="Tipo de transacción:", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)
        combobox_metodo_pago = ttk.Combobox(nueva_ventana, textvariable=metodo_pago, state="readonly", values=["Tarjeta", "Efectivo"])
        combobox_metodo_pago.pack(pady=5)

        # Botones de Confirmar y Cancelar
        botones_frame = ttk.Frame(nueva_ventana)
        botones_frame.pack(pady=20)

        cancelar_btn = ttk.Button(botones_frame, text="Cancelar", command=nueva_ventana.destroy)
        cancelar_btn.grid(row=0, column=0, padx=10)

        confirmar_btn = ttk.Button(botones_frame, text="Confirmar", command=lambda: compra_exitosa(nueva_ventana, videojuego, metodo_pago.get()))
        confirmar_btn.grid(row=0, column=1, padx=10)

    def compra_exitosa(ventana_compra, videojuego, metodo_pago):
        ventana_compra.destroy()
         # Obtener la fecha actual en formato de cadena
        fecha_inicio = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        fecha_final = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        messagebox.showinfo("Compra Exitosa", f"Has comprado '{videojuego}' con éxito.\nMétodo de pago: {metodo_pago} \nNombre: {nombreText}"+
                            f"\nCalle: {calleText} \nFecha inicio: {fecha_inicio}, Fecha Final: {fecha_final}  ")

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

    videojuegos = [
        "The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey", "Halo Infinite", "God of War Ragnarok",
        "Elden Ring", "Hollow Knight", "Minecraft", "Fortnite", "Cyberpunk 2077", "Red Dead Redemption 2",
        "The Witcher 3", "Among Us", "League of Legends", "Call of Duty: Modern Warfare II", "Final Fantasy XVI"
    ]

    videojuegos_disponibles = [
        "The Legend of Zelda: Breath of the Wild", "God of War Ragnarok", "Elden Ring", "Minecraft", "Red Dead Redemption 2"
    ]

    plataformas = {
        "The Legend of Zelda: Breath of the Wild": "Nintendo Switch",
        "Super Mario Odyssey": "Nintendo Switch",
        "Halo Infinite": "Xbox Series X|S",
        "God of War Ragnarok": "PlayStation 5",
        "Elden Ring": "Multiplataforma",
        "Hollow Knight": "Multiplataforma",
        "Minecraft": "Multiplataforma",
        "Fortnite": "Multiplataforma",
        "Cyberpunk 2077": "Multiplataforma",
        "Red Dead Redemption 2": "Multiplataforma",
        "The Witcher 3": "Multiplataforma",
        "Among Us": "Multiplataforma",
        "League of Legends": "PC",
        "Call of Duty: Modern Warfare II": "Multiplataforma",
        "Final Fantasy XVI": "PlayStation 5"
    }

    actualizar_lista(videojuegos)

# Inicio de la aplicación
ventana = tk.Tk()
mostrar_agregar_direccion()
ventana.mainloop()