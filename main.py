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
variables = tkinter.Entry()     # Le pedimos las variales respecto a las cuales derivar
variables.place(x=150, y=120)
delta_x = tkinter.Entry()       #Le pedimos que ingrese la inertidumbre absoluta o aparente de las variables
delta_x.place(x=300, y=120)

desviacionDatos = tkinter.Button(text="Desviacion entre datos", command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas= delta_x.get()))       # Hacemos un boton con el cual ejecutar las acciones que queramos
desviacionResultados = tkinter.Button(text= "Desviacion entre resultados")


desviacionDatos.place(x=10, y=100) 
desviacionResultados.place(x=10,y=120)

root.mainloop()                 # Corremos la aplicación