class Cachorro:
    def __init__(self,nome,cor,acordado=True):
        print('Iniciando cachorro')
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print('Destruindo cachorro')


    def falar(self):
        print(f'{self.nome} fala: "Au au"')
        

def criar_cachorro():
    c = Cachorro('Zeus','branca e marrom',False)
    print(c.nome)
        
# c = Cachorro('Chiquinha','branca',False)
# c.falar()

criar_cachorro()