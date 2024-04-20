from datetime import datetime

class Pessoa:
    def __init__(self,nome,ano_nascimento):
        self.nome = nome
        self.ano_nascimento = ano_nascimento
    
    @property
    def idade(self):
        _ano_atual = datetime.now().year
        return _ano_atual - self.ano_nascimento  

pessoa = Pessoa('João', 1990)
print(f'Nome: {pessoa.nome}, Idade: {pessoa.idade}')
