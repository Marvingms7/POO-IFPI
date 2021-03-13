class Cliente:
    def __init__(self, cpf, nome, idade):
        self.__cpf = cpf
        self.__nome = nome
        self.__idade = idade
    @property
    def cpf(self):
        return self.__cpf
    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade


    def __str__(self):
        return f'cpf: {self.__cpf}\nnome: {self.__nome}\nidade: {self.__idade}'

class Seguro:
    def __init__(self, num_apolice, proprietario):
        self._num_apolice = num_apolice
        if type(proprietario) == Cliente:
            self._proprietario = proprietario
        else:
            self._proprietario = None
    def __str__(self):
        pass

    def calcularValor(self):
        pass
    def calcularPremio(self):
        pass

class SeguroVida(Seguro):
    def __init__(self, num_apolice, proprietario, nome_beneficiario):
        super().__init__(num_apolice, proprietario)
        self.__nome_beneficiario = nome_beneficiario
    def nome_beneficiario(self):
        return self.__nome_beneficiario

    def calcularValor(self):
        valor = 0
        if self._proprietario.idade <= 30:
            valor = 800
        elif self._proprietario.idade >= 31 and self._proprietario.idade <= 50:
            valor = 1300
        elif self._proprietario.idade > 50:
            valor = 1600
        return valor
    def calcularPremio(self):
        valor = 0
        if self._proprietario.idade <= 30:
            valor = 50000
        elif self._proprietario.idade >= 31 and self._proprietario.idade <= 50:
            valor = 30000
        elif self._proprietario.idade > 50:
            valor = 20000
        return valor

    def __str__(self):
        return f'numero apolice: {self._num_apolice}\nproprietario: {self._proprietario.nome}\nnome beneficiario: {self.__nome_beneficiario.nome}\nvalor: {self.calcularValor()}\npremio:{self.calcularPremio()}'

class SeguroAutomovel(Seguro):
    def __init__(self, num_apolice, proprietario, numero_licenca, nome_modelo, ano, valorAutomovel):
        super().__init__(num_apolice, proprietario)
        self.__numero_licenca = numero_licenca
        self.__nome_modelo = nome_modelo
        self.__ano = ano
        self.__valorAutomovel = valorAutomovel
    @property
    def numero_lecenca(self):
        return  self.__numero_licenca
    @property
    def nome_modelo(self):
        return self.__nome_modelo
    @property
    def ano(self):
        return self.__ano
    @property
    def valorAutomovel(self):
        return self.__valorAutomovel

    def calcularValor(self):
        valorSeguro = self.__valorAutomovel * 0.03
        return valorSeguro

    def calcularPremio(self):
        premio = self.__valorAutomovel * 0.8
        return premio

    def calcularFranquia(self):
        franquia = (self.__valorAutomovel * 0.03)* 0.4
        return franquia

    def __str__(self):
        return f'numero apolice: {self._num_apolice}\nnome do segurado: {self._proprietario.nome}\nvalor: {self.calcularValor():.0f}\npremio: {self.calcularPremio():.0f}\nfranquia: {self.calcularFranquia():.0f}'




