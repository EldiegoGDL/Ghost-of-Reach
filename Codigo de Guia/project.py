import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import Menu
import sqlite3 as sql
from tkinter import PhotoImage
#show
#Diego ignacio Garcia Diaz de Leon
#projecto
#09/04/2023
# Version_1.10.2

#definimos las funciones

def register():        #registramos un usuario

    def click(): # le damos la accion del boton crear usuario
        #entran los datos
        conn=sql.connect("usuariosnew.db")
        cursor= conn.cursor()
        n1=str(nombre_sql.get())
        n2=str(usuario_sql.get())
        n3=str(contraseña_sql.get())
        n4=(telefono_sql.get())
        #verificamos que los datos concuerden con lo que solicitamos ejemplo=numeros sean digitos y no letras
        if n4.isdigit()==False:
            try:
                n4=(telefono_sql.get())
                num=int(n4)
                if 1000000000 <= num <= 10000000000:
                    return(num)
            except ValueError:
                messagebox.showerror('ERROR RECOPILACION','Numero incompleto')
                ventana.state("iconic")
        else:
            #verificamos que todos los espacios deben de estar llenos   
            if n1=="" or n2=="" or n3=="" or n4=="":
                messagebox.showerror("ERROR","completa todo los apartados")
                ventana.state("iconic")
            else:
                num=int(n4)
                if num <= 1000000000 or  num>= 10000000000:
                    messagebox.showerror("ERROR","numero incompleto")
                    ventana.state("iconic")
                else:
                    #guardamos los datos ingresados a la base de datos
                    bin = "INSERT INTO usuarios (nombre, usuario, contraseña, direccion) VALUES (?, ?, ?, ?)"
                    cursor.execute(bin, (n1,n2,n3,n4))
                    conn.commit()
                    messagebox.showinfo("REGISTRO COMPLETADO","TU CUENTA YA HA SIDO REGISTRADA" )
                    conn.close()
                    regis.destroy()
                    ventana.state('normal')
        
    regis=tk.Tk()
    regis.geometry("600x300")
    regis.title("Registro de Usuario")
    regis.resizable(0,0)
    #textos de registro
    text_nombre=ttk.Label(regis, text="NOMBRE",font=("Times New Roman",15))
    text_nombre.place(x=0,y=50)
    text_usuario=ttk.Label(regis, text="USUARIO",font=("Times New Roman",15))
    text_usuario.place(x=0,y=100)
    text_contraseña=ttk.Label(regis, text="CONTRASEÑA",font=("Times New Roman",15))
    text_contraseña.place(x=0,y=150)
    text_direccion=ttk.Label(regis, text="TELEFONO",font=("Times New Roman",15))
    text_direccion.place(x=0,y=200)
    #entrada de datos de registro
    n=tk.StringVar()
    nombre_sql=ttk.Entry(regis,width=20, textvariable=n,font=("Times New Roman",10))
    nombre_sql.place(x=150,y=50)
    usuario_sql=ttk.Entry(regis,width=20, font=("Times New Roman",10))
    usuario_sql.place(x=150,y=100)
    contraseña_sql=tk.Entry(regis,width=20, font=("Times New Roman",10))
    contraseña_sql.place(x=150,y=150)
    telefono_sql=ttk.Entry(regis,width=25,font=("Times New Roman",10))
    telefono_sql.place(x=150,y=200)
    
    sqlregistro=tk.Button(regis, text="crar usuario",command=click)
    sqlregistro.place(x=150,y=225)


def iniciarsecion():    #inicio de secion
    n1=usu.get() 
    n2=contra.get()
    
    conn=sql.connect("usuariosnew.db")
    cursor= conn.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?', (n1, n2))
     
    if cursor.fetchall():
        messagebox.showinfo("Bienvenido",'HOLA '+n1)
        ventana.destroy()
        Punto_de_venta()
         
    else:
        messagebox.showerror("Error",'contraseña o usuario incorrectos')
        
