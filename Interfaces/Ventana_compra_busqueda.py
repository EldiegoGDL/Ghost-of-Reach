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
    """Abre una nueva ventana con la información del videojuego seleccionado."""
    nueva_ventana = tk.Toplevel(ventana)
    nueva_ventana.geometry("300x200")
    nueva_ventana.title(f"Detalles de {videojuego}")
    nueva_ventana.config(bg="#c8c8c8")

    # Obtener plataforma del videojuego
    plataforma = plataformas[videojuego]

    etiqueta = ttk.Label(nueva_ventana, text=f"Plataforma: {plataforma}", font=("Times New Roman", 12),background="#c8c8c8")
    etiqueta.pack(pady=20)

    comprar_btn = ttk.Button(nueva_ventana, text="Comprar", command=lambda: confirmar_compra(videojuego))
    comprar_btn.pack(pady=10)

    cerrar_btn = ttk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy)
    cerrar_btn.pack(pady=10)

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
