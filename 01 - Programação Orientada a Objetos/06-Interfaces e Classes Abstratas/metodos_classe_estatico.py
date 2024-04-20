from datetime import datetime

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_apartir_data_nascimento(cls,ano,mes,dia,nome):
        idade = 2024 - ano
        return cls(nome,idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
        
        
p = Pessoa.criar_apartir_data_nascimento(1990,1,1,'João')
print(p.nome,p.idade)


print(Pessoa.e_maior_idade(17))
print(Pessoa.e_maior_idade(18))