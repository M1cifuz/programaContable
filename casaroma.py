# Gestor base de datos productos
from tkinter import *
from tkinter import messagebox
import sqlite3
from modulo_crud import *

#----------INICIO FUNCIONES----------

#----------Crear bases de datos----------

#----------Crear tabla----------

def conexionBBDDproductos ():
    miConexion = sqlite3.connect("tabla_productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    try:
        miCursor.execute("""
                        CREATE TABLE TABLA_PRODUCTOS (
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
    miConexion = sqlite3.connect("tabla_productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("INSERT INTO TABLA_PRODUCTOS VALUES(NULL,'"+ elProducto.get() +"','"+ laMarca.get() +"','"+ laPresentacion.get() +"' ,'"+ elPrecio.get() +"')")
    miConexion.commit() # confirmar cambios
    messagebox.showinfo("BBDD","Registro insertado con éxito")

def leerProducto():
    miConexion = sqlite3.connect("tabla_productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("SELECT * FROM TABLA_PRODUCTOS WHERE ID_PRODUCTO = " + elId.get())
    usuario = miCursor.fetchall() # fetchall debuelve un array con todos los registros que cumplan la consulta sql
    for i in usuario:
        elId.set(i[0])
        elProducto.set(i[1])
        laMarca.set(i[2])
        laPresentacion.set(i[3])
        elPrecio.set(i[4])
    miConexion.commit()

def actualizarProducto():
    miConexion = sqlite3.connect("tabla_productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("UPDATE TABLA_PRODUCTOS SET NOMBRE_PRODUCTO='"+ elProducto.get() +"',MARCA_PRODUCTO='"+ laMarca.get() +"',PRESENTACION='"+ laPresentacion.get() +"',PRECIO='"+ elPrecio.get() +"'WHERE ID_PRODUCTO="+ elId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro actualizado con éxito")

def borrarProducto():
    miConexion = sqlite3.connect("tabla_productos")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    miCursor.execute("DELETE FROM TABLA_PRODUCTOS WHERE ID_PRODUCTO=" + elId.get())
    miConexion.commit()
    messagebox.showinfo("BBDD","Registro borrado con éxito")

def borrarCampos():
    elId.set("")
    elProducto.set("")
    laMarca.set("")
    laPresentacion.set("")
    elPrecio.set("")

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

elId = StringVar()
elProducto = StringVar()
laMarca = StringVar()
laPresentacion = StringVar()
elPrecio = StringVar()

bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDDproductos)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos", command=borrarCampos)

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear", command=crearProducto)
crudMenu.add_command(label="Leer", command=leerProducto)
crudMenu.add_command(label="Actualizar", command=actualizarProducto)
crudMenu.add_command(label="Borrar", command=borrarProducto)

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

textoIDProducto = Entry(miFrame, textvariable=elId)
textoIDProducto.config(justify="center", font=12)
textoIDProducto.grid(row=0, column=1)

labelProducto = Label(miFrame, text="Producto:", font=(12))
labelProducto.grid(row=1, column=0, sticky="e", pady=5, padx=3)
labelProducto.config(bg="#E48F45")

textoProducto = Entry(miFrame, textvariable=elProducto)
textoProducto.grid(row=1, column=1)

labelMarca = Label(miFrame, text="Marca:", font=(12))
labelMarca.grid(row=1, column=2, sticky="e", pady=5, padx=3)
labelMarca.config(bg="#E48F45")

textoMarca = Entry(miFrame, textvariable=laMarca)
textoMarca.grid(row=1, column=3)

labelPresentacion = Label(miFrame, text="Presentaciòn:", font=(12))
labelPresentacion.grid(row=2, column=0, sticky="e", pady=5, padx=3)
labelPresentacion.config(bg="#E48F45")

textoPresentacion = Entry(miFrame, textvariable=laPresentacion)
textoPresentacion.grid(row=2, column=1)

labelPrecio = Label(miFrame, text="Precio:", font=(12))
labelPrecio.grid(row=2, column=2, sticky="e", pady=5, padx=3)
labelPrecio.config(bg="#E48F45")

textoPrecio = Entry(miFrame, textvariable=elPrecio)
textoPrecio.grid(row=2, column=3)

#-----Botones-----

botonCrear = Button(miFrameBotones, text="Crear", font=10)
botonCrear.grid(row=0, column=0, sticky="w", pady=5, padx=3)
botonCrear.config(bg="#994D1C", command=crearProducto)

botonLeer = Button(miFrameBotones, text="Leer", font=10)
botonLeer.grid(row=0, column=1, sticky="w", pady=5, padx=3)
botonLeer.config(bg="#994D1C", command=leerProducto)

botonActualizar = Button(miFrameBotones, text="Actualizar", font=10)
botonActualizar.grid(row=0, column=2, sticky="w", pady=5, padx=3)
botonActualizar.config(bg="#994D1C", command=actualizarProducto)

botonBorrar = Button(miFrameBotones, text="Borrar", font=10)
botonBorrar.grid(row=0, column=3, sticky="w", pady=5, padx=3)
botonBorrar.config(bg="#994D1C", command=borrarProducto)
#----- fin labels-----

root.mainloop()
#----------fin Modulo interfaz grafica----------