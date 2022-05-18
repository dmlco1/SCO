# import math
import math

from tabulate import tabulate
import data2 as d2
import data as d1

# emissores banda pelo critério de nyquist
banda = d2.Rb_canal / 2 * 1.20
print("Banda pelo critério de nyquist: " + str(banda))

ch = d2.Rb_total / d2.Rb_canal
print("número de canais: " + str(ch))

figuras_merito = []
emissores = [i for i in d2.emissor]
recetores = [i for i in d2.recetor]
awg = [i for i in d2.awgs]

for i in d2.emissor:
    if i[3] >= banda:
        for j in awg:
            if 2 * d2.Rb_canal + 2 * i[5] <= j[2] <= j[1]:
                # print(j[0] + " pode ser usado")
                pass
            else:
                emissores.remove(i)
    else:
        emissores.remove(i)
print(emissores)

for i in d2.recetor:
    if i[5] < banda:
        recetores.remove(i)
print(recetores)

combinacoes = [(x, y) for x in emissores for y in recetores]
print("Combinações")
for i in combinacoes:
    print(i)

# banda de AWG contida na banda do EDFA... AWG limita a banda

canais_binf = [d2.canal5_inf + (i - 5) * d2.awgs[0][1] for i in range(1, 6)]
# print(f"banda inferior: {canais_binf}")
canais_bsup = [d2.canal1_sup - (i - 5) * d2.awgs[0][1] for i in range(1, 6)]
canais_bsup = canais_bsup[::-1]
# print(f"banda superior: {canais_bsup}")
canais_bmed = [d2.canal_medio - 2*d2.awgs[0][1], d2.canal_medio - d2.awgs[0][1], d2.canal_medio,d2.canal_medio + d2.awgs[0][1], d2.canal_medio + 2*d2.awgs[0][1]]
# TODO dudu reve isto... em principio o algoritmo dps deve conseguir meter as bandas médias
count = -2
c=[]
for i in range(1,6):
    c.append(d2.canal_medio+count*d2.awgs[0][1])
    count += 1
print(c)
tab = []

tab.insert(0, ["", "Banda inferior", "Banda inferior","Banda central", "Banda central","Banda superior","Banda superior"])
tab.insert(1, ["Id canal", "𝒗 [THz]", "λ [m]", "𝒗 [THz]", "λ [m]", "𝒗 [THz]", "λ [m]"])

for i in range(2, 7):
    tab.insert(i, [f"{i-1}", f"{canais_binf[i-2]}",f"{d1.c/canais_binf[i-2]}", f"{canais_bmed[i-2]}",f"{d1.c/canais_bmed[i-2]}", f"{canais_bsup[i-2]}",f"{d1.c/canais_bsup[i-2]}"])


print(tabulate(tab, tablefmt="fancy_grid", stralign="center"))

n_juntas = [math.floor(i/2.5) - 1 for i in d1.lengths_section]
print(n_juntas)
