#ritmo binario de canal em bits
R_b_canal = 13e9

# nome, potencia emissor do bit 1(mW), rext(dB),LB(-3dB)GHz, largura de linha(meia potência)MHz, deriva máxiam de frequenciaGHz
emissor=[['A',16,8,12,10,4],
        ['B',13,9,10,6,3],
        ['C',10,10,8,2,2],
        ['D',7,12,6,8,3.5],
        ['E',5,14,4,4,2.5],
        ['F',3,16,2,1,4.5]]
#nome, eff quantica(%, NEP (pW/Hz^1/2), ordem do filtro butterworth, parametro de sobrecarga(dBm),largura de banda(a -3dB)(GHz)
recetor=[['A', 75,15,4,-4,9],
        ['B', 65,20,5,-5,11],
        ['C', 55,25,5,-6,13],
        ['D', 50,2,2,1,2],
        ['E', 75,4,2,0,3],
        ['F', 65,6,3,-1,4],
        ['G', 55,8, 3,-2,4.5],
        ['H', 50,10, 4,-3,6.5]]