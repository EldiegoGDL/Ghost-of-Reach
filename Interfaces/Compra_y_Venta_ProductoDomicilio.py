import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def buscar_en_lista(event=None):
    """Filtra los videojuegos según el texto ingresado en el Entry."""
    termino = entrada.get().lower()  # Obtener texto del Entry y convertir a minúsculas
    lista_filtrada = [item for item in videojuegos if termino in item.lower()]  # Filtrar lista
    actualizar_lista(lista_filtrada)

def actualizar_lista(lista_filtrada):
    """Actualiza el Listbox con los videojuegos filtrados."""
    listbox.delete(0, tk.END)  # Eliminar elementos actuales
    for item in lista_filtrada:
        listbox.insert(tk.END, item)  # Insertar elementos filtrados

def buscar_elemento():
    """Verifica si el videojuego seleccionado está disponible y realiza la acción correspondiente."""
    try:
        seleccionado = listbox.get(listbox.curselection())  # Obtener el videojuego seleccionado
        if seleccionado in videojuegos_disponibles:
            abrir_nueva_ventana(seleccionado)
        else:
            messagebox.showinfo("No disponible", f"El videojuego '{seleccionado}' no está disponible.")
    except tk.TclError:
        messagebox.showwarning("Selección vacía", "Por favor, selecciona un videojuego para buscar.")

def abrir_nueva_ventana(videojuego):
    """Abre una nueva ventana con la información detallada del videojuego seleccionado."""
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.geometry("350x400")
    nueva_ventana.title(f"Detalles de {videojuego}")
    nueva_ventana.config(bg="#f9f9f9")

    plataforma = plataformas[videojuego]
    precio_unitario = 1200  # Precio fijo por videojuego (puedes cambiarlo según tu lógica)
    cantidad = tk.IntVar(value=1)  # Variable para la cantidad seleccionada
    costo_envio = tk.DoubleVar(value=30.0)  # Variable para el costo de envío

    def calcular_total():
        """Calcula el total basado en la cantidad y el costo de envío."""
        try:
            envio = costo_envio.get()
            total = (precio_unitario * cantidad.get()) + envio
            total_label.config(text=f"$ {total:.2f}")
        except tk.TclError:
            total_label.config(text="Error en los valores")

    # Título del videojuego
    ttk.Label(nueva_ventana, text=f"{videojuego}", font=("Times New Roman", 14, "bold"), background="#f9f9f9").pack(pady=10)

    # Plataforma
    ttk.Label(nueva_ventana, text=f"Plataforma: {plataforma}", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)

    # Cantidad
    ttk.Label(nueva_ventana, text="Cantidad:", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)
    cantidad_entry = ttk.Entry(nueva_ventana, textvariable=cantidad, width=5, justify="center")
    cantidad_entry.pack(pady=5)
    cantidad.trace("w", lambda *args: calcular_total())  # Actualizar total al cambiar la cantidad

    # Costo de envío
    ttk.Label(nueva_ventana, text="Costo de envío:", font=("Times New Roman", 12), background="#f9f9f9").pack(pady=5)
    envio_entry = ttk.Entry(nueva_ventana, textvariable=costo_envio, width=10, justify="center")
    envio_entry.pack(pady=5)
    costo_envio.trace("w", lambda *args: calcular_total())  # Actualizar total al cambiar el costo de envío

    # Total
    ttk.Label(nueva_ventana, text="Total:", font=("Times New Roman", 12, "bold"), background="#f9f9f9").pack(pady=5)
    total_label = ttk.Label(nueva_ventana, text=f"$ {precio_unitario + costo_envio.get():.2f}", font=("Times New Roman", 12), background="#f9f9f9")
    total_label.pack(pady=5)

    # Botones de Confirmar y Cancelar
    botones_frame = ttk.Frame(nueva_ventana)
    botones_frame.pack(pady=20)

    cancelar_btn = ttk.Button(botones_frame, text="Cancelar", command=nueva_ventana.destroy)
    cancelar_btn.grid(row=0, column=0, padx=10)

    confirmar_btn = ttk.Button(botones_frame, text="Confirmar", command=lambda: compra_exitosa(nueva_ventana, videojuego))
    confirmar_btn.grid(row=0, column=1, padx=10)


def confirmar_compra(videojuego):
    """Abre una ventana para confirmar la compra del videojuego."""
    ventana_compra = tk.Toplevel(ventana)
    ventana_compra.geometry("300x150")
    ventana_compra.title("Confirmar Compra")
    ventana_compra.config(bg="#c8c8c8")

    etiqueta = ttk.Label(ventana_compra, text=f"¿Deseas comprar '{videojuego}'?", font=("Times New Roman", 12),background="#c8c8c8")
    etiqueta.pack(pady=20)

    confirmar_btn = ttk.Button(ventana_compra, text="Confirmar", command=lambda: compra_exitosa(ventana_compra, videojuego))
    confirmar_btn.pack(pady=5)

    cancelar_btn = ttk.Button(ventana_compra, text="Cancelar", command=ventana_compra.destroy)
    cancelar_btn.pack(pady=5)

def compra_exitosa(ventana_compra, videojuego):
    """Muestra un mensaje de compra exitosa y cierra la ventana de confirmación."""
    ventana_compra.destroy()
    messagebox.showinfo("Compra Exitosa", f"Has comprado '{videojuego}' con éxito.")

# Crear ventana principal
ventana = tk.Tk()
ventana.geometry('600x400')
ventana.resizable(0, 0)
ventana.title("Buscador de Videojuegos")
ventana.config(bg="#c8c8c8")

# Etiqueta para el Entry
etiqueta = ttk.Label(ventana, text="Buscar:", font=("Times New Roman", 15),background="#c8c8c8")
etiqueta.pack(pady=10, anchor="w", padx=20)

# Entry para ingresar el texto de búsqueda
entrada = ttk.Entry(ventana, width=50)
entrada.pack(pady=5, padx=20, anchor="w")
entrada.bind("<KeyRelease>", buscar_en_lista)  # Buscar en tiempo real

# Listbox para mostrar los videojuegos
listbox_frame = ttk.Frame(ventana)
listbox_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

scrollbar = ttk.Scrollbar(listbox_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox = tk.Listbox(listbox_frame, font=("Times New Roman", 12), yscrollcommand=scrollbar.set)
listbox.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Botón para buscar videojuego
boton_buscar = ttk.Button(ventana, text="Buscar", command=buscar_elemento)
boton_buscar.pack(pady=10)

# Lista inicial de videojuegos
videojuegos = [
    "The Legend of Zelda: Breath of the Wild", "Super Mario Odyssey", 
    "Halo Infinite", "God of War Ragnarok", "Elden Ring", 
    "Hollow Knight", "Minecraft", "Fortnite", "Cyberpunk 2077", 
    "Red Dead Redemption 2", "The Witcher 3", "Among Us", 
    "League of Legends", "Call of Duty: Modern Warfare II", 
    "Final Fantasy XVI"
]

# Lista de videojuegos disponibles
videojuegos_disponibles = [
    "The Legend of Zelda: Breath of the Wild", "God of War Ragnarok", 
    "Elden Ring", "Minecraft", "Red Dead Redemption 2"
]

# Diccionario de plataformas
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

# Cargar videojuegos iniciales en el Listbox
actualizar_lista(videojuegos)

# Ejecutar la ventana
ventana.mainloop()
