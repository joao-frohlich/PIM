import skimage
import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

class ImagemRGB:
    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho)
    
    def salvar_imagem(self, nome):
        cv2.imwrite(nome, self.imagem)
    
    def equalizar(self):
        img = cv2.cvtColor(self.imagem, cv2.COLOR_BGR2YUV)

        altura = len(img)
        largura = len(img[0])
        num_pixels = altura*largura

        freq = [0]*256
        for i in range(0,altura):
            for j in range(0,largura):
                freq[img[i][j][0]]+=1

        soma_prefixa = 0
        aux = [0]*256
        for i in range(0,256):
            p = freq[i]/num_pixels
            soma_prefixa += p
            aux[i] = soma_prefixa

        for i in range(0,altura):
            for j in range(0,largura):
                img[i][j][0] = int(aux[img[i][j][0]]*255)

        self.imagem_equalizada = cv2.cvtColor(img, cv2.COLOR_YUV2BGR)

    def salvar_imagem_equalizada(self, nome):
        cv2.imwrite(nome, self.imagem_equalizada)

    def gerar_histograma(self, img):
        plt.clf()
        plt.cla()
        plt.close()
        plt.hist(cv2.cvtColor(img, cv2.COLOR_BGR2YUV)[:,:,0].ravel(), 256, [0,256])

    def salvar_histograma(self, nome):
        self.gerar_histograma(self.imagem)
        plt.savefig(nome)
    
    def salvar_histograma_equalizado(self, nome):
        self.gerar_histograma(self.imagem_equalizada)
        plt.savefig(nome)

    def mostrar_histograma(self):
        self.gerar_histograma(self.imagem)
        plt.show()
