import tkinter as tk

# ----------------------------------------------------------------------------
ventana = tk.Tk()
ventana.geometry("600x400+500+200")
ventana.minsize(600,400)
ventana.maxsize(600,400)
ventana.resizable(False, False)

ventana.iconbitmap("Icono/icono.ico")
ventana.title("Ejemplo entry")
ventana.configure(bg="black")
ventana.attributes("-alpha", 0.9)

contenedor_titulo = tk.Frame(ventana)
contenedor_titulo.configure(width=600, height=50, bg="black", bd=0)
contenedor_titulo.pack()

titulo = tk.Label(contenedor_titulo, text="Lo de abajo es un entry")
titulo.config(fg="white", bg="black", font=("Arial", 15, "bold"))
titulo.pack()
# ----------------------------------------------------------------------------

# ----------------------------------------------------------------------------
# ENTRY: La clase Entry nos permite crear objetos que actuen como campos de entrada de informacion como si fueran un input
entrada = tk.Entry(ventana) # Se instancia un objeto de la clase Entry posicionado en la ventana
entrada.config(fg="blue", bg="white", font=("Arial", 10)) # Se crea la configuracion del objeto
entrada.pack() # Se muestra en ventana

# Cuando se desea que el input (objeto tipo Entry) cuente con un texto por defecto se implementa el metodo insert
entrada.insert(0, "Nombre") # Se inserta un texto por defecto al objeto Entry con el metodo insert() pasandole como parametro la posicion
                                # en la que se desee que se encuentre el texto que en este caso es "0" que indica que el texto estara en
                                    # el principio y como segundo parametro el texto por defecto que se desea mostrar

# Se guarda en una variable lo que se escriba en el objeto
texto = entrada.get() # Con el metodo get() se extrae lo que haya en el cuadro de texto
print(texto) # Se imprime por consola lo que capturo la variable texto

boton = tk.Button(ventana, text="Aplicar cambio")
def capturar_texto():
    texto_cambiado = entrada.get()
    titulo.config(text=texto_cambiado)

boton.config(command=capturar_texto)
boton.pack()
# ----------------------------------------------------------------------------

ventana.mainloop()

