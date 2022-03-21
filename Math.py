import math

penalidadeMax = 1.5

fatorMeritoMax = math.sqrt(10 ** (penalidadeMax / 5) - 1) / 8

ritmoBinario = 13e9
lambda0 = 1545.32e-9
c = 2.9979e8

# DresMax em s/m = 0.582039 ...
# DresMax em ps/nm = 582.039 ...
dResMax = (fatorMeritoMax * (2 * math.pi) * c) / ((ritmoBinario ** 2) * (lambda0 ** 2))


