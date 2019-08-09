import matplotlib.pyplot as plt
import numpy as np

""" 
Matplotlib "Hello World"

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show() 

"""

membros = ["Associações","Financiadoras/Agencias de Fomento","Orgãos Governamentais","Entidades de Armazenamento de Dados","Editoras","Institutos de Pesquisa/Universidades","Outros"]
qtd = [38,33,33,75,35,833,5]

y_pos = np.arange(len(membros))

plt.barh(y_pos, qtd, align='center', alpha=0.5, color="orange")
plt.yticks(y_pos, membros)
plt.xlabel("Quantidade de Membros Parceiros")

for i, v in enumerate(qtd):
    plt.text(v + 3, i, str(qtd[i]), color="black")

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()
