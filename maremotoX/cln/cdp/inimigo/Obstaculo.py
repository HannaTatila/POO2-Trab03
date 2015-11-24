from cln.cdp.tipo.TipoMovimento import TipoMovimento

_author__ = 'Hanna e Neimar'


class Obstaculo:
    def __init__(self, nome, posicao, deslocamentox, deslocamentoy, tipomovimento):
        self.nome = nome
        self.posicao = posicao
        self.tipomovimento = tipomovimento
        self.deslocamentox = deslocamentox
        self.deslocamentoy = deslocamentoy
        self.ehtangivel = True

    def movimenta(self, limitesuperior, limiteinferior):
        self.movimenta_horizontalmente()
        self.altera_movimento_vertical(limitesuperior, limiteinferior)
        self.movimenta_verticalmente()

    def altera_movimento_vertical(self, limitesuperior, limiteinferior):
        if self.posicao.eixoy < limiteinferior:
            self.tipomovimento = TipoMovimento.subindo
        elif self.posicao.eixoy > limitesuperior:
            self.tipomovimento = TipoMovimento.descendo

    def movimenta_horizontalmente(self):
        self.posicao.eixox -= self.deslocamentox

    def movimenta_verticalmente(self):
        if self.tipomovimento == TipoMovimento.subindo:
            self.sobe()
        elif self.tipomovimento == TipoMovimento.descendo:
            self.desce()

    def sobe(self):
        self.posicao.eixoy += self.deslocamentoy

    def desce(self):
        self.posicao.eixoy -= self.deslocamentoy

    def torna_intangivel(self):
        self.ehtangivel = False