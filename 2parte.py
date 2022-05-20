# import math
import math

from tabulate import tabulate
import data2 as d2
import data as d1
"""===================ESCOLHA DE EMISSORES E RECETORES==================="""
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
# print(emissores)

for i in d2.recetor:
    if i[5] < banda:
        recetores.remove(i)
# print(recetores)

combinacoes = [(x, y) for x in emissores for y in recetores]
# print("Combinações")
# for i in combinacoes:
#   print(i)


""""===================Dimensionamento de canais ==================="""


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
# print(c)
tab = []

tab.insert(0, ["", "Banda inferior", "Banda inferior", "Banda central", "Banda central", "Banda superior",
               "Banda superior"])
tab.insert(1, ["Id canal", "𝒗 [THz]", "λ [m]", "𝒗 [THz]", "λ [m]", "𝒗 [THz]", "λ [m]"])

for i in range(2, 7):
    tab.insert(i, [f"{i - 1}", f"{canais_binf[i - 2]}", f"{d1.c / canais_binf[i - 2]}", f"{canais_bmed[i - 2]}",
                   f"{d1.c / canais_bmed[i - 2]}", f"{canais_bsup[i - 2]}", f"{d1.c / canais_bsup[i - 2]}"])

print(tabulate(tab, tablefmt="fancy_grid", stralign="center"))


"""===================EStudo de pre amp==================="""


n_juntas = [math.ceil(i / 1.5) - 1 for i in d1.lengths_section_longo]
# print(n_juntas)
# print(sum(d1.lengths_section_longo))


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


perdas_totais = d2.alfaL + (5 * d2.n_con * d2.a_con) + sum(
    n_juntas) * d2.a_junt + 2 * d2.dcm80 + 2 * d2.dcm60 + d2.dcm100 + perdas_drop + 4 * perdas_passagem + perdas_add
# print(perdas_totais)

tab4 = []
tab4.insert(0, ["Secao [km]", "Perdas por secção [dB]"])

perdas_totais_sec = []
count = 1
for i in range(5):
    if i == 0:
        # print("add")
        perdas_t = d2.alfa * d1.lengths_section_longo[i] + (d2.n_con * d2.a_con) + n_juntas[i] * d2.a_junt + d2.dcms[
            i]  # + perdas_drop * 0 + perdas_passagem * 0 + perdas_add
        perdas_totais_sec.append(perdas_t)

    else:
        # print("pass")
        perdas_t = d2.alfa * d1.lengths_section_longo[i] + (d2.n_con * d2.a_con) + n_juntas[i] * d2.a_junt + d2.dcms[
            i]  # + perdas_drop * 0 + perdas_passagem + perdas_add * 0
        perdas_totais_sec.append(perdas_t)
        if i == 4:
            # perdas_t = perdas_drop
            perdas_totais_sec[4] = perdas_totais_sec[4]  # + perdas_drop

    # print("Seccao: " + str(d1.lengths_section_longo[i]) + "; Perdas: " + str(perdas_totais_sec[i]))
    tab4.insert(count, [f"{d1.lengths_section_longo[i]}", f"{perdas_totais_sec[i]}"])
    count += 1


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

    # print("potencia emitida " + str(ps))
    # print("sensibilidade " + str(pi))

    m = ps - pi - d2.pen - perdas_totais
    margem.append(m)
    # print(m)
    # print("Não é preciso pré" if m >= 3 else "é preciso pré")
    tab3.insert(count, [f"{i[0][0]}-{i[1][0]}", f"{ps}", f"{pi}", f"{perdas_totais}", f"{d2.pen}", f"{m}"])
    count += 1

print(tabulate(tab3, tablefmt="fancy_grid", stralign="center"))
print(tabulate(tab4, tablefmt="fancy_grid", stralign="center"))

"""===================Estudo de pos amp==================="""

# sec, perdas por secção, perdas de passagem + con, perdas totais, ganho do pos, ganho requirido do pre
tab5 = []
tab5.insert(0, ["secção [km]", "perdas por secção [dB]", "perdas de passagem + con [dB]", "Perdas totais [dB]", "Ganho do pos [dB]", "Ganho requirido ao pre [dB]"])

