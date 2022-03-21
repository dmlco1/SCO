import matplotlib.pyplot as plt
import math

ssmfDispertion = []
dcfDispertion = []

with open('DCMs.csv', 'r') as file:
    for line in file:
        if 'Dispersão SSMF' in line:
            newLine = line.replace(',', '.')
            ssmfDispertion = [float(i) for i in newLine.split(';')[1:6]]

        if 'Dispersão DCF Ojetivo' in line:
            newLine = line.replace(',', '.')
            dcfDispertion = [float(i) for i in newLine.split(';')[1:6]]

    x1 = [0, 72, 72, 121, 121, 187, 187, 281, 281, 364, 364]

    step = [0] * 10
    for i in range(10):
        if i == 0:
            print(step[0])
            step[i] = ssmfDispertion[0]
            print(step[i])
        elif i % 2 == 0:
            step[i] = step[i - 1] + ssmfDispertion[math.floor(i / 2)]
            print(step[i])
        elif i % 2 != 0:
            step[i] = step[i - 1] + dcfDispertion[math.floor(i / 2)]
            print(step[i])

    y2 = [0, ssmfDispertion[0], 0, ssmfDispertion[1], 0, ssmfDispertion[2], 0, ssmfDispertion[3], 0, ssmfDispertion[4],
          0]
    step.insert(0, 0)
    # plt.plot(x1, y1, color='red')
    plt.plot(x1, step, color='red', label='Máxima Dispersão Residual')
    plt.plot(x1, y2, color='green', linestyle="--", label='Compensação Perfeita de Dispersão')
    plt.legend(loc='upper left')
    plt.title('Regra da Máxima Dispersão Residual', color='#2362b7')
    plt.ylabel('Dispersão Acumulada [ps/nm]', color='#1e5cac')
    plt.xlabel('Distância ao Emissor [km]', color='#1e5cac')
    plt.show()
