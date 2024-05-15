""" 
TKINTER

- Tkinter es una libreria grafica de Python que nos permite crear interfaces de usuario de forma 
rapida y sencilla

- Es una herramienta perfecta para principiantes que deseen agregar elementos visuales a sus proyectos
en Python

- Cuando accedemos al contructor de la clase Tkinter y activamos la ventana, todos los metodos que vayamos
a utilizar se deben de ingresar dentro de la linea de codigo donde se llama al contructor y el metodo donde
se avilita la pestaña
"""

# Importamos la libreria tkinter, cuando es en un archivo Python solo con importarlo vasta, pero si
# se habla de un proyecto en el cual se utilizan entornos de desarrollo es importante instalar el paquete
import tkinter as tk

# A una variable se le asigna el constructor de la clase tkinter el cual es Tk(), esto con el fin de poder
# dar visualizacion a la ventana y a los elementos de la ventana que tendra el ejecutable, si este contructor
# no se inicializa en una variable desde el principio el ejecutable no mostrara nada.
# El resto de metodos se asignan a la misma variable ya que es la que activo el contructor
ventana = tk.Tk()
 
# El metodo tittle nos permite agregarle un titulo principal a la ventana del ejecutable 
ventana.title("Mi primer ejecutable")

# El metodo geometry nos permite asignarle a la ventana un rango especifico
ventana.geometry("600x400+500+200")

"""
Exiten dos metodos que son aliados del metodo geometry que es el minsize y el maxsize, que lo que hacen
es indicarle un tamaño maximo y un tamaño minimo para el cual se pueda reducio o se pueda extender la ventana
"""
ventana.minsize(600, 400)
ventana.maxsize(600, 400)

# El metodo iconbitmap nos permite cambiar el icono por defecto de la plumita que ya cuenta Tkinter por el
# icono que deseemos siempre y cuando tenga extencion .ico y accedamos a la ruta de una manera correcta
ventana.iconbitmap("Icono/icono.ico")

# El metodo resizable nos recibe dos parametros el primero tomando el tamaño de la ventana de manera vertical
# y el segundo parametro tomando el tamaño de la ventana de manera horizontal, cuando alguno de estos dos parametros
# se encuentra en True es por que la ventana se le puede modificar el tamaño segun la posicion del parametro en la
# que se encuentre, y si esta en False no se podra modificar el tamaño
ventana.resizable(False, False)

# Un metodo que nos permite cambiarle el color de fondo a la ventana es el metodo configure() con parametro bg "background"
# seguido del nombre del color que se desea colocar, hay una pagina el cual muestra el nombre de todos los colores que se pueden colocar
# https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html 
ventana.configure(bg="snow")

# El metodo attributes nos permite graduar la opasidad de la ventana, este metodo acepta dos parametro el primero que es "-alpha" y el
# segundo que actuara como la graduacion de transparecia que deseemos que tenga la ventana siendo 1 la mas clara y 0 la mas transparente
ventana.attributes("-alpha", 1)

# A la variable que ya contiene el contructor de la clase Tkinter se le asigna el metodo mainloop() que
# proporciona que la ventana del ejecutable se pueda visualizar
ventana.mainloop()
