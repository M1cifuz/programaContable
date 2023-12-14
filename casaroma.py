# Gestor base de datos productos
from tkinter import *
from tkinter import messagebox
import sqlite3

#----------INICIO FUNCIONES----------

#----------Crear bases de datos----------

#----------Crear tabla----------

def conexionBBDDproductos ():
    miConexion = sqlite3.connect("productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    try:
        miCursor.execute("""
                        CREATE TABLE PRODUCTOS (
                        ID_PRODUCTO INTEGER PRIMARY KEY AUTOINCREMENT,
                        NOMBRE_PRODUCTO VARCHAR(40), 
                        MARCA_PRODUCTO VARCHAR(40), 
                        PRESENTACION INTEGER, 
                        PRECIO INTEGER)
                        """)
        messagebox.showinfo("BBDD", "BBDD creada con èxito")
    except:
        messagebox.showwarning("¡ATENCIÒN!", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()
    
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


#----------inicio Modulo interfaz grafica----------

root = Tk()
root.title("Gestor Base de datos productos") # titulo de la ventana 
root.resizable(False,False) # Controla el poder redimensionar la ventana
root.geometry("500x180") # Establece el tamaño de la ventana principal
root.config(bg="#E48F45")

#----- inicio barra menu-----
barraMenu=Menu(root)
root.config(menu=barraMenu)

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDDproductos)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia")
ayudaMenu.add_command(label="Acerca de...")

barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#----- inicio frame para labels-----

miFrame=Frame(root, width=350, height=350)
miFrame.config(bg="#E48F45")
miFrame.pack()

#----- fin frame para labels-----
#----- inicio frame para botones-----

miFrameBotones=Frame(root, width=350, height=350)
miFrameBotones.config(bg="#E48F45")
miFrameBotones.pack()

#----- fin frame para botones-----

#----- inicio labels-----

labelIDProducto = Label(miFrame, text="ID producto:", font=(12))
labelIDProducto.grid(row=0, column=0, sticky="e", pady=5, padx=3)
labelIDProducto.config(bg="#E48F45")

textoIDProducto = Entry(miFrame)
textoIDProducto.config(justify="center", font=12)
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

textoPrecio = Entry(miFrame)
textoPrecio.grid(row=2, column=3)

#-----Botones-----

botonCrear = Button(miFrameBotones, text="Crear", font=10)
botonCrear.grid(row=0, column=0, sticky="w", pady=5, padx=3)
botonCrear.config(bg="#994D1C")

botonLeer = Button(miFrameBotones, text="Leer", font=10)
botonLeer.grid(row=0, column=1, sticky="w", pady=5, padx=3)
botonLeer.config(bg="#994D1C")

botonActualizar = Button(miFrameBotones, text="Actualizar", font=10)
botonActualizar.grid(row=0, column=2, sticky="w", pady=5, padx=3)
botonActualizar.config(bg="#994D1C")

botonBorrar = Button(miFrameBotones, text="Borrar", font=10)
botonBorrar.grid(row=0, column=3, sticky="w", pady=5, padx=3)
botonBorrar.config(bg="#994D1C")
#----- fin labels-----

root.mainloop()
#----------fin Modulo interfaz grafica----------