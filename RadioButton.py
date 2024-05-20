import tkinter as tk

# -------------------------------------------------------------
ventana = tk.Tk()
ventana.iconbitmap("Icono/icono.ico")
ventana.title("Radio Button")

ventana.geometry("600x400+500+200")
ventana.minsize(600,400)
ventana.maxsize(600,400)
ventana.resizable(False,False)
ventana.config(bg="black")
ventana.attributes("-alpha",0.9)
# -------------------------------------------------------------

# -------------------------------------------------------------
titulo = tk.Label(ventana, text="Ejemplo RadioButton")
titulo.configure(fg="white", bg="black", font=("Arial", 13, "bold"))
titulo.pack()
# -------------------------------------------------------------


entrada = tk.Entry(ventana)
entrada.insert(0, "Ingrese el nuevo titulo")



entrada.pack()



boton = tk.Button(ventana, text="Boton")

def cambiarTexto():
    entrada_recibida = entrada.get()
    titulo.config(text=entrada_recibida)
    print(entrada_recibida)


boton.config(command=cambiarTexto)
boton.pack()

ventana.mainloop()