import tkinter as tk
def saludar():
    nombre = entrada_nombre.get()
    etiqueta_saludo.config(text=f"Hola, {nombre}!")

ventana= tk.Tk()
ventana.title("what's up")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=3)

entrada_nombre = tk.Entry(ventana, text="nombre")
entrada_nombre.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

boton_saludar = tk.Button(ventana, text="Saludar", command=saludar)
boton_saludar.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="ew") 

etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="ew")
ventana.mainloop()