## En esta sección estaremos usando Tkinter para hacer una interfaz gráfica para nnuestro programa

import tkinter as tk
from tkinter import ttk
import funciones as fun

###########Declaración de variables##############

#################################################

root = tk.Tk()             # creamos una ventana
root.title("DatMeasure")        # Nombre de la aplicación

##  Dimensiones ##

PX=root.winfo_screenwidth()/2-433.5
PY=root.winfo_screenheight()/2-350
root.geometry('867x650+%d+%d'%(PX,PY))        # Tamaño de la ventana centrada


formula = tk.Entry()       # Le pedimos al usuario la formula a derivar
formula.place(x=150, y=100)
variables = tk.Entry()     # Le pedimos las variales respecto a las cuales derivar
variables.place(x=150, y=120)
delta_x = tk.Entry()       #Le pedimos que ingrese la inertidumbre absoluta o aparente de las variables
delta_x.place(x=300, y=120)

desviacionDatos = tk.Button(text="Desviacion entre datos", command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas= delta_x.get(), trigger=False))       # Hacemos un boton con el cual ejecutar las acciones que queramos
desviacionResultados = tk.Button(text= "Desviacion entre resultados")


desviacionDatos.place(x=10, y=150) 
desviacionResultados.place(x=10,y=170)

root.mainloop()                 # Corremos la aplicación