import numpy as np

listaDatosExperimentales = [[1,2,3,4,5,6],[1,2,3,4,5,6]]

def evaluaciones_f():
    lista_evaluar=[]
    
    for i in range(len(listaDatosExperimentales[0])):
        listita=[]
        for j in range(len(listaDatosExperimentales)):
            listita.append(listaDatosExperimentales[j][i])
        lista_evaluar.append(listita)
    
    return lista_evaluar

print(evaluaciones_f())
cadena = "x  "
variables = [letra.lstrip().rstrip() for letra in cadena.split(',')]

print(variables)