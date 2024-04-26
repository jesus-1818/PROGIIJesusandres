from tkinter import *
from PIL import Image, ImageTk 
import tkinter as tk

def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)
    
ventana = Tk()
import tkinter as tk

ventana.geometry(f"{600}x{400}")

etiqueta = tk.Label(ventana, text="¡HOLA QUE TAL MUNDO!", bg="black", fg="RED", font=("Colonna MT", 16), width=50, height=10, anchor="center")

etiqueta.pack()
boton1 = tk.Button(ventana, text="cambiar", bg="white", fg="black", font=("Arial", 14))
boton1.pack()

boton2 = tk.Button(ventana, text="siguiente", bg="white", fg="black", font=("Arial", 14))
boton2.pack()

etiqueta = tk.Label(ventana, text="Texto ingresado: ")
etiqueta.pack()

cuadro_texto = tk.Entry(ventana, width=30)
cuadro_texto.pack()

boton = tk.Button(ventana, text="Obtener Texto", command=obtener_texto)
boton.pack()

marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="solid")
marco1.pack()
etiqueta1 = tk.Label(marco1, text="CERRAR")
etiqueta1.pack()
marco1 = tk.Frame(ventana, width=200, height=100, bd=2, relief="raised")
marco1.pack()


ventana.mainloop()