from Imagem import Imagem
from ImagemRGB import ImagemRGB

figura_clara = Imagem('../Imagens/figuraClara.jpg')
figura_clara.entropia()
figura_clara.media()
figura_clara.variancia()
figura_clara.salvar_histograma('../Histogramas/figuraClara.png')
# figura_clara.equalizar()
# figura_clara.salvar_imagem_equalizada('../Equalizadas/figuraClara.png')

print()

lena = Imagem('../Imagens/lena.jpg')
lena.entropia()
lena.media()
lena.variancia()
lena.salvar_histograma('../Histogramas/lena.png')

print()

figura_escura = Imagem('../Imagens/figuraEscura.jpg')
figura_escura.entropia()
figura_escura.media()
figura_escura.variancia()
figura_escura.salvar_histograma('../Histogramas/figuraEscura.png')
# figura_escura.equalizar()
# figura_escura.salvar_imagem_equalizada('../Equalizadas/figuraEscura.png')

marilyn = Imagem('../Imagens/marilyn.jpg')
marilyn.equalizar()
marilyn.salvar_imagem_equalizada('../Equalizadas/marilyn.png')

outono_LC = ImagemRGB('../Imagens/outono_LC.png')
outono_LC.equalizar()
outono_LC.salvar_imagem('../Equalizadas/outono_LC.png')