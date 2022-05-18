import data
# ritmo binario de canal em bits
Rb_canal = 13e9
# ritmo binario total em bits
Rb_total = 65e9

# nome, potencia emissor do bit 1(mW), rext(dB),LB(-3dB)GHz, largura de linha(meia potência)MHz, deriva máxiam de frequenciaGHz
emissor = [['A', 16, 8, 12e9, 10, 4],
           ['B', 13, 9, 10e9, 6, 3],
           ['C', 10, 10, 8e9, 2, 2],
           ['D', 7, 12, 6e9, 8, 3.5],
           ['E', 5, 14, 4e9, 4, 2.5],
           ['F', 3, 16, 2e9, 1, 4.5]]

# nome, eff quantica(%, NEP (pW/Hz^1/2), ordem do filtro butterworth, parametro de sobrecarga(dBm),largura de banda(a -3dB)(GHz)
recetor = [['A', 75, 15, 4, -4, 9],
           ['B', 65, 20, 5, -5, 11],
           ['C', 55, 25, 5, -6, 13],
           ['D', 50, 2, 2, 1, 2],
           ['E', 75, 4, 2, 0, 3],
           ['F', 65, 6, 3, -1, 4],
           ['G', 55, 8, 3, -2, 4.5],
           ['H', 50, 10, 4, -3, 6.5]]
#nome,espaçamento entre canais, banda a -3dB de AWG
#como so temos 5 canais vamos usar o AWG50
awgs=[['AWG50', 50e9, 35e9],
   ['AWG100', 100e9, 75e9]]
#banda inferior (lambda min, freq max)
banda_inf=[1543e-9, data.c/1543e-9]
#canal5 em teras
canal5_inf=194.25e12
#banda superior (lambda max, freq min)
banda_sup=[1545.79e-9, data.c/1545.79e-9]
"""193.90-(espaçamentoCH/2)"""
#canal 5 em teras
canal5_sup=193.95e12