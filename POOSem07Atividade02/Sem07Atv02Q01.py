class ContaCorrente:
    def __init__(self, Numero, Saldo):
        self.__Numero = Numero
        self._Saldo = Saldo
    @property
    def Saldo(self):
        return self._Saldo
    @Saldo.getter
    def Saldo(self):
        return self._Saldo

    def creditar(self, valor):
        self._Saldo += valor
        return self._Saldo

    def debitar(self, valor):
        if self._Saldo >= valor:
            self._Saldo -= valor
        return self._Saldo
    def transferir(self, valor, conta):
        if self._Saldo >= valor:
            self._Saldo -= valor
            conta.Saldo += valor
            return self._Saldo

    def __str__(self):
        return f'Numero: {self.__Numero}\nSaldo: {self._Saldo}'

class ContaPoupanca(ContaCorrente):
    def __init__(self,Numero, Saldo, Taxa_juros):
        super().__init__(Numero, Saldo)
        self.Taxa_juros = Taxa_juros

    def Saldo(self):
        return self._Saldo

    def rendejuros(self):
        self._Saldo += self._Saldo * (self.Taxa_juros / 100)
        return self._Saldo

    def __str__(self):
        return super().__str__()+f'\nSaldo atualizado: {self._Saldo}'

class ContaImposto(ContaCorrente):
    def __init__(self, Numero, Saldo, Percentual_imposto):
        super().__init__(Numero, Saldo)
        self.Percentual_imposto = Percentual_imposto
        self._Saldo = Saldo

    def calcularImposto(self):
        self._Saldo -= self._Saldo * (self.Percentual_imposto / 100)
        return self._Saldo

    def __str__(self):
        return super().__str__() + f"\nSaldo Atualizado após o imposto de {self.Percentual_imposto}%: R$ {self._Saldo}"

conta01 = ContaCorrente(1, 300)
conta02 = ContaPoupanca(2, 400, 10)
conta03 = ContaImposto(3, 900, 10)
print(conta01)
conta02.rendejuros()
print(conta02)
conta03.calcularImposto()
print(conta03)

