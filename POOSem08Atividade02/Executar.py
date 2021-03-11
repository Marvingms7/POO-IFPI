from Funcionario import *
class ControleDeFuncionarios:
    def __init__(self, valor_pago = 0):
        self._valor_pago = valor_pago
        self._funcionarios = []   

    def adicionarFuncionario(self, funcionario):
        self._funcionarios.append(funcionario)

    def atualizaSalario(self, percentual_aumento):
        for i in self._funcionarios:
            if type(i):
                i.reajustaSalario(percentual_aumento)
    def relatorioDePagamento(self):
        self._valor_pago = 0
        for i in self._funcionarios:
            self._valor_pago += i.getSalarioMensal()
            print(f"Funcionario: {i.nome}, recebeu: {i.getSalarioMensal()}")

    @property
    def valor_pago(self):
        return self._valor_pago

controle = ControleDeFuncionarios()
controle.adicionarFuncionario(Funcionario('Marcus Vinicius', '123456789-11', 1000.0))
controle.adicionarFuncionario(Vendedor('João Vitor', '4545658757-33', 1000, 5000))
controle.adicionarFuncionario(Vigilante('Raimunda Oliveira', '1245859565-44', 1000.0, 10, 12))
controle.atualizaSalario(10)
controle.relatorioDePagamento()
print(f"\nO total pago é: R$ {controle._valor_pago:.2f}")
