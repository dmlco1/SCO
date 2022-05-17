import math
import data2 as d2

# emissores banda pelo critério de nyquist
banda = d2.Rb_canal/2 * 1.20
print("Banda pelo critério de nyquist: " + str(banda))

ch = d2.Rb_total/d2.Rb_canal
print("número de canais: "+str(ch))

figuras_merito = []
emissores = [ i for i in d2.emissor]
awg = [i for i in d2.awgs]

for i in d2.emissor:
    if i[3] >= banda:
        potencia = 10 * math.log10(i[1])
        rext = 1 / i[2]
        fm = potencia - 10 * math.log10(abs((rext + 1) / (rext - 1)))
        print(i[0] + " " + str(fm))
        for j in awg:
            if 2*d2.Rb_canal+2*i[5]<=j[2]<=j[1]:
                print(j[0] + " pode ser usado")
            else:
                emissores.remove(i)

    else:
        emissores.remove(i)
        
canais_binf = [d2.canal5_inf+(i-5)*d2.awgs[0][1] for i in range(1,6)]
print(f"banda inferior: {canais_binf}")
canais_bsup = [d2.canal5_sup-(i-5)*d2.awgs[0][1] for i in range(1,6)]
print(f"banda superior: {canais_bsup}")