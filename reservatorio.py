class Reservatorio:
    def __init__(self):
        self.capacidade = 10000 # capacidade maxima de agua do reservatorio
        self.volumeAtual = 5000 # volume atual de água do reservatorio
        self.transbordo = 0 # variavel que armazena o que não foi possivel captar
        self.captada = 0
        self.naoDrenada = 0

    def getAguaCaptadaTotal(self):
        return self.captada

    def getAguaTotalPerdida(self):
        return self.transbordo

    def getAguaTotalNaoDrenada(self):
        return self.naoDrenada

    def getVolumeAtual(self):
        return self.volumeAtual

    def isEmpty(self):
        if self.getVolumeAtual() == 0:
            return True
        return False


    def encherResevatorio(self, aguaPluvial):
        if (self.volumeAtual + aguaPluvial) > self.capacidade:
            transbordo = self.volumeAtual + aguaPluvial - self.capacidade
            self.transbordo += transbordo
            self.volumeAtual = self.capacidade
            self.captada += aguaPluvial - transbordo
        else:
            self.volumeAtual += aguaPluvial
            self.captada += aguaPluvial

    def drenarReservatorio(self, drenagem):
        if (self.volumeAtual - drenagem) < 0 or self.volumeAtual == 0:
            self.naoDrenada += drenagem - self.volumeAtual
            self.volumeAtual = 0
        else:
            self.volumeAtual -= drenagem
