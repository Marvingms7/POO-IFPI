class Criadouro_de_peixe:
    def __init__(self, Numero, ValorPeixe, CapacidadeAtualDePeixe, CapacidadeMaximaDePeixe, CapacidadeAtualEmLitros, CapacidadeMaximaEmLitros, QuantidadeVendida = 0, ValorFaturado = 0, TipoDePeixe = 'Tambaqui'):
     self.__Numero = Numero
     self.__ValorPeixe = ValorPeixe
     self.__CapacidadeAtualDePeixe = CapacidadeAtualDePeixe
     self.__CapacidadeMaximaDepeixe = CapacidadeMaximaDePeixe
     self.__CapacidadeAtualEmLitros = CapacidadeAtualEmLitros
     self.__CapacidadeMaximaEmLitros = CapacidadeMaximaEmLitros
     self.__QuantidadeVendida = QuantidadeVendida
     self.__ValorFaturado = ValorFaturado
     self.__TipoDePeixe = TipoDePeixe

    def colocarPeixe(self, Valor):
        if self.__CapacidadeMaximaDepeixe >= self.__CapacidadeAtualDePeixe + Valor:
            self.__CapacidadeAtualDePeixe += Valor
        else:
            self.__CapacidadeAtualDePeixe = self.__CapacidadeMaximaDepeixe
        return self.__CapacidadeAtualDePeixe

    def retirarPeixe(self, Valor):
        if Valor <= self.__CapacidadeAtualDePeixe:
            self.__CapacidadeAtualDePeixe -= Valor
        return self.__CapacidadeAtualDePeixe

    def Encher(self, Valor):
        if self.__CapacidadeAtualEmLitros + Valor <= self.__CapacidadeMaximaEmLitros:
            self.__CapacidadeAtualEmLitros += Valor
        return self.__CapacidadeAtualEmLitros
    def Esvaziar(self, Valor):
        if self.__CapacidadeAtualEmLitros >= Valor and self.__CapacidadeAtualDePeixe == 0:
            self.__CapacidadeAtualEmLitros -= Valor
        elif self.__CapacidadeAtualEmLitros < Valor and self.__CapacidadeAtualDePeixe == 0:
            self.__CapacidadeAtualEmLitros = 0
        return self.__CapacidadeAtualEmLitros
    def venderPeixe(self, Valor):
        fatura = Valor * self.__ValorPeixe
        if self.__CapacidadeAtualDePeixe >= Valor:
            self.__CapacidadeAtualDePeixe -= Valor
            self.__ValorFaturado += fatura
            self.__QuantidadeVendida += Valor
            return self.__QuantidadeVendida
    @property
    def ValorPeixe(self):
        return self.__ValorPeixe
    @ValorPeixe.setter
    def ValorPeixe(self, Valor):
        self.__ValorPeixe = Valor
        return self.__ValorPeixe
    def __str__(self):
        return f'Capacidade atual de peixes: {self.__CapacidadeAtualDePeixe}\nCapacidade maxima de peixes: {self.__CapacidadeMaximaDepeixe}\nCapacidade atual em litros: {self.__CapacidadeAtualEmLitros}\nCapacidade maxima em litros: {self.__CapacidadeMaximaEmLitros}\nValor peixe: {self.__ValorPeixe}\nQuantidade Vendida: {self.__QuantidadeVendida}\nValor faturado: {self.__ValorFaturado}\nTipo de peixe: {self.__TipoDePeixe}'

Criadouro01 = Criadouro_de_peixe(Numero=1, ValorPeixe=8, CapacidadeAtualDePeixe=3000, CapacidadeMaximaDePeixe=7000, CapacidadeAtualEmLitros=120000, CapacidadeMaximaEmLitros=150000)
Criadouro01.colocarPeixe(5000)
Criadouro01.retirarPeixe(20)
Criadouro01.Encher(20000)
Criadouro01.retirarPeixe(6980)
Criadouro01.Esvaziar(2000)
Criadouro01.colocarPeixe(50)
Criadouro01.venderPeixe(20)
print(Criadouro01)
print(f'#='*50)
Criadouro02 = Criadouro_de_peixe(Numero=2, ValorPeixe=36, CapacidadeAtualDePeixe=50000, CapacidadeMaximaDePeixe=88000, CapacidadeAtualEmLitros=300000, CapacidadeMaximaEmLitros=400000, TipoDePeixe='Salmão')
Criadouro02.colocarPeixe(20000)
Criadouro02.retirarPeixe(20)
Criadouro02.Encher(20000)
Criadouro02.retirarPeixe(3000)
Criadouro02.Esvaziar(2000)
Criadouro02.colocarPeixe(50)
Criadouro02.venderPeixe(20)
print(Criadouro02)
print(f'#='*50)
Criadouro03 = Criadouro_de_peixe(Numero=3, ValorPeixe=60, CapacidadeAtualDePeixe=8000, CapacidadeMaximaDePeixe=25000, CapacidadeAtualEmLitros=190000, CapacidadeMaximaEmLitros=220000, TipoDePeixe='Bacalhau')
Criadouro03.colocarPeixe(9000)
Criadouro03.retirarPeixe(500)
Criadouro03.Encher(20000)
Criadouro03.retirarPeixe(3000)
Criadouro03.Esvaziar(2000)
Criadouro03.colocarPeixe(50)
Criadouro03.venderPeixe(40)
print(Criadouro03)
print(f'#='*50)
Criadouro04 = Criadouro_de_peixe(Numero=4, ValorPeixe=22, CapacidadeAtualDePeixe=3000, CapacidadeMaximaDePeixe=20000, CapacidadeAtualEmLitros=150000, CapacidadeMaximaEmLitros=180000, TipoDePeixe='Tilápia')
Criadouro04.colocarPeixe(4000)
Criadouro04.retirarPeixe(20)
Criadouro04.Encher(20000)
Criadouro04.retirarPeixe(1000)
Criadouro04.Esvaziar(2000)
Criadouro04.colocarPeixe(50)
Criadouro04.venderPeixe(20)
print(Criadouro04)
print(f'#='*50)

