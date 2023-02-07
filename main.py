## En esta sección estaremos usando Tkinter para hacer una interfaz gráfica para nnuestro programa

import tkinter
import sympy as sp
import numpy as np
import funciones as fun

###########Declaración de variables##############
guardarFormula = None
guardarVariables = None
#################################################

root = tkinter.Tk()
root.title("DatMeasure")
root.geometry("500x300")

formula = tkinter.Entry()
formula.place(x=150, y=100)
variables = tkinter.Entry()
variables.place(x=150, y=120)

button = tkinter.Button(text="Derivar", command=lambda: fun.obtenerFormula(formula, variables, guardarFormula, guardarVariables))
button.place(x=50, y=100)
 


root.mainloop()