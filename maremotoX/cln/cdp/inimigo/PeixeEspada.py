from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixeEspada(Obstaculo):
    DESLOCAMENTO_X = 9
    DESLOCAMENTO_Y = 7

    def __init__(self):
        super(PeixeEspada, self).__init__("peixeespada", EstiloElementos.posicao_inimigo(), self.DESLOCAMENTO_X,
                                          self.DESLOCAMENTO_Y, TipoMovimento.subindo)

    @staticmethod
    def __copy__(self):
        return PeixeEspada()
