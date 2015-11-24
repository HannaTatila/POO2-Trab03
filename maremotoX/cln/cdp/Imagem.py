import os
import pygame
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna e Neimar'


class Imagem:

    def __init__(self, imagem):
        self.nomeimagem = imagem

    def carrega_imagem(self):
        if self.nomeimagem == "personagem.png":
            return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), self.nomeimagem))
        else:
            return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_obstaculos(), self.nomeimagem))

