import math
from numpy import vstack, ones
from numpy.linalg import lstsq
import data


# dlambda para a nossa frequencia
Dlambda = ((data.So/4) * (data.lambda1 - (data.lambda0**4/data.lambda1**3)))
Dlambda_psnmkm = Dlambda *(1e12/(1e9*1e-3))
print(f"Dlambda {Dlambda}")
print(f"Dlambda_psnmkm {Dlambda_psnmkm}")

#fator de mérito
fatorMeritoMax = math.sqrt(10 ** (data.penalidadeMax / 5) - 1) / 8
print(f"Fator de mérito {fatorMeritoMax}")

#Dres máximo
# DresMax em s/m = 0.582039 ...
# DresMax em ps/nm = 582.039 ...
DresMax = (fatorMeritoMax * (2 * math.pi) * data.c) / ((data.ritmoBinario ** 2) * (data.lambda1 ** 2))  # s/m
print(f"DresMax {DresMax}")

# interpolação
def line_eq(pontos):
    x_coords, y_coords = zip(*pontos)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, rcond=None)[0]
    # print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
    return m, c


def interpolation_values():
    results = []
    for i in data.val_data_sheet:
        # print(i)
        declive, b = line_eq(i)
        x = ((data.lambda1*10**9)-b)/declive
        results.append(x)
    #print(f"dcm{results}")
    return results



# Ddcf dos links (objetivo)
def dcf_obj():
    ddcf_obj = [((DresMax*1000)/len(data.lengths_worst_case))-(Dlambda_psnmkm*l) for l in data.lengths_worst_case]
    # print(DresMax*1000)
    print(f"\nDCF dos links (objetivo) {ddcf_obj}\n")
    return ddcf_obj

# discpersão do DCF escolhido
def escolhido():
    interpolation_data_sheet = interpolation_values()
    escolhido = [interpolation_data_sheet[5], interpolation_data_sheet[4], interpolation_data_sheet[5], interpolation_data_sheet[6], interpolation_data_sheet[6]]
    print(f"DCF escolhido {escolhido}")
    return escolhido

# disperção ssmf
def disp_ssmf():
    disp_ssmf = [Dlambda_psnmkm * l for l in data.lengths_worst_case]
    print(f"Disp SSMF {disp_ssmf}")
    return disp_ssmf

#Dres secção
def dres_sec():
    dres_link = [i+j for i,j in zip(disp_ssmf(), escolhido())]
    print(dres_link)

    total = sum(dres_link)
    print(f"Total Dres {total}")
    return dres_link, total

# substimação
def substimacao():
    substimacao = [i - j for i,j in zip(escolhido(), dcf_obj())]
    print(substimacao)
    return substimacao

def table():

    return [dcf_obj(), escolhido(), disp_ssmf(), dres_sec()[0], substimacao(), dres_sec()[1]]