# pos amps compensam perfeitamente a perda de passagem do roadm (perdas de passagme mais connectores)
# ganho maximo de amplificadores é de 32 dB e um pre-amp que precisa de de 33.9 dB de ganho, logo é preciso 1 amplificador de linha

ganhos_amp=[]
for i in range(5):
    pp_c = perdas_passagem + 2*d2.a_con
    ganhos_amp.append(perdas_totais_sec[i])
    tab5.insert(i+1, [f"{d1.lengths_section_longo[i]}", f"{perdas_totais_sec[i]}", f"{pp_c}", f"{perdas_totais_sec[i]+pp_c}", f"{pp_c}", f"{perdas_totais_sec[i]}"])

print(tabulate(tab5, tablefmt="fancy_grid", stralign="center"))

ganhos_amp[-1] = ganhos_amp[-1]/2
ganhos_amp[0] = ganhos_amp[0]/2
ganhos_amp.insert(1,ganhos_amp[0])
ganhos_amp.append(ganhos_amp[-1])
ganhos_amp.append(perdas_passagem+2*d2.a_con)

"""===================-Estudo de amp linha SEC=94km-==================="""

tab6 = []
tab6.insert(0,["AMP", "Ganho [dB]", "Potencia de ruido ASE (1 polarização) [W]"])
amp = ["sec 83, Pre","Sec 83 linha", "sec 72, Pre", "sec 49, Pre", "sec 66, Pre", "sec 94, Pre", "sec 94, linha", "Pos"]
pase_vec = []
for i in range(8):
    # usar o amplificador oa4500 pois é o amplificador que consegue acomudar estes ganhos
    fn= 10**(d2.oa4500[1]/10)
    g = 10**(ganhos_amp[i]/10)
    v = d1.c/d1.lambda4
    pase = round((fn/2) * (g - 1) * d2.PLANK_CONST * v * d2.awgs[0][2],9)
    pase_vec.append(pase)

    tab6.insert(i+1, [f"{amp[i]}", f"{round(ganhos_amp[i],2)}", f"{pase}"])
tab7 = []
tab7.insert(0 , ["Par", "OSNR [dB]", "OSNR Requerida [dB]", "Valor de penalidade", "Margem"])

comp = [54.864, 28.136, 72, 49, 66, 63, 31]
leff = [d2.leff(i) for i in comp]

def potencia():
    pmax_edfa = (10**(d2.oa4500[2]/10)/ch)*10**-3 # em W
    # print(pmax_edfa)
    lambda_menor = 1.543717816683831e-06
    phi_nl = d2.gamma(lambda_menor) * 1000 * (2 * ch - 1)
    pin = 3/(phi_nl * sum(leff)/1000)
    # print(pin*1000)
    return pin if pin < pmax_edfa else pmax_edfa

for i in range(len(combinacoes)):
    #print(i)
    rext = 10 ** (combinacoes[i][0][2] / 10)
    #print(rext)
    parte1 = ((d2.Q ** 2) * (d2.butval(combinacoes[i][1][3]) * combinacoes[i][1][5])) / (d2.awgs[0][2])
    #print(parte1)
    parterext = ((rext + 1) / (rext - 1))**2
    #print(parterext)
    comboio = 1 + math.sqrt(((4*rext)/((1+rext)**2)) * parterext**-1 * parte1**-1)
    #print(comboio)
    osnr_req = (parte1)*(parterext) * comboio
    #print(osnr_req)

    pn = 2 * sum(pase_vec)

    osnr = potencia()/pn # linear

    tab7.insert(i + 1,
                [f"{combinacoes[i][0][0]}-{combinacoes[i][1][0]}", f"{10 * math.log10(osnr)}", f"{10 * math.log10(osnr_req)}", f"{d2.pen}",
                 f"{10 * math.log10(osnr)-10 * math.log10(osnr_req)-d2.pen}"])



print(tabulate(tab6, tablefmt="fancy_grid", stralign="center"))
print(tabulate(tab7, tablefmt="fancy_grid", stralign="center"))
