import sympy as sp
import numpy as np
import tkinter as tk

# Definimos funciones con las que vamos a trabajar

################ Funciones matemáticas ######################
listaDerivadas = []
listaDerivadasNumerica = []
def derivacionFormula(polinomio, variables):
    
    listaDerivadas.clear()
    listaDerivadasNumerica.clear()

    for var in variables:
        derivada = sp.diff(polinomio, var)
        numericDeriv = sp.lambdify(var, derivada)
        listaDerivadas.append(derivada)
        listaDerivadasNumerica.append(numericDeriv)

def obtenerFormula(formula,variables,guardarFormula, guardarVariables):
    guardarFormula = formula.get()
    guardarVariables = variables.get()

    derivacionFormula(guardarFormula, guardarVariables.split())

 #   La derivación ya está guardada en dos listas, una como expresión algebraica y otra como función numérica
  #  La lista que contiene las expresiones algebraicas la usaremos después para mostrala al usuario en formato LaTex
  #  Mientras que la de funciones numéricas las usaremos para meterle los valores que nos de el usuario

    print(listaDerivadas)

def suma_cuadratura(*sumandos):
    suma = None
    for i in sumandos:
        suma = i^2
    
    resultado = np.sqrt(suma)
    return resultado
#############################################################


##################### Funciones de interfaz##################
#def confirmacion():
#    
#    obtenerFormula(formula, variables, guardarFormula, guardarVariables)

def datos_variables():
    ventana_nueva1 = tk.Toplevel()
    ventana_nueva1.title("Introduce tus valores medidos")
    entrada_datos = tk.Entry(ventana_nueva1)
    entrada_datos.grid(row=2)
###########################################################