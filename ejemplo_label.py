# Importamos el módulo time para trabajar con el tiempo
import time
# Importamos Tkinter para crear la interfaz gráfica
import tkinter as tk

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Ejemplo Label") # Título de la ventana
ventana.configure(bg="black") # Color de fondo de la ventana
ventana.geometry("600x400+500+200") # Geometría de la ventana

# Creación del título del Label
etiqueta_titulo = tk.Label(ventana, text="Ejemplo Reloj")
etiqueta_titulo.config(fg="white", bg="black", font=("Arial", 17, "bold")) # Configuracion de la etiqueta_titulo
etiqueta_titulo.pack() # Visualizamos el Label en la ventana

# Creación del Label para mostrar la hora
hora = tk.Label(ventana, text="...")
hora.config(fg="white", bg="black", font=("Arial", 14, "bold"))

# Función para actualizar la hora
def actualizar_hora():
    hora.config(text=time.strftime("%H:%M:%S")) # Actualizamos el texto con la hora actual con el metodo strftime de la clase time
    ventana.after(1000, actualizar_hora) # Llamamos a esta función nuevamente después de 1000ms (1 segundo), cada 1 segundo la ventana
                                            # ejecutara el metodo actualizar hora, conviertiendo esa funcion en un bucle infinito ya que
                                                # la etiqueta hora se hira actualizando cada 1 segundo

# Llamamos a la función por primera vez para iniciar la actualización de la hora, se llama el metodo con el fin de que sea la linea la cual
# ejecute la funcion para ya poder generar el bucle infinito que se consigue con el metodo after
actualizar_hora()

hora.pack()  # Visualizamos el Label hora en la ventana
ventana.mainloop()  # Ejecutamos el bucle principal de la aplicación