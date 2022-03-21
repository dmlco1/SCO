import math
from numpy import vstack, ones
from numpy.linalg import lstsq

penalidadeMax = 1.5  # dB

fatorMeritoMax = math.sqrt(10 ** (penalidadeMax / 5) - 1) / 8

ritmoBinario = 13e9  # bps
lambda0 = 1545.32e-9  # m
c = 2.9979e8  # m/s

# DresMax em s/m = 0.582039 ...
# DresMax em ps/nm = 582.039 ...
DresMax = (fatorMeritoMax * (2 * math.pi) * c) / ((ritmoBinario ** 2) * (lambda0 ** 2))  # s/m

# x = disperção

vals = [
      [(-48, 1530), (-51, 1550)],
      [(-159, 1530), (-171, 1550)],
      [(-320, 1530), (-343, 1550)],
      [(-479, 1530), (-514, 1550)],
      [(-639, 1530), (-685, 1550)],
      [(-959, 1530), (-1028, 1550)],
      [(-1278, 1530), (-1371, 1550)],
      [(-1598, 1530), (-1713, 1550)]
      ]


def line_eq(pontos):
    x_coords, y_coords = zip(*pontos)
    A = vstack([x_coords, ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords, rcond=None)[0]
    # print("Line Solution is y = {m}x + {c}".format(m=m, c=c))
    return m, c


results = []
for i in vals:
    print(i)
    declive, b = line_eq(i)
    x = ((lambda0*10**9)-b)/declive
    results.append(x)
    print(x)
