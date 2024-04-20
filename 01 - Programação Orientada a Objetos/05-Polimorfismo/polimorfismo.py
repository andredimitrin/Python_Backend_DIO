class Passaro:
    def voar(self):
        print('Voando...')       

class Pardal(Passaro):
    def voar(self):
        return super().voar()

class Avestruz(Passaro):
    def voar(self):
        print('Avestruz não pode voar')

# FIXME: exemplo ruim de uso de herança para ganhar o metodo voar
class Aviao(Passaro):
    def voar(self):
        print('Aviao está decolando')

def plano_voo(objeto):
    objeto.voar()
    
plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
