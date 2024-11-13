import tkinter as tk
from tkinter import messagebox


# Função para calcular o IMC
def calcular_imc():
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get())

        if peso <= 0 or altura <= 0:
            raise ValueError("Peso e altura devem ser valores positivos!")

        imc = peso / (altura ** 2)
        resultado_imc.config(text=f"IMC: {imc:.2f}")

        # Classificação do IMC
        if imc < 18.5:
            classificacao = "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            classificacao = "Peso normal"
        elif 25 <= imc < 29.9:
            classificacao = "Sobrepeso"
        elif 30 <= imc < 39.9:
            classificacao = "Obesidade"
        else:
            classificacao = "Obesidade grave"

        resultado_classificacao.config(text=f"Classificação: {classificacao}")

    except ValueError as e:
        messagebox.showerror("Erro", str(e))


# Configuração da janela
root = tk.Tk()
root.title("Calculadora de IMC")
root.configure(bg="white")

# Tamanho da janela
root.geometry("350x300")

# Título
titulo = tk.Label(root, text="Calculadora de IMC", font=("Helvetica", 16), bg="white", fg="green")
titulo.pack(pady=10)

# Peso
label_peso = tk.Label(root, text="Peso (kg):", font=("Helvetica", 12), bg="white", fg="green")
label_peso.pack(pady=5)
entry_peso = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="green", borderwidth=2)
entry_peso.pack(pady=5)

# Altura
label_altura = tk.Label(root, text="Altura (m):", font=("Helvetica", 12), bg="white", fg="green")
label_altura.pack(pady=5)
entry_altura = tk.Entry(root, font=("Helvetica", 12), bg="white", fg="green", borderwidth=2)
entry_altura.pack(pady=5)

# Botão para calcular o IMC
botao_calcular = tk.Button(root, text="Calcular IMC", font=("Helvetica", 12), bg="green", fg="white",
                           command=calcular_imc)
botao_calcular.pack(pady=10)

# Resultado do IMC
resultado_imc = tk.Label(root, text="IMC: ", font=("Helvetica", 12), bg="white", fg="green")
resultado_imc.pack(pady=5)

# Classificação do IMC
resultado_classificacao = tk.Label(root, text="Classificação: ", font=("Helvetica", 12), bg="white", fg="green")
resultado_classificacao.pack(pady=5)

# Iniciar o loop da interface gráfica
root.mainloop()
