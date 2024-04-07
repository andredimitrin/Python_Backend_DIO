class Bicicleta:
    def __init__(self,cor,modelo,ano,valor,aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        
    def buzinar(self):
        print("Plim Plim")
        
    def parar(self):
        print("Parando bicicleta")
        
    def correr(self):
        print("Vrummmmm")
        
    
    
    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    
    
    
b1 = Bicicleta("Vermelha","Caloi",2020,2000)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.ano,b1.cor,b1.modelo,b1.valor)

b2 = Bicicleta("Preta","Monark",2020,1500)

Bicicleta.buzinar(b2)
print(b2.cor)