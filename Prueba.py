from numpy import *                               # 1.21.1
from sympy import *                               # 1.8
from tkinter import *                             # 8.6
from tkinter import filedialog,ttk,messagebox
import funciones as fun

import pandas as pd
from tkinter import filedialog, messagebox


root = Tk()             # creamos una ventana
root.title("DatMeasure")


def cargar_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    
    if ruta_archivo:
        try:
            df = pd.read_csv(ruta_archivo)
            # Puedes imprimir el DataFrame o hacer cualquier otra operación con él.
            print("DataFrame cargado exitosamente:\n", df, type(df))
            primera_columna_lista = df.iloc[:, 0].tolist()
            print(primera_columna_lista)
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
    else:
        messagebox.showwarning("No se seleccionó ningún archivo.")


boton_cargar = Button(root, text="Cargar archivo CSV", command=cargar_archivo)
boton_cargar.grid(row=6)

##Convertimos a lista los datos de la primera columna del dataframe


root.mainloop()
