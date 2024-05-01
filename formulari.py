import tkinter as tk
from tkinter import messagebox

def registrar():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    edad = entry_edad.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    sexo = var_sexo.get()
    ciudad = listbox_ciudad.get(tk.ACTIVE)
    
    mensaje = f"Nombre: {nombre}\n"
    mensaje += f"Apellido: {apellido}\n"
    mensaje += f"Edad: {edad}\n"
    mensaje += f"Dirección: {direccion}\n"
    mensaje += f"Teléfono: {telefono}\n"
    mensaje += f"Sexo: {sexo}\n"
    mensaje += f"Ciudad: {ciudad}"
    
    messagebox.showinfo("Información de Registro", mensaje)


ventana = tk.Tk()
ventana.title("Formulario de Registro")


label_nombre = tk.Label(ventana, text="Nombre:")

label_nombre.grid(row=0, column=0, sticky="w")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1)

label_apellido = tk.Label(ventana, text="Apellido:")

label_apellido.grid(row=1, column=0, sticky="w")
entry_apellido = tk.Entry(ventana)
entry_apellido.grid(row=1, column=1)

label_edad = tk.Label(ventana, text="Edad:")

label_edad.grid(row=2, column=0, sticky="w")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=2, column=1)

label_direccion = tk.Label(ventana, text="Dirección:")

label_direccion.grid(row=3, column=0, sticky="w")
entry_direccion = tk.Entry(ventana)
entry_direccion.grid(row=3, column=1)

label_telefono = tk.Label(ventana, text="Teléfono:")

label_telefono.grid(row=4, column=0, sticky="w")
entry_telefono = tk.Entry(ventana)
entry_telefono.grid(row=4, column=1)

label_sexo = tk.Label(ventana, text="Sexo:")
label_sexo.grid(row=5, column=0, sticky="w")

var_sexo = tk.StringVar()

radio_masculino = tk.Radiobutton(ventana, text="Masculino", variable=var_sexo, value="Masculino")

radio_masculino.grid(row=5, column=1, sticky="w")
radio_femenino = tk.Radiobutton(ventana, text="Femenino", variable=var_sexo, value="Femenino")
radio_femenino.grid(row=5, column=1, sticky="e")

label_ciudad = tk.Label(ventana, text="Ciudad:")

label_ciudad.grid(row=6, column=0, sticky="w")

listbox_ciudad = tk.Listbox(ventana, selectmode=tk.SINGLE)
listbox_ciudad.grid(row=6, column=1)
ciudades = ["Ciudad A", "Ciudad B", "Ciudad C", "Ciudad D"]

for ciudad in ciudades:
    listbox_ciudad.insert(tk.END, ciudad)

button_registrar = tk.Button(ventana, text="Registrar", command=registrar)
button_registrar.grid(row=7, column=0, columnspan=2)

ventana.mainloop()