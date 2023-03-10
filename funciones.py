import sympy as sp
import numpy as np
import tkinter as tk
import math
from tkinter import messagebox

# Definimos funciones con las que vamos a trabajar

################ Funciones matemáticas ######################
listaDerivadas = []
listaDerivadasNumerica = []
listaDatosExperimentales = []
contador_ventanas = 0
promedios = []
Formula = sp.lambdify(Variables, guardarFormula)

def derivacionFormula(polinomio, variables):
    
    listaDerivadas.clear()
    listaDerivadasNumerica.clear()

    for var in variables:
        derivada = sp.diff(polinomio, var)
        numericDeriv = sp.lambdify(variables, derivada)
        listaDerivadas.append(derivada)
        listaDerivadasNumerica.append(numericDeriv)

def obtenerFormula(formula,variables, deltas, trigger = bool):
    global guardarFormula 
    guardarFormula = formula
    global Variables 
    Variables = variables.split()
    global lista_apariencia
    lista_apariencia = deltas.split()

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


##################### Funciones de interfaz##################

def nuevasVentanasDatos(trigg):
    global contador_ventanas 
    contador_ventanas += 1


    ventana_nueva1 = tk.Toplevel()
    ventana_nueva1.title("Introduce tus valores medidos")
    ventana_nueva1.geometry("500x300")
    entrada_datos = tk.Entry(ventana_nueva1)
    entrada_datos.grid(row=2)

    if contador_ventanas > len(Variables):
        obtenerDatos(entrada_datos.get(), ventana_nueva1, trigg)
    
    boton_nueva_ventana = tk.Button(ventana_nueva1, text="Siguiente variable", command= lambda: obtenerDatos(entrada_datos.get(), ventana_nueva1))
    boton_nueva_ventana.grid(row=3)
    boton_cancelar = tk.Button(ventana_nueva1, text="Cancelar", command= ventana_nueva1.destroy)
    boton_cancelar.grid(row=4)

def obtenerDatos(entrada, ventana, encendido):
    
        
    if contador_ventanas > len(Variables) & encendido==True:
        ventana.destroy()
        print([incertidumbre_absoluta(promedios), incertidumbre_estadistica(promedios), incertidumbre_nominal(promedios)])
        
    else:
        listaDatosExperimentales.append(entrada.split())
        ventana.destroy()
        nuevasVentanasDatos()

###########################################################