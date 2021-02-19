# Classe:
class televisao:
    # Construtor:
    def __init__(self, Canal = 2, Canal_minimo = 2, Canal_maximo = 99, Volume = 2, Volume_minimo = 0, Volume_maximo = 100,Ligada = False):
        self.Canal = Canal
        self.Canal_minimo = Canal_minimo
        self.Canal_maximo = Canal_maximo
        self.Volume = Volume
        self.Volume_minimo = Volume_minimo
        self.Volume_maximo = Volume_maximo
        self.Ligada = Ligada
    # Métodos
    def ligar(self):
            self.Ligada = True
            self.Volume = self.Volume_minimo
            print(f'A tv está ligada e no Volume {self.Volume_minimo}!')
    def desligar(self):
            self.Ligada = False
            print(f'A tv está Desligada!')
    def aumentar_canal(self, Valor):
        if self.Ligada == True:
            if self.Canal >= self.Canal_minimo and self.Canal <= self.Canal_maximo:
                if self.Canal + Valor < self.Canal_maximo:
                    self.Canal += Valor
                    print(f'Canal aumentado para {self.Canal}')
                else:
                    print(f'A tv possui apenas canais do {self.Canal_minimo} até o canal {self.Canal_maximo}')
    def diminuir_canal(self, Valor):
        if self.Ligada == True:
            if self.Canal >= self.Canal_minimo and self.Canal <= self.Canal_maximo:
                if self.Canal - Valor > self.Canal_minimo:
                    self.Canal -= Valor
                    print(f'Canal diminuido para {self.Canal}')
                else:
                    print(f'A tv possui apenas canais do {self.Canal_minimo} até o canal {self.Canal_maximo}')

    def aumentar_volume(self,Valor):
        if self.Ligada == True:
            if self.Volume >= self.Volume_minimo and self.Volume <= self.Volume_maximo:
                if self.Volume + Valor <= self.Volume_maximo:
                    self.Volume += Valor
                    print(f'O volume foi aumentado para {self.Volume}')
                else:
                    print(f'O volume vai apenas do {self.Volume_minimo} até o {self.Volume_maximo}')
    def diminuir_volume(self, Valor):
        if self.Ligada == True:
            if self.Volume >= self.Volume_minimo and self.Volume <= self.Volume_maximo:
                if self.Volume - Valor >= self.Volume_minimo:
                    self.Volume -= Valor
                    print(f'O volume foi diminuido para {self.Volume}')
                else:
                    print(f'O volume vai apenas do {self.Volume_minimo} até o {self.Volume_maximo}')

# Objeto 01:
tv_da_sala = televisao(Canal=2, Canal_minimo=2, Canal_maximo=99, Volume=2, Volume_minimo=1, Volume_maximo=100, Ligada=True)
tv_da_sala.ligar()
tv_da_sala.desligar()
tv_da_sala.ligar()
tv_da_sala.aumentar_canal(2)
tv_da_sala.aumentar_canal(50)
tv_da_sala.aumentar_canal(50)
tv_da_sala.aumentar_canal(50)
tv_da_sala.diminuir_canal(10)
tv_da_sala.diminuir_canal(60)
tv_da_sala.aumentar_volume(60)
tv_da_sala.aumentar_volume(60)
tv_da_sala.aumentar_volume(30)
tv_da_sala.diminuir_volume(60)

print(f'#' * 50)

# Objeto 02:
tv_do_quarto = televisao(Canal=4, Canal_minimo=4, Canal_maximo=999, Volume=2, Volume_minimo=1, Volume_maximo=100, Ligada=True)
tv_do_quarto.ligar()
tv_do_quarto.desligar()
tv_do_quarto.ligar()
tv_do_quarto.aumentar_canal(2)
tv_do_quarto.aumentar_canal(50)
tv_do_quarto.aumentar_canal(50)
tv_do_quarto.aumentar_canal(50)
tv_do_quarto.diminuir_canal(10)
tv_do_quarto.diminuir_canal(60)
tv_do_quarto.aumentar_volume(12)
tv_do_quarto.aumentar_volume(65)
tv_do_quarto.aumentar_volume(30)
tv_do_quarto.diminuir_volume(42)

