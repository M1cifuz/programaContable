# Gestor tabla clientes
from tkinter import *
from tkinter import messagebox
import sqlite3

#----------Crear tabla----------

def conexionBBDDproductos ():
    miConexion = sqlite3.connect("tabla_clientes")   # crear una conexiòn
    miCursor = miConexion.cursor()    # crear puntero
    try:
        miCursor.execute("""
                        CREATE TABLE TABLA_CLIENTES (
                        COD_CLIENTE INTEGER PRIMARY KEY AUTOINCREMENT,
                        RAZON_SOCIAL VARCHAR(40), 
                        NOMBRE_CONTACTO VARCHAR(40), 
                        TELEFONO1 INTEGER, 
                        TELEFONO2 INTEGER,
                        DIRECCION VARCHAR(40),
                        COMENTARIOS VARCHAR(100))
                        """)
        messagebox.showinfo("BBDD", "BBDD creada con èxito")
    except:
        messagebox.showwarning("¡ATENCIÒN!", "La BBDD ya existe")

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor=="yes":
        root.destroy()

#----------inicio Modulo interfaz grafica----------

root = Tk()
root.title("Gestor tabla clientes") # titulo de la ventana 
root.resizable(False,False) # Controla el poder redimensionar la ventana
root.geometry("430x350") # Establece el tamaño de la ventana principal
root.config(bg="#E48F45")

#----- inicio barra menu-----
barraMenu=Menu(root)
root.config(menu=barraMenu)

elCodigo = StringVar()
laRazonSocial = StringVar()
elNombreContacto = StringVar()
elTelefono1 = StringVar()
elTelefono2 = StringVar()
laDireccion = StringVar()
#elPrecio = StringVar()

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

#----- inicio frame para botones-----

miFrameBotones=Frame(root, width=350, height=350)
miFrameBotones.config(bg="#E48F45")
miFrameBotones.pack()

#----- fin frame para botones-----

#----- inicio labels y entrys-----

labelCodigoCliente = Label(miFrame, text="COD cliente:", font=(12))
labelCodigoCliente.grid(row=0, column=0, sticky="e", pady=5, padx=3)
labelCodigoCliente.config(bg="#E48F45")

textoCodigoCliente = Entry(miFrame, textvariable=elCodigo)
textoCodigoCliente.config(justify="center", font=12)
textoCodigoCliente.grid(row=0, column=1)

labelRazonSocial = Label(miFrame, text="Razón social:", font=(12))
labelRazonSocial.grid(row=1, column=0, sticky="e", pady=5, padx=3)
labelRazonSocial.config(bg="#E48F45")

textoProducto = Entry(miFrame, textvariable=laRazonSocial)
textoProducto.grid(row=1, column=1)

labelNombreContacto = Label(miFrame, text="Nombre contacto:", font=(12))
labelNombreContacto.grid(row=2, column=0, sticky="e", pady=5, padx=3)
labelNombreContacto.config(bg="#E48F45")

textoNombreContacto = Entry(miFrame, textvariable=elNombreContacto)
textoNombreContacto.grid(row=2, column=1)

labelTelefono1 = Label(miFrame, text="Telefono 1:", font=(12))
labelTelefono1.grid(row=3, column=0, sticky="e", pady=5, padx=3)
labelTelefono1.config(bg="#E48F45")

textoTelefono1 = Entry(miFrame, textvariable=elTelefono1)
textoTelefono1.grid(row=3, column=1)

labelTelefono2 = Label(miFrame, text="Telefono 2:", font=(12))
labelTelefono2.grid(row=4, column=0, sticky="e", pady=5, padx=3)
labelTelefono2.config(bg="#E48F45")

textoTelefono2 = Entry(miFrame, textvariable=elTelefono2)
textoTelefono2.grid(row=4, column=1)

labelDireccion = Label(miFrame, text="Dirección:", font=(12))
labelDireccion.grid(row=5, column=0, sticky="e", pady=5, padx=3)
labelDireccion.config(bg="#E48F45")

textoDireccion = Entry(miFrame, textvariable=laDireccion)
textoDireccion.grid(row=5, column=1)

labelComentarios = Label(miFrame, text="Comentarios", font=(12))
labelComentarios.grid(row=6, column=0, sticky="ne", pady=5, padx=3)
labelComentarios.config(bg="#E48F45")

textoComentarios = Text(miFrame, width=16, height=5)
textoComentarios.grid(row=6, column=1, padx=10, pady=10)
scrollVert = Scrollbar(miFrame, command=textoComentarios.yview)
scrollVert.grid(row=6, column=2, sticky="nsew")

textoComentarios.config(yscrollcommand=scrollVert.set)

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