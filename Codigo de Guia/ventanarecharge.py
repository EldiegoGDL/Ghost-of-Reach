import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage

#funciones
def ticket():
    # guardamos los datos
    comp=compañia.get()
    numerotelefono=num1.get()
    canti=cantidad.get()
    M=print(" ",comp,"\n",numerotelefono,"\n",canti)
    return(M)
def clickr():
    n1=num1.get()
    n2=num2.get()

    #verificamos que los datos concuerden con lo que solicitamos ejemplo=numeros sean digitos y no letras
    if (n1.isdigit()==False) or (n2.isdigit()==False) :
        try:
            n1=(num1.get())
            n2=(num2.get())
            num=int(n1)
            numm=int(n2)
            if (1000000000 <= num <= 10000000000) or (1000000000 <= numm <= 10000000000):
                return(num,numm)
        except ValueError:
            messagebox.showerror('ERROR RECOPILACION','Numero incompleto')
    else:
        #verificamos que todos los espacios deben de estar llenos   
        if n1=="" or n2=="":
            messagebox.showerror("ERROR","completa todo los apartados")
        else:
            num=int(n1)
            numm=int(n2)
            if (num <= 1000000000 or  num>= 10000000000) or (numm <= 1000000000 or  numm>= 10000000000):
                messagebox.showerror("ERROR","numero incompleto")
            else:
                if num==numm:
                    messagebox.showinfo("Recarga","La recarga ha sido completada exitosamente")
                    ticket()
                else:
                    messagebox.showerror("Error","Los Numeros no coinciden")
       
#ventana de las recargas
ventanarecarga=tk.Tk()
ventanarecarga.geometry('800x600')
ventanarecarga.title('Recargas')
#textos
Comp=ttk.Label(ventanarecarga, text='Compañia',font=('Times New Roman',20))
Comp.place(x=75,y=15)

Numero=ttk.Label(ventanarecarga, text='Numero de Telefono',font=('Times New Roman',30))
Numero.place(x=100,y=100)

confNumero=ttk.Label(ventanarecarga, text='Confirmar Numero de Telefono',font=('Times New Roman',30))
confNumero.place(x=100,y=250)

can=ttk.Label(ventanarecarga, text='Cantidad a pagar',font=('Times New Roman',20))
can.place(x=100,y=370)
#entrada del numero
num1=ttk.Entry(ventanarecarga,show="*",font=('Times New Roman',20))
num1.place(x=100,y=150)

num2=ttk.Entry(ventanarecarga,font=('Times New Roman',20))
num2.place(x=100,y=300)

#lista de compañias 
compañia=ttk.Combobox(state="readonly",
          values=("Telcel","AT&T","Movistar","Unefon"))
compañia.place(x=200,y=25)

cantidad=ttk.Combobox(state='readonly',
                      values=("$20","$30","$50","$100","$150","$200","$250","$300"))
cantidad.place(x=300,y=380)
#boton para guardar
imagen=PhotoImage(file="guardar.png")
save = ttk.Button(width=5,image=imagen)
save.place(x=350, y=22)

cobro=ttk.Button(width=50,command=clickr,text="cobrar")
cobro.place(x=200, y=450)



       
        
ventanarecarga.mainloop()