from random import random, gauss
from reservatorio import Reservatorio
import math

#função que gera uma variável de Poisson
def randpoi(media):
    k, p = 0, 1
    elam = math.exp(-media)
    while (True):
        k += 1
        p = p * random()
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

#variaveis que vão receber o total
AguaCaptadaTotal = 0
AguaTotalPerdida = 0
AguaTotalNaoDrenada = 0
VolumeAtual = 0
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

print(f"Media de água que foi captada = {round(AguaCaptadaTotal/NEXP, 2)} m³")
print(f"Media de água que não pode ser captada = {round(AguaTotalPerdida/NEXP, 2)} m³")
print(f"Media de água que não pode ser drenada = {round(AguaTotalNaoDrenada/NEXP,2)} m³")
print(f"Media do tempo que o reservatório ficou Vazio = {round(tempoVazio/NEXP,2)} dias")
print(f"Media volume atual do reservatório = {round(VolumeAtual/NEXP,2)} m3")
