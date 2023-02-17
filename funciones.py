import sympy as sp
import numpy as np
import tkinter as tk

# Definimos funciones con las que vamos a trabajar

################ Funciones matemáticas ######################
listaDerivadas = []
listaDerivadasNumerica = []
listaDatosExperimentales = []
contador_ventanas = 0
def derivacionFormula(polinomio, variables):
    
    listaDerivadas.clear()
    listaDerivadasNumerica.clear()

    for var in variables:
        derivada = sp.diff(polinomio, var)
        numericDeriv = sp.lambdify(var, derivada)
        listaDerivadas.append(derivada)
        listaDerivadasNumerica.append(numericDeriv)

def obtenerFormula(formula,variables):
    global guardarFormula 
    guardarFormula = formula
    global Variables 
    Variables = variables.split()

    derivacionFormula(guardarFormula, Variables)
    nuevasVentanasDatos()

 #   La derivación ya está guardada en dos listas, una como expresión algebraica y otra como función numérica
  #  La lista que contiene las expresiones algebraicas la usaremos después para mostrala al usuario en formato LaTex
  #  Mientras que la de funciones numéricas las usaremos para meterle los valores que nos de el usuario

    print(listaDerivadas)

def suma_cuadratura(Lista_de_sumandos):
    suma = None
    for i in Lista_de_sumandos:
        suma = i^2
    
    resultado = np.sqrt(suma)
    return resultado
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
    entrada_datos = tk.Entry(ventana_nueva1)
    entrada_datos.grid(row=2)

    boton_nueva_ventana = tk.Button(ventana_nueva1, ext="Siguiente variable", command= nuevasVentanasDatos)
    boton_nueva_ventana.grid(row=3)
    boton_cancelar = tk.Button(ventana_nueva1, text="Cancelar", command= ventana_nueva1.destroy)
    boton_cancelar.grid(row=4)

    if contador_ventanas > len(Variables):
        ventana_nueva1.destroy()
    listaDatosExperimentales.append(entrada_datos.get().split())

###########################################################