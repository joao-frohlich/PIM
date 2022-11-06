import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
from skimage.color import rgb2gray
from skimage import img_as_float
from skimage.metrics import structural_similarity as ssim
from skimage.filters import gaussian

def fourier_masker_Ver(image, original, i):
        f_size = 15

        # Aplica um filtro gaussiano e a transforamção de fourier na imagem
        image_grey_fourier = np.fft.fftshift(np.fft.fft2(gaussian(rgb2gray(image))))
        image_grey_fourier[:580, 955:965] = i
        image_grey_fourier[-580:,955:965] = i
        
        # Verifica a similaridade estrutural
        imgo = img_as_float(rgb2gray(original))
        img = img_as_float(np.log(abs(image_grey_fourier)))
        ssim_img = ssim(img, imgo, data_range=imgo.max() - imgo.min())

        # Plota os resultados
        _, ax = plt.subplots(1,3,figsize=(15,15))
        ax[0].imshow(np.log(abs(image_grey_fourier)), cmap='gray')
        ax[0].set_title('Masked Fourier Ver', fontsize = f_size)
        ax[1].imshow(image, cmap = 'gray')
        ax[1].set_title('Greyscale Image', fontsize = f_size)
        ax[2].imshow(abs(np.fft.ifft2(image_grey_fourier)), cmap='gray')
        ax[2].set_title('Transformed Greyscale Image', fontsize = f_size)
        ax[2].set_xlabel(f'i: {i}, SSIM: {ssim_img:.2f}')



def fourier_masker_Hor(image, original, i):
        f_size = 15

        # Aplica um filtro gaussiano e a transforamção de fourier na imagem
        image_grey_fourier = np.fft.fftshift(np.fft.fft2(gaussian(rgb2gray(image))))
        image_grey_fourier[595:605, 0:930] = i
        image_grey_fourier[595:605, 990:] = i

        # Verifica a similaridade estrutural
        imgo = img_as_float(rgb2gray(original))
        img = img_as_float(np.log(abs(image_grey_fourier)))
        ssim_img = ssim(img, imgo, data_range=imgo.max() - imgo.min())

        # Plota os resultados
        _, ax = plt.subplots(1,3,figsize=(15,15))
        ax[0].imshow(np.log(abs(image_grey_fourier)), cmap='gray')
        ax[0].set_title('Masked Fourier Hor', fontsize = f_size)
        ax[1].imshow(image, cmap = 'gray')
        ax[1].set_title('Greyscale Image', fontsize = f_size)
        ax[2].imshow(abs(np.fft.ifft2(image_grey_fourier)), cmap='gray')
        ax[2].set_title('Transformed Greyscale Image', fontsize = f_size)
        ax[2].set_xlabel(f'i: {i}, SSIM: {ssim_img:.2f}')


def fourier_masker_VerHor(image, original, i):
        f_size = 15

        # Aplica um filtro gaussiano e a transforamção de fourier na imagem
        image_grey_fourier = np.fft.fftshift(np.fft.fft2(gaussian(rgb2gray(image))))
        image_grey_fourier[:580, 955:965] = i
        image_grey_fourier[-580:,955:965] = i
        image_grey_fourier[595:605, 0:930] = i
        image_grey_fourier[595:605, 990:] = i

        # Verifica a similaridade estrutural
        imgo = img_as_float(rgb2gray(original))
        img = img_as_float(np.log(abs(image_grey_fourier)))
        ssim_img = ssim(img, imgo, data_range=imgo.max() - imgo.min())

        # Plota os resultados
        _, ax = plt.subplots(1,3,figsize=(15,15))
        ax[0].imshow(np.log(abs(image_grey_fourier)), cmap='gray')
        ax[0].set_title('Masked Fourier', fontsize = f_size)
        ax[1].imshow(image, cmap = 'gray')
        ax[1].set_title('Greyscale Image', fontsize = f_size)
        ax[2].imshow(abs(np.fft.ifft2(image_grey_fourier)), cmap='gray')
        ax[2].set_title('Transformed Greyscale Image', fontsize = f_size)
        ax[2].set_xlabel(f'i: {i}, SSIM: {ssim_img:.2f}')

def fourier_iterator(image, original, value_list):
    for i in value_list:
        fourier_masker_VerHor(image, original, i)

image = imread('folhas1_Reticulada.png')
original = imread('folhas1.png')

dark_image_grey = rgb2gray(image)
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(dark_image_grey, cmap='gray');

dark_image_grey_fourier = np.fft.fftshift(np.fft.fft2(dark_image_grey))
plt.figure(num=None, figsize=(8, 6), dpi=80)
plt.imshow(np.log(abs(dark_image_grey_fourier)), cmap='gray');

fourier_iterator(image, original, [1, 50, 100])
fourier_masker_Hor(image, original, 1)
fourier_masker_Ver(image, original, 1)

plt.show()
