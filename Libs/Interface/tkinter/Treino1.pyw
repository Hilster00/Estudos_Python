import tkinter as tk
from tkinter import messagebox


def funcao(event):
    # Obtém o índice do rótulo que foi clicado
    i = rotulos.index(event.widget)
    # Função de contagem de caracteres
    if i == 1:
        quantidade = dict()
        for c in caixa_texto.get().lower():
            quantidade[c] = quantidade.get(c, 0) + 1
        labels[1].config(text=quantidade)
    # Função de texto em maiúsculo
    elif i == 2:
        labels[2].config(text=caixa_texto.get().upper())
    else:
        caixa_texto.delete(0, tk.END)
        caixa_texto.insert(0, "Hilster Barbosa Santos")


# Funções de sair
def perguntar_sair():
    if messagebox.askyesno("Confirmação", "Você realmente deseja sair?"):
        sair()
        
def sair():
    janela.quit()
    janela.destroy()


# Criação da janela
janela = tk.Tk()
janela.geometry("250x130")
janela.title("Janela do Hilster")

# Criação dos labels e caixas de texto
labels = []
for i in range(3):
    label = tk.Label(janela, text=f"Texto {i+1}")
    labels.append(label)
caixa_texto = tk.Entry(janela, font=("Arial", 12), width=20)
labels[0].config(text="Programa do Hilster")


# Criação dos rótulos
rotulos = []
for i, texto in enumerate(["Entrada","Ação 1", "Ação 2"]):
    rotulo = tk.Label(janela, text=texto, padx=1)
    rotulo.grid(row=i+2, column=1, sticky=tk.W)
    rotulos.append(rotulo)
    rotulo.bind("<Button-1>", funcao)


# Criação do botão para imprimir o conteúdo das caixas de texto
botao_sair = tk.Button(janela, text="Fechar", command=perguntar_sair)


# Posicionamento dos widgets na janela
labels[0].grid(row=1, column=2, padx=10, pady=1)
caixa_texto.grid(row=2, column=2, padx=10, pady=1)
labels[1].grid(row=3, column=2, padx=10, pady=1)
labels[2].grid(row=4, column=2, padx=10, pady=1)
botao_sair.grid(row=5, column=2, padx=10, pady=1)


# Associando a tecla "q" à função "perguntar_sair"
janela.bind("<KeyPress-q>", lambda event: perguntar_sair())


# Início do loop principal da janela
janela.mainloop()
