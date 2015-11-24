from ciu.cih.TelaCadastro import TelaCadastro

_author__ = 'Hanna e Neimar'


class TelaLogin(TelaCadastro):
    POSICAO_INICIAL_DADOS = 270

    def __init__(self):
        super(TelaLogin, self).__init__()

    def enviar_dados_jogador(self, ldadosjogador):
        return self.aplcadastrarjogador.validar_login(ldadosjogador)