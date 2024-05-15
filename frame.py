import tkinter as tk

# Se crea un nuevo objeto tkinter con el metodo Tk()
ventana = tk.Tk()

# Propiedades de las ventanas #
# Se añade un icono el cual esta en la ruta que recibe como parametro el metodo iconbitmap()
ventana.iconbitmap("Icono/icono.ico")

# Se agrega un titulo para la ventana
ventana.title("Ventana con frames")

# Con el metodo geometry se calcula el ancho y el largo + la posicion en la que se desea mostrar cuando este se ejecute
ventana.geometry("600x400+500+200")

# Las siguientes lineas permiten que el minimo y el maximo de la ventana sea el mismo que el inicial, ademas con el
# metodo resizable() con los dos parametros en False permite que la ventana no se pueda expandir mas del tamaño identificado
ventana.minsize(600, 400)
ventana.maxsize(600, 400)
ventana.resizable(False, False)

# ------------------------------- INSTANCIA DE OBJETOS PARA LA CLASE FRAME/BUTTON/LABELFRAME -----------------------------------------
# Se instancia un nuevo objeto pero esta vez de la clase Frame, los frame funcionan como contenedores dentro de la ventana
# para su mejor organizacion dentro de esta, los contenedores dentro pueden contener mas contenedores o diferentes tipos de
# acciones como entradas de texto, botones etc.
# A la hora de crear un objeto de la clase Frame se le asigna como parametro el contenedor que lo va a contener, en este
# caso el objeto frame1 estara dentro del objeto ventana que hace referencia a la ventana del ejecutable
frame1 = tk.Frame(ventana)

# Los objetos tipo Frame utilizan el metodo configure(), el cual funciona como las propiedades de dicho objeto, como parametro
# puede aceptar lo que es width(ancho), height(alto), bg(background/color), bd(bordes)
frame1.configure(width=200, height=200, bg="black", bd=20)

# El metodo pack() nos permite que se visualize el objeto Frame dentro de la ventana del ejecutable
frame1.pack()

# Se crea un nuevo objeto Frame que estara dentro del objeto nombrado frame1
frame2 = tk.Frame(frame1)

# Se crean sus propiedades
frame2.configure(width=150, height=150, bg="white", bd=0)

# Se instancia un objeto de la clase Button el cual recibe como parametro el Frame que lo contendra y el parametro con palabra 
# reservada text="" que indica el nombre que tendra el boton es decir que dira el boton que se mostrara en la ventana
boton = tk.Button(frame2, text="Boton")
boton.pack()

# Se visualiza en la ventana del ejecutable
frame2.pack()

# Se inicializa un objeto de la clase LabelFrame, un LabelFrame es un widget de diferente tipo que su funcionalidad es la misma
# que la del resto el cual es funcionar como un contenedor, a diferencia que este contiene con propiedades diferentes como lo son
# el crearle un titulo de encabezado a dicho contenedor con el parametro text="", ademas del color con bg="", el padding pady="" que
# funciona como el margen que tendra el contenedor por dentro, entre otros parametros
labelframe = tk.LabelFrame(ventana, text="Grupo de widgets", bg="yellow", pady=10)

# Se crea la configuracion con el mismo metodo con el que se crea la configuracion de los objetos tipo Frame, a excepcion que este
# solo recibira 2 parametros el cual es width(ancho) y el height(alto)
labelframe.configure(width=200, height=200)

# Se visualiza el objeto LabelFrame
labelframe.pack()

# Visualizacion del objeto ventana con el metodo mainloop()
ventana.mainloop()