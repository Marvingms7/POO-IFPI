from Sem07Atv02Q01 import *
class Banco:
    def __init__(self, saldo_total = 0):
        self._saldo_total = saldo_total
        self._contas = []

    @property
    def contas(self):
        return self._contas

    def CadastrarConta(self, conta):
        self._contas.append(conta)

    def Relatorio(self):
        total = conta_c = conta_p = 0
        for i in self._contas:
            self._saldo_total += i.get_Saldo()
            if type(i) is ContaCorrente:
                conta_c += 1
                total += 1
            else:
                conta_p += 1
                total += 1

            print(f'Constam {total} contas cadastradas\nConta Corrente tem: {conta_c}\nConta Poupança tem: {conta_p}')

    @property
    def saldo_total(self):
        return self._saldo_total

controle = Banco()
controle.CadastrarConta(ContaCorrente(1, 500))
controle.CadastrarConta(ContaPoupanca(2, 500, 10))
controle.CadastrarConta(ContaPoupanca(3, 800, 0))
controle.Relatorio()
print(f"\nO saldo total é: R$ {controle._saldo_total:.2f}")
