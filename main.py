## En esta sección estaremos usando Tkinter para hacer una interfaz gráfica para nnuestro programa

from tkinter import*
from tkinter import ttk
import funciones as fun
import customtkinter as ctk

###########Declaración de variables##############

#################################################

root = ctk.CTk()             # creamos una ventana
root.title("DatMeasure")        # Nombre de la aplicación

##  Dimensiones ##

PX=root.winfo_screenwidth()/2-433.5
PY=root.winfo_screenheight()/2-350
root.geometry('700x650+%d+%d'%(PX,PY))        # Tamaño de la ventana centrada
root.minsize(480,600)

##Creamos un frame

frame = ctk.CTkFrame(root, fg_color="#bd7737")
frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)
frame.columnconfigure(0, weight=1)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

logo = PhotoImage(file='images/logo.png')
ctk.CTkLabel(frame, image = logo, text="").grid(columnspan=2, row=0)

formula = ctk.CTkEntry(frame, placeholder_text= 'Expresion a derivar', fg_color= '#010101',width =220,height=40,
    justify= CENTER)               # Le pedimos al usuario la formula a derivar
formula.grid(columnspan=2, row=1,padx=4, pady =4)

variables = ctk.CTkEntry(frame, placeholder_text= 'Variables', fg_color= '#010101',width =220,height=40,
    justify= CENTER)               # Le pedimos al usuario las variables a derivar
variables.grid(columnspan=2, row=2,padx=4, pady =4)

deltas = ctk.CTkEntry(frame, placeholder_text= 'Deltas asociadas', fg_color= '#010101',width =220,height=40,
    justify= CENTER)                # Le pedimos al usuario la incertidumbre asociada a cada variable
deltas.grid(columnspan=2, row=3,padx=4, pady =4)



desviacionDatos = ctk.CTkButton(root, text="Desviacion entre datos", 
    command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas= deltas.get(),
     trigger=False))       # Hacemos un boton con el cual ejecutar las acciones que queramos
desviacionResultados = ctk.CTkButton(root, text= "Desviacion entre resultados")

desviacionDatos.grid(row=1, column=0, padx=20, pady=20, sticky="ew")
desviacionResultados.grid(row=2, column=0, padx=20, pady=20, sticky="ew")



root.mainloop()                 # Corremos la aplicación