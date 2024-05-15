import tkinter as tk

ventana = tk.Tk()
ventana.geometry("600x400+500+200")
ventana.minsize(600,400)
ventana.maxsize(600,400)
ventana.resizable(False, False)

ventana.iconbitmap("Icono/icono.ico")
ventana.title("Ejercicio para capturar un texto")

titulo = tk.Label(ventana, text="Ejercicio personal")
titulo.config(fg="black", bg="white", font=("Arial", 14, "bold"))
titulo.pack()

entrada = tk.Entry(ventana)
entrada.config(fg="black", bg="white", font=("Arial", 12))
entrada.pack()

boton = tk.Button(ventana, text="Boton")
texto_guardado = tk.StringVar()

def capturar_texto():
    texto_guardado.set(entrada.get())

boton.config(command=capturar_texto)    
boton.pack()

ventana.mainloop()

print(f"Este es el texto capturado: {texto_guardado.get()}")
