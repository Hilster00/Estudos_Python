import matplotlib.pyplot as plt
import numpy as np

# Dados para os gráficos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Gráfico de Linha
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sen(x)')
plt.title('Gráfico de Linha')
plt.xlabel('X')
plt.ylabel('Sen(X)')
plt.legend()
plt.grid(True)
plt.show()

# Gráfico de Dispersão
np.random.seed(0)
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
area = (30 * np.random.rand(50))**2

plt.figure(figsize=(8, 6))
plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.title('Gráfico de Dispersão')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()

# Gráfico de Barras
x = ['A', 'B', 'C', 'D', 'E']
y = [3, 7, 2, 5, 8]

plt.figure(figsize=(8, 6))
plt.bar(x, y)
plt.title('Gráfico de Barras')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(axis='y')
plt.show()

# Gráfico de Histograma
data = np.random.randn(1000)

plt.figure(figsize=(8, 6))
plt.hist(data, bins=30, edgecolor='black')
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()

# Gráfico de Pizza
labels = ['Maçãs', 'Laranjas', 'Bananas', 'Morangos']
sizes = [30, 25, 20, 25]
explode = (0, 0.1, 0, 0)  # destaca a segunda fatia (laranjas)

plt.figure(figsize=(8, 6))
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Gráfico de Pizza')
plt.axis('equal')  # Assegura que o gráfico seja desenhado como um círculo.
plt.show()

# Salvar um gráfico em um arquivo
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='Sen(x)')
plt.title('Gráfico de Linha')
plt.xlabel('X')
plt.ylabel('Sen(X)')
plt.legend()
plt.grid(True)
plt.savefig('grafico_linha.png')  # Salva o gráfico como 'grafico_linha.png'

# Múltiplos gráficos na mesma janela
plt.figure(figsize=(10, 8))

plt.subplot(2, 2, 1)
plt.plot(x, y)
plt.title('Gráfico 1')

plt.subplot(2, 2, 2)
plt.scatter(x, y)
plt.title('Gráfico 2')

plt.subplot(2, 2, 3)
plt.bar(x, y)
plt.title('Gráfico 3')

plt.subplot(2, 2, 4)
plt.hist(data, bins=20)
plt.title('Gráfico 4')

plt.tight_layout()
plt.show()
