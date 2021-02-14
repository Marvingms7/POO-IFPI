class carro:
    nome = None
    ano = None
    cor = None
    veloc_max = None
    veloc_atual = 0
    ligado = False

    def __init__(self, nome, cor, velocidade_maxima, ligado):
        self.nome = nome
        self.cor = cor
        self.veloc_max = velocidade_maxima
        self.ligado = ligado

    def ligar(self):
        ligado = self.ligado
        if self.ligado == True:
            print("ligado")
        else:
            carro.desligar(self, ligado)

    def acelerar(self, velocidade_atual):
        if self.ligado == True and self.nome == "fusca":
            self.velocidade_maxima = 80
            self.velocidade_atual = velocidade_atual
            if self.velocidade_atual > self.velocidade_maxima:
                print(f"A velocidade atual do {self.nome} ultrapassa a permitida do veículo que é {self.velocidade_maxima}.")
                return
            else:
                print(f"A velocidade atual do {self.nome} é {self.velocidade_atual}.")

        elif self.ligado == True and self.nome == "ferrari":
            self.velocidade_maxima = 300
            self.velocidade_atual = velocidade_atual
            if self.velocidade_atual > self.velocidade_maxima:
                print(f"A velocidade atual da {self.nome} ultrapassa a permitida do veículo que é {self.velocidade_maxima}.")
            else:
                print(f"A velocidade atual da {self.nome} é {self.veloc_atual}.")

    def desligar(self, ligado):
        if self.ligado == False:
            print("desligado")

    def parar(self, velocidade_atual):
        if self.veloc_atual:
            print("carro não está em movimento!")



meu_carro1 = carro("fusca","Branca",80, True)
meu_carro1.acelerar(40)
meu_carro1 = carro("fusca","Branca",80, False)
meu_carro1.ligar()
meu_carro1 = carro("fusca","branca",80, True)
meu_carro1.ligar()
meu_carro1.acelerar(100)
meu_carro1 = carro("fusca","Branca",80, False)
meu_carro1.ligar()

meu_carro2 = carro("ferrari","Branca",300, True)
meu_carro2.acelerar(200)
meu_carro2.ligar()
meu_carro2.acelerar(350)
meu_carro2.parar(0)
meu_carro2 = carro("ferrari","branca",300, False)
meu_carro2.ligar()