def Punto_de_venta():
    def regreso():
        def register():        #registramos un usuario

            def click(): # le damos la accion del boton crear usuario
                #entran los datos
                conn=sql.connect("usuariosnew.db")
                cursor= conn.cursor()
                n1=str(nombre_sql.get())
                n2=str(usuario_sql.get())
                n3=str(contraseña_sql.get())
                n4=(telefono_sql.get())
                #verificamos que los datos concuerden con lo que solicitamos ejemplo=numeros sean digitos y no letras
                if n4.isdigit()==False:
                    try:
                        n4=(telefono_sql.get())
                        num=int(n4)
                        if 1000000000 <= num <= 10000000000:
                            return(num)
                    except ValueError:
                        messagebox.showerror('ERROR RECOPILACION','Numero incompleto')
                        ventana.state("iconic")
                else:
                    #verificamos que todos los espacios deben de estar llenos   
                    if n1=="" or n2=="" or n3=="" or n4=="":
                        messagebox.showerror("ERROR","completa todo los apartados")
                        ventana.state("iconic")
                    else:
                        num=int(n4)
                        if num <= 1000000000 or  num>= 10000000000:
                            messagebox.showerror("ERROR","numero incompleto")
                            ventana.state("iconic")
                        else:
                            #guardamos los datos ingresados a la base de datos
                            bin = "INSERT INTO usuarios (nombre, usuario, contraseña, direccion) VALUES (?, ?, ?, ?)"
                            cursor.execute(bin, (n1,n2,n3,n4))
                            conn.commit()
                            messagebox.showinfo("REGISTRO COMPLETADO","TU CUENTA YA HA SIDO REGISTRADA" )
                            conn.close()
                            regis.destroy()
                            ventana.state('normal')
                
            regis=tk.Tk()
            regis.geometry("600x300")
            regis.title("Registro de Usuario")
            regis.resizable(0,0)
            #textos de registro
            text_nombre=ttk.Label(regis, text="NOMBRE",font=("Times New Roman",15))
            text_nombre.place(x=0,y=50)
            text_usuario=ttk.Label(regis, text="USUARIO",font=("Times New Roman",15))
            text_usuario.place(x=0,y=100)
            text_contraseña=ttk.Label(regis, text="CONTRASEÑA",font=("Times New Roman",15))
            text_contraseña.place(x=0,y=150)
            text_direccion=ttk.Label(regis, text="TELEFONO",font=("Times New Roman",15))
            text_direccion.place(x=0,y=200)
            #entrada de datos de registro
            n=tk.StringVar()
            nombre_sql=ttk.Entry(regis,width=20, textvariable=n,font=("Times New Roman",10))
            nombre_sql.place(x=150,y=50)
            usuario_sql=ttk.Entry(regis,width=20, font=("Times New Roman",10))
            usuario_sql.place(x=150,y=100)
            contraseña_sql=tk.Entry(regis,width=20, font=("Times New Roman",10))
            contraseña_sql.place(x=150,y=150)
            telefono_sql=ttk.Entry(regis,width=25,font=("Times New Roman",10))
            telefono_sql.place(x=150,y=200)
            
            sqlregistro=tk.Button(regis, text="crar usuario",command=click)
            sqlregistro.place(x=150,y=225)
    
        def iniciarsecion():    #inicio de secion
            n1=usu.get()
            n2=contra.get()
            
            conn=sql.connect("usuariosnew.db")
            cursor= conn.cursor()
            cursor.execute('SELECT * FROM usuarios WHERE usuario = ? AND contraseña = ?', (n1, n2))
            
            if cursor.fetchall():
                messagebox.showinfo("Bienvenido",'HOLA '+n1)
                ventana.destroy()
                Punto_de_venta()
                
            else:
                messagebox.showerror("Error",'contraseña o usuario incorrectos')

        puntoventa.destroy()
        ventana=tk.Tk()
        ventana.geometry('500x200')
        ventana.resizable(0,0)


        #inicio de secion
        usuari=ttk.Label(text="Usuario",font=("Times Nwe Roman",10))
        contrasena=ttk.Label(text="contraseña",font=("Times Nwe Roman",10))
        usuari.place(x=150,y=5)
        contrasena.place(x=150,y=60)

        #entrada de informacion
        usuario1=tk.StringVar()
        contrasena2=tk.StringVar()

        #entrada de datos de secion
        usu=ttk.Entry(ventana, width=50, textvariable=usuario1,font=("Times New Roman",10))
        contra=ttk.Entry(ventana, width=50,show="*" ,textvariable=contrasena2,font=("Times New Roman",10))
        usu.place(x=150,y=25,width=150,height=20)
        contra.place(x=150,y=80,width=150,height=20)

        #botones
        iniciarsecion=ttk.Button(ventana, text='iniciar secion',command=iniciarsecion)
        iniciarsecion.place(x=150,y=110)
        crearsecion=ttk.Button(ventana, text='registrarse',command=register)
        crearsecion.place(x=250,y=110)
        invitado=ttk.Button(ventana, text="ENTRAR COMO INVITADO")
        invitado.place(x=150,y=150)
        ventana.mainloop()
    def Recarga_de_saldo():
        
        puntoventa.state("iconic")
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
                            ventanarecarga.destroy()
                        else:
                            messagebox.showerror("Error","Los Numeros no coinciden")
            
        #ventana de las recargas
        ventanarecarga=tk.Tk()
        ventanarecarga.geometry('800x600')
        ventanarecarga.title('Recargas')
        ventanarecarga.resizable(0,0)
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
        compañia=ttk.Combobox(ventanarecarga,state="readonly",
                values=("Telcel","AT&T","Movistar","Unefon"))
        compañia.place(x=200,y=25)

        cantidad=ttk.Combobox(ventanarecarga,state='readonly',
                            values=("$20","$30","$50","$100","$150","$200","$250","$300"))
        cantidad.place(x=300,y=380)
        #boton para guardar

        cobro=ttk.Button(ventanarecarga,width=50,command=clickr,text="cobrar")
        cobro.place(x=200, y=450)
               
        ventanarecarga.mainloop()        

    #ventana del punto de venta
    puntoventa=tk.Tk()
    puntoventa.geometry("1071x600")
    puntoventa.resizable(0,0)
    
    #fondo
    fondo=PhotoImage(file="oxxo.png")
    background=tk.Label(image=fondo)
    background.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        #menu
    BarraMenu=tk.Menu()
    puntoventa.config(menu=BarraMenu)
    inicio=tk.Menu(BarraMenu, tearoff=False)
    Contactos=tk.Menu(BarraMenu, tearoff=False)
    Recargas=tk.Menu(BarraMenu, tearoff=False)
    carrito=tk.Menu(BarraMenu, tearoff=False)

    #ubicacion de las pestanas
    BarraMenu.add_cascade(menu=carrito, label="Carrito")
    BarraMenu.add_cascade(menu=Recargas, label="Recargas")
    BarraMenu.add_cascade(menu=Contactos, label="Contactos")   
    BarraMenu.add_cascade(menu=inicio, label="perfil")
    
    #botones del menu de venta
    Contactos.add_command(label='Provedores')
    Contactos.add_command(label='Soporte Tecnico')
    Contactos.add_command(label='CEO')
    
    inicio.add_command(label='cerrar sesion', command=regreso)
    
    Recargas.add_command(label='Recarga de saldo', command=Recarga_de_saldo)
    
    
    
    #ciclo de ventana
    puntoventa.mainloop()    
        
ventana=tk.Tk()
ventana.geometry('500x200')
ventana.resizable(0,0)


#inicio de secion
usuari=ttk.Label(text="Usuario",font=("Times Nwe Roman",10))
contrasena=ttk.Label(text="contraseña",font=("Times Nwe Roman",10))
usuari.place(x=150,y=5)
contrasena.place(x=150,y=60)

#entrada de informacion
usuario1=tk.StringVar()
contrasena2=tk.StringVar()

#entrada de datos de secion
usu=ttk.Entry(ventana, width=50, textvariable=usuario1,font=("Times New Roman",10))
contra=ttk.Entry(ventana, width=50,show="*" ,textvariable=contrasena2,font=("Times New Roman",10))
usu.place(x=150,y=25,width=150,height=20)
contra.place(x=150,y=80,width=150,height=20)

#botones
iniciarsecion=ttk.Button(text='iniciar secion',command=iniciarsecion)
iniciarsecion.place(x=150,y=110)
crearsecion=ttk.Button(text='registrarse',command=register)
crearsecion.place(x=250,y=110)
invitado=ttk.Button(text="ENTRAR COMO ADMINISTRADOR")
invitado.place(x=150,y=150)
ventana.mainloop()