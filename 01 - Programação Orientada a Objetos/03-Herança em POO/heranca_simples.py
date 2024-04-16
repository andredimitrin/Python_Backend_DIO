class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas
        
    def ligar_motor(self):
        print('Ligando o motor')

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado
        
    def esta_carrregado(self):     
        print(f"{'Sim' if self.carregado else 'Não'} está carregado")

# moto = Motocicleta('Branca', 'ABC1234', 2)
# moto.ligar_motor()

# carro = Carro('Vermelho', 'DEF5678', 4)
# carro.ligar_motor()
# carro.esta_carrregado()

caminhao = Caminhao('Prata', 'GHI9012', 8, True) 
caminhao.ligar_motor()
caminhao.esta_carrregado()
