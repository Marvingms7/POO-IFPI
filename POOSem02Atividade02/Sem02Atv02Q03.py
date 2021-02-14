class Celular:
    Nome = None
    Ano = None
    Cor = None
    Peso = None
    Ligado = False

    def __init__(self, Nome, Ano, Cor, Peso, Ligado):
        self.Nome = Nome
        self.Ano = Ano
        self.Cor = Cor
        self.Peso = Peso
        self.Ligado = Ligado
    def ligar(self):
        Ligado = self.Ligado
        if self.Ligado == True:
            print(f'O celular {self.Nome} esta ligado')
        else:
            Celular.desligar(self, Ligado)
    def jogo(self):
        if self.Ligado == True:
            print(f'Atualizando Apps do sistema')
    def desligar(self):
        if self.Ligado == False:
            print(f"O celular {self.Nome} esta desligado.")

Meu_Celular = Celular('Redmi Note 7', 2018, 'Azul','130 Gramas', True)
Meu_Celular.ligar()
Meu_Celular.jogo()
Meu_Celular.desligar()

class Console:
    Nome = None
    Ano = None
    Cor = None
    Peso = None
    Ligado = False

    def __init__(self, Nome, Ano, Cor, Peso, Ligado):
        self.Nome = Nome
        self.Ano = Ano
        self.Cor = Cor
        self.Peso = Peso
        self.Ligado = Ligado
    def ligar(self):
        Ligado = self.Ligado
        if self.Ligado == True:
            print(f'O Console {self.Nome} esta ligado')
        else:
            Console.desligar(self, Ligado)
    def Atualizacao(self):
        if self.Ligado == True:
            print(f'Acionando Atualizações de seus games mais jogados')
    def desligar(self):
        if self.Ligado == False:
            print(f"O Console {self.Nome} esta desligado.")
Meu_Console = Console('Ps4', 2014, 'Preto','1kg', True)
Meu_Console.ligar()
Meu_Console.Atualizacao()
Meu_Console.desligar()





