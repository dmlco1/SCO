import math
from numpy import vstack, ones
from numpy.linalg import lstsq
import data


# dlambda para a nossa frequencia
Dlambda = ((data.So/4) * (data.lambda4 - (data.lambda0**4/data.lambda4**3)))
Dlambda_psnmkm = Dlambda *(1e12/(1e9*1e-3))
print(f"- Dlambda {Dlambda}")
print(f"- Dlambda_psnmkm {Dlambda_psnmkm}")

#fator de mérito
fatorMeritoMax = math.sqrt(10 ** (data.penalidadeMax / 5) - 1) / 8
print(f"- Fator de mérito {fatorMeritoMax}")

#Dres máximo
# DresMax em s/m = 0.582039 ...
# DresMax em ps/nm = 582.039 ...
DresMax = (fatorMeritoMax * (2 * math.pi) * data.c) / ((data.ritmoBinario ** 2) * (data.lambda4 ** 2))  # s/m
print(f"- DresMax {DresMax}\n")

# interpolação
def line_eq(pontos):
    x_coords, y_coords = zip(*pontos)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, rcond=None)[0]
    # print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
    return m, c


def interpolation_values():
    results1 = []
    results2 = []
    for i in data.val_data_sheet:
        # print(i)
        declive, b = line_eq(i[0])
        x = ((data.lambda4*10**9)-b)/declive
        results1.append(x)
        results2.append(f"DCM-{i[1]}")
    print(f"Dispersoes das DCM para 1545,32nm: {results1}\n")
    return results1,results2



# Ddcf dos links (objetivo)
def dcf_obj():
    ddcf_obj = [((DresMax*1000)/(len(data.lengths_section)-1))-(Dlambda_psnmkm*l) for l in data.lengths_section]
    # print(DresMax*1000)
    #print(f"\nDCF dos links (objetivo): {ddcf_obj}\n")
    return ddcf_obj

# discpersão do DCF escolhido
def escolhido():
    interpolation_data_sheet, names = interpolation_values()
    escolhido= [interpolation_data_sheet[i] for i in data.chosen_dcms]
    escolhido_nome = [names[i] for i in data.chosen_dcms]
    #escolhido = [interpolation_data_sheet[6], interpolation_data_sheet[3], interpolation_data_sheet[5],
    #             interpolation_data_sheet[4], interpolation_data_sheet[5], interpolation_data_sheet[7]]
    #escolhido_nome = [names[6], names[3], names[5], names[4], names[5], names[7]]
    #print(f"DCF escolhido: {escolhido}\n")
    return escolhido, escolhido_nome

# disperção ssmf
def disp_ssmf():
    disp_ssmf = [Dlambda_psnmkm * l for l in data.lengths_section]
    #print(f"Disp SSMF: {disp_ssmf}\n")
    return disp_ssmf

#Dres secção
def dres_sec():
    dres_link = [i+j for i,j in zip(disp_ssmf(), escolhido()[0])]
    #print(dres_link)

    total = sum(dres_link)
    #print(f"Total Dres: {total}\n")
    return dres_link, total

# substimação
def substimacao():
    substimacao = [i - j for i,j in zip(escolhido()[0], dcf_obj())]
    #print(f"Substimacao {substimacao}\n")
    return substimacao

def table():
    return [dcf_obj(), escolhido()[1], escolhido()[0], disp_ssmf(), dres_sec()[0], substimacao(), dres_sec()[1]]

interpolation_values()
