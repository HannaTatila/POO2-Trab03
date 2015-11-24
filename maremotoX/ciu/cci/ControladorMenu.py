import pygame
from pygame import KEYDOWN
from pygame import QUIT, K_DOWN, K_UP, K_RETURN, K_ESCAPE

from ciu.cih.TelaCadastro import TelaCadastro
from ciu.cih.TelaLogin import TelaLogin
from ciu.cih.TelaMenu import TelaMenu
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.Posicao import Posicao
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna e Neimar'


class ControladorMenu():
    POSICAOX_SETA = 245
    POSICAOY_SETA = 260
    POSICAOX_OPCAO_MENU = 302
    POSICAOY_OPCAO_MENU = 30
    DISTANCIA_OPCAO_MENU = 40
    TAMANHO_OPCAO_MENU_PADRAO = 30
    TAMANHO_OPCAO_MENU_SELECAO = 40
    COR_PRETO = (0, 0, 0)
    COR_CINZA = (80, 80, 80)

    def __init__(self, controladorjogo):
        pygame.init()
        self.telamenu = TelaMenu()
        self.caminhoimagem = CaminhoRecursos.caminho_imagens()
        self.controladorjogo = controladorjogo
        self.telacadastro  = TelaCadastro()
        self.telalogin = TelaLogin()
        self.lopcoes = ["INICIAR", "CADASTRAR", "CONFIGURACOES", "SAIR"]
        self.mensagemsucesso = "Jogador cadastrado com sucesso!"
        self.mensagemerro = "Login informado ja existe!"
        self.mensagemdadoinvalido = "Os dados informados nao sao validos!"

    def exibir_tela_menu(self):
        self.telamenu.exibe_imagem(self.caminhoimagem, "fundomenu.jpg", EstiloElementos.posicao_imagem_fundo())
        self.telamenu.exibe_imagem(self.caminhoimagem, "titulojogo.png", EstiloElementos.posicao_titulo_jogo())

    def exibir_musica(self):
        self.telamenu.exibe_musica(CaminhoRecursos.caminho_musicas(), "music1.mp3")

    def exibe_opcoes_menu(self, menuselecao):
        alteraposicao = 0
        for id, opcao in enumerate(self.lopcoes):
            tam = self.TAMANHO_OPCAO_MENU_PADRAO
            cor = self.COR_CINZA
            if id + 1 == menuselecao:
                tam = self.TAMANHO_OPCAO_MENU_SELECAO
                cor = self.COR_PRETO
            self.telamenu.exibe_texto_menu(opcao, tam, cor,
                                           Posicao(self.POSICAOX_OPCAO_MENU, self.POSICAOY_OPCAO_MENU + alteraposicao))
            alteraposicao = alteraposicao + self.DISTANCIA_OPCAO_MENU

    def exibe_tela_mensagem_cadastro(self, mensagem):
        self.manipula_seta(2)
        self.telamenu.exibe_mensagem_cadastro(mensagem, EstiloElementos.posicao_mensagem_cadastro())
        self.telamenu.exibe_texto_menu("VOLTAR", self.TAMANHO_OPCAO_MENU_SELECAO, self.COR_PRETO,
                                       Posicao(self.POSICAOX_OPCAO_MENU, 70))
        pygame.display.flip()


    def manipula_seta(self, menuselecao):
        if (menuselecao >= 1) & (menuselecao <= len(self.lopcoes)):
            self.telamenu.exibe_imagem(self.caminhoimagem, "seta.gif",
                                       Posicao(self.POSICAOX_SETA, self.POSICAOY_SETA + 40 * (menuselecao - 1)))

    def menu_selecao(self, menuselecao):
        ## TELA MENU PRINCIPAL
        if (menuselecao >= 1) & (menuselecao <= len(self.lopcoes)):
            self.exibe_opcoes_menu(menuselecao)

        ## REGRAS DA TELA MENU PRINCIPAL:
        elif (menuselecao < 1) | (menuselecao == 113) | (menuselecao == 213) | (menuselecao == 216):
            menuselecao = 1  # nao incrementar estado se apertar p cima de novo
        elif menuselecao == len(self.lopcoes) + 1:
            menuselecao = len(self.lopcoes)  # nao incrementar estado se apertar p baixo de novo

        elif (menuselecao == 11) | (menuselecao == 99) | (menuselecao == 101):
            menuselecao = 100  # se der enter na opcao 'INICIAR'
        elif (menuselecao == 12) | (menuselecao == 199) | (menuselecao == 201):
            menuselecao = 200  # se der enter na opcao 'CADASTRAR'
        elif menuselecao == 13:
            menuselecao = 3  # PARA, POR ENQUANTO, NAO FUNCIONAR NADA EM CONFIGURACOES
        elif menuselecao == 14:
            exit()  # se der enter na opcao 'SAIR'

        ## TELA LOGIN
        elif menuselecao == 100:
            self.telalogin.exibe_tela_informar_dados()
            if self.telalogin.cadastro():
                self.controladorjogo.jogo()
            else:
                menuselecao = 103
                self.exibe_tela_mensagem_cadastro(self.mensagemdadoinvalido)

        ## REGRAS DA TELA LOGIN
        elif menuselecao == 103:
            self.exibe_tela_mensagem_cadastro(self.mensagemdadoinvalido)
        elif (menuselecao == 102) | (menuselecao == 104):
            menuselecao = 103

        ## TELA CADASTRO
        elif menuselecao == 200:
            self.telacadastro.exibe_tela_informar_dados()
            if self.telacadastro.cadastro():
                menuselecao = 203
                self.exibe_tela_mensagem_cadastro(self.mensagemsucesso)
            else:
                menuselecao = 206
                self.exibe_tela_mensagem_cadastro(self.mensagemerro)
        elif menuselecao == 203:
            self.exibe_tela_mensagem_cadastro(self.mensagemsucesso)
        elif menuselecao == 206:
            self.exibe_tela_mensagem_cadastro(self.mensagemerro)

        ## REGRAS DA TELA CADASTRO
        elif (menuselecao == 202) | (menuselecao == 204):
            menuselecao = 203
        elif (menuselecao == 205) | (menuselecao == 207):
            menuselecao = 206

        return menuselecao


    def menu(self):
        menuselecao = 1
        # self.exibir_musica()
        while True:
            self.exibir_tela_menu()
            self.manipula_seta(menuselecao)
            menuselecao = self.menu_selecao(menuselecao)
            pygame.display.update()
            pygame.display.flip()
            for e in pygame.event.get():
                if e.type == QUIT:
                    exit()
                if e.type == KEYDOWN:
                    if e.key == K_DOWN:
                        menuselecao += 1
                    elif e.key == K_UP:
                        menuselecao -= 1
                    elif e.key == K_RETURN:
                        menuselecao += 10
                    elif e.key == K_ESCAPE:
                        menuselecao -= 10