
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

#recebe a base de dados do arquivo txt
#questão a
df = pd.read_csv('dados_tarefa2.txt', skiprows=3, delimiter='|')

#filtra abase de dados
#questão b
filtrado=df[(0.3<df['b'])&(df['b']<0.7)]

#questão c
b=np.array(filtrado.loc[:,'b'])
v=np.array(filtrado.loc[:,'v'])
z=np.array(filtrado.loc[:,'z'])
m=np.array(filtrado.loc[:,'m'])


#questão d
mu=np.array(filtrado.loc[:,'mu'])
sd=np.array(filtrado.loc[:,'sd'])
nd=np.array(filtrado.loc[:,'nd'])
sc=np.array(filtrado.loc[:,'sc'])
ssd=np.array(filtrado.loc[:,'ssd'])

#questão e
c=(v+z+m)/3
print(filtrado)


fig, ax = plt.subplots()

plt.xlabel('b')
plt.ylabel('v,z,m')
plt.plot(b, v, color='red', label='Linha V')
plt.plot(b, z, color='blue', label='Linha Z')
plt.plot(b, m, color='green', label='Linha M')

plt.legend()
plt.savefig('C.png')
#plt.show()

plt.subplots()

plt.xlabel('mu')
plt.ylabel('sd,nd,sc,ssd')
plt.plot(mu, sd, color=(1, 0, 0), label='Linha V')
plt.plot(mu, nd, color='blue', label='Linha Z')
plt.plot(mu, sc, color='green', label='Linha M')
plt.plot(mu, ssd, color='purple', label='Linha SSD')
plt.legend()

plt.savefig('D.png')
#plt.show()

plt.subplots()

plt.xlabel('b')
plt.ylabel('c')
plt.plot(b, c, color=(1, 0, 0), label='Linha C')
plt.legend()

plt.savefig('e.png')
#plt.show()


