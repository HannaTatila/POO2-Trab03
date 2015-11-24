import os

import pygame

from ciu.cih.TelaJogo import TelaJogo
from cln.cdp.EntradaUsuario import EntradaUsuario
from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.FlyweightFabrica import FlyweightFabrica
from cln.cgt.AplJogo import AplJogo
from principal.CaminhoRecursos import CaminhoRecursos

_author__ = 'Hanna e Neimar'

class ControladorJogo:
    TAM_FONTE_PONTUACAO = 40
    DESLOCAMENTO_TELA = 5
    POSICAO_TROCA_TELA = -500

    def __init__(self):
        pygame.init()
        self.apljogo = AplJogo()
        self.telajogo = TelaJogo()
        self.imagempersonagem = self.get_imagem("personagem.png")
        self.posicaotela = EstiloElementos.posicao_imagem_fundo()
        self.entradas = EntradaUsuario()
        self.fabricaimagens = FlyweightFabrica()

    @staticmethod
    def get_obstaculo(nomeobstaculo):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens_obstaculos(), nomeobstaculo))

    @staticmethod
    def get_imagem(nomeimagem):
        return pygame.image.load(os.path.join(CaminhoRecursos.caminho_imagens(), nomeimagem))

    @staticmethod
    def get_musica(nomemusica):
        return os.path.join(CaminhoRecursos.caminho_musicas(), nomemusica)

    @staticmethod
    def get_som(nomesom):
        return os.path.join(CaminhoRecursos.caminho_sons(), nomesom)

    def exibir_tela_jogo(self):
        imagem = self.get_imagem("fundojogo.png")
        self.telajogo.exibe_imagem(imagem, self.posicaotela)
        self.anda_tela()

    def anda_tela(self):
        self.posicaotela.eixox -= self.DESLOCAMENTO_TELA
        if self.posicaotela.eixox == self.POSICAO_TROCA_TELA:
            self.posicaotela.eixox = 0

    def exibir_vidas(self):
        for numvida in range(self.apljogo.personagem.vida):
            imagem = self.get_imagem("vida.png")
            self.telajogo.exibe_imagem(imagem, EstiloElementos.get_posicao_vida(numvida))

    def exibir_pontuacao(self, mensagem):
        self.telajogo.exibe_texto(mensagem + str(self.apljogo.pontos), self.TAM_FONTE_PONTUACAO,
                                  EstiloElementos.posicao_pontuacao())

    def exibir_fim_de_jogo(self):
        imagem = self.get_imagem("gameover.png")
        self.telajogo.exibe_imagem(imagem, EstiloElementos.posicao_imagem_fundo())
        self.posicaotela.eixox = 0

    def exibir_mensagem(self, mensagem):
        self.telajogo.exibe_texto(mensagem, self.TAM_FONTE_PONTUACAO, EstiloElementos.posicao_mensagem())

    def atualiza_tela(self):
        self.exibir_tela_jogo()
        self.fabricaimagens.get_flyweight("personagem").desenhar_imagem(self.apljogo.personagem.posicao)
        for obstaculo in self.apljogo.lobstaculos:
            self.fabricaimagens.get_flyweight(obstaculo.nome).desenhar_imagem(obstaculo.posicao)
        self.exibir_pontuacao("Score: ")
        self.exibir_vidas()

    def entrada_jogador(self):
        for event in pygame.event.get():
            self.entradas.reset()
            if event.type == pygame.QUIT:
                self.entradas.quit_pressed = True
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_SPACE):
                    self.entradas.quit_pressed = True
            if (event.type == pygame.KEYDOWN):
                if (event.key == pygame.K_UP):
                    self.apljogo.personagem.diminui_deslocamento()
            if (event.type == pygame.KEYUP):
                if (event.key == pygame.K_UP):
                    self.apljogo.personagem.aumenta_deslocamento()
            pygame.key.set_repeat(1)

    def jogo(self):
        self.apljogo.configuracao()
        continua = True
        while continua:
            self.entrada_jogador()
            self.apljogo.jogar()
            self.atualiza_tela()
            for obstaculo in self.apljogo.lobstaculos:
                imagemobstaculo = self.get_obstaculo(obstaculo.nome + ".png")
                if self.apljogo.verifica_colisao_personagem(self.imagempersonagem, imagemobstaculo, obstaculo):
                    self.apljogo.penaliza_jogador()
                    som = self.get_som("colisao.wav")
                    self.telajogo.exibe_som(som)
            if self.apljogo.fimdejogo:
                self.exibir_fim_de_jogo()
            if self.entradas.quit_pressed:
                exit(0)
        pygame.quit()