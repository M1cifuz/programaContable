# Gestor base de datos productos
from tkinter import *
from tkinter import messagebox
import sqlite3
#----------inicio Modulo interfaz grafica----------
root = Tk()
root.title("Gestor Base de datos productos") # titulo de la ventana 
root.resizable(False,False) # Controla el poder redimensionar la ventana
root.geometry("420x200") # Establece el tamaño de la ventana principal
root.config(bg="#E48F45")
#----- inicio primer frame-----
miFrame=Frame(root, width=350, height=350)
miFrame.config(bg="#E48F45")
miFrame.pack()
#-----fin primer frame-----

#----- inicio labels-----
labelIDProducto = Label(miFrame, text="ID producto:", font=(12))
labelIDProducto.grid(row=0, column=0, sticky="e", pady=5, padx=3)
labelIDProducto.config(bg="#E48F45")

textoIDProducto = Entry(miFrame)
textoIDProducto.grid(row=0, column=1)

labelProducto = Label(miFrame, text="Producto:", font=(12))
labelProducto.grid(row=1, column=0, sticky="e", pady=5, padx=3)
labelProducto.config(bg="#E48F45")

textoProducto = Entry(miFrame)
textoProducto.grid(row=1, column=1)

labelMarca = Label(miFrame, text="Marca:", font=(12))
labelMarca.grid(row=1, column=2, sticky="e", pady=5, padx=3)
labelMarca.config(bg="#E48F45")

textoMarca = Entry(miFrame)
textoMarca.grid(row=1, column=3)

labelPresentacion = Label(miFrame, text="Presentaciòn:", font=(12))
labelPresentacion.grid(row=2, column=0, sticky="e", pady=5, padx=3)
labelPresentacion.config(bg="#E48F45")

textoPresentacion = Entry(miFrame)
textoPresentacion.grid(row=2, column=1)

labelPrecio = Label(miFrame, text="Precio:", font=(12))
labelPrecio.grid(row=2, column=2, sticky="e", pady=5, padx=3)
labelPrecio.config(bg="#E48F45")

textoFecha = Entry(miFrame)
textoFecha.grid(row=2, column=3)

#-----Botones-----
#----------Crear tabla----------
def crearTabla ():
    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_PRODUCTO VARCHAR(40), MARCA_PRODUCTO VARCHAR(40), PRESENTACION INTEGER, PRECIO INTEGER)")

botonCrear = Button(miFrame, text="Crear", font=10, command=crearTabla)
botonCrear.grid(row=3, column=0, sticky="w")
botonCrear.config(bg="#994D1C")

botonLeer = Button(miFrame, text="Leer", font=10)
botonLeer.grid(row=4, column=0, sticky="w")
botonLeer.config(bg="#994D1C")

botonActualizar = Button(miFrame, text="Actualizar", font=10)
botonActualizar.grid(row=3, column=1, sticky="w")
botonActualizar.config(bg="#994D1C")

botonBorrar = Button(miFrame, text="Borrar", font=10)
botonBorrar.grid(row=4, column=1, sticky="w")
botonBorrar.config(bg="#994D1C")
#----- fin labels-----

root.mainloop()
#----------fin Modulo interfaz grafica----------



#----------INICIO FUNCIONES----------
#----------Crear bases de datos----------

#----------Funciones CRUD para listas----------

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