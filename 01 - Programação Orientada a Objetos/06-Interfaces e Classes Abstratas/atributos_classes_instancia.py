class Estudante:
    escola = 'DIO'
    
    def __init__(self,nome,matricula) -> None:
        self.nome = nome 
        self.matricula = matricula
    
    def __str__(self) -> str:
        return f'Nome: {self.nome} | Matricula: {self.matricula} | Escola: {self.escola}'
    
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
    
aluno_1 = Estudante('João',1)
aluno_2 =Estudante('Maria',2)
mostrar_valores(aluno_1,aluno_2)


Estudante.escola = 'Python DIO'
aluno_3 = Estudante('Pedro',3)
mostrar_valores(aluno_1,aluno_2,aluno_3)