import sympy as sp
import numpy as np
import tkinter as tk
from tkinter import filedialog
import math
import pandas as pd
from tkinter import messagebox
import customtkinter as ctk
import random

# Definimos funciones con las que vamos a trabajar

################ Funciones matemáticas ######################
listaDerivadas = []
listaDerivadasNumerica = []
listaDatosExperimentales = []
global contador_ventanas
contador_ventanas = 0
promedios = []

eval_resultados=0

global data_frame
data_frame = None


def derivacionFormula(polinomio, variables):
    
    listaDerivadas.clear()
    listaDerivadasNumerica.clear()
    listaDatosExperimentales.clear()
    promedios.clear()

    for var in variables:
        derivada = sp.diff(polinomio, var)
        numericDeriv = sp.lambdify(variables, derivada)
        listaDerivadas.append(derivada)
        listaDerivadasNumerica.append(numericDeriv)

def obtenerFormula(formula,variables, deltas, trigger: bool, datos:bool):
    global guardarFormula 
    guardarFormula = formula
    global Variables 
    Variables = [letra.lstrip().rstrip() for letra in variables.split(',')]
    global lista_apariencia
    lista_apariencia = [letra.lstrip().rstrip() for letra in deltas.split(',')]

    global contador_ventanas
    contador_ventanas = 0

    derivacionFormula(guardarFormula, Variables)

#   La derivación ya está guardada en dos listas, una como expresión algebraica y otra como función numérica
#   La lista que contiene las expresiones algebraicas la usaremos después para mostrala al usuario en formato LaTex
#   Mientras que la de funciones numéricas las usaremos para meterle los valores que nos de el usuario

    nuevasVentanasDatos(trigger,datos)

    print(listaDerivadas)

def suma_cuadratura(Lista_de_sumandos):
    suma = 0
    for i in Lista_de_sumandos:
        suma = suma + i**2
    resultado = math.sqrt(suma)
    return resultado

def incertidumbre_absoluta_datos(lista_prom):

    for i in range(len(listaDatosExperimentales)):
        promedios.append(funcion_promedios(list(np.float_(listaDatosExperimentales[i]) )))

    return math.sqrt(incertidumbre_estadistica_datos(lista_prom)**2+incertidumbre_nominal(lista_prom)**2)

def funcion_promedios(datos):
    suma_datos = 0
    for i in datos:
        suma_datos += i
    return suma_datos/len(datos)

def evaluaciones_f():
    evaluaciones=[]
    lista_evaluar=[]
    
    for i in range(len(listaDatosExperimentales[0])):
        listita=[]
        for j in range(len(listaDatosExperimentales)):
            listita.append(listaDatosExperimentales[j][i])
        lista_evaluar.append(listita)
    
    formulanum = sp.lambdify(Variables, guardarFormula)

    for i in range(len(lista_evaluar)):
        evaluaciones.append(formulanum(*lista_evaluar[i]))
    
    return [evaluaciones, lista_evaluar]

def incert_estadistica_resultados(lista):
    return np.std(lista, ddof=1)

def incert_nominal_resultados(lista):
    nominales=[]
    for i in range(len(lista)):
        nominales.append(incertidumbre_nominal(lista[i]))
    return random.choice(nominales)

def incert_absoluta_resultados():
    l = [incert_estadistica_resultados(evaluaciones_f()), incert_nominal_resultados(evaluaciones_f())]
    return suma_cuadratura(l)
    
    
    

def incertidumbre_estadistica_datos(lista):
    sumandos = []
    lista_standar = [np.std(np.float_(i), ddof=1) for i in listaDatosExperimentales]

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


##################### Funciones de interfaz##################

def nuevasVentanasDatos(trigg, datos):
    global contador_ventanas
    contador_ventanas += 1


    ventana_nueva1 = ctk.CTkToplevel(takefocus=True)
    ventana_nueva1.title(f"Introduce tus valores medidos para la variable {Variables[contador_ventanas-1]}")
    ventana_nueva1.geometry('500x300+%d+%d'%(ventana_nueva1.winfo_screenwidth()/2-433.5,ventana_nueva1.winfo_screenheight()/2-350))

    entrada_datos = ctk.CTkEntry(ventana_nueva1)
    entrada_datos.grid(row=2)


    if contador_ventanas >= len(Variables):
        trigg = True
    
    boton_nueva_ventana = ctk.CTkButton(ventana_nueva1, text="Siguiente variable", 
        command= lambda: obtenerDatos(entrada_datos.get(), ventana_nueva1, trigg, datos))
    boton_nueva_ventana.grid(row=3)

    boton_cancelar = ctk.CTkButton(ventana_nueva1, text="Cancelar", command= ventana_nueva1.destroy)
    boton_cancelar.grid(row=4)

    boton_cargar = ctk.CTkButton(ventana_nueva1, text="Cargar archivo CSV", command=lambda: cargar_archivo(ventana_nueva1, trigg, datos))
    boton_cargar.grid(row=6)

    

def obtenerDatos(entrada, ventana, encendido, datos):
    
        
    if encendido:
        listaDatosExperimentales.append([letra.lstrip().rstrip() for letra in entrada.split(',')])
        ventana.destroy()
        if datos:
            desv_datos()
        else:
            desv_resultados()
    else:
        listaDatosExperimentales.append([letra.lstrip().rstrip() for letra in entrada.split(',')])
        ventana.destroy()
        nuevasVentanasDatos(encendido)

##Función para poder cargar archivos con los datos para cada una de las variables

def cargar_archivo(ventana, encendido, datos):
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    
    if ruta_archivo:
        try:
            df = pd.read_csv(ruta_archivo)
            # Hacemos un data frame y lo ponemos en la variabel local df
            print("DataFrame cargado exitosamente:\n")
            #Vamos a escoger solamente los valores de la primera columna y convertirlo en una lista
            primera_columna_lista = df.iloc[:, 0].tolist()

            #Lo metemos en la lista de datos experimentales
            listaDatosExperimentales.append(primera_columna_lista)

            ventana.destroy()

            if encendido:
                if datos:
                    desv_datos()
                else:
                    desv_resultados()
            else:
                nuevasVentanasDatos(encendido, datos)
            
        except Exception as e:
            messagebox.showerror(message=f"Error al cargar el archivo: {e}")
    else:
        messagebox.showwarning("No se seleccionó ningún archivo.")


def desv_datos():
    print([incertidumbre_absoluta_datos(promedios), incertidumbre_estadistica_datos(promedios), incertidumbre_nominal(promedios)])

def desv_resultados():

    eval_resultados = evaluaciones_f()

    estadistica = incert_estadistica_resultados(eval_resultados[0])
    nominal = incert_nominal_resultados(eval_resultados[1])
    absoluta = suma_cuadratura([estadistica, nominal])
    
    print({'estadistica':estadistica,
        'Nominal': nominal,
        'Absoluta': absoluta})

###########################################################