#Classe:
class carro:
    # Construtor:
    def __init__(self, Ano, Velocidade_maxima, Velocidade_atual , Nitro = 'Sem nitro', Estado = 'Desligado', Nome = 'Sem Nome'):
        self.__Estado = Estado
        self.__Nome = Nome
        self.__Ano = Ano
        self.__Velocidade_maxima = Velocidade_maxima
        self.__Velocidade_atual = Velocidade_atual
        self.__Nitro = Nitro
    def getEstado(self):
        return self.__Estado
    def getNome(self):
        return self.__Nome
    def getAno(self):
        return self.__Ano
    def getVelocidade_maxima(self):
        return self.__Velocidade_maxima
    def getVelocidade_atual(self):
        return self.__Velocidade_atual
    def getNitro(self):
        return self.__Nitro
    # Métodos:
    def getligar_desligar(self,Estado):
        self.__Estado = Estado

    def getmudar_nome(self,Nome):
        self.__Nome = Nome
    def getacelerar(self):
        if self.__Estado == 'Ligado':
            if self.__Velocidade_atual < self.__Velocidade_maxima:
                self.__Velocidade_atual += 1
                print(f'A velocidade atual acelerada agora é de {self.__Velocidade_atual} km/h')
            if self.__Velocidade_atual == self.__Velocidade_maxima:
                print(f'Velocidade maxima de {self.__Velocidade_maxima} km/h atingida!')
    def getfrear(self):
        if self.__Estado == 'Ligado' and self.__Velocidade_atual > 0:
            self.__Velocidade_atual -= 1
            print(f'Velocidade atual reduzida para {self.__Velocidade_atual} km/h')


# Objeto 01
Meu_carro = carro( 2013, 250, 0, Estado='Ligado', Nome='Camaro')
print(f'Nome:{Meu_carro.getNome()}')
print(f'Ano: {Meu_carro.getAno()}')
print(f'Velocidade maxima: {Meu_carro.getVelocidade_maxima()}')
print(f'Estado: {Meu_carro.getEstado()}')
print(f'Status de Nitro: {Meu_carro.getNitro()}')
print(f'Velocidade atual : {Meu_carro.getVelocidade_atual()}')
Meu_carro.getacelerar()
Meu_carro.getfrear()
Meu_carro.getacelerar()
Meu_carro.getacelerar()
Meu_carro.getfrear()
print(f'-=' * 40)

# Objeto 02
Meu_carro = carro(2019, 300, 0, Estado='Ligado', Nitro= 'Nitro Seco x8', Nome= 'Mustang', )
print(f'Nome: {Meu_carro.getNome()}')
print(f'Ano: {Meu_carro.getAno()}')
print(f'Velocidade maxima: {Meu_carro.getVelocidade_maxima()}')
print(f'Estado: {Meu_carro.getEstado()}')
print(f'Status de Nitro: {Meu_carro.getNitro()}')
print(f'Velocidade atual : {Meu_carro.getVelocidade_atual()}')
Meu_carro.getacelerar()
Meu_carro.getacelerar()
Meu_carro.getfrear()

