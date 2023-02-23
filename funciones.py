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
def derivacionFormula(polinomio, variables):
    
    listaDerivadas.clear()
    listaDerivadasNumerica.clear()

    for var in variables:
        derivada = sp.diff(polinomio, var)
        numericDeriv = sp.lambdify(var, derivada)
        listaDerivadas.append(derivada)
        listaDerivadasNumerica.append(numericDeriv)

def obtenerFormula(formula,variables, deltas):
    global guardarFormula 
    guardarFormula = formula
    global Variables 
    Variables = variables.split()
    global lista_apariencia
    lista_apariencia = deltas.split()

    derivacionFormula(guardarFormula, Variables)
    nuevasVentanasDatos()

 #   La derivación ya está guardada en dos listas, una como expresión algebraica y otra como función numérica
  #  La lista que contiene las expresiones algebraicas la usaremos después para mostrala al usuario en formato LaTex
  #  Mientras que la de funciones numéricas las usaremos para meterle los valores que nos de el usuario

    print(listaDerivadas)

def suma_cuadratura(Lista_de_sumandos):
    suma = None
    for i in Lista_de_sumandos:
        suma = i**2
    
    resultado = math.sqrt(suma)
    return resultado

def incertidumbre_absoluta():

    print(list(np.float_(listaDatosExperimentales)))

    for i in range(0,len(listaDatosExperimentales)):
        promedios.append(funcion_promedios(list(np.float_(listaDatosExperimentales[i]) )))

    return math.sqrt(incertidumbre_estadistica(promedios)**2+incertidumbre_nominal(promedios)**2)

def funcion_promedios(datos):
    suma_datos = 0
    for i in datos:
        suma_datos += i
    return suma_datos/len(datos)

def incertidumbre_estadistica(lista_promedios):
    sumandos = []
    arr_varianza = np.var(np.float_(listaDatosExperimentales), axis=1)
    lista_varianza = list(arr_varianza)
    for i in range(0,len(listaDerivadasNumerica)):
        multiplicados = (abs(listaDerivadasNumerica[i](lista_promedios[i])))**2 * lista_varianza[i]
        sumandos.append(multiplicados)

    return suma_cuadratura(sumandos)

def incertidumbre_nominal(lista_promedios):
    sumandos = []
    print(listaDerivadasNumerica)
    print(lista_apariencia)
    for i in range(0,len(listaDerivadasNumerica)):
        multiplicados = (abs(listaDerivadasNumerica[i](lista_promedios[i])))**2 * (list(float(lista_apariencia[i]) ))**2
        sumandos.append(multiplicados)

    return suma_cuadratura(sumandos)

#############################################################


##################### Funciones de interfaz##################
#def confirmacion():
#    
#    obtenerFormula(formula, variables, guardarFormula, guardarVariables)

def nuevasVentanasDatos():
    global contador_ventanas 
    contador_ventanas += 1


    ventana_nueva1 = tk.Toplevel()
    ventana_nueva1.title("Introduce tus valores medidos")
    ventana_nueva1.geometry("500x300")
    entrada_datos = tk.Entry(ventana_nueva1)
    entrada_datos.grid(row=2)

    if contador_ventanas > len(Variables):
        obtenerDatos(entrada_datos.get(), ventana_nueva1)
    
    boton_nueva_ventana = tk.Button(ventana_nueva1, text="Siguiente variable", command= lambda: obtenerDatos(entrada_datos.get(), ventana_nueva1))
    boton_nueva_ventana.grid(row=3)
    boton_cancelar = tk.Button(ventana_nueva1, text="Cancelar", command= ventana_nueva1.destroy)
    boton_cancelar.grid(row=4)

def obtenerDatos(entrada, ventana):
        
    if contador_ventanas > len(Variables):
        ventana.destroy()
        print([incertidumbre_absoluta(), incertidumbre_estadistica(promedios), incertidumbre_nominal(promedios)])
    else:
        listaDatosExperimentales.append(entrada.split())
        ventana.destroy()
        nuevasVentanasDatos()

###########################################################