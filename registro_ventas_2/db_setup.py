import sqlite3

# Configuración inicial de la base de datos
def setup_database():
    # Usamos un contexto 'with' para manejar la conexión y asegurar su cierre
    with sqlite3.connect('ventas.db') as conn:
        try:
            c = conn.cursor()
            
            # Crear tabla clientes (cedula como TEXT)
            c.execute(''' 
                CREATE TABLE IF NOT EXISTS clientes (
                    cedula TEXT PRIMARY KEY,  -- Cambiado a TEXT para permitir ceros iniciales
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    email TEXT NOT NULL,
                    telefono TEXT NOT NULL,  -- También podría ser TEXT si deseas mantener ceros iniciales
                    direccion TEXT NOT NULL
                )
            ''')

            # Crear tabla productos
            c.execute('''
                CREATE TABLE IF NOT EXISTS productos (
                    codigo INTEGER PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    precio REAL NOT NULL,
                    stock INTEGER NOT NULL,
                    talla TEXT NOT NULL,
                    color TEXT NOT NULL,
                    modelo TEXT NOT NULL,
                    tipo_tela TEXT NOT NULL
                )
            ''')

            # Crear tabla ventas
            c.execute(''' 
                CREATE TABLE IF NOT EXISTS venta (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cedula_cliente TEXT,  -- Cambiado a TEXT para permitir ceros iniciales
                    fecha TEXT NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY (cedula_cliente) REFERENCES clientes (cedula)
                )
            ''')

            # Crear tabla facturas
            c.execute(''' 
                CREATE TABLE IF NOT EXISTS factura (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    id_venta INTEGER,
                    codigo_producto INTEGER,
                    cantidad INTEGER NOT NULL,
                    precio_unitario REAL NOT NULL,
                    total REAL NOT NULL,
                    FOREIGN KEY (id_venta) REFERENCES venta (id),
                    FOREIGN KEY (codigo_producto) REFERENCES productos (codigo)
                )
            ''')

            conn.commit()
            print("Base de datos configurada exitosamente.")
        except sqlite3.Error as e:
            print(f"Error en la configuración de la base de datos: {e}")

# Función para agregar un cliente a la base de datos
def add_cliente(cedula, nombre, apellido, email, telefono, direccion):
    try:
        with sqlite3.connect('ventas.db', timeout=10) as conn:
            c = conn.cursor()
            c.execute(''' 
                INSERT INTO clientes (cedula, nombre, apellido, email, telefono, direccion)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (cedula, nombre, apellido, email, telefono, direccion))
            conn.commit()
            print("Cliente agregado con éxito.")
    except sqlite3.OperationalError as e:
        print(f"Error al agregar el cliente: {e}")

# Función para agregar un producto a la base de datos
def add_producto(codigo, nombre, precio, stock, talla, color, modelo, tipo_tela):
    try:
        with sqlite3.connect('ventas.db', timeout=10) as conn:
            c = conn.cursor()
            c.execute(''' 
                INSERT INTO productos (codigo, nombre, precio, stock, talla, color, modelo, tipo_tela)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (codigo, nombre, precio, stock, talla, color, modelo, tipo_tela))
            conn.commit()
            print("Producto agregado con éxito.")
    except sqlite3.OperationalError as e:
        print(f"Error al agregar el producto: {e}")

# Ejecutar la configuración de la base de datos
setup_database()

# Ejemplos de uso
add_cliente("0123456789", "Juan", "Pérez", "juan.perez@example.com", "0123456789", "Calle Falsa 123")
add_producto(1001, "Camiseta", 19.99, 10, "M", "Rojo", "Modelo1", "Algodón")
