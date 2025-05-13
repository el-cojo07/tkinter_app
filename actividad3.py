import tkinter as tk
from tkinter import messagebox
venta_principal = tk.Tk()
venta_principal.title("Sistema de Ventas")
venta_principal.geometry("900x600")
venta_principal.config(bg="lightblue")
etiqueta_titulo = tk.Label(venta_principal, text="No soy Cupido, pero tengo un piropo para ti 😘", font=("Arial", 24), bg="lightblue")
etiqueta_titulo.pack(pady=20)
etiqueta_titulo.pack()
def acion_boton():
    messagebox.showinfo("Hola", "Eres la razón por la que sonrío cada día 😊")
boton = tk.Button(venta_principal, text="toca aqui🥰", command=acion_boton, bg="lightpink", font=("Arial", 14))
boton.pack(pady=10)
venta_principal.mainloop()