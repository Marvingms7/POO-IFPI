class televisão:
    def __init__(self, canal = 2, canal_minimo = 2, canal_maximo = 99, volume = 2, volume_minimo = 0, volume_maximo = 100, ligada = False ):
        self.__canal = canal
        self.__canal_minimo = canal_minimo
        self.__canal_maximo = canal_maximo
        self.__volume = volume
        self.__volume_minimo = volume_minimo
        self.__volume_maximo = volume_maximo
        self.__ligada = ligada

    @property
    def canal(self):
        return self.__canal
    @property
    def canal_minimo(self):
        return self.__canal_minimo
    @property
    def canal_maximo(self):
        return self.__canal_maximo
    @property
    def volume(self):
        return self.__volume
    @property
    def volume_minimo(self):
        return self.__volume_minimo
    @property
    def volume_maximo(self):
        return self.__volume_maximo
    @property
    def ligada(self):
        return self.__ligada

    @ligada.setter
    def ligada(self, valor):
        if valor == True:
            self.__ligada = True
            print(f'A tv está Ligada!')
        if valor == False:
            self.__ligada = False
            print(f'A tv está Desligada!')

    @canal.setter
    def canal(self, valor):
        if self.__ligada == True:
            if valor < self.__canal_maximo and valor > self.__volume_minimo:
                self.__canal = valor
                print(f'Canal alterado para o {self.__canal}')
            else:
                print(f'Canal suportado pela tv é apenas entre {self.__canal_minimo} e {self.__canal_maximo}')
        else:
            print(f'A tv está Desligada!')


    @volume.setter
    def volume(self, valor):
        self.__volume = valor

    def aumentar_volume(self):
        if self.__ligada == True:
            if self.__volume < self.__volume_maximo and self.__volume >= self.__volume_minimo:
                self.__volume += 1
                print(f'Volume alterado para {self.__volume}')
            else:
                print(f'O volume suportado pela tv é apenas entre {self.__volume_minimo} e {self.__volume_maximo}')
        else:
            print(f'A tv está Desligada!')

    def diminuir_volume(self):
        if self.__ligada == True:
            if self.__volume <= self.__volume_maximo and self.__volume > self.__volume_minimo:
                self.__volume -= 1
                print(f'Volume alterado para {self.__volume}')
            else:
                print(f'O volume suportado pela tv é apenas entre {self.__volume_minimo} e {self.__volume_maximo}')
        else:
            print(f'A tv está Desligada!')


print(f'Objeto01')
print(f'')
Minha_tv = televisão(canal=5, canal_minimo=2, canal_maximo=99, volume=2, volume_minimo=0, volume_maximo=100, ligada=True)
#atual:
print('canal',Minha_tv.canal)
print('canal minimo',Minha_tv.canal_minimo)
print('canal maximo',Minha_tv.canal_maximo)
print('volume',Minha_tv.volume)
print('volume minimo',Minha_tv.volume_minimo)
print('volume maximo',Minha_tv.volume_maximo)
print('Estado',Minha_tv.ligada)
#alterado:
Minha_tv.ligada = False
Minha_tv.canal = 40
Minha_tv.volume = 99
Minha_tv.ligada = True
Minha_tv.canal = 68
Minha_tv.volume = 70
print(f'Volume', Minha_tv.volume)
Minha_tv.aumentar_volume()
Minha_tv.diminuir_volume()

print(f'#=' * 50)
print(f'Objeto02')
print(f'')
Tv_da_sala = televisão(canal=4, canal_minimo=4, canal_maximo=999, volume=2, volume_minimo=1, volume_maximo=100, ligada=True)
print('canal',Tv_da_sala.canal)
print('canal minimo',Tv_da_sala.canal_minimo)
print('canal maximo',Tv_da_sala.canal_maximo)
print('volume',Tv_da_sala.volume)
print('volume minimo',Tv_da_sala.volume_minimo)
print('volume maximo',Tv_da_sala.volume_maximo)
print('Estado',Tv_da_sala.ligada)
#alterado:
Tv_da_sala.ligada = False
Tv_da_sala.canal = 415
Tv_da_sala.volume = 50
Tv_da_sala.ligada = True
Tv_da_sala.canal = 255
Tv_da_sala.volume = 68
print(f'Volume', Tv_da_sala.volume)
Tv_da_sala.aumentar_volume()
Tv_da_sala.diminuir_volume()
Tv_da_sala.diminuir_volume()
Tv_da_sala.diminuir_volume()




