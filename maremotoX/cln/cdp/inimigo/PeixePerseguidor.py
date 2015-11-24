from cln.cdp.EstiloElementos import EstiloElementos
from cln.cdp.inimigo.Obstaculo import Obstaculo
from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class PeixePerseguidor(Obstaculo):
    DESLOCAMENTO_X = 9
    DESLOCAMENTO_Y = 4

    def __init__(self):
        super(PeixePerseguidor, self).__init__("peixeperseguidor", EstiloElementos.posicao_inimigo(),
                                               self.DESLOCAMENTO_X, self.DESLOCAMENTO_Y, TipoMovimento.reto)

    @staticmethod
    def __copy__(self):
        return PeixePerseguidor()
