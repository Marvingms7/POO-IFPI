class Bateria:
    def __init__(self, codigo, capacidade, percentual_carga):
        self.__codigo = codigo
        self.__capacidade = capacidade
        self.__percentual_carga = percentual_carga

    @property
    def codigo(self):
        return self.__codigo
    @property
    def capacidade(self):
        return self.__capacidade
    @property
    def percentual_carga(self):
        return self.__percentual_carga

    def carregar(self, Valor):
        if self.__percentual_carga + Valor <= 100:
            self.__percentual_carga += Valor
        return self.__percentual_carga

    def descarregar(self, Valor):
        if self.__percentual_carga + Valor <= 100 and self.__percentual_carga + Valor > 0:
            self.__percentual_carga -= Valor
        return self.__percentual_carga
class celular:
    def __init__(self, Mei, Wifi, Ligado):
        self.__Mei = Mei
        self.__Bateria = None
        self.__Wifi = Wifi
        self.__Ligado = Ligado
    @property
    def Mei(self):
        return self.__Mei
    @property
    def Wifi(self):
        return self.__Wifi
    @property
    def Ligado(self):
        return self.__Ligado
    @property
    def Bateria(self):
        return self.__Bateria

    def __str__(self):
        if self.__Bateria == None:
            status_bateria = "não tem bateria"
        else:
            status_bateria = self.__Bateria.percentual_carga
            carregar = self.__Bateria.carregar
        return f'Status da bateria igual a {status_bateria}'

    def LigarDesligar(self):
        if self.__Bateria == 0:
            self.__Estado = False
            print(f'O celular está com {self.__Bateria} de bateria')
        else:
            self.__Estado = True
            print(f'O celular está com {self.__Bateria} de bateria')
    def colocarBateria(self, bateria):
        if type(bateria) == Bateria:
            self.__Bateria = bateria
            print(f'Bateria colocada')

    def retirarBateria(self):
        if self.__Bateria == None:
            print(f'Celular ja está sem bateria')
        else:
            self.__Bateria = None
            print(f'Celular sem bateria')
    def LigarDesligarWifi(self):
        if self.__Wifi == True:
            print(f'Wifi ligado')
        else:
            print(f'Wifi Desligado')
    def assistirVideo(self, tempo):
        total = tempo * 5
        if self.__Wifi == True and self.__Bateria.percentual_carga >= total:
            b01.descarregar(total)
        else:
            print(f'Bateria tem apenas {self.__Bateria.percentual_carga}% de carga e não suporta')

    def carregar(self, valor):
        if type(valor) == Bateria:
            b01.carregar(valor)

    def descarregar(self, valor):
        if type(valor) == Bateria:
            b01.descarregar(valor)

b01 = Bateria(codigo=111, capacidade=100, percentual_carga=60)
c01 = celular(Mei=1111, Wifi=True, Ligado=True)
c01.colocarBateria(b01)
c01.retirarBateria()
c01.colocarBateria(b01)
c01.LigarDesligarWifi()
b01.descarregar(10)
b01.descarregar(10)
b01.carregar(10)
c01.assistirVideo(8)
print(c01)



