class pessoa:
    def __init__(self, nome, idade, peso, altura, sexo, estado = 'vivo(a)', estado_civil = 'solteiro(a)', conjuge = None):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__altura = altura
        self.__sexo = sexo
        self.__estado = estado
        self.__estado_civil = estado_civil
        self.__conjuge = conjuge

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def peso(self):
        return self.__peso
    @property
    def altura(self):
        return self.__altura
    @property
    def sexo(self):
        return self.__sexo
    @property
    def estado(self):
        return self.__estado
    @property
    def estado_civil(self):
        return self.__estado_civil
    @property
    def conjugue(self):
        return self.__conjuge
    def __str__(self):
        return f'Nome: {self.__nome}\nidade: {self.__idade}\npeso: {self.__peso}\naltura: {self.__altura}\nsexo: {self.__sexo}\nestado: {self.__estado}\nestado civil: {self.__estado_civil}\nconjuge: {self.__conjuge}'

    def envelhecer(self):
        self.__idade += 1
        if self.__idade < 21:
            self.__altura += 5
    def engordar(self, valor):
        self.__peso += valor
    def emagrecer(self, valor):
        self.__peso -= valor

    def crescer(self, valor):
        if self.__idade <= 21:
            self.__altura += valor
        if self.__idade >= 21:
            print(f'{self.__nome} não pode crescer pois está com 21 anos ou mais')
    def casar(self, valor):
        if self.__estado == 'vivo' and self.__idade > 18 and self.__estado_civil == 'solteiro':
            self.__conjuge = valor
            self.__estado_civil = 'casado(a)'
            print(f'{self.__nome} está casado com {self.__conjuge}')
        elif self.__estado == 'morto':
            print(f'{self.__nome} não pode se casar pois está {self.__estado}')
        elif self.__idade < 18:
            print(f'{self.__nome} não pode se casar pois é menor de idade, tem só {self.__idade} anos.')
        elif self.__estado_civil == 'casado':
            print(f'{self.__nome} não pode se casar pois já está casado')
        elif self.__conjuge == 'Maria' or self.__conjuge == 'Carlos' or self.__conjuge == 'João':
            print(f'Casamento não permitido. {self.__conjuge} é de menor.')


    def morrer(self):
        self.__estado = 'morto'
        print(f'{self.__nome} morreu')

Maria = pessoa(nome='Maria',idade=5, peso=20, altura=100, sexo='F')
Joao = pessoa(nome='joao',idade=12, peso=40, altura=140, sexo='M')
Pedro = pessoa(nome='Pedro',idade=22, peso=65, altura=170, sexo='M')
Bia = pessoa(nome='Bia',idade=18, peso=55, altura=160, sexo='F')
Julia = pessoa(nome='Julia',idade=30, peso=65, altura=170, sexo='F')
Carlos = pessoa(nome='Carlos',idade=2, peso=11, altura=80, sexo='M')
Jonas = pessoa(nome='Jonas',idade=34, peso=70, altura=180, sexo='M')
print(Maria)
print(f'#='*50)
print(Joao)
print(f'#='*50)
print(Pedro)
print(f'#='*50)
print(Bia)
print(f'#='*50)
print(Julia)
print(f'#='*50)
print(Carlos)
print(f'#='*50)
print(Jonas)
Carlos.crescer(10)
print(Carlos)
Carlos.envelhecer()
print(Carlos)
Pedro.crescer(5)
Bia.morrer()
Pedro.casar(Julia)
print(Pedro)





