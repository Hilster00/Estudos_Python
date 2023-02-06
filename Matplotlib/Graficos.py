import matplotlib.pyplot as plt 
import numpy as np

#set das variáveis iniciais 
x0=0
v0=0
a=9.8
q=30 

#Funções anonimas para cada formula
#x(t) = x0 + v0t + (a/2)t^2
f1=lambda t:(x0+v0+(a/2)*(t**2))
#v(t) = v0 + at
f2=lambda t:(v0+a*t)

#vetores em cada instante
x=[f1(t) for t in range(q+1)]
y=[f2(t) for t in range(q+1)]
t=np.array(list(range(q+1)))
x = np.array(x)
y = np.array(y) 


fig, ax = plt.subplots()
# Redefinindo os limites do eixo x 
ax.set_xlim(x[0]-100, x[-1]+100)
# Redefinindo os limites do eixo y
ax.set_ylim(y[0]-100, y[-1]+100) 


print(f'Instante 0:(posição:{x[0]}, velocidade:{y[0]})') 
print(f'Instante {q}:(posição:{x[-1]}, velocidade:{y[-1]})') 

for i,v in enumerate(y):
    if v > 0:
        print(f'Instante {i} a velocidade muda de direção, e fica com o valor de {v:.2f}')
        break
    
plt.scatter(x, y,s=5)
plt.xlabel('Posição')
plt.ylabel('Velocidade')
plt.title('Gráfico de Linha 0')
plt.savefig('grafico0.png')
plt.show() 

plt.scatter(x, t,s=5)
plt.xlabel('Posição')
plt.ylabel('tempo')
plt.title('Gráfico de Linha 1')
plt.savefig('grafico1.png')
plt.show() 

plt.scatter(y, t,s=5)
plt.xlabel('Velocidade')
plt.ylabel('tempo')
plt.title('Gráfico de Linha 2')
plt.savefig('grafico2.png') 
plt.show()
