penalidadeMax = 1.5  # dB

ritmoBinario = 13e9  # bps

lambda1 = 1545.32e-9  # m

c = 2.9979e8  # m/s

#So = 88 # s/km^3
So = 92 # s/km^3
# lambda0 = 1317e-9 #m
lambda0 = 1310e-9 #m
#interpolado com os casos de -val+val
val_data_sheet = [
      [(-46, 1530), (-49, 1550)],
      [(-152, 1530), (-163, 1550)],
      [(-304, 1530), (-327, 1550)],
      [(-455, 1530), (-490, 1550)],
      [(-607, 1530), (-653, 1550)],
      [(-911, 1530), (-980, 1550)],
      [(-1214, 1530), (-1307, 1550)],
      [(-1518, 1530), (-1633, 1550)]
      ] # valores da datatsheet da draka para interpolar a disperção do dcm

lengths_worst_case = [83, 33, 72, 49, 66, 94] # km

paths_starting_with_sec_k = [[0,1,2,3,4],
                            [1,2,3,4,5],
                            [2,3,4,5,0],
                            [3,4,5,0,1],
                            [4,5,0,1,2],
                            [5,0,1,2,3,]]
