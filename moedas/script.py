import cv2

class DSU:
    def __init__(self, n):
        self.n = n
        self.sz = [1]*(n+5)
        self.pa = []
        for i in range(0,n+5):
            self.pa.append(i)

    def root(self, a):
        if self.pa[a] != a: self.pa[a] = self.root(self.pa[a])
        return self.pa[a]
    
    def find(self, a, b):
        return self.root(a) == self.root(b)
    
    def union(self, a, b):
        root_a = self.root(a)
        root_b = self.root(b)
        if root_a != root_b:
            if self.sz[root_a] > self.sz[root_b]: root_a, root_b = root_b, root_a
            self.pa[root_a] = root_b
            self.sz[root_b] += self.sz[root_a]
    
    def tam_conjuntos(self):
        szs = []
        for i in range(0,self.n):
            if self.pa[i] == i:
                szs.append(self.sz[i])
        return szs

class Imagem:
    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho, 2)
        self.altura = len(self.imagem)
        self.largura = len(self.imagem[0])
    
    def mostrar_imagem(self):
        cv2.imshow("Imagem", self.imagem)
        cv2.waitKey(0)
    
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
        return (x >= 0 and x <= self.altura and y >= 0 and y <= self.largura)

    def vizinhanca(self):
        pixels = []
        dicio = {}
        for i in range(self.altura):
            for j in range(self.largura):
                if self.imagem[i][j] == 255:
                    dicio[(i,j)] = len(pixels)
                    pixels.append((i,j))
        conjuntos = DSU(len(pixels))
        for (a,b) in pixels:
            if self.valido(a-1,b):                
                if self.imagem[a-1][b] == 255:
                    conjuntos.union(dicio[(a,b)], dicio[(a-1,b)])
            if self.valido(a,b-1):
                if self.imagem[a][b-1] == 255:
                    conjuntos.union(dicio[(a,b)], dicio[(a,b-1)])
        print(conjuntos.tam_conjuntos())



img = Imagem('moeda.jpeg')
img.limiar(0,230)
img.vizinhanca()