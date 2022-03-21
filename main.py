import matplotlib.pyplot as plt

# plot Máxima Dispersão Residual
x = [0, 72, 72, 121, 121, 187, 187, 281, 281, 364, 364]
y = [0, 1156.32, 160.26, 947.2, 320.52, 1380.48, 480.78, 1990.42, 641.04, 1974.02, 801.3]

plt.plot(x, y, color='#a14442')
plt.title('Regra da Máxima Dispersão Residual', color='#2362b7')
plt.ylabel('Dispersão Acumulada [ps/nm]', color='#1e5cac')
plt.xlabel('Distância ao Emissor [km]', color='#1e5cac')
plt.show()