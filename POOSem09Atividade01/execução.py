from Sem09Atv01Q01 import *


class ControledeSeguros:
    def __init__(self, total_valores=0, total_premio=0):
        self._total_valores = total_valores
        self._total_premio = total_premio
        self._seguros = []

    def adicionarSeguros(self, seguro):
        self._seguros.append(seguro)
        print(f'Seguro cadastrado com sucesso!')

    def relatorio(self):
        self._total_valores = 0
        sa = sv = 0
        for i in self._seguros:
            self._total_valores += i.calcularValor()
            self._total_premio += i.calcularPremio()
            if type(i) is SeguroAutomovel:
                sa += 1
            else:
                sv += 1
            print(i)
            print()
        print(f"Seguro de Automóveis (Qtd): {sa}\nSeguro de Vida (Qtd): {sv}")

    @property
    def total_valores(self):
        return self._total_valores
    @property
    def total_premio(self):
        return self._total_premio


controle = ControledeSeguros()
Marcus = Cliente(111111,'Marcus',20)
Jose = Cliente(222222,'Jose', 35)
Ricardo = Cliente(333333,'Ricardo', 54)
controle.adicionarSeguros(SeguroVida(1,Marcus, Jose))
controle.adicionarSeguros(SeguroAutomovel(1, Jose, 10, 'Camaro', 2020, 450000))
controle.relatorio()
print(f"O Total dos Valores: R$ {controle._total_valores:.2f}")
print(f"O Total dos Premios: R$ {controle._total_premio:.2f}")
