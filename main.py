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
root.geometry('480x700+%d+%d'%(PX,PY))        # Tamaño de la ventana centrada
root.minsize(480,700)

##Creamos un frame

frame = ctk.CTkFrame(root, fg_color="#bd7737")
frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)
frame.columnconfigure(0, weight=1)

frame_datos = ctk.CTkFrame(root)
frame_datos.grid(column=0, row=1, sticky="nsw")

frame_resultados = ctk.CTkFrame(root)
frame_resultados.grid(column=0, row=1, sticky="nse")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

####Imagen de fondo####
logo = PhotoImage(file='images/logo.png')
ctk.CTkLabel(frame, image = logo, text="").grid(columnspan=2, row=0)

####Imagenes de los botones####
img1 = PhotoImage(file='images/datos.png')
img1 = img1.subsample(3)
datos = ctk.CTkLabel(frame_datos, image = img1, text="").grid(row=0)

img2 = PhotoImage(file='images/resultados.png')
img2 = img2.subsample(3)
ctk.CTkLabel(frame_resultados, image = img2, text="").grid(row=0)

### Le pedimos al usuario la formula a derivar
formula = ctk.CTkEntry(frame, placeholder_text= 'Expresion a derivar', fg_color= '#010101',width =220,height=40,
    justify= CENTER)              
formula.grid(columnspan=2, row=1,padx=4, pady =4)


# Le pedimos al usuario las variables a derivar
variables = ctk.CTkEntry(frame, placeholder_text= 'Variables', fg_color= '#010101',width =220,height=40,
    justify= CENTER)               
variables.grid(columnspan=2, row=2,padx=4, pady =4)


 # Le pedimos al usuario la incertidumbre asociada a cada variable
deltas = ctk.CTkEntry(frame, placeholder_text= 'Deltas asociadas', fg_color= '#010101',width =220,height=40,
    justify= CENTER)               
deltas.grid(columnspan=2, row=3,padx=4, pady =4)


# Hacemos un boton con el cual ejecutar Desviación entre datos (monton de mediciones para un mismo dato)
desviacionDatos = ctk.CTkButton(frame_datos, text="Desviacion entre datos", 
    command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas= deltas.get(),trigger=False, datos=True))
desviacionDatos.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

       
desviacionResultados = ctk.CTkButton(frame_resultados, text= "Desviacion entre resultados", 
    command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas= deltas.get(),trigger=False, datos=False))
desviacionResultados.grid(row=2, column=0, padx=20, pady=20, sticky="ew")



root.mainloop()                 # Corremos la aplicación