from tkinter import *
from PIL import Image, ImageTk 
import tkinter as tk

#definiciones para que los widget sean ejecutable
def obtener_texto():
    texto_ingresado = cuadro_texto.get()
    etiqueta.config(text="Texto ingresado: " + texto_ingresado)
    
def obtener_seleccion():
    seleccionados = cuadro_lista.curselection()
    for index in seleccionados:
        elemento = cuadro_lista.get(index)
        print("Elemento seleccionado:", elemento)

def obtener_estado():
    if variable.get() == 1:
        print("La casilla de verificación está seleccionada")
    else:
        print("La casilla de verificación no está seleccionada")

def obtener_seleccion():
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
    elif seleccion == 2:
        print("Opción 2 seleccionada")
    elif seleccion == 3:
        print("Opción 3 seleccionada")

 #funcionalidad   
ventana = Tk()
variable = tk.IntVar()

#importacion
import tkinter as tk

#ajustes de la ventana de interfas
ventana.geometry(f"{600}x{400}")

#codigo a funcionar
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

cuadro_lista = tk.Listbox(ventana, width=30, selectmode="multiple")
cuadro_lista.pack()

elementos = ["agua", "fuego", "tierra", "aire"]

for elemento in elementos:
    cuadro_lista.insert(tk.END, elemento)

boton = tk.Button(ventana, text="Obtener", command=obtener_seleccion)
boton.pack()

casilla_verificacion = tk.Checkbutton(ventana, text="variable", variable=variable, command=obtener_estado)
casilla_verificacion.pack()

opcion1 = tk.Radiobutton(ventana, text="fuego", variable=variable, value=1, command=obtener_seleccion)
opcion1.pack()

opcion2 = tk.Radiobutton(ventana, text="tierra", variable=variable, value=2, command=obtener_seleccion)
opcion2.pack()

opcion3 = tk.Radiobutton(ventana, text="agua", variable=variable, value=3, command=obtener_seleccion)
opcion3.pack()

opcion4 = tk.Radiobutton(ventana, text="aire", variable=variable, value=3, command=obtener_seleccion)
opcion4.pack()



ventana.mainloop()