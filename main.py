## En esta sección estaremos usando Tkinter para hacer una interfaz gráfica para nnuestro programa

from tkinter import*
from tkinter import ttk
import funciones as fun

###########Declaración de variables##############

#################################################

root = Tk()             # creamos una ventana
root.title("DatMeasure")        # Nombre de la aplicación

##  Dimensiones ##

PX=root.winfo_screenwidth()/2-433.5
PY=root.winfo_screenheight()/2-350
root.geometry('867x650+%d+%d'%(PX,PY))        # Tamaño de la ventana centrada

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

formula = ttk.Entry(root)       # Le pedimos al usuario la formula a derivar
formula.place(x=150, y=80)
variables = ttk.Entry(root)     # Le pedimos las variales respecto a las cuales derivar
variables.place(x=150, y=120)
delta_x = ttk.Entry(root)       #Le pedimos que ingrese la inertidumbre absoluta o aparente de las variables
delta_x.place(x=300, y=120)

desviacionDatos = ttk.Button(root, text="Desviacion entre datos", command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas= delta_x.get(), trigger=False))       # Hacemos un boton con el cual ejecutar las acciones que queramos
desviacionResultados = ttk.Button(root, text= "Desviacion entre resultados")


desviacionDatos.place(x=10, y=150) 
desviacionResultados.place(x=10,y=190)

root.mainloop()                 # Corremos la aplicación