import sympy as sp
import numpy as np
from tkinter import filedialog
import math
import pandas as pd
import customtkinter as ctk
import random
from CTkMessagebox import CTkMessagebox as messagebox
import pyperclip as clipboard


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

global datos
datos = False


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

def obtenerFormula(formula,variables, deltas, trigger: bool, data:bool):
    global guardarFormula 
    guardarFormula = formula
    global Variables 
    Variables = [letra.lstrip().rstrip() for letra in variables.split(',')]
    global lista_apariencia
    lista_apariencia = [letra.lstrip().rstrip() for letra in deltas.split(',')]
    global contador_ventanas
    contador_ventanas = 0

    global datos
    datos = data

    derivacionFormula(guardarFormula, Variables)

#   La derivación ya está guardada en dos listas, una como expresión algebraica y otra como función numérica
#   La lista que contiene las expresiones algebraicas la usaremos después para mostrala al usuario en formato LaTex
#   Mientras que la de funciones numéricas las usaremos para meterle los valores que nos de el usuario

    nuevasVentanasDatos(trigger)

    print(listaDerivadas)

def suma_cuadratura(Lista_de_sumandos):
    suma = 0
    for i in Lista_de_sumandos:
        suma = suma + i**2
    resultado = math.sqrt(suma)
    return resultado

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
        lista_evaluar.append(np.float_(listita))
    
    formulanum = sp.lambdify(Variables, guardarFormula)

    for i in range(len(lista_evaluar)):

        evaluaciones.append(formulanum(*np.float_(lista_evaluar[i])))
    
    return [evaluaciones, lista_evaluar]

def incert_estadistica_resultados(lista):
    return np.std(lista, ddof=1)

def incert_nominal_resultados(lista):
    nominales=[]
    for i in range(len(lista)):
        nominales.append(incertidumbre_nominal(lista[i]))
    return nominales


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

def nuevasVentanasDatos(trigg):
    global contador_ventanas
    contador_ventanas += 1


    ventana_nueva = ctk.CTkToplevel(takefocus=True)
    ventana_nueva.title(f"Introduce tus valores medidos para la variable {Variables[contador_ventanas-1]}")
    ventana_nueva.geometry('500x300+%d+%d'%(ventana_nueva.winfo_screenwidth()/2-433.5,ventana_nueva.winfo_screenheight()/2-350))
    ventana_nueva.after(100, ventana_nueva.lift)
    ventana_nueva.minsize(400,300)

    frame = ctk.CTkFrame(ventana_nueva, fg_color="#bd7737")
    frame.grid(column=0, row = 0, sticky='nsew',padx=50, pady =50)
    frame.columnconfigure(0, weight=1)

    ventana_nueva.columnconfigure(0, weight=1)
    ventana_nueva.rowconfigure(0, weight=1)


    entrada_datos = ctk.CTkEntry(frame, placeholder_text= 'Datos (separador: ",")', fg_color= '#010101',
        width =220,height=40) 
    entrada_datos.grid(columnspan=2, row=1,padx=4, pady =4)


    if contador_ventanas >= len(Variables):
        trigg = True
    
    boton_nueva_ventana = ctk.CTkButton(frame, text="Siguiente variable", 
        command= lambda: obtenerDatos(entrada_datos.get(), ventana_nueva, trigg))
    boton_nueva_ventana.grid(columnspan=2, row=2,padx=4, pady =4)

    boton_cancelar = ctk.CTkButton(frame, text="Cancelar", command= ventana_nueva.destroy)
    boton_cancelar.grid(columnspan=2, row=3,padx=4, pady =4)

    boton_cargar = ctk.CTkButton(frame, text="Cargar archivo CSV o Excel", 
        command=lambda: cargar_archivo(ventana_nueva, trigg))
    boton_cargar.grid(columnspan=2, row=4,padx=4, pady =4)

    

def obtenerDatos(entrada, ventana, encendido):
    
        
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

def cargar_archivo(ventana, encendido):
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV o XLSX", 
        filetypes=[("Archivos CSV o Excel",("*.csv", "*.xlsx"))])
    
    if ruta_archivo:
        try:
            df = 0
            if ruta_archivo.endswith('.csv'):
                df = pd.read_csv(ruta_archivo)
            elif ruta_archivo.endswith('.xlsx'):
                df = pd.read_excel(ruta_archivo)
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
                nuevasVentanasDatos(encendido)
            
        except Exception as e:
            messagebox(title="Algo malio sal",message=f"Error al cargar el archivo: {e}", icon = 'cancel')
    else:
        messagebox(title="Cuidado!",message="No se seleccionó ningún archivo.", icon='warning')


def desv_datos():

    for i in range(len(listaDatosExperimentales)):
        promedios.append(funcion_promedios(list(np.float_(listaDatosExperimentales[i]) )))

    estadistica = incertidumbre_estadistica_datos(promedios)
    nominal = incertidumbre_nominal(promedios)
    absoluta = suma_cuadratura([estadistica, nominal])

    ms = messagebox(title="Incertidumbres", 
               message=f"Estadistica: {estadistica}\nNominal: {nominal}\nAbsoluta: {absoluta}\nLista de derivadas parciles: {listaDerivadas}", 
               icon='info',
               option_1="Guardar resultados",
               option_2="Copiar al portapapeles",
               option_3="Salir",
               width=600,
               height=300,
               font=("Arial", 20))
    if ms.get() == "Guardar resultados":
        guardar_resultados(estadistica, nominal, absoluta)
    elif ms.get() == "Copiar al portapapeles":
        copiar_resultados(estadistica, nominal, absoluta)
    else:
        pass
def desv_resultados():

    eval_resultados = evaluaciones_f()

    estadistica = incert_estadistica_resultados(eval_resultados[0])
    nominal = incert_nominal_resultados(eval_resultados[1])
    absoluta = suma_cuadratura([estadistica, nominal])
    
    ms = messagebox(title="Incertidumbres",
               message=f"Estadistica: {estadistica}\nNominal: {nominal}\nAbsoluta: {absoluta}\nLista de derivadas parciles:{listaDerivadas}", 
               icon='info',
               option_1="Guardar resultados",
               option_2="Copiar al portapapeles",
               option_3="Salir",
               width=600,
               height=300,
               font=("Arial", 20))
    if ms.get() == "Guardar resultados":
        guardar_resultados(estadistica, nominal, absoluta)
    elif ms.get() == "Copiar al portapapeles":
        copiar_resultados(estadistica, nominal, absoluta)
    else:
        pass

def copiar_resultados(estadistica, nominal, absoluta):
    clipboard.copy(f"Estadistica: {estadistica}\nNominal: {nominal}\nAbsoluta: {absoluta}\nLista de derivadas parciles: {listaDerivadas}")
    pass

def guardar_resultados(estadistica, nominal, absoluta):
    ruta = filedialog.asksaveasfilename(title="Guardar resultados", 
                                        filetypes=[("Archivo de texto", "*.txt")], 
                                        initialdir="C:/",
                                        initialfile="incertidumbres.txt")
    open(ruta, 'w').write(f"Estadistica: {estadistica}\nNominal: {nominal}\nAbsoluta: {absoluta}\nLista de derivadas parciles: {listaDerivadas}")
    pass

###########################################################