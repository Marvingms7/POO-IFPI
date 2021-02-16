class Bicicleta:
    # Atributos
    Estado = None
    Cor = None
    Aro = None
    Calibragem_pneu = 0
    Altura_cela = 0
    Ano = None
    Velocidade_atual = 0
    Velocidade_max = 0

    # Métodos
    def parar(self):
        if self.Velocidade_atual == 0:
            self.Estado = 'Parada'
        else:
            self.Estado = 'Em movimento'

    def calibrar_pneu(self, Valor):
        if self.Estado == 'Parada':
            if Valor > 0 and Valor <= 25:
                self.Calibragem_pneu = Valor
                print(f'A calibragem atual do peneu é de {self.Calibragem_pneu} Libras')


    def pedalar(self):
        if self.Velocidade_max >= self.Velocidade_atual:
            self.Velocidade_atual += 1
            if self.Velocidade_atual <= 50:
                print(f'Velocidade atual igual a {self.Velocidade_atual} Km/h')
                if self.Velocidade_atual == 50:
                    print(f'Velocidade maxima de {self.Velocidade_atual} Km/h atingida!')
    def Aumentar_cela(self):
        if self.Estado == 'Parada' and self.Altura_cela >= 1  and self.Altura_cela <= 5:
            self.Altura_cela += 1
            if self.Altura_cela == 6:
                self.Altura_cela = 5
                if self.Altura_cela == 5:
                    print(f'A cela já está na altura maxima!')
            print(f'Altura da cela ajustado para {self.Altura_cela}')
        elif self.Estado == 'Em movimento':
            print(f'A cela não pode ser ajustada com a bicileta em movimento!')
        else:
            print(f'A altura da cela só pode ser ajustada entre 1 e 5!')
    def Diminuir_cela(self):
        if self.Altura_cela >= 1  and self.Altura_cela <= 5:
            self.Altura_cela -= 1
            print(f'Altura da cela ajustado para {self.Altura_cela }')
        if self.Estado == 'Em movimento':
            print(f'A cela não pode ser ajustada com a bicileta em movimento!')
        else:
            print(f'A altura da cela só pode ser ajustada entre 1 e 5!')

Minha_Bike = Bicicleta()
Minha_Bike.Estado = 'Em movimento'
Minha_Bike.Cor = 'Verde Neon'
Minha_Bike.Velocidade_max = 50
Minha_Bike.Velocidade_atual = 45
Minha_Bike.Aro = 26
Minha_Bike.Estado = 'Parada'
Minha_Bike.Altura_cela = 1
Minha_Bike.Aumentar_cela()
Minha_Bike.Aumentar_cela()
Minha_Bike.Aumentar_cela()
Minha_Bike.Diminuir_cela()
Minha_Bike.pedalar()
Minha_Bike.pedalar()
Minha_Bike.pedalar()
Minha_Bike.pedalar()
Minha_Bike.pedalar()
Minha_Bike.Estado = 'Em movimento'
print(f'A bicicleta está {Minha_Bike.Estado}')
Minha_Bike.calibrar_pneu(25)
print(f'A altura da cela é de {Minha_Bike.Altura_cela} CM')
print(f'A cor da bicicleta é {Minha_Bike.Cor}')
print(f'O aro da bicicleta é o de tamanho {Minha_Bike.Aro}')






