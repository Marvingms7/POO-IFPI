class televisao():
    def __init__(self, estado, canal=0, volume=0, canal_min=2, canal_max=99,volume_min=2, volume_max=100):
        self.__estado = estado
        self.__canal = canal
        self.__volume = volume
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.volume_min = volume_min
        self.volume_max = volume_max

    @property
    def estado(self):
        return self.__estado
    @property
    def canal(self):
        return self.__canal
    @property
    def volume(self):
        return self.__volume

    @canal.setter
    def canal(self, canal):
        self.__canal = canal

    @volume.setter
    def volume(self, volume):
        self.__volume = volume

    def estado(self):
        if self.__estado == True:
            print("A Tv está ligada.")
        else:
            print("A Tv está desligada.")

    def mudar_canal(self):
        canal = self.__canal
        if self.__estado == True:
            if canal > self.canal_max:
                print("O valor ultrapassa o limite máximo de canais.")
            elif canal < self.canal_min:
                print("O valor está abaixo do limite mínimo de canais.")
            else:
                self.__canal = canal
                print(f"O canal escolhido foi {self.canal}.")

    def aumentar_canal(self):
        canal = self.__canal
        if self.__estado == True:
            self.__canal += canal
            if self.__canal > self.canal_max:
                print("O canal ultrapassa o limite máximo de canais na TV.")
            elif canal == 0:
                self.__canal += 1
                print(f"Canal atual: {self.canal}.")
            else:
                print(f"Canal atual: {self.canal}.")

    def diminuir_canal(self):
        canal = self.__canal
        if self.__estado == True:
            self.__canal -= canal
            if self.__canal < self.canal_min:
                print("O canal está abaixo do limite máximo de canais na TV.")
            elif canal == 0:
                self.__canal -= 1
                print(f"Canal atual: {self.canal}.")
            else: print(f"Canal atual: {self.canal}.")

    def aumentar_volume(self):
        volume = self.__volume
        if self.__estado == True:
            self.__volume += volume
            if self.__volume > self.volume_max:
                print("O volume ultrapassa o limite máximo permitido da TV.")
            elif volume == 0:
                self.__volume += 1
                print(f"Volume atual: {self.volume}.")
            else: print(f"Volume atual: {self.volume}.")

    def diminuir_volume(self):
        volume = self.__volume
        if self.__estado == True:
            self.__volume -= volume
            if self.__volume < self.volume_min:
                print("O volume está abaixo do permitido da TV.")
            elif volume == 0:
                self.__volume -= 1
                print(f"Volume atual: {self.volume}.")
            else: print(f"Volume atual: {self.volume}.")

class ControleRemoto:
    def __init__(self, ligado, tv = None):
        self.__ligado = ligado
        self.__tv = tv

    @property
    def ligado(self):
        return self.__ligado

    @property
    def tv(self):
        return self.__tv

    def LigarDesligar(self):
        if self.__ligado == True:
            print("O controle está ligado!")
        else:
            print("O controle está desligado!")

    def vincularTv(self, tv):
        if type(tv) == televisao:
            self.__tv = tv

    def desvincularTv(self):
        self.__tv = None

    def ligarTv(self):
        if self.__tv == None:
            None
        else:
            if self.__ligado == True:
                self.tv.estado()
                self.tv.mudar_canal()
                self.tv.aumentar_canal()
                self.tv.diminuir_canal()
                self.tv.aumentar_volume()
                self.tv.diminuir_volume()
            else:
                None