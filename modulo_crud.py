from tkinter import *
from tkinter import messagebox
import sqlite3

#----------Funciones CRUD para listas----------

def crearProducto(conexion, producto, marca, presentacion, precio):
    conexion # crear una conexiòn
    miCursor = conexion.cursor()    # crear puntero
    miCursor.execute("INSERT INTO TABLA_PRODUCTOS VALUES(NULL,'"+ producto +"','"+ marca +"','"+ presentacion +"' ,'"+ precio +"')")
    conexion.commit() # confirmar cambios
    messagebox.showinfo("BBDD","Registro insertado con éxito")

