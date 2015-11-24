from ciu.cih.TelaJogo import TelaJogo
from cln.cdp.Imagem import Imagem

_author__ = 'Hanna e Neimar'

class Sprite():

    def __init__(self, nomeimagem):
        self.imagem = Imagem(nomeimagem)
        self.telajogo = TelaJogo()

    def desenhar_imagem(self, posicao):
        self.telajogo.exibe_imagem(self.imagem.carrega_imagem(), posicao)

