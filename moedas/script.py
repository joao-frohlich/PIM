from Imagem import *

img = Imagem('foto2.jpg')
img.salvar_imagem('cinza.jpg')
img.limiar(0,160)
img.salvar_imagem('limiar.jpg')
tam_conjuntos = img.pegar_objetos()
print(tam_conjuntos)
tam_ord = list(reversed(sorted(tam_conjuntos)))
print(tam_ord)

base = tam_ord[0]
to_erase = []

for conjunto in tam_ord:
    if conjunto/base < 0.01:
        to_erase.append(conjunto)

for conjunto in to_erase:
    tam_conjuntos.remove(conjunto)
    tam_ord.remove(conjunto)

print(tam_conjuntos)
print(tam_ord)

moedas = [1, 0]
moeda = 0

for i in range(1,len(tam_ord)):
    if tam_ord[i]/tam_ord[i-1] < 0.8:
        moeda += 1
    if moeda > 1: break
    moedas[moeda]+=1
    

print('R$ ' + f'{moedas[0] + 0.1*moedas[1]:.2f}')
