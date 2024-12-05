import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage

#Ventana Inicio

MainV= tk.Tk()
MainV.geometry ("300x500")
MainV.resizable(0,0)
MainV.configure(bg="cornflowerblue")
MainV.title("Ventana Principal")

#Texto Ventana
bienvenida=ttk.Label(text="Bienvenidos", font=("Arial Black",15) )

#ubicacion de los textos
bienvenida.place(x=75,y=10)

# Estilo para botones
style = ttk.Style()
style.configure("TButton",
                background="#0000FF",  # Color azul para los botones
                foreground="blue",     # Texto azul en los botones
                font=("Arial", 10))

#Botones 
inventario= ttk.Button(text="Inventario")
inventario.place(x=100,y=150)

compraFisica=ttk.Button(text="Compra Fisica")
compraFisica.place(x=95,y=200)

compraDomicilio=ttk.Button(text="Compra A Domicilio")
compraDomicilio.place(x=80, y=250)


MainV.mainloop()
