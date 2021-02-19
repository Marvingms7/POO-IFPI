# Classe:
class Ponto2D():
    #Atributos
    X = None
    Y = None

    #Construtor:
    def __init__(self, X=0, Y=0):
        self.X = X
        self.Y = Y

    # Método:
    def Eigual(self, outroPonto):
        X = outroPonto
        Y = outroPonto
        if self.X == X:
            print("X", True)
        elif self.Y == Y:
            print("Y", True)
        else: print(False)

# Objetos:
PontoX = Ponto2D(X=9)
PontoX.Eigual(9)
PontoY = Ponto2D(Y=8)
PontoY.Eigual(7)