import matplotlib.pyplot as plt
import math
import Math as calcs
import data
from tabulate import tabulate

ssmfDispertion = calcs.disp_ssmf()
dcfDispertion = calcs.dcf_obj()

x1 = [0, 72, 72, 121, 121, 187, 187, 281, 281, 364, 364]

step = [0] * 10
for i in range(10):
    if i == 0:
        #print(step[0])
        step[i] = ssmfDispertion[0]
        #print(step[i])
    elif i % 2 == 0:
        step[i] = step[i - 1] + ssmfDispertion[math.floor(i / 2)]
        #print(step[i])
    elif i % 2 != 0:
        step[i] = step[i - 1] + dcfDispertion[math.floor(i / 2)]
        #print(step[i])

y2 = [0, ssmfDispertion[0], 0, ssmfDispertion[1], 0, ssmfDispertion[2], 0, ssmfDispertion[3], 0, ssmfDispertion[4], 0]
step.insert(0, 0)

tab = calcs.table()

tab.insert(0,["ㅤ","Secção 1 (83km)","Secção 2 (33km)","Secção 3 (72km)", "Secção 4 (49km)" ,"Secção 5 (66km)",
              "Secção 6 (94km)"])

tab[1].insert(0, "Dcf Objetivo")
tab[2].insert(0, "DCM escolhido")
tab[3].insert(0, "Dres DCM escolhido")
tab[4].insert(0, "Disperção SSMF")
tab[5].insert(0, "Dres secção")
tab[6].insert(0, "Substimação DCM")

total = tab.pop(len(tab)-1)

drespath = [0]*6
var = 0
temp = calcs.dres_sec()[0]

for x in data.paths_starting_with_sec_k:
    for i in x:
        drespath[var]= drespath[var] + temp[i]
    var +=1

drespath.insert(0, "Dres max do path a começar na seção k")
tab.append(drespath)
print(tabulate(tab,tablefmt="fancy_grid", stralign="center"))
print(f"Total {total}")


# plt.plot(x1, y1, color='red')
plt.plot(x1, step, color='red', label='Máxima Dispersão Residual')
plt.plot(x1, y2, color='green', linestyle="--", label='Compensação Perfeita de Dispersão')
plt.axhline(y=582.039, color='blue',  linestyle="--", label='Dres máx')
plt.legend(loc='upper left')
plt.title('Regra da Máxima Dispersão Residual', color='#2362b7')
plt.ylabel('Dispersão Acumulada [ps/nm]', color='#1e5cac')
plt.xlabel('Distância ao Emissor [km]', color='#1e5cac')
plt.show()
