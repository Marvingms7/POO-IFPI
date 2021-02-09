class carro:
    Nome = None
    Ano = None
    Cor = None
    Veloc_max = None
    Veloc_atual = 0
    Estado = None

    def ligar(self):
        self.Estado = 'Ligado'
        print(f'O carro está {self.Estado}')
    def desligar(self):
        if self.Estado == 'Ligado':
            self.Estado = 'Desligado'
            print(f'O carro está {self.Estado}')
    def acelerar(self):
        if self.Estado == 'Ligado':
            self.Veloc_atual += 1
            print(f'Velocidade atual {self.Veloc_atual}')


    def frear(self):
        if self.Estado == 'Ligado' and self.Veloc_atual > 0:
            self.Veloc_atual -= 1
            print(f'A velocidade atual foi reduziada pra {self.Veloc_atual}')


Meu_carro = carro()
Meu_carro.Veloc_max = 300
Meu_carro.Veloc_atual = 50
Meu_carro.ligar()
Meu_carro.desligar()
Meu_carro.ligar()
print(f'Velocidade maxima é de {Meu_carro.Veloc_max} Km/h')
Meu_carro.acelerar()
Meu_carro.acelerar()

