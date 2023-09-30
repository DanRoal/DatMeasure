import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import filedialog
import math
import pandas as pd
from tkinter import messagebox

# Definimos funciones con las que vamos a trabajar

################ Funciones matemáticas ######################
listaDerivadas = []
listaDerivadasNumerica = []
listaDatosExperimentales = []
global contador_ventanas
contador_ventanas = 0
promedios = []


def derivacionFormula(polinomio, variables):
    
    listaDerivadas.clear()
    listaDerivadasNumerica.clear()

    for var in variables:
        derivada = sp.diff(polinomio, var)
        numericDeriv = sp.lambdify(variables, derivada)
        listaDerivadas.append(derivada)
        listaDerivadasNumerica.append(numericDeriv)

def obtenerFormula(formula,variables, deltas, trigger: bool):
    global guardarFormula 
    guardarFormula = formula
    global Variables 
    Variables = variables.split()
    global lista_apariencia
    lista_apariencia = deltas.split()

    global contador_ventanas
    contador_ventanas = 0

    derivacionFormula(guardarFormula, Variables)
    nuevasVentanasDatos(trigger)

 #   La derivación ya está guardada en dos listas, una como expresión algebraica y otra como función numérica
  #  La lista que contiene las expresiones algebraicas la usaremos después para mostrala al usuario en formato LaTex
  #  Mientras que la de funciones numéricas las usaremos para meterle los valores que nos de el usuario

    print(listaDerivadas)

def suma_cuadratura(Lista_de_sumandos):
    suma = 0
    for i in Lista_de_sumandos:
        suma = suma + i**2
    resultado = math.sqrt(suma)
    return resultado

def incertidumbre_absoluta(lista_prom):

    for i in range(len(listaDatosExperimentales)):
        promedios.append(funcion_promedios(list(np.float_(listaDatosExperimentales[i]) )))

    return math.sqrt(incertidumbre_estadistica(lista_prom)**2+incertidumbre_nominal(lista_prom)**2)

def funcion_promedios(datos):
    suma_datos = 0
    for i in datos:
        suma_datos += i
    return suma_datos/len(datos)

def incertidumbre_f():
    evaluaciones_f = []
    
    
    

def incertidumbre_estadistica(lista):
    sumandos = []
    arr_standar = np.std(np.float_(listaDatosExperimentales), axis=1, ddof=1)
    lista_standar = list(arr_standar)

    for i in range(len(listaDerivadasNumerica)):
        multiplicados = (abs(listaDerivadasNumerica[i](*lista))) * lista_standar[i]
        sumandos.append(multiplicados)

    return suma_cuadratura(sumandos)

def incertidumbre_nominal(lista):
    sumandos = []
    for i in range(len(lista_apariencia)):
        df = abs(listaDerivadasNumerica[i](*lista))
        ap = np.float_(lista_apariencia[i])
        multiplicados = (df) * (ap)
        sumandos.append(multiplicados)

    return suma_cuadratura(sumandos)

#############################################################

###################### Clases ###############################
'''
import tkinter as tk

class SecondaryWindow:

    alive = False

    def __init__(self, master, name):
        self.master = master
        self.master.title("Ingresa los datos de la variable {name}")
        self.label = tk.Label(self.master, text=f"oli caracoli")
        self.label.pack()
        if (contador_ventanas == len(Variables)):
            self.button_close = ttk.Button(
                self,
                text="Terminar",
                command=self.destroy
            )
        else:
            self.button_close = ttk.Button(
                self,
                text="Siguiente variable",
                command=self.destroy
            )

    # Create a list of window names
    window_names = ["Window 1", "Window 2", "Window 3", "Window 4", "Window 5"]

    # Create secondary windows with different names using a for loop
    for name in window_names:
        new_window = tk.Toplevel(root)
        SecondaryWindow(new_window, name)
'''
#############################################################


##################### Funciones de interfaz##################

def nuevasVentanasDatos(trigg):
    global contador_ventanas
    contador_ventanas += 1


    ventana_nueva1 = tk.Toplevel()
    ventana_nueva1.title(f"Introduce tus valores medidos para la variable {Variables[contador_ventanas-1]}")
    ventana_nueva1.geometry("500x300")
    entrada_datos = tk.Entry(ventana_nueva1)
    entrada_datos.grid(row=2)

    boton_cargar = tk.Button(ventana_nueva1, text="Cargar archivo CSV", command=cargar_archivo)
    boton_cargar.grid(row=6)

    if contador_ventanas >= len(Variables):
        trigg = True
    
    boton_nueva_ventana = tk.Button(ventana_nueva1, text="Siguiente variable", command= lambda: obtenerDatos(entrada_datos.get(), ventana_nueva1, trigg))
    boton_nueva_ventana.grid(row=3)
    boton_cancelar = tk.Button(ventana_nueva1, text="Cancelar", command= ventana_nueva1.destroy)
    boton_cancelar.grid(row=4)

def obtenerDatos(entrada, ventana, encendido):
    
        
    if encendido==True:
        listaDatosExperimentales.append(entrada.split())
        ventana.destroy()
        print([incertidumbre_absoluta(promedios), incertidumbre_estadistica(promedios), incertidumbre_nominal(promedios)])
        
    else:
        listaDatosExperimentales.append(entrada.split())
        ventana.destroy()
        nuevasVentanasDatos(encendido)

def cargar_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    
    if ruta_archivo:
        try:
            df = pd.read_csv(ruta_archivo)
            # Puedes imprimir el DataFrame o hacer cualquier otra operación con él.
            print("DataFrame cargado exitosamente:\n", df)
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")

###########################################################