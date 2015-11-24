from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class Baiacu(Obstaculo):
    DESLOCAMENTO_X = 9
    DESLOCAMENTO_Y = 0

    def __init__(self):
        super(Baiacu, self).__init__("baiacu", EstiloElementos.posicao_inimigo(), self.DESLOCAMENTO_X,
                                     self.DESLOCAMENTO_Y, TipoMovimento.reto)

    @staticmethod
    def __copy__(self):
        return Baiacu()
