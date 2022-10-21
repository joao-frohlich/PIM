import cv2
import numpy as np
import math

class Imagem:
    def __init__(self, caminho):
        self.imagem = cv2.imread(caminho, 2)
        self.altura = len(self.imagem)
        self.largura = len(self.imagem[0])
        self.tam_conjuntos = []
    
    def salvar_imagem(self, nome):
        cv2.imwrite(nome, self.imagem)
        cv2.imwrite(nome.replace('.png', '_Gx.png'), self.gx)
        cv2.imwrite(nome.replace('.png', '_Gy.png'), self.gy)
        cv2.imwrite(nome.replace('.png', '_magnitude.png'), self.imagem_magnitude)
        cv2.imwrite(nome.replace('.png', '_direcao.png'), self.imagem_direcao)
        cv2.imwrite(nome.replace('.png', '_high_boost.png'), self.imagem_high_boost)


    def median(self, vet):
        vet = sorted(vet)
        n = len(vet)
        # print(n)
        if n % 2 == 0:
            return (int(vet[n//2])+int(vet[int(n//2)-1]))//2
        return vet[n//2]

    def valido(self, px, py):
        return px >= 0 and py >= 0 and px < self.altura and py < self.largura

    def filtro_passa_baixa(self):
        aux_img = self.imagem.copy()
        for l in range(0, self.altura):
            for c in range(0, self.largura):
                vet = []
                for i in range(-1,2):
                    for j in range(-1,2):
                        if self.valido(l+i, c+j):
                            vet.append(self.imagem[l+i][c+j])
                aux_img[l][c] = self.median(vet)
        self.imagem = aux_img
    
    def filtro_derivativo(self, operador_x, operador_y):
        img_aux = np.zeros((self.altura+2, self.largura+2), np.uint8)
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                img_aux[i][j] = self.imagem[i][j]
        
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                janela = img_aux[i:i+3, j:j+3]
                self.gx[i][j] = np.abs(np.sum(operador_x @ janela))
                self.gy[i][j] = np.abs(np.sum(janela @ operador_y))
    
    def magnitude_gradiente(self):
        self.imagem_magnitude = self.imagem.copy()
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                self.imagem_magnitude[i][j] = (self.gy[i][j]**2 + self.gx[i][j]**2)**(1/2.0)
    
    def direcao_gradiente(self):
        self.imagem_direcao = self.imagem.copy()
        eps = 10**(-8)
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                self.imagem_direcao[i][j] = math.degrees(math.atan2(self.gy[i][j],self.gx[i][j]+eps))
    
    def selecao_gradientes(self):
        self.max_locais = []
        for i in range(0,self.altura):
            for j in range(0,self.largura):
                x = (0,0)
                y = (0,0)
                d_px = self.imagem_direcao[i][j]

                if -180 <= d_px and d_px <= -157.5:
                    y = (i,j-1)
                    x = (i,j+1)
                elif -157.5 < d_px and d_px <= -112.5:
                    y = (i+1,j-1)
                    x = (i-1,j+1)
                elif -112.5 < d_px and d_px <= -67.5:
                    y = (i+1,j)
                    x = (i-1,j)
                elif -67.5 < d_px and d_px <= -22.5:
                    y = (i+1,j+1)
                    x = (i-1,j-1)
                elif -22.5 < d_px and d_px <= 22.5:
                    y = (i,j+1)
                    x = (i,j-1)
                elif 22.5 < d_px and d_px <= 67.5:
                    y = (i-1,j+1)
                    x = (i+1,j-1)
                elif 67.5 < d_px and d_px <= 112.5:
                    y = (i-1,j)
                    x = (i+1,j)
                elif 112.5 < d_px and d_px <= 157.5:
                    y = (i-1,j-1)
                    x = (i+1,j+1)
                else:
                    y = (i,j-1)
                    x = (i,j+1)
                
                if self.valido(x[0], x[1]) and self.valido(y[0], y[1]):
                    mag_ij = self.imagem_magnitude[i][j]
                    mag_x = self.imagem_magnitude[x[0]][x[1]]
                    mag_y = self.imagem_magnitude[y[0]][y[1]]

                    if (mag_ij > mag_x and mag_ij > mag_y):
                        self.max_locais.append((i,j))


    def high_boost(self, k):
        self.imagem_high_boost = self.imagem.copy()
        for (i, j) in self.max_locais:
            mask_ij = int(self.imagem_magnitude[i][j])-int(self.imagem[i][j])
            self.imagem_high_boost[i][j] += k*mask_ij
            # self.imagem_high_boost[ml[0]][ml[1]] = 
        # for i in range(0,self.altura):
        #     for j in range(0,self.largura):
        #         self.imagem_high_boost[i][j] = min(255, self.imagem_high_boost[i][j]+self.imagem_magnitude[i][j])

    def sobel(self):
        self.gx = self.imagem.copy()
        self.gy = self.imagem.copy()
        operador_x = np.array([
            [-1, 0, 1],
            [-2, 0, 2],
            [-1, 0, 1]
        ])

        operador_y = np.array([
            [-1, -2, -1],
            [0, 0, 0],
            [1, 2, 1]
        ])

        self.filtro_derivativo(operador_x, operador_y)
    
    def prewitt(self):
        self.gx = self.imagem.copy()
        self.gy = self.imagem.copy()
        operador_x = np.array([
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1]
        ])

        operador_y = np.array([
            [-1, -1, -1],
            [0, 0, 0],
            [1, 1, 1]
        ])

        self.filtro_derivativo(operador_x, operador_y)

    def scharr(self):
        self.gx = self.imagem.copy()
        self.gy = self.imagem.copy()
        operador_x = np.array([
            [-3, 0, 3],
            [-10, 0, 10],
            [-3, 0, 3]
        ])

        operador_y = np.array([
            [-3, -10, -3],
            [0, 0, 0],
            [3, 10, 3]
        ])

        self.filtro_derivativo(operador_x, operador_y)