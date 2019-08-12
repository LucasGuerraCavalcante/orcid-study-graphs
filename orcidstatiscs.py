
import matplotlib.pyplot as plt
import numpy as np

identificadores = ["Total de Identificadores Ativos","Vinculados a Identificadores Externos"]
qtd = [6903403,2854313]

y_pos = np.arange(len(identificadores))

plt.barh(y_pos, qtd, align='center', alpha=0.5, color=["orange","green"])
plt.yticks(y_pos, identificadores)
plt.xlabel("Quantidade de Identificadores")
plt.title("Identificadores ORCiD Ativos")

for i, v in enumerate(qtd):
    plt.text(v + 3, i, str(qtd[i]), color="black")

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()

education = ["Total de Identificadores Ativos","Vinculados a Instituições de Ensino","Instituições de Ensino"]
qtd2 = [6903403,1921502,519903]

y_pos = np.arange(len(education))

plt.barh(y_pos, qtd2, align='center', alpha=0.5, color=["orange","green","blue"])
plt.yticks(y_pos, education)
plt.xlabel("Quantidade de Identificadores")
plt.title("Identificadores ORCiD Ativos Vinculados a Instituições de Ensino")

for i, v in enumerate(qtd2):
    plt.text(v + 3, i, str(qtd2[i]), color="black")

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()

employment = ["Total de Identificadores Ativos","Identificadores com Afiliação de Emprego","Organizações de Emprego"]
qtd3 = [6903403,1857336,939040]

y_pos = np.arange(len(employment))

plt.barh(y_pos, qtd3, align='center', alpha=0.5, color=["orange","green","blue"])
plt.yticks(y_pos, employment)
plt.xlabel("Quantidade de Identificadores")
plt.title("Identificadores ORCiD Ativos Vinculados a Algum Emprego")

for i, v in enumerate(qtd3):
    plt.text(v + 3, i, str(qtd3[i]), color="black")

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()

funding = ["Identificadores com Afiliação à Financiadoras","Organizações de Financiamento"]
qtd4 = [190463,185701]

y_pos = np.arange(len(funding))

plt.barh(y_pos, qtd4, align='center', alpha=0.5, color=["green","blue"])
plt.yticks(y_pos, funding)
plt.xlabel("Quantidade de Identificadores")
plt.title("Identificadores ORCiD Ativos Vinculados com Afiliação à Financiadoras")

for i, v in enumerate(qtd4):
    plt.text(v + 3, i, str(qtd4[i]), color="black")

ax = plt.gca()
ax.spines["right"].set_visible(False)
ax.spines["top"].set_visible(False)

plt.show()