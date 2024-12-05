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
MainV.title("Ventana Principal")

#Texto Ventana
bienvenida=ttk.Label(text="Bienvenidos", font=("Arial Black",15) )
#inventario=ttk.Label(text="Inventario",font=("Arial Black",15))
#compraFisica=ttk.Label(text="Compra Fisica",font=("Arial Black",15))
#compraDomicilio=ttk.Label(text="Compra Domicilio",font=("Arial Black",15))


#ubicacion de los textos
bienvenida.place(x=75,y=10)
#inventario.place(x=75,y=125)
#compraFisica.place(x=75,y= 250)
#compraDomicilio.place(x=60,y=350)

#Botones 
inventario= ttk.Button(text="Inventario")
inventario.place(x=100,y=150)

compraFisica=ttk.Button(text="Compra Fisica")
compraFisica.place(x=95,y=200)

compraDomicilio=ttk.Button(text="Compra A Domicilio")
compraDomicilio.place(x=80, y=250)


MainV.mainloop()
