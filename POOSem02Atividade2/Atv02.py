class televisao():
    ligada = False
    canal = None
    volume = None
    volume_min = None
    volume_max = None

    def __init__(self, ligada=False, canal=2, canal_min=2, canal_max=99,volume_min=2, volume_max=100):
        self.ligada = ligada
        self.canal = canal
        self.canal_min = canal_min
        self.canal_max = canal_max
        self.volume_min = volume_min
        self.volume_max = volume_max

    def ligar(self):
        self.ligada = True
        self.volume = volume_min
        print(f"A TV está ligada e está no volume {self.volume}.")

    def desligar(self):
        self.ligada = False
        print("A TV está desligada.")

    def mudar_canal(self, valor):
        if self.ligada == True:
            if valor > self.canal_max:
                print("O valor ultrapassa o limite máximo de canais.")
            elif valor < self.canal_min:
                print("O valor está abaixo do limite mínimo de canais.")
            else:
                self.canal = valor
                print(f"O canal escolhido foi {self.canal}.")

    def aumentar_canal(self):
        if self.ligada == True:
            self.canal += 1
            if self.canal > self.canal_max:
                print("O canal ultrapassa o limite máximo de canais na TV.")
            print(f"Canal: {self.canal}.")

    def diminuir_canal(self):
        if self.ligada == True:
            self.canal -= 1
            if self.canal < self.canal_min:
                print("O canal está abaixo do limite máximo de canais na TV.")
            print(f"Canal: {self.canal}.")

    def aumentar_volume(self, volume):
        if self.ligada == True:
            volume += 1
            if volume > self.volume_max:
                print("O volume ultrapassa o limite máximo permitido da TV.")
            print(f"Volume: {volume}.")

    def diminuir_volume(self, volume):
        if self.ligada == True:
            volume -= 1
            if volume < self.volume_min:
                print("O volume está abaixo do permitido da TV.")
            print(f"Volume: {volume}.")


tv_da_sala = televisao(True, 7)
tv_da_sala.aumentar_volume(10)
for n in range(2, 12):
    n*=2
tv_da_sala.aumentar_volume(n-1)
tv_da_sala.mudar_canal(120)
for a in range(2, 23):
    a -= 15
tv_da_sala.aumentar_volume(a-1)
tv_da_sala.desligar()


tv_do_quarto = televisao(True, 13)
tv_do_quarto.aumentar_volume(50)
tv_do_quarto.diminuir_canal()
for i in range(2, 54):
    i //= 3
tv_do_quarto.diminuir_volume(i+1)
tv_do_quarto.desligar()
tv_do_quarto = televisao(True, 13)
tv_do_quarto.aumentar_canal()
tv_do_quarto.aumentar_canal()
