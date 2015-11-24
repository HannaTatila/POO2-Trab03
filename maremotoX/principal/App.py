from ciu.cci.ControladorJogo import ControladorJogo
from ciu.cci.ControladorMenu import ControladorMenu
from cln.cdp.FlyweightFabrica import FlyweightFabrica
from cln.cdp.Sprite import Sprite

_author__ = 'Hanna e Neimar'

controlador = ControladorMenu(ControladorJogo())
controlador.menu()