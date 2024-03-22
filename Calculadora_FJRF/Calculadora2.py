import tkinter as tk
import re

def calcular():
    expresion = entry.get().replace(" ", "")  # Eliminar espacios en blanco
    expresion = expresion.replace("+-", "-")  # Corregir signo de resta 
    expresion = re.sub(r'\b0+(\d+)', r'\1', expresion) # Eliminar ceros a la izquierda de los números


    try:
        resultado = eval(expresion)
        resultado = round(resultado, 4)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora")

# Crear la entrada
entry = tk.Entry(root, font=("Arial", 15), justify="right")
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Crear los botones
botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    boton = tk.Button(root, text=texto, font=("Arial", 15), command=lambda t=texto: entry.insert(tk.END, t))
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

# Botón de borrar
borrar = tk.Button(root, text="C", font=("Arial", 15), command=lambda: entry.delete(0, tk.END))
borrar.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

# Botón de borrar último caracter
borrar_caracter = tk.Button(root, text="<", font=("Arial", 15), command=lambda: entry.delete(len(entry.get())-1, tk.END))
borrar_caracter.grid(row=4, column=2, columnspan=1, padx=5, pady=5, sticky="nsew")

# Botón de calcular
boton_calcular = tk.Button(root, text="=", font=("Arial", 15), command=calcular)
boton_calcular.grid(row=5, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")

# Configuración del tamaño de las columnas y filas
for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

# Ejecutar la aplicación
root.mainloop()
