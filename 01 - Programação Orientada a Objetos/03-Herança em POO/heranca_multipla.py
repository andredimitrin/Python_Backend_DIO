class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}:{', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

class Mamifero(Animal):
    def __init__(self, cor_pelo, **kwargs):
        self.cor_pelo = cor_pelo
        super().__init__(**kwargs)

class Ave(Animal):
    def __init__(self, cor_bico=None, **kwargs):
        self.cor_bico = cor_bico
        super().__init__(**kwargs)

class Gato(Mamifero):
    pass

class Ornitorrinco(Mamifero, Ave):
    def __init__(self, nro_patas, cor_pelo, cor_bico):
        Mamifero.__init__(self, cor_pelo=cor_pelo, nro_patas=nro_patas)
        Ave.__init__(self, cor_bico=cor_bico, nro_patas=nro_patas)

ornitorrinco = Ornitorrinco(4, 'vermelho', 'amarelo')
print(ornitorrinco)

gato = Gato(nro_patas=4, cor_pelo='branco')
print(gato)