import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage


class BaseDatos:
    def __init__(self, db_name):
        self.db_name = db_name

    def conectar(self):
        return sql.connect(self.db_name)

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

#creacion de ventana 
ventana = tk.Tk()
ventana.title("Empleado_cliente")
ventana.config(background="#2f3e46")
ventana.geometry("400x300")

tk.Label(text="Bienvenidos al registro de clientes y empleados",font=10, bg="#2f3e46",fg="#cad2c5").pack(pady=10)
tk.Button( text="Agregar Empleado",font=10,  bg="#52796f", fg="#cad2c5").pack(pady=30)
tk.Button( text="Agregar Cliente",font=10, bg="#52796f", fg="#cad2c5").pack(pady=30)

# Ejecutar la ventana
ventana.mainloop()