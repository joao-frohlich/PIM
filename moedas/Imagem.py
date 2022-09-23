import cv2
from queue import Queue

class Imagem:
    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho, 2)
        self.altura = len(self.imagem)
        self.largura = len(self.imagem[0])
        self.tam_conjuntos = []
    
    def salvar_imagem(self, nome):
        cv2.imwrite(nome, self.imagem)

    def limiar(self, esquerda, direita):
        for i in range(0, self.altura):
            for j in range(0, self.largura):
                pixel = self.imagem[i][j]
                if pixel >= esquerda and pixel <= direita:
                    self.imagem[i][j] = 255
                else:
                    self.imagem[i][j] = 0
    
    def valido(self, x, y):
        return (x >= 0 and x < self.altura and y >= 0 and y < self.largura)

    def pegar_objetos(self):
        pixels = []
        dicio = {}
        visitados = []
        for i in range(self.altura):
            visitados.append([False]*self.largura)
        for i in range(self.altura):
            for j in range(self.largura):
                if self.imagem[i][j] == 255 and not visitados[i][j]:
                    q = Queue()
                    q.put((i,j))
                    sz = 0
                    while not q.empty():
                        (pi, pj) = q.get()
                        if visitados[pi][pj]:
                            continue
                        visitados[pi][pj] = True
                        sz += 1
                        mvs = [(1,0), (-1,0), (0,1), (0,-1)]
                        for mv in mvs:
                            if self.valido(pi+mv[0], pj+mv[1]) and self.imagem[pi+mv[0]][pj+mv[1]] == 255:
                                q.put((pi+mv[0], pj+mv[1]))
                    self.tam_conjuntos.append(sz)
        return self.tam_conjuntos
