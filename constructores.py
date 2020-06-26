from fabricas import FabricaSpritesJugador_uno, FabricaSpritesJugador_dos
from Factories import MegamanSpritesFactory
from jugador import Jugador
from Jugador_Adapter import Jugador_adapter

class Director():
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder
    
    def getJugador(self,idf):
        if idf == "c":
            self.jugador = Jugador()
            
        elif idf == "n":
            self.jugador = Jugador_adapter()
            
        self.jugador.set_sprites(self.__builder.get_sprites())
        return self.jugador

class Constructor():
    def get_sprites(self): pass

class ConstructorJugador_uno(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesJugador_uno()


    def get_sprites(self):
        return [self.fabrica.crear_vistafre(),
                self.fabrica.crear_vistaatras(),
                self.fabrica.crear_vistaiz(),
                self.fabrica.crear_vistade()] 

class ConstructorJugador_dos(Constructor):
    def __init__(self):
        self.fabrica = FabricaSpritesJugador_dos()


    def get_sprites(self):
        return [self.fabrica.crear_vistafre(),
                self.fabrica.crear_vistaatras(),
                self.fabrica.crear_vistaiz(),
                self.fabrica.crear_vistade()] 

class ConstructorJugador_nuevo(Constructor):
    def __init__(self):
        self.fabrica = MegamanSpritesFactory()

    def get_sprites(self):
        return [self.fabrica.moveLeft(),
                self.fabrica.moveRight(),
                self.fabrica.moveUp(),
                self.fabrica.moveDown(),
                self.fabrica.power()]