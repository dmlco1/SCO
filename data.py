penalidadeMax = 1.5  # dB

ritmoBinario = 13e9  # bps
#lambda parte 1
lambda1 = 1545.32e-9  # m

#lambda banda inferior
lambda2 = 1531.8855390904445e-09
#lambda banda meio
lambda3 = 1547.3032258064515e-09
#lambda banda superior
lambda4 = 1562.6270523846755e-09
c = 2.9979e8  # m/s

#So = 88 # s/km^3
So = 92 # s/km^3
# lambda0 = 1317e-9 #m
lambda0 = 1310e-9 #m
#interpolado com os casos de -val+val
val_data_sheet = [
      [[(-46, 1530), (-49, 1550)],3],
      [[(-152, 1530), (-163, 1550)],10],
      [[(-304, 1530), (-327, 1550)], 20],
      [[(-455, 1530), (-490, 1550)], 30],
      [[(-607, 1530), (-653, 1550)], 40],
      [[(-911, 1530), (-980, 1550)],60],
      [[(-1214, 1530), (-1307, 1550)],80],
      [[(-1518, 1530), (-1633, 1550)],100]
      ] # valores da datatsheet da draka para interpolar a disperção do dcm

lengths_section = [83, 33, 72, 49, 66, 94] # km
lengths_section_longo = [83, 72, 49, 66, 94] # km
# 1º passo secção 3: 5 -> 6
# 2º passo secção 4: 4 -> 5
chosen_dcms = [6, 3, 6, 5, 5, 7]

chosen_dcms_inf = [6, 3, 6, 5, 5, 7]

chosen_dcms_med = [6, 3, 6, 5, 5, 7]

chosen_dcms_sup = [6, 3, 6, 5, 5, 7]

paths_starting_with_sec_k = [[0,1,2,3,4],
                            [1,2,3,4,5],
                            [2,3,4,5,0],
                            [3,4,5,0,1],
                            [4,5,0,1,2],
                            [5,0,1,2,3,]]
