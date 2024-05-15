# Se importa la libreria Tkinter para manejo de ejecutables
import tkinter as tk

# ----------------------------------------------------------------------------------------------
# Configuracion de la ventana
ventana = tk.Tk() # Se crea una instancia de la clase Tk() convirtiendo ventana en el ejecutable
ventana.geometry("600x400+500+200") # Se inicializan la posicion y el tamaño de la ventana
ventana.minsize(600,400) # Se maneja un minimo de px para la ventana
ventana.maxsize(600,400) # Se maneja un maximo de px para la ventana
ventana.resizable(False, False) # Con el metodo resizable() se indica que la ventana no se podra modificar ni por ancho ni por largo

# Configuracion del encabezado del ejecutable
ventana.iconbitmap("Icono/icono.ico") # Se inserta una imagen con extencion .ico como icono del ejecutable
ventana.title("Ejemplo Boton") # Titulo de la ventana

# Configuracion de la ventana "Apariencia"
ventana.configure(bg="black") # Se da un background a la ventana de color negro
ventana.attributes("-alpha", 0.8) # Con el metodo attributes y los parametros "-alpha", 1 se da una graduacion de opacidad a la ventana
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# Instancia de un objeto Frame que funciona como el contenedor del titulo("Label") principal
espacio = tk.Frame(ventana) # Se instancia un objeto de la clase Frame posicionado en la ventana
espacio.configure(width="600", height="50", bg="black", bd=0) # Se crea su configuracion: ancho, largo, background, borde
espacio.pack() # Se muestra en la ventana
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# Instancia de un objeto Label que funcione como titulo principal
titulo = tk.Label(espacio, text="Ejemplo Buttons") # Se instancia un objeto de la clase Label posicionado en el objeto Frame
titulo.config(fg="white", bg="black", font=("Arial", 17, "bold")) # Se crea la configuracion: color de letra, background, fuente
titulo.pack() # Se muestra en ventana
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# Instancia de un objeto Button
boton = tk.Button(ventana, text="Presiona aqui") # Se instancia un objeto de la clase Button posicionado en ventana, con el parametro text
                                                    # el cual indica el nombre que tendra el boton
boton.config(fg="black", bg="white", font=("Arial", 10, "bold")) # Se crea la configuracion del boton
# ----------------------------------------------------------------------------------------------

# ----------------------------------------------------------------------------------------------
# Accionar la instancia del boton, cambiando el texto al precionar
# Este código crea un botón que cambia una palabra mostrada en un Label cuando se presiona.
# Primero, se crea un nuevo objeto Label que contiene la palabra inicial.
# Luego, se define una función llamada cambiar_texto() que cambia la palabra del Label utilizando el método config.
# A continuación, se configura el botón para que, al ser presionado, ejecute la función cambiar_texto().
# Esto asegura que cada vez que se presione el botón, se llame a la función para actualizar la palabra mostrada en el Label.

# Se crea un nuevo objeto Label que contendrá el texto a cambiar
texto = tk.Label(ventana, text="Texto inicial")
texto.config(fg="white", bg="black", font=("Arial", 13))

# Se define una función llamada cambiar_texto() que cambia el texto del Label al ser llamada
def cambiar_texto():
    texto.config(text="Texto cambiado por el botón")

# Se configura el botón para que al ser presionado ejecute la función cambiar_texto()
boton.config(command=cambiar_texto)

# Se empaqueta el botón y el Label en la ventana
boton.pack()
texto.pack()
# ----------------------------------------------------------------------------------------------


ventana.mainloop()