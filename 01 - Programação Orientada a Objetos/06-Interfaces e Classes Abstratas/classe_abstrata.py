from abc import ABC, abstractmethod, abstractproperty

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando o controle')
        print('Ligado!')

    def desligar(self):
        print('Desligando o controle')
        print('Desligado!')
    @property
    def marca(self):
        return 'LG'

class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando o Ar Condicionado')
        print('Ligado!')

    def desligar(self): 
        print('Desligando o Ar Condicionado')
        print('Desligado!')
    @property 
    def marca(self):
        return 'Samsung'


controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()