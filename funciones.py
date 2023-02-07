import sympy as sp
import numpy as np
import tkinter as tk

# Definimos funciones con las que vamos a trabajar

################ Funciones matemáticas ######################
listaDerivadas = []
def derivacionFormula(polinomio, variables):

    for var in variables:
        derivada = sp.diff(polinomio, var)
#        numericDeriv = sp.lambdify(var, derivada)
        listaDerivadas.append(derivada)

def obtenerFormula(formula,variables,guardarFormula, guardarVariables):
    guardarFormula = formula.get()
    guardarVariables = variables.get()

    derivacionFormula(guardarFormula, guardarVariables.split())
    print(listaDerivadas)

    



#############################################################