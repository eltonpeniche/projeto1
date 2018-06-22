from random import random, gauss
from reservatorio import Reservatorio
import math

#função que gera uma variável de Poisson
def randpoi(media):
    k = 0
    p = 1
    elam = math.exp(-media)
    while (True):
        k += 1
        r = random()
        p = p * r
        if (p < elam):
            return k - 1


periodo = 50  # em semanas
diasDasemana = 7
MediaChuvaSemana = 2 # media de chuva por semana seguindo uma distribuição de poisson

media = 600  # media
desvioP = 100  # desvio padrão

aguaPluvial = 0

drenagem = 180  #drenagem em m³ diario
#drenagem = 160  #drenagem em³ diario
NEXP = 10000


AguaCaptadaTotal = 0
AguaTotalPerdida = 0
AguaTotalNaoDrenada = 0
VolumeAtual = 0
totalTempoVazio = 0
tempoVazio = 0 # tempo que o reservatorio ficou vazio em semanas

for i in range(NEXP):
    reservatorio = Reservatorio()
    for semana in range(periodo):
        diasDeChuva = randpoi(MediaChuvaSemana) # dias que choveu em um periodo
        for dia in range(diasDasemana):
            if dia < diasDeChuva:
                aguaPluvial = gauss(media, desvioP)
                reservatorio.encherResevatorio(aguaPluvial)
            reservatorio.drenarReservatorio(drenagem)
            if reservatorio.isEmpty():
                tempoVazio += 1
    AguaCaptadaTotal += reservatorio.getAguaCaptadaTotal()
    AguaTotalPerdida += reservatorio.getAguaTotalPerdida()
    AguaTotalNaoDrenada += reservatorio.getAguaTotalNaoDrenada()
    VolumeAtual += reservatorio.getVolumeAtual()
    del reservatorio

print("media Agua total captada = ", round(AguaCaptadaTotal/NEXP, 2))
print("media Total perdido ", round(AguaTotalPerdida/NEXP,2))
print("media Não pode ser drenada", round(AguaTotalNaoDrenada/NEXP,2))
print("media tempo Vazio em dias = ", round(tempoVazio/NEXP,2))
print("media volume atual" , round(VolumeAtual/NEXP,2))
