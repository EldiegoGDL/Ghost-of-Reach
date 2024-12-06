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
        
        
#empleado
class Empleado(BaseDatos):
     def __init__(self, db_name):
        super().__init__(db_name)
     def crear_empleado(self,nombreEm, apellido, telefono,contraseña, id_departamento ):
         self.ejecutar('''
                  INSERT INTO Empleado (nombre_empleado, apellido_empleado, Telefono, contraseña,id_departamento)
                  VALUES(?, ?, ?, ?, ?)
                  ''',(nombreEm, apellido, telefono,contraseña, id_departamento ))
#crear instancia 
empleado_db=Empleado('Prueva.db')

#agregar empleado

def agregar_empleado():
    def agregar():
        nombreEm = entry_nombreEm.get()
        apellido = entry_apellido.get()
        telefono = entry_telefono.get()
        contraseña = entry_contraseña.get()
        id_departamento = entry_id_departamento.get()
        empleado_db.crear_empleado(nombreEm, apellido, telefono,contraseña, id_departamento )  
        messagebox.showinfo("Empleado Agregado", "Empleado agregado exitosamente")
        agregarE.destroy()
        
    agregarE = tk.Toplevel()
    agregarE.title("Agregar Empleado")
    agregarE.geometry("300x450")
    agregarE.configure(bg="#2f3e46")
    agregarE.resizable(0,0)
    
    tk.Label(agregarE, text="Nombre", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_nombreEm = tk.Entry(agregarE, bg="#84a98c", fg="#2f3e46")
    entry_nombreEm.pack(pady=5)

    tk.Label(agregarE, text="Apellido", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_apellido = tk.Entry(agregarE, bg="#84a98c", fg="#2f3e46")
    entry_apellido.pack(pady=5)

    tk.Label(agregarE, text="Telefono", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_telefono = tk.Entry(agregarE, bg="#84a98c", fg="#2f3e46")
    entry_telefono.pack(pady=5)

    tk.Label(agregarE, text="contraseña", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_contraseña = tk.Entry(agregarE, bg="#84a98c", fg="#2f3e46")
    entry_contraseña.pack(pady=5)

    tk.Label(agregarE, text="id_departamento", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_id_departamento = tk.Entry(agregarE, bg="#84a98c", fg="#2f3e46")
    entry_id_departamento.pack(pady=5)
    
    tk.Button(agregarE, text="Agregar", command=agregar, bg="#52796f", fg="#cad2c5").pack(pady=10)
    
    
#Cliente 
class Cliente(BaseDatos):
    def __init__(self, db_name):
        super().__init__(db_name)
    def crear_cliente(self, nombreC, telefono):
            self.ejecutar('''
                          INSERT INTO cliente (nombre_cliente, telefono)
                          VALUES(?, ?)
                          ''',(nombreC, telefono))
#crear instancia             
cliente_db=Cliente('Prueva.db')  

#agregar empleado

def agregar_cliente():
    def agregarCliente():
        nombreC = entry_nombreC.get()
        telefono = entry_telefono.get()
        cliente_db.crear_cliente(nombreC,telefono)
        messagebox.showinfo("Cliente Agregado", "Cliente agregado exitosamente")
        agregarC.destroy()
        
    agregarC = tk.Toplevel()
    agregarC.title("Agregar Cliente")
    agregarC.geometry("300x450")
    agregarC.configure(bg="#2f3e46")
    agregarC.resizable(0,0)
    
    tk.Label(agregarC, text="Nombre", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_nombreC = tk.Entry(agregarC, bg="#84a98c", fg="#2f3e46")
    entry_nombreC.pack(pady=5)

    tk.Label(agregarC, text="Telefono", bg="#52796f", fg="#cad2c5").pack(pady=5)
    entry_telefono = tk.Entry(agregarC, bg="#84a98c", fg="#2f3e46")
    entry_telefono.pack(pady=5)
        
    tk.Button(agregarC, text="Agregar", command=agregarCliente, bg="#52796f", fg="#cad2c5").pack(pady=10)

#creacion de ventana 
root = tk.Tk()
root.title("Empleado_cliente")
root.config(background="#2f3e46")
root.geometry("400x300")

tk.Label(root,text="Bienvenidos al registro de clientes y empleados",font=10, bg="#2f3e46",fg="#cad2c5").pack(pady=10)
tk.Button(root, text="Agregar Empleado",command=agregar_empleado,font=10,  bg="#52796f", fg="#cad2c5").pack(pady=30)
tk.Button(root, text="Agregar Cliente",command=agregar_cliente,font=10, bg="#52796f", fg="#cad2c5").pack(pady=30)

# Ejecutar la ventana
root.mainloop()