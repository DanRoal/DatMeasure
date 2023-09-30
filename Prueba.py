import tkinter as tk
from tkinter import filedialog
import pandas as pd

def cargar_archivo():
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV", filetypes=[("Archivos CSV", "*.csv")])
    
    if ruta_archivo:
        try:
            df = pd.read_csv(ruta_archivo)
            # Puedes imprimir el DataFrame o hacer cualquier otra operación con él.
            print("DataFrame cargado exitosamente:\n", df)
        except Exception as e:
            print(f"Error al cargar el archivo: {e}")
    else:
        print("No se seleccionó ningún archivo.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cargar archivo CSV")

# Crear un botón para cargar el archivo
boton_cargar = tk.Button(root, text="Cargar archivo CSV", command=cargar_archivo)
boton_cargar.pack(pady=20)

# Iniciar el bucle de la interfaz gráfica
root.mainloop()