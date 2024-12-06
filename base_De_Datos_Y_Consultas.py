import sqlite3
#Creacion debase de datos
try:
    conexion = sqlite3.connect('Prueva.db')
    cursor = conexion.cursor()

    # Crear tabla departamento
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS departamento (
            id_departamento INTEGER PRIMARY KEY,
            nombre_departamento TEXT NOT NULL       
        )
    ''')

    # Crear tabla empleado
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS empleado (
            id_Empleado INTEGER PRIMARY KEY,
            nombre_Empleado TEXT NOT NULL,
            apellido_Empleado TEXT NOT NULL,
            Telefono INTEGER NOT NULL,
            contraseña TEXT NOT NULL,
            id_departamento INTEGER,
            FOREIGN KEY (id_departamento) REFERENCES departamento (id_departamento)       
        )
    ''')

    # Crear tabla proveedor
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS proveedor (
            id_proveedor INTEGER PRIMARY KEY,
            nombre_proveedor TEXT NOT NULL,
            Telefono_proveedor INTEGER NOT NULL,
            correo TEXT NOT NULL        
        )
    ''')

    # Crear tabla cliente
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cliente (
            id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre_cliente TEXT NOT NULL,
            telefono INTEGER NOT NULL        
        )
    ''')

    # Crear tabla producto
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS producto (
            id_producto INTEGER PRIMARY KEY,
            nombre_producto TEXT NOT NULL,
            precio DOUBLE NOT NULL,
            genero TEXT,
            Calificacion INTEGER NOT NULL,
            plataforma TEXT NOT NULL,
            cantidad INTEGER NOT NULL       
        )
    ''')

    # Crear tabla transacciones
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS transacciones (
            id_transaccion INTEGER PRIMARY KEY,
            id_empleado INTEGER,
            id_cliente INTEGER,
            id_producto INTEGER,
            monto DOUBLE NOT NULL,
            direccion TEXT,
            fecha_inicio DATETIME, 
            fecha_final DATETIME, 
            tarifa_envio DOUBLE, 
            fecha_compra DATETIME, 
            tipo_transaccion TEXT NOT NULL,
            FOREIGN KEY (id_empleado) REFERENCES empleado (id_Empleado),
            FOREIGN KEY (id_cliente) REFERENCES cliente (id_cliente),
            FOREIGN KEY (id_producto) REFERENCES producto (id_producto)
        )
    ''')

    # Confirmar los cambios
    conexion.commit()
except Exception as e:
    print(f"Error al conectarse a la base de datos: {e}")
finally:
    # Cerrar la conexión
    conexion.close()

#Base para la gestion 
class BaseDatos:
    def __init__(self, db_name):
        self.db_name = db_name

    def conectar(self):
        return sqlite3.connect(self.db_name)

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
#Productos 
class Producto(BaseDatos):
    def __init__(self, db_name):
        super().__init__(db_name)

    def crear_producto(self, nombre, precio, genero, calificacion, plataforma, cantidad):
        self.ejecutar('''
            INSERT INTO producto (nombre_producto, precio, genero, Calificacion, plataforma, cantidad)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (nombre, precio, genero, calificacion, plataforma, cantidad))


#cliente

class Cliente(BaseDatos):
    def __init__(self, db_name):
        super().__init__(db_name)

    def crear_cliente(self, nombre_cliente, telefono):
        self.ejecutar('''
            INSERT INTO cliente (nombre_cliente, telefono)
            VALUES (?, ?)
        ''', (nombre_cliente, telefono))


#transaccion
class Transaccion(BaseDatos):
    def __init__(self, db_name):
        super().__init__(db_name)

    def crear_transaccion(self, id_empleado, id_cliente, id_producto, monto, direccion, fecha_inicio, fecha_final, tarifa_envio, fecha_compra, tipo_transaccion):
        self.ejecutar('''
            INSERT INTO transacciones (id_empleado, id_cliente, id_producto, monto, direccion, fecha_inicio, fecha_final, tarifa_envio, fecha_compra, tipo_transaccion)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (id_empleado, id_cliente, id_producto, monto, direccion, fecha_inicio, fecha_final, tarifa_envio, fecha_compra, tipo_transaccion))
