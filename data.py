penalidadeMax = 1.5  # dB

ritmoBinario = 13e9  # bps

lambda1 = 1545.32e-9  # m

c = 2.9979e8  # m/s

So = 88 # s/m^2

lambda0 = 1317e-9 #m

val_data_sheet = [
      [(-48, 1530), (-51, 1550)],
      [(-159, 1530), (-171, 1550)],
      [(-320, 1530), (-343, 1550)],
      [(-479, 1530), (-514, 1550)],
      [(-639, 1530), (-685, 1550)],
      [(-959, 1530), (-1028, 1550)],
      [(-1278, 1530), (-1371, 1550)],
      [(-1598, 1530), (-1713, 1550)]
      ] # valores da datatsheet da draka para interpolar a disperção do dcm

lengths_worst_case = [72, 49, 66, 94, 83] # km