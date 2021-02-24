class gato:
    def __init__(self, Peso, Idade, Nome = "Sem Nome", Raça = "Sem raça"):
        self.__Peso = Peso
        self.__Idade = Idade
        self.__Nome = Nome
        self.Raça = Raça

    def getnome(self):
        return self.__Nome

    def getengordar(self):
        self.__Peso += self.__Peso
        return self.__Peso

    def getenvelhecer(self):
        self.__Idade += 1
        return self.__Idade

gato01 = gato(1, 3, Nome='Nina', Raça='Siames')
print(f'Nome: {gato01.getnome()}')
print(f'Peso: {gato01.getengordar()}')
print(f'Idade: {gato01.getenvelhecer()}')
print(f'Raça: {gato01.Raça}')

print('#=' * 40)

gato02 = gato(0.5, 5, Nome='Chiquinho', Raça='Wirehair')
print(f'Nome: {gato02.getnome()}')
print(f'Peso: {gato02.getengordar()}')
print(f'Idade: {gato02.getenvelhecer()}')
print(f'Raça: {gato02.Raça}')







