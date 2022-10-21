import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

class Imagem:
    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho, 2)
        self.altura = len(self.imagem)
        self.largura = len(self.imagem[0])
        self.num_pixels = self.altura*self.largura
        self.intensidades = [0]*256
        for linha in self.imagem:
            for pixel in linha:
                self.intensidades[pixel]+=1
        self.p = [0.0]*256
        for i in range(0,256):
            self.p[i] = self.intensidades[i]/self.num_pixels
    
    def salvar_imagem(self, nome):
        cv2.imwrite(nome, self.imagem)
    
    def salvar_imagem_equalizada(self, nome):
        cv2.imwrite(nome, self.imagem_equalizada)

    def gerar_histograma(self, img):
        plt.clf()
        plt.cla()
        plt.close()
        plt.hist(img.ravel(), 256, [0,256])

    def salvar_histograma(self, nome):
        self.gerar_histograma(self.imagem)
        plt.savefig(nome)

    def salvar_histograma_equalizado(self, nome):
        self.gerar_histograma(self.imagem_equalizada)
        plt.savefig(nome)

    def mostrar_histograma(self):
        self.gerar_histograma(self.imagem)
        plt.show()

    def entropia(self):
        self.entropia = 0
        for i in range(0,256):
            if self.p[i] == 0: continue
            self.entropia -= self.p[i] * math.log2(self.p[i])
        print('Entropia: ', self.entropia)
    
    def media(self):
        self.media = 0
        for i in range(0, 256):
            self.media += i*self.p[i]
        print('Media: ', self.media)
    
    def variancia(self):
        self.variancia = 0
        for i in range(0,256):
            self.variancia += ((i-self.media)**2)*self.p[i]
        print('Variancia: ', self.variancia)

    def equalizar(self):
        self.imagem_equalizada = self.imagem.copy()
        soma_prefixa = 0
        aux = [0]*256
        for i in range(0,256):
            soma_prefixa += self.p[i]
            aux[i] = soma_prefixa
        for i in range(0, self.altura):
            for j in range(0, self.largura):
                self.imagem_equalizada[i][j] = int(255*aux[self.imagem[i][j]])

        # for i in range(0, self.altura):
        #     for j in range(120, self.largura):
        #         janela = self.imagem[max(i-1, 0):min(i+2, self.altura), max(j-1, 0):min(j+2, self.largura)]
        #         freq = [0]*256
        #         altura_janela = len(janela)
        #         largura_janela = len(janela[0])
        #         num_pixels_janela = altura_janela*largura_janela
        #         for linha in janela:
        #             for pixel in linha:
        #                 freq[pixel]+=1
        #         soma_prefixa = 0
        #         p = [0]*256
        #         for i in range(0,256):
        #             soma_prefixa += freq[i]*1.0/num_pixels_janela
        #             p[i] = soma_prefixa
        #         self.imagem_equalizada[i][j] = int(255*p[self.imagem[i][j]])
                
