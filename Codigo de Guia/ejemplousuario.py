import sqlite3 as sql
import math

conn=sql.connect("usuariosnew.db")
cursor= conn.cursor()
cursor.execute('select contraseña from usuarios')
fila=cursor.fetchone()
if fila!=None:
    print(fila)
    
    

conn.close()