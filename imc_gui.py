# imc_gui.py
# Interface simples para calcular IMC usando tkinter
# Execute: python imc_gui.py

import tkinter as tk
from tkinter import ttk, messagebox

def calcular_imc():
    try:
        peso = float(entry_peso.get().replace(',', '.'))
        altura = float(entry_altura.get().replace(',', '.'))
        if peso <= 0 or altura <= 0:
            raise ValueError("Valores devem ser positivos.")
    except ValueError:
        messagebox.showerror("Erro", "Informe peso e altura válidos (ex: 70.5 e 1.75).")
        return

    imc = peso / (altura ** 2)
    imc_rounded = round(imc, 2)
    classif = classificar_imc(imc)

    resultado_texto = f"IMC: {imc_rounded}\nClassificação: {classif}"
    lbl_resultado.config(text=resultado_texto)

def classificar_imc(imc):
    # Classificação usada comumente (ver referência do enunciado)
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obesidade (Grau I)"
    elif 35 <= imc < 40:
        return "Obesidade (Grau II)"
    else:
        return "Obesidade (Grau III)"

def limpar():
    entry_nome.delete(0, tk.END)
    entry_peso.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    lbl_resultado.config(text="")

# --- Janela principal ---
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("380x300")
root.resizable(False, False)
padding = {"padx": 10, "pady": 8}

frm = ttk.Frame(root)
frm.pack(fill=tk.BOTH, expand=True)

# Nome
ttk.Label(frm, text="Nome:").grid(column=0, row=0, sticky=tk.W, **padding)
entry_nome = ttk.Entry(frm)
entry_nome.grid(column=1, row=0, **padding)

# Peso (kg)
ttk.Label(frm, text="Peso (kg):").grid(column=0, row=1, sticky=tk.W, **padding)
entry_peso = ttk.Entry(frm)
entry_peso.grid(column=1, row=1, **padding)

# Altura (m)
ttk.Label(frm, text="Altura (m):").grid(column=0, row=2, sticky=tk.W, **padding)
entry_altura = ttk.Entry(frm)
entry_altura.grid(column=1, row=2, **padding)

# Botões
btn_calcular = ttk.Button(frm, text="Calcular IMC", command=calcular_imc)
btn_calcular.grid(column=0, row=3, **padding)

btn_limpar = ttk.Button(frm, text="Limpar", command=limpar)
btn_limpar.grid(column=1, row=3, **padding)

# Resultado
lbl_resultado = ttk.Label(frm, text="", font=("Helvetica", 11, "bold"))
lbl_resultado.grid(column=0, row=4, columnspan=2, **padding)

# Observação (pequena instrução)
ttk.Label(frm, text="Informe peso em kg e altura em metros (ex: 1.75).").grid(column=0, row=5, columnspan=2, **padding)

root.mainloop()
