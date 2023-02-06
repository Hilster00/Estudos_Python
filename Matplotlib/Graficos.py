import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()


# Redefinindo os limites do eixo x
ax.set_xlim(-10, 10)

# Redefinindo os limites do eixo y
ax.set_ylim(-10, 10)

x = np.array(list(range(10)))
y = np.array(list(range(10)))

plt.scatter(x, y)
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Gráfico de Linha')
plt.savefig('grafico.png')
plt.show()
