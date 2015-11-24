import pygame
from pygame.constants import KEYDOWN, K_RETURN

from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.Posicao import Posicao
from cln.cgt.AplCadastrarJogador import AplCadastrarJogador

_author__ = 'Hanna e Neimar'


class TelaCadastro:
    POSICAO_SUBMIT = Posicao(302, 120)
    COR_PRETO = (0, 0, 0)
    COR_BRANCO = (255, 255, 255)
    TAMANHO_LETRA_MENU = 40
    TAMANHO_LETRA_DADOS = 24
    POSICAOX_LETRA_DADOS = 225
    POSICAO_INICIAL_DADOS = 270
    POSICAOX_OPCAO_MENU = 105
    POSICAOY_INICIAL_OPCAO_MENU = 25
    INCREMENTA_ESPACAMENTO = 40

    def __init__(self):
        self.telamenu = TelaMenu()
        self.aplcadastrarjogador = AplCadastrarJogador()
        self.lopcoes = ["LOGIN:", "SENHA:"]
        self.nomecorrente = []
        self.nome = ""
        self.posicaoimprimenome = self.POSICAO_INICIAL_DADOS

    def exibe_tela_informar_dados(self):
        espacamentovertical = 0
        for id, opcao in enumerate(self.lopcoes):
            self.telamenu.exibe_texto_menu(opcao, self.TAMANHO_LETRA_MENU, self.COR_PRETO,
                                           Posicao(self.POSICAOX_OPCAO_MENU,
                                                   self.POSICAOY_INICIAL_OPCAO_MENU + espacamentovertical))
            pygame.draw.rect(self.telamenu.tela, self.COR_BRANCO, (220, 270 + espacamentovertical, 300, 30), 0)
            espacamentovertical = espacamentovertical + self.INCREMENTA_ESPACAMENTO

        self.telamenu.exibe_texto_menu("CONFIRMAR", self.TAMANHO_LETRA_MENU, self.COR_PRETO, self.POSICAO_SUBMIT)
        pygame.display.flip()

    @staticmethod
    def get_key():
        while 1:
            event = pygame.event.poll()
            if event.type == KEYDOWN:
                return event.key

    def imprime_nome(self):
        tela = self.telamenu.tela
        self.nome = ""
        for i in range(len(self.nomecorrente)):
            self.nome = self.nome + self.nomecorrente[i]

        fonte = pygame.font.SysFont("Arial", self.TAMANHO_LETRA_DADOS, False, False)
        texto = fonte.render(self.nome, True, self.COR_PRETO)
        tela.blit(texto, (self.POSICAOX_LETRA_DADOS, self.posicaoimprimenome))
        pygame.display.flip()

    def enviar_dados_jogador(self, ldadosjogador):
        return self.aplcadastrarjogador.cadastrar_jogador(ldadosjogador)

    def cadastro(self):
        ldadosjogador = []
        while True:
            tecla = self.get_key()
            if tecla == K_RETURN:
                ldadosjogador.append(self.nome)
                self.nome = ""
                self.nomecorrente = []
                if len(ldadosjogador) == len(self.lopcoes):
                    self.posicaoimprimenome = self.POSICAO_INICIAL_DADOS
                    return self.enviar_dados_jogador(ldadosjogador)
                else:
                    self.posicaoimprimenome = self.posicaoimprimenome + self.INCREMENTA_ESPACAMENTO
            elif tecla <= 127:
                self.nomecorrente.append(chr(tecla))
                self.imprime_nome()
