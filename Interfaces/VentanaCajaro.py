import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage


def ventana_busqueda():
    def pasar_ventana():
        Ventana.destroy()
        realizar_compra()
    ## abrimos la ventana

    # asignamos los tamanios de la ventana
    Ventana = tk.Tk()
    Ventana.geometry('750x350')
    Ventana.resizable(0,0)
    Ventana.config(bg="darkgray")

    # asignamos las celdas de los elementos
    texto_nombre = ttk.Label(text="Nombre Producto",font=("Times Nwe Roman",15),background='darkgray')
    
    texto_nombre.place(x=20,y=50)
    
    # almacenamos la entrada de texto
    Entrada_texto_nombre = tk.StringVar()
    Entrada_texto_plataforma = tk.StringVar()

    # asignamos las cajas de texto
    caja_texto_nombre = tk.Entry(Ventana, width=60, textvariable=Entrada_texto_nombre,font=("Times Nwe Roman",10))

    caja_texto_nombre.place(x=250,y=50)

    #boton
    Buscar=tk.Button(text='Buscar',width=15,bg='lightgrey',command=pasar_ventana)

    Buscar.place(x=330,y=270)
    Ventana.state()


    ## ciclamos la ventana
    Ventana.mainloop()


def realizar_compra():
    Ventana_compra = tk.Tk()
    Ventana_compra.geometry('750x350')
    Ventana_compra.resizable(0,0)
    Ventana_compra.config(bg="darkgray")


    Ventana_compra.mainloop()

ventana_busqueda()