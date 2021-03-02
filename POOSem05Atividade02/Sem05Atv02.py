Fatura = []
class bomba_de_combustivel:
    def __init__(self, Numero, ValorLitro, CapacidadeDaBomba, QuantidadeDeCombustivel, ValorFaturado = 0, QuantidadeVendida = 0, TipoDeCombustivel = 'Gasolina Comum'):
        self.__Numero = Numero
        self.__ValorLitro = ValorLitro
        self.__CapacidadeDaBomba = CapacidadeDaBomba
        self.__QuantidadeDeCombustivel = QuantidadeDeCombustivel
        if self.__QuantidadeDeCombustivel > self.__CapacidadeDaBomba:
            self.__QuantidadeDeCombustivel = self.__CapacidadeDaBomba
        self.__ValorFaturado = ValorFaturado
        self.__QuantidadeVendida = QuantidadeVendida
        self.__TipoDeCombustivel = TipoDeCombustivel

    def abastecerBomba(self, Valor):
        if self.__CapacidadeDaBomba >= self.__QuantidadeDeCombustivel + Valor:
            self.__QuantidadeDeCombustivel += Valor
        else:
            self.__QuantidadeDeCombustivel = self.__CapacidadeDaBomba
        return self.__QuantidadeDeCombustivel

    def abastecerVeiculoPorValor(self, Valor):
        Litro = Valor / self.__ValorLitro
        if self.__QuantidadeDeCombustivel >= Litro:
            self.__QuantidadeVendida += Litro
            self.__ValorFaturado += Valor
            if self.__QuantidadeDeCombustivel >= self.__QuantidadeVendida:
                self.__QuantidadeDeCombustivel -= self.__QuantidadeVendida
        return self.__QuantidadeVendida

    def abastecerVeiculoPorLitro(self, Valor):
        Valor_Litro = Valor * self.__ValorLitro
        if self.__QuantidadeDeCombustivel >= Valor:
            self.__QuantidadeVendida += Valor
            self.__ValorFaturado += Valor_Litro
            Fatura.append(self.__ValorFaturado)
            if self.__QuantidadeDeCombustivel >= self.__QuantidadeVendida:
                self.__QuantidadeDeCombustivel -= Valor
        return self.__QuantidadeVendida
    @property
    def ValorLitro(self):
        return self.__ValorLitro

    @ValorLitro.setter
    def ValorLitro(self, Valor):
        self.__ValorLitro = Valor
        return self.__ValorLitro

    def __str__(self):
        return f'Tipo de Combustivel: {self.__TipoDeCombustivel}\nValor do Litro: {self.__ValorLitro}\nQuantidade de litros: {self.__QuantidadeDeCombustivel:.2f}\nQuantidade de litros vendidos: {self.__QuantidadeVendida:.2f}\nValor total da fatura: {self.__ValorFaturado:.2f}'

Bomba01 = bomba_de_combustivel(Numero=1, ValorLitro=4.5, CapacidadeDaBomba= 5000, QuantidadeDeCombustivel=2000)
Bomba01.abastecerBomba(2999)
Bomba01.abastecerVeiculoPorValor(16)
Bomba01.abastecerVeiculoPorLitro(2)
print(Bomba01)
print(f'#='* 50)
Bomba02 = bomba_de_combustivel(Numero=2, ValorLitro=5, CapacidadeDaBomba= 10000, QuantidadeDeCombustivel=4000, TipoDeCombustivel='Gasolina Aditivada')
Bomba02.abastecerBomba(5000)
Bomba02.abastecerVeiculoPorValor(30)
Bomba02.abastecerVeiculoPorLitro(5)
print(Bomba02)
print(f'#='* 50)
Bomba03 = bomba_de_combustivel(Numero=3, ValorLitro=3, CapacidadeDaBomba= 7000, QuantidadeDeCombustivel=500, TipoDeCombustivel='Etanol')
Bomba03.abastecerBomba(4000)
Bomba03.abastecerVeiculoPorValor(20)
Bomba03.abastecerVeiculoPorLitro(5)
print(Bomba03)
print(f'#='* 50)
Bomba04 = bomba_de_combustivel(Numero=4, ValorLitro=4, CapacidadeDaBomba= 40000, QuantidadeDeCombustivel=22000, TipoDeCombustivel='Diesel')
Bomba04.abastecerBomba(13000)
Bomba04.abastecerVeiculoPorValor(300)
Bomba04.abastecerVeiculoPorLitro(8)
print(Bomba04)
print(f'#='* 50)
print(f'Valor total faturado de todas as bombas {sum(Fatura)}')
