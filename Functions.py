import matplotlib.pyplot as plt
import math

ssmfDispertion = []
dcfDispertion = []
"""
with open('DCMs.csv', 'r') as file:
    for line in file:
        if 'Dispersão SSMF' in line:
            newLine = line.replace(',', '.')
            ssmfArray = newLine.split(';')[1:6]

        if 'Dispersão DCF Ojetivo' in line:
            newLine = line.replace(',', '.')
            dcfArray = newLine.split(';')[1:6]

    for i in ssmfArray:
        ssmfDispertion.append(float(i))
    for i in dcfArray:
        dcfDispertion.append(float(i))
"""
with open('DCMs.csv', 'r') as file:
    for line in file:
        if 'Dispersão SSMF' in line:
            newLine = line.replace(',', '.')
            ssmfDispertion = [float(i) for i in newLine.split(';')[1:6]]

        if 'Dispersão DCF Ojetivo' in line:
            newLine = line.replace(',', '.')
            dcfDispertion = [float(i) for i in newLine.split(';')[1:6]]

    #for i in ssmfArray:
    #    ssmfDispertion.append(float(i))
    #for i in dcfArray:
    #    dcfDispertion.append(float(i))

    x1 = [0, 72, 72, 121, 121, 187, 187, 281, 281, 364, 364]
    """
    step0 = ssmfDispertion[0]
    step1 = ssmfDispertion[0] + dcfDispertion[0]
    step2 = step1 + ssmfDispertion[1]
    step3 = step2 + dcfDispertion[1]
    step4 = step3 + ssmfDispertion[2]
    step5 = step4 + dcfDispertion[2]
    step6 = step5 + ssmfDispertion[3]
    step7 = step6 + dcfDispertion[3]
    step8 = step7 + ssmfDispertion[4]
    step9 = step8 + dcfDispertion[4]
    """

    step = [0]*10
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

    # y1 = [0, step0, step1, step2, step3, step4, step5, step6, step7, step8, step9]

    y2 = [0, ssmfDispertion[0], 0, ssmfDispertion[1], 0, ssmfDispertion[2], 0, ssmfDispertion[3], 0, ssmfDispertion[4],
          0]
    step.insert(0,0)
    #plt.plot(x1, y1, color='red')
    plt.plot(x1, step, color='red', label='Máxima Dispersão Residual')
    plt.plot(x1, y2, color='green',linestyle="--", label='Compensação Perfeita de Dispersão')
    plt.legend(loc="upper left")
    plt.title('Regra da Máxima Dispersão Residual', color='#2362b7')
    plt.ylabel('Dispersão Acumulada [ps/nm]', color='#1e5cac')
    plt.xlabel('Distância ao Emissor [km]', color='#1e5cac')
    plt.show()

'''
x = [0, 72, 72, 121, 121, 187, 187, 281, 281, 364, 364]
y = [0, 1156.32, 160.26, 947.2, 320.52, 1380.48, 480.78, 1990.42, 641.04, 1974.02, 801.3]




plt.plot(x, y, color='#a14442')
plt.title('Regra da Máxima Dispersão Residual', color='#2362b7')
plt.ylabel('Dispersão Acumulada [ps/nm]', color='#1e5cac')
plt.xlabel('Distância ao Emissor [km]', color='#1e5cac')
plt.show()

'''
