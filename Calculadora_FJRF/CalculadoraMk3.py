import tkinter as tk
import re

def validar(event):
    if event.char not in '0123456789+-*/.':
        return "break"
    if event.char == '.' and '.' in entry.get():
        return "break"
    if event.char in '+-*/' and entry.get() and entry.get()[-1] in '+-*/':
        return "break"

def validar_boton(texto):
    if texto in '+-*/' and entry.get() and entry.get()[-1] in '+-*/':
        return
    if texto == '.' and '.' in entry.get():
        return
    entry.insert(tk.END, texto)

def calcular(event=None):
    expresion = entry.get().replace(" ", "")
    expresion = expresion.replace("+-", "-")
    expresion = re.sub(r'\b0+(\d+)', r'\1', expresion)
    expresion = re.sub(r'\.{2,}', '.', expresion)

    try:
        if "/0" in expresion or expresion[-1] in "+-*/":
            raise ValueError("Hay un error en tu operación")
        resultado = eval(expresion)
        resultado = round(resultado, 4)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(resultado))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Hay un error en tu operación")

def retroceso(event):
    if entry.get():
        entry.delete(len(entry.get())-1, tk.END)
    return "break"

root = tk.Tk()
root.title("Calculadora")
root.configure(bg='black')

entry = tk.Entry(root, font=("Arial", 12), justify="right", width=50)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
entry.bind("<Key>", validar)
entry.bind("<BackSpace>", retroceso)
entry.bind("<Return>", calcular)

botones = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('.', 4, 0), ('0', 4, 1), ('+', 4, 3),
]

for (texto, fila, columna) in botones:
    boton = tk.Button(root, text=texto, font=("Arial", 15), command=lambda t=texto: validar_boton(t), bg='black', fg='white')
    boton.grid(row=fila, column=columna, padx=5, pady=5, sticky="nsew")

borrar = tk.Button(root, text="C", font=("Arial", 15), command=lambda: entry.delete(0, tk.END), bg='black', fg='white')
borrar.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

borrar_caracter = tk.Button(root, text="<", font=("Arial", 15), command=lambda: entry.delete(len(entry.get())-1, tk.END), bg='black', fg='white')
borrar_caracter.grid(row=4, column=2, columnspan=1, padx=5, pady=5, sticky="nsew")

boton_calcular = tk.Button(root, text="=", font=("Arial", 15), command=calcular, bg='black', fg='white')
boton_calcular.grid(row=5, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")

for i in range(5):
    root.grid_columnconfigure(i, weight=1)
    root.grid_rowconfigure(i, weight=1)

root.mainloop()
