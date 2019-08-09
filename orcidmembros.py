import matplotlib.pyplot as plt
import numpy as np

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
