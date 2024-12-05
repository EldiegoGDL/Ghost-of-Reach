import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage

def agregar_articulo():
    def imprimir():
        #conectamos base de datos
        N1=entr_cantidad.get()
        conn=sql.connect("usuariosnew.db")
        cursor= conn.cursor()
        cursor.execute("SELECT Precio*Cantidad From Inventario")
        fila=cursor.fetchall()
        print(fila)


        conn.close()
        
    #entrada de datos
    cosos=tk.Tk()
    cosos.geometry("500x50")
    cosos.title("Articulo")
    cosos.resizable(0,0)

    #entrada de texto en el articulo
    cos_articulo=ttk.Label(cosos,text="Articulo",font=("Arial Black",10))
    cos_cantidad=ttk.Label(cosos,text="cantidad",font=("Arial Black",10))
    cos_articulo.place(x=0,y=0)
    cos_cantidad.place(x=200,y=0)

    #Entrada de datos en la ventana de articulos
    entr_articulo=ttk.Entry(cosos)
    entr_cantidad=ttk.Entry(cosos)
    entr_articulo.place(x=0,y=20)
    entr_cantidad.place(x=200,y=20)

    algo=ttk.Button(cosos,text="agregar",command=imprimir)
    algo.place(x=400,y=20)

    #cerramos la base de datos y la ventana
    cosos.mainloop()

#ventana
carrito=tk.Tk()
carrito.geometry("800x600")
carrito.resizable(0,0)
carrito.title("CARRITO")

#texto de la ventana
mssArticulo=ttk.Label(text="Articulo",font=("Arial Black",15))
mssCantidad=ttk.Label(text="Cantidad",font=("Arial Black",15))
mssPresio=ttk.Label(text="Presio",font=("Arial Black",15))
mssCosto=ttk.Label(text="Total",font=("Arial Black",15))
#ubicacion de los textos
mssArticulo.place(x=50,y=1)
mssCantidad.place(x=200,y=1)
mssCosto.place(x=500,y=1)
mssPresio.place(x=350,y=1)

#botones
agregar=ttk.Button(text="Agregar Articulo",command=agregar_articulo)
agregar.place(x=650,y=10)

cobrarr=ttk.Button(text="Cobrar")
cobrarr.place(x=650,y=75)

carrito.mainloop()