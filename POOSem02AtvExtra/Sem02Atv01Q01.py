class Radio:
    Estado = None
    Peso = None
    Cor = None
    Modo = None
    Estacao = None
    Volume = 0
    def Ligar(self):
        self.Estado = "Ligado"
        print(f'O radio está {self.Estado}')
    def Desligar(self):
        if self.Estado == "Ligado":
            self.Estado = "Desligado"
            print(f'O radio está {self.Estado}')
    def Bluetoofh(self):
        if self.Estado == 'Ligado':
            self.Modo = 'Bluetoofh'
            print(f'O radio esta no {self.Modo}')
    def estacaoFM(self):
        if self.Estado == 'Ligado':
            self.Estacao = 'FM'
            print(f'o radio está na Estação {self.Estacao}')
    def estacaoAM(self):
        if self.Estado == 'Ligado':
            self.Estacao = 'AM'
            print(f'o radio está na Estação {self.Estacao}')
    def volume(self, valor):
        if self.Estado == 'Ligado':
            self.Volume = valor
            print(f'o volume esta no {self.Volume}')
    def aumentar_volume(self):
        if self.Estado == 'Ligado':
            if self.Volume <= 31:
                self.Volume += 1
                print(f'O volume atual é {self.Volume}')
                if self.Volume == 32:
                    print(f'Volume maximo atingido!')



Meu_radio = Radio()
Meu_radio.Ligar()
Meu_radio.Cor = 'Azul'
Meu_radio.Peso = '2Kg'
Meu_radio.Desligar()
Meu_radio.Ligar()
Meu_radio.Bluetoofh()
Meu_radio.estacaoFM()
Meu_radio.estacaoAM()
Meu_radio.volume(29)
Meu_radio.aumentar_volume()
Meu_radio.aumentar_volume()
Meu_radio.aumentar_volume()
print(f'Cor:{Meu_radio.Cor}')
print(f'Peso:{Meu_radio.Peso}')



