from Imagem import *

img = Imagem('foto2.jpg')
# img.salvar_imagem('cinza.jpg')
img.limiar(0,160)
# img.salvar_imagem('limiar.jpg')
conjuntos = list(reversed(sorted(img.vizinhanca())))

base = conjuntos[0]
to_erase = []

for conjunto in conjuntos:
    if conjunto/base < 0.01:
        to_erase.append(conjunto)

for conjunto in to_erase:
    conjuntos.remove(conjunto)

print(conjuntos)
