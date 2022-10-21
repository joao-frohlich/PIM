from Imagem import Imagem
from ImagemRGB import ImagemRGB

figura_clara = Imagem('../Imagens/figuraClara.jpg')
print('Figura clara')
figura_clara.entropia()
figura_clara.media()
figura_clara.variancia()
figura_clara.salvar_histograma('../Histogramas/figuraClara.png')
figura_clara.equalizar()
figura_clara.salvar_histograma_equalizado('../Histogramas/figuraClara_equalizada.png')
figura_clara.salvar_imagem_equalizada('../Equalizadas/figuraClara.png')

print()


lena = Imagem('../Imagens/lena.jpg')
print('Lena')
lena.entropia()
lena.media()
lena.variancia()
lena.salvar_histograma('../Histogramas/lena.png')

print()

figura_escura = Imagem('../Imagens/figuraEscura.jpg')
print('Figura escura')
figura_escura.entropia()
figura_escura.media()
figura_escura.variancia()
figura_escura.salvar_histograma('../Histogramas/figuraEscura.png')
figura_escura.equalizar()
figura_escura.salvar_histograma_equalizado('../Histogramas/figuraEscura_equalizada.png')
figura_escura.salvar_imagem_equalizada('../Equalizadas/figuraEscura.png')

print('\nMarilyn')
marilyn = Imagem('../Imagens/marilyn.jpg')
marilyn.salvar_histograma('../Histogramas/marilyn.png')
marilyn.equalizar()
marilyn.salvar_histograma_equalizado('../Histogramas/marilyn_equalizada.png')
marilyn.salvar_imagem_equalizada('../Equalizadas/marilyn.png')

print('\nOutono_LC')
outono_LC = ImagemRGB('../Imagens/outono_LC.png')
outono_LC.salvar_histograma('../Histogramas/outono_LC.png')
outono_LC.equalizar()
outono_LC.salvar_histograma_equalizado('../Histogramas/outono_LC_equalizada.png')
outono_LC.salvar_imagem_equalizada('../Equalizadas/outono_LC.png')