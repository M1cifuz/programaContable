#programa contable estandar casaroma
import sqlite3
#from productos import producto

#----------INICIO FUNCIONES----------
#----------Crear bases de datos----------
#----------Crear tabla----------
def crearTabla ():
    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_PRODUCTO VARCHAR(50), PRECIO INTEGER, PROVEEDOR VARCHAR(20))")
#----------Crear listas----------

def crearProducto():
    producto = input('Nombre del producto: ')
    precio = int(input('Precio del producto: '))
    proveedor = input('Proveedor del producto: ')
    
    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("INSERT INTO PRODUCTOS (NOMBRE_PRODUCTO, PRECIO, PROVEEDOR) VALUES (?,?,?)", (producto, precio, proveedor))                  
    miConexion.commit() # confirmar cambios
    miConexion.close()  # cerrar conexiòn

def leerLista():
    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero

    miCursor.execute("SELECT * FROM PRODUCTOS")
    todosLosProductos = miCursor.fetchall()
    
    for producto in todosLosProductos:
        print(producto)

    miConexion.close()  # cerrar conexiòn

def actualizarProducto():
    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero

    miCursor.execute("UPDATE PRODUCTOS SET PRECIO = 10000 WHERE NOMBRE_ARTICULO = 'oregano'")

    miConexion.close()  # cerrar conexiòn


def borrarProducto():
    #idNombre =

    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero

    miCursor.execute("DELETE FROM PRODUCTOS WHERE NOMBRE_PRODUCTO = 'oregano'")

    miConexion.close()  # cerrar conexiòn
#----------FIN FUNCIONES----------

#   1 Modulo CRUD: crear, leer, actualizar o eliminar productos
#----------INICIO MODULO CRUD----------
opcion = int(input("""Escoja entre las siguientes opciones: 
    0 Crear una tabla nueva                   
    1 Crear nuevo producto
    2 Consultar la lista de productos
    3 Actualizar uno o varios productos
    4 Borrar un producto
    """))
if opcion == 0:
    crearTabla()
elif opcion == 1:
    crearProducto()
elif opcion == 2:
    leerLista()
elif opcion == 3:
    actualizarProducto()
elif opcion == 4:
    borrarProducto()    
else:
    pass
#----------FIN MODULO CRUD----------
        
#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)


#   2 aplicacion de ganancias
#   3 modulo de compras
    #miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosProductos)
#   4 modulo de ventas