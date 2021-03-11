class Funcionario:
    def __init__(self, nome, cpf, salarioBase):
        self.__nome = nome
        self.__cpf = cpf
        self._salariobase = salarioBase
    @property
    def nome(self):
        return self.__nome

    def getSalarioMensal(self):
        return self._salariobase

    def reajustaSalario(self, percentual):
        self._salariobase += (self._salariobase * percentual) / 100
        return self._salariobase
    def __str__(self):
        return f'nome:{self.__nome}\ncpf:{self.__cpf}\nsalario base:{self._salariobase}'

class Vendedor(Funcionario):
    def __init__(self, nome, cpf, salarioBase, valor_vendas_mes):
        super().__init__(nome, cpf, salarioBase)
        self._valor_vendas_mes = valor_vendas_mes

    def getSalarioMensal(self):
        return self._salariobase + self._valor_vendas_mes * 0.1


    def reajustaSalario(self, percentual):
        self._salariobase += self._salariobase * (percentual / 100)
        return self._salariobase

class Vigilante(Funcionario):
    def __init__(self, nome, cpf, salarioBase, valor_adicional_noturno = 0, numero_de_noites_trabalhada = 0):
        super().__init__(nome, cpf, salarioBase, )
        self._valor_adicional_noturno = valor_adicional_noturno
        self._numero_de_noites_trabalhada = numero_de_noites_trabalhada

    def getSalarioMensal(self):
        return self._salariobase + (self._valor_adicional_noturno * self._numero_de_noites_trabalhada)

    def reajustaSalario(self, percentual):
        self._salariobase += (self._salariobase * percentual) / 100
        self._valor_adicional_noturno += (self._valor_adicional_noturno * percentual) / 100
        return  self._salariobase




