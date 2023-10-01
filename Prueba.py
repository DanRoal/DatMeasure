from numpy import *                               # 1.21.1
from sympy import *                               # 1.8
from tkinter import *                             # 8.6
from tkinter import filedialog,ttk,messagebox
import matplotlib.pyplot as plt                   # 3.4.3
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg\
import FigureCanvasTkAgg
from matplotlib.figure import Figure 
from PIL import ImageTk,Image,ImageChops,ImageOps # 8.3.1
import pandas as pd                               # 1.3.1
import math as m
import io
import funciones as fun

root = Tk()
root.title("DatMeasure")
root.geometry("500x300")

PX=root.winfo_screenwidth()/2-433.5
PY=root.winfo_screenheight()/2-350
root.geometry('867x650+%d+%d'%(PX,PY)) 

style = ttk.Style(root)

# Nombramos nuestros propios colores, código HEX:
cfondo='#E5ECFF'
cbotones='#2E68FF'
cbotonessele='#0048FF'
cmbotones='#CAD9FF'
cmbotonessele='#A5BEFF'
cscrolls='#B7CBFF'
cscrollssele='#8AAAFF'
cletras='#5A5B5F'
cletrasgraf='#5A5B5F'


###Creamos estilo 
style.theme_create('Estilo', settings={
    # Los botones:
    "TButton": {
        "configure": {
            "background": cbotones,
            "focuscolor": "background",
            "foreground": 'white',
            "highlightthickness": 1,
            "font":('Helvetica',12),
            "anchor":"center",
            "padding": [5,2]
        },
        "map": {
            "background": [('pressed','!focus', 
                cbotonessele),('active',cbotonessele)], 
            "relief": [('pressed','groove'),('!pressed',
                'ridge')],
            "foreground": [('disabled','white'),('pressed',
                'white'),('active','white')],
        }
    }
})
style.theme_use("Estilo")  # Puedes probar con "clam", "alt", "default", etc.


style.configure(".", font=("Arial", 12))
style.configure("TEntry", padding=5, relief="raised")


formula = ttk.Entry(root)
formula.place(x=150, y=80)

variables = ttk.Entry(root)
variables.place(x=150, y=120)

delta_x = ttk.Entry(root)
delta_x.place(x=300, y=120)

desviacionDatos = ttk.Button(root, text="Desviacion entre datos", command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas=delta_x.get(), trigger=False))
desviacionResultados = ttk.Button(root, text="Desviacion entre resultados")

desviacionDatos.place(x=10, y=150)
desviacionResultados.place(x=10, y=190)

root.mainloop()