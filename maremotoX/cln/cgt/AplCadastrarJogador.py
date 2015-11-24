from cgd.DAOJogador import DAOJogador

_author__ = 'Hanna e Neimar'


class AplCadastrarJogador():
    @staticmethod
    def cadastrar_jogador(ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        jogadorexiste = jog.consultar_jogador()
        if not jogadorexiste:
            jog.inserir_jogador()
        jog.fechar_banco()
        return not jogadorexiste

    @staticmethod
    def validar_login(ldadosjogador):
        jog = DAOJogador(ldadosjogador)
        if jog.validar_login():
            jog.fechar_banco()
            return True
        else:
            return False
