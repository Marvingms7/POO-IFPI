class animal:
    def __init__(self, Peso, Nome):
        self.Peso = Peso
        self.Nome = Nome
    def __str__(self):
        return f'Peso: {self.Peso}\nNome: {self.Nome}'


class peixe(animal):
    def __init__(self, Peso, Nome, Tipo_habitat):
        super().__init__(Peso, Nome)
        self.Tipo_habitat = Tipo_habitat
    def __str__(self):
        return f'Peso: {self.Peso}\nNome: {self.Nome}\nTipo de habitat: {self.Tipo_habitat}'


class cachorro(animal):
    def __init__(self, Peso, Nome, Raca):
        super().__init__(Peso, Nome)
        self.Raca = Raca
    def __str__(self):
        return f'Peso: {self.Peso}\nNome: {self.Nome}\nRaça: {self.Raca}'


