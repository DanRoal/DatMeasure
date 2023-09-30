import tkinter as tk
from tkinter import ttk
import funciones as fun

root = tk.Tk()
root.title("DatMeasure")
root.geometry("500x300")

style = ttk.Style()
style.theme_use("clam")  # Puedes probar con "clam", "alt", "default", etc.
style.configure(".", font=("Arial", 12))
style.configure("TButton", padding=6, relief="flat", background="#4285F4", foreground="white")
style.map("TButton", background=[("active", "#0d47a1")])

style.configure("TEntry", padding=6, relief="flat", background="#f2f2f2", foreground="#333333")

formula = ttk.Entry(root)
formula.place(x=150, y=100)

variables = ttk.Entry(root)
variables.place(x=150, y=120)

delta_x = ttk.Entry(root)
delta_x.place(x=300, y=120)

desviacionDatos = ttk.Button(root, text="Desviacion entre datos", command=lambda: fun.obtenerFormula(formula.get(), variables.get(), deltas=delta_x.get(), trigger=False))
desviacionResultados = ttk.Button(root, text="Desviacion entre resultados")

desviacionDatos.place(x=10, y=150)
desviacionResultados.place(x=10, y=170)

root.mainloop()