from random import random, gauss
from reservatorio import Reservatorio
import math

#função que gera uma variável de Poisson
def randpoi(media):
    k, p = 0, 1
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

dreno_diario = 180  #drenagem em m³ diario
#dreno_diario = 160  #drenagem em³ diario
NEXP = 10000


AguaCaptadaTotal = 0
AguaTotalPerdida = 0
AguaTotalNaoDrenada = 0
VolumeAtual = 0
totalTempoVazio = 0
tempoVazio = 0 # tempo que o reservatorio ficou vazio em semanas

for i in range(NEXP):
    reservatorio = Reservatorio()
    for semana in range(periodo): # simulação do periodo
        diasDeChuva = randpoi(MediaChuvaSemana) # dias que choveu em um periodo
        for dia in range(diasDasemana): # simulação dos dias da semana
            if dia < diasDeChuva: #verificando se nesse dia choveu
                aguaPluvial = gauss(media, desvioP) # quantidade de agua que choveu
                reservatorio.encherResevatorio(aguaPluvial) # enchendo o reservatorio
            reservatorio.drenarReservatorio(dreno_diario) # esvaziando o reservatorio
            if reservatorio.isEmpty(): # verificando se o reservatorio está vazio
                tempoVazio += 1
    AguaCaptadaTotal += reservatorio.getAguaCaptadaTotal()
    AguaTotalPerdida += reservatorio.getAguaTotalPerdida()
    AguaTotalNaoDrenada += reservatorio.getAguaTotalNaoDrenada()
    VolumeAtual += reservatorio.getVolumeAtual()
    del reservatorio

print("Media de água que foi captada em m³ = ", round(AguaCaptadaTotal/NEXP, 2))
print("Media de água que não pode ser captada em m³ = ", round(AguaTotalPerdida/NEXP,2))
print("Media de água que não pode ser drenada em m³ em m³ = ", round(AguaTotalNaoDrenada/NEXP,2))
print("Media do tempo que o reservatório ficou Vazio em dias = ", round(tempoVazio/NEXP,2))
print("Media volume atual do reservatório em m3 = ", round(VolumeAtual/NEXP,2))
