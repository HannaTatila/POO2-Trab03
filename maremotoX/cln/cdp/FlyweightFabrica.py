from cln.cdp.Sprite import Sprite

_author__ = 'Hanna e Neimar'

class FlyweightFabrica(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(FlyweightFabrica, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.flyweights = list()
        self.flyweights.append(Sprite("personagem.png"))
        self.flyweights.append(Sprite("peixeespada.png"))
        self.flyweights.append(Sprite("baiacu.png"))
        self.flyweights.append(Sprite("peixerapido.png"))
        self.flyweights.append(Sprite("peixeperseguidor.png"))


    def get_flyweight(self, sprite):
        if sprite == "personagem":
            return self.flyweights[0]
        elif sprite == "peixeespada":
            return self.flyweights[1]
        if sprite == "baiacu":
            return self.flyweights[2]
        elif sprite == "peixerapido":
            return self.flyweights[3]
        if sprite == "peixeperseguidor":
            return self.flyweights[4]