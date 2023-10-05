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


cadena = "x  "
variables = [letra.lstrip().rstrip() for letra in cadena.split(',')]


import matplotlib.pyplot as plt
import numpy as np

# Data for plotting
s = np.linspace(0.3, 1.7, 10)
t = s

dis = np.random.normal(1, 0.1, 10)
tiem = np.random.normal(1, 0.1, 10)

fig, ax= plt.subplots()
fig2, ax2= plt.subplots()

ax.scatter(s,t, s=150)

ax.set(ylabel='Tiempo (s)', xlabel='Distancia (m)',
       title='Calculo de la velocidad', xlim=[0,2], ylim=[0,2])
ax.grid()

ax2.scatter(dis, tiem, s=150)

ax2.set(ylabel='Tiempo (s)', xlabel='Distancia (m)',
       title='Calculo de la velocidad', xlim=[0,2], ylim=[0,2])
ax2.grid()

plt.show()