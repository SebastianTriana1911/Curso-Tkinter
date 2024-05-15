import tkinter as tk

ventana = tk.Tk()
ventana.iconbitmap("Icono/icono.ico")
ventana.title("Ejemplo Label")
ventana.geometry("600x400+500+200")
ventana.minsize(600,400)
ventana.maxsize(600,400)
ventana.resizable(False, False)

# Se instancia un objeto de la clase Label, un Label es una etiqueta la cual a diferencia de los Frames o los LabelFrame no es un
# contenedor si no como se decia es una etiqueta, los parabletros a la hora de instanciar es el contenedor en el que va a estar dicho
# objeto y lo que va a decir con la palabra reservada text
etiqueta = tk.Label(ventana, text="Hola, soy un Label")

# La configuracion de este tipo de objetos se realiza con el metodo config, el cual acepta como parametros el color de la letra fg="",
# el color del fondo bg="", y su tipografia font=(detro de los parentecis se puede ingresar el tipo de letra, el tamaño y su tipo)
etiqueta.config(fg="white", bg="black", font=("Arial", 15, "bold"))

# Visualizacion del objeto Label
etiqueta.pack()


ventana.mainloop()