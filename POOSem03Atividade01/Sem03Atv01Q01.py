#Classe:
class carro:
    # Construtor:
    def __init__(self, Ano, Velocidade_maxima, Velocidade_atual , Nitro = 'Sem nitro', Estado = 'Desligado', Nome = 'Sem Nome'):
        self.Estado = Estado
        self.Nome = Nome
        self.Ano = Ano
        self.Velocidade_maxima = Velocidade_maxima
        self.Velocidade_atual = Velocidade_atual
        self.Nitro = Nitro
    # Métodos:
    def ligar_desligar(self,Estado):
        self.Estado = Estado

    def mudar_nome(self,Nome):
        self.Nome = Nome
    def acelerar(self):
        if self.Estado == 'Ligado':
            if self.Velocidade_atual < self.Velocidade_maxima:
                self.Velocidade_atual += 1
                print(f'A velocidade atual acelerada agora é de {self.Velocidade_atual} km/h')
            if self.Velocidade_atual == self.Velocidade_maxima:
                print(f'Velocidade maxima de {self.Velocidade_maxima} km/h atingida!')
    def frear(self):
        if self.Estado == 'Ligado' and self.Velocidade_atual > 0:
            self.Velocidade_atual -= 1
            print(f'Velocidade atual reduzida para {self.Velocidade_atual} km/h')


# Objeto 01
Meu_carro = carro( 2005, 100, 0, Estado='Ligado', Nome='Golf')
print(f'Nome: {Meu_carro.Nome}')
print(f'Ano: {Meu_carro.Ano}')
print(f'Velocidade maxima: {Meu_carro.Velocidade_maxima}')
print(f'Estado: {Meu_carro.Estado}')
print(f'Status de Nitro: {Meu_carro.Nitro}')
print(f'Velocidade atual : {Meu_carro.Velocidade_atual}')
Meu_carro.acelerar()
Meu_carro.acelerar()
Meu_carro.frear()

# Objeto 02
Meu_carro = carro(2020, 400, 0, Estado='Ligado', Nitro= 'Nitro Seco x8', Nome= 'Koenigsegg', )
print(f'Nome: {Meu_carro.Nome}')
print(f'Ano: {Meu_carro.Ano}')
print(f'Velocidade maxima: {Meu_carro.Velocidade_maxima}')
print(f'Estado: {Meu_carro.Estado}')
print(f'Status de Nitro: {Meu_carro.Nitro}')
print(f'Velocidade atual : {Meu_carro.Velocidade_atual}')
Meu_carro.acelerar()
Meu_carro.acelerar()
Meu_carro.acelerar()
Meu_carro.acelerar()
Meu_carro.frear()











