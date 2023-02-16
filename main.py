## En esta sección estaremos usando Tkinter para hacer una interfaz gráfica para nnuestro programa

import tkinter
import sympy as sp
import numpy as np
import funciones as fun

###########Declaración de variables##############

#################################################

root = tkinter.Tk()             # creamos una ventana
root.title("DatMeasure")        # Nombre de la aplicación
root.geometry("500x300")        # Tamaño de la ventana

formula = tkinter.Entry()       # Le pedimos al usuario la formula a derivar
formula.place(x=150, y=100)
variables = tkinter.Entry()     # Le pedimos las variales respecto a las cules derivar
variables.place(x=150, y=120)

button = tkinter.Button(text="Derivar", command=lambda: fun.obtenerFormula(formula.get(), variables.get()))       # Hacemos un boton con el cual ejecutar las acciones que queramos
button.place(x=50, y=100)
 


root.mainloop()                 # Corremos la aplicación