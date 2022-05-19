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
canais_bmed = [d2.canal_medio - 2 * d2.awgs[0][1], d2.canal_medio - d2.awgs[0][1], d2.canal_medio,
               d2.canal_medio + d2.awgs[0][1], d2.canal_medio + 2 * d2.awgs[0][1]]
# TODO dudu reve isto... em principio o algoritmo dps deve conseguir meter as bandas médias
count = -2
c = []
for i in range(1, 6):
    c.append(d2.canal_medio + count * d2.awgs[0][1])
    count += 1
print(c)
tab = []

tab.insert(0, ["", "Banda inferior", "Banda inferior", "Banda central", "Banda central", "Banda superior",
               "Banda superior"])
tab.insert(1, ["Id canal", "𝒗 [THz]", "λ [m]", "𝒗 [THz]", "λ [m]", "𝒗 [THz]", "λ [m]"])

for i in range(2, 7):
    tab.insert(i, [f"{i - 1}", f"{canais_binf[i - 2]}", f"{d1.c / canais_binf[i - 2]}", f"{canais_bmed[i - 2]}",
                   f"{d1.c / canais_bmed[i - 2]}", f"{canais_bsup[i - 2]}", f"{d1.c / canais_bsup[i - 2]}"])

print(tabulate(tab, tablefmt="fancy_grid", stralign="center"))

# TODO mandar mail sobre o -1
n_juntas = [math.ceil(i / 1.5) - 1 for i in d1.lengths_section_longo]
print(n_juntas)
print(sum(d1.lengths_section_longo))

# TODO TABELA DE PERDAS

perdas_passagem = d2.perdas_demux * 2 + d2.perda_os
perdas_drop = d2.perdas_demux + d2.perda_os + d2.a_con
perdas_add = d2.perdas_demux + d2.perda_os + d2.a_con

tab2 = []

tab2.insert(0, ["Modo de Funcionamento", "Perdas Demux", "Perdas de comutadores", "Perdas mux", "Perdas conectores",
                "total"])
tab2.insert(1, ["Passagem", f"{d2.perdas_demux}", f"{d2.perda_os}", f"{d2.perdas_demux}", "--", f"{perdas_passagem}"])
tab2.insert(2, ["Extração", f"{d2.perdas_demux}", f"{d2.perda_os}", "--", f"{d2.a_con}", f"{perdas_drop}"])
tab2.insert(3, ["Inserção", "--", f"{d2.perda_os}", f"{d2.perdas_demux}", f"{d2.a_con}", f"{perdas_add}"])

print(tabulate(tab2, tablefmt="fancy_grid", stralign="center"))

# TODO TABELAS por secçaõ

perdas_totais = d2.alfaL + (5 * d2.n_con * d2.a_con) + sum(
    n_juntas) * d2.a_junt + 2 * d2.dcm80 + 2 * d2.dcm60 + d2.dcm100 + perdas_drop + 4 * perdas_passagem + perdas_add
print(perdas_totais)

tab4 = []
tab4.insert(0, ["Secao [km]", "Ganho Requerido [dB]"])

perdas_totais_sec = []
for i in range(5):
    if i == 0:
        print("add")
        perdas_t = d2.alfa * d1.lengths_section_longo[i] + (d2.n_con * d2.a_con) + n_juntas[i] * d2.a_junt + d2.dcms[
            i] + perdas_drop * 0 + perdas_passagem * 0 + perdas_add
        perdas_totais_sec.append(perdas_t)

    else:
        print("pass")
        perdas_t = d2.alfa * d1.lengths_section_longo[i] + (d2.n_con * d2.a_con) + n_juntas[i] * d2.a_junt + d2.dcms[
            i] + perdas_drop * 0 + perdas_passagem + perdas_add * 0
        perdas_totais_sec.append(perdas_t)
        if i == 4:
            # perdas_t = perdas_drop
            perdas_totais_sec[4] = perdas_totais_sec[4] + perdas_drop
    print("Seccao: " + str(d1.lengths_section_longo[i]) + "; Perdas: " + str(perdas_totais_sec[i]))
    tab4.insert(count, [f"{d1.lengths_section_longo[i]}", f"{perdas_totais_sec[i]}"])



print(tabulate(tab4, tablefmt="fancy_grid", stralign="center"))

print(perdas_totais_sec)
print(sum(perdas_totais_sec))

potencia_emitida = []
sensibilidade = []
margem = []

tab3 = []
tab3.insert(0, ["combinações", "Potencia emitida", "sensibilidade", "Perdas de caminho", "Penalidade", "margem"])
count = 1
for i in combinacoes:
    rext = 10 ** (i[0][2] / 10)
    ps = 10 * math.log10((i[0][1] + i[0][1] / rext) / 2)  # dBm
    potencia_emitida.append(ps)

    pi = 10 * math.log10((rext + 1) / (rext - 1) * d2.Q * i[1][2] * 10 ** -9 * math.sqrt(d2.butval(i[1][3]) * i[1][5]))
    sensibilidade.append(pi)

    print("potencia emitida " + str(ps))
    print("sensibilidade " + str(pi))

    m = ps - pi - d2.pen - perdas_totais
    margem.append(m)
    print(m)
    print("Não é preciso pré" if m >= 3 else "é preciso pré")
    tab3.insert(count, [f"{i[0][0]}-{i[1][0]}", f"{ps}", f"{pi}", f"{perdas_totais}", f"{d2.pen}", f"{m}"])
    count += 1

print(tabulate(tab3, tablefmt="fancy_grid", stralign="center"))
