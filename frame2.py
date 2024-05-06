import tkinter as tk


def informacion():
    
    print("Usuario:", usuario_entry.get())
    
    print("Contraseña:", clave_entry.get())


ventana = tk.Tk()
ventana.title("iniciando sesión")
ventana.resizable(True, True) 
ventana.config(bg="gray")


frame_i = tk.Frame(ventana)
frame_i.pack(side="left", padx=10, pady=10)


foto = tk.PhotoImage(file="E:\Pictures\polar GOD")
foto_label = tk.Label(frame_i, image=foto)
foto_label.pack()


frame_d = tk.Frame(ventana)
frame_d.pack(side="right", padx=10, pady=10)


titulo_label = tk.Label(frame_d, text="Inicio de sesión", font=("Helvetica", 16))
titulo_label.grid(row=0, column=0, columnspan=2, pady=10)


usuario_label = tk.Label(frame_d, text="Usuario:")
usuario_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

usuario_entry = tk.Entry(frame_d)
usuario_entry.grid(row=1, column=1, padx=5, pady=5)


clave_label = tk.Label(frame_d, text="Contraseña:")
clave_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

clave_entry = tk.Entry(frame_d, show="*")
clave_entry.grid(row=2, column=1, padx=5, pady=5)


ingresar_button = tk.Button(frame_d, text="Ingresar", command=ingresar)
ingresar_button.grid(row=3, column=0, columnspan=2, pady=10)


ventana.mainloop()
