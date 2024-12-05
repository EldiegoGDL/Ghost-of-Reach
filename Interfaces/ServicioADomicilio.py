from tkinter import *
import sqlite3 as sql

ventana = Tk()
ventana.title("HOME")
ventana.geometry("600x600")
ventana.config(bg="gray")

miFrame = Frame(ventana, width=500, height=500, bg="#c8c8c8")
miFrame.pack()

#cuadros de las infos
nombreLab = Label(miFrame, text="Nombre ")
nombreLab.place(x=50, y=50)
numeroText = Entry(miFrame)
numeroText.place(x=110, y=50)

numeroLab = Label(miFrame, text="Numero de \ntelefono ")
numeroLab.place(x=250, y=50)
numeroText = Entry(miFrame)
numeroText.place(x=320, y=50)

calleLab = Label(miFrame, text="Calle ")
calleLab.place(x=50, y=100)
calleText = Entry(miFrame)
calleText.place(x=100, y=100)

numExtLab = Label(miFrame, text="N. Exterior ")
numExtLab.place(x=250, y=100)
numExtText = Entry(miFrame)
numExtText.place(x=320, y=100)

coloniaLab = Label(miFrame, text="Colonia ")
coloniaLab.place(x=50, y=150)
coloniaText = Entry(miFrame)
coloniaText.place(x=100, y=150)

codPostLab = Label(miFrame, text="Codigo \nPostal ")
codPostLab.place(x=250, y=150)
codPostText = Entry(miFrame)
codPostText.place(x=300, y=150)

referenciaLab = Label(miFrame, text="Referencia ")
referenciaLab.place(x=50, y=200)
referenciaText = Entry(miFrame)
referenciaText.place(x=120, y=200, width=300)

confirmBoton = Button(miFrame, text="Confirmar", bg="green", fg="white").place(x=300, y=450)
cancelBoton = Button(miFrame, text="atras", bg="red", fg="white").place(x=100, y=450)


ventana.mainloop()