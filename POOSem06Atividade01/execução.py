from classes import *;
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

