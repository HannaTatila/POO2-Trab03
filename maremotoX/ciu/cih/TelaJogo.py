import pygame
from pygame.mixer import music, Sound

_author__ = 'Hanna e Neimar'


class TelaJogo:
    def __init__(self):
        self.branco = (255, 255, 255)
        self.preto = (0, 0, 0)
        self.vermelho = (255, 0, 0)
        self.ceu = (192, 217, 217)
        pygame.init()
        self.tamanhotelax = 700
        self.tamanhotelay = 500
        self.tela = pygame.display.set_mode((self.tamanhotelax, self.tamanhotelay))
        pygame.display.set_caption("Mar&moto")

    def exibe_imagem(self, imagem, posicao):
        self.tela.blit(imagem, (posicao.eixox, posicao.eixoy))

    def exibe_texto(self, texto, tamanhofonte, posicao):
        fonte = pygame.font.SysFont("Agency FB", tamanhofonte, False, False)
        text = fonte.render(texto, True, self.branco)
        self.tela.blit(text, (posicao.eixox, posicao.eixoy))

    @staticmethod
    def exibe_musica(musica):
        music.load(musica)
        music.play()

    @staticmethod
    def exibe_som(som):
        som = Sound(som)
        som.play()
