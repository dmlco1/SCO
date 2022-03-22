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
    # print(results)
    return results

interpolation_data_sheet = interpolation_values()

# Ddcf dos links (objetivo)
ddcf_obj = [(DresMax/len(data.lengths_worst_case))-(Dlambda_psnmkm*l) for l in data.lengths_worst_case]
print(f"\nDCF dos links (objetivo) {ddcf_obj}\n")

# discpersão do DCF escolhido
escolhido = [interpolation_data_sheet[5], interpolation_data_sheet[4], interpolation_data_sheet[5], interpolation_data_sheet[6], interpolation_data_sheet[6]]
print(f"DCF escolhido {escolhido}")


