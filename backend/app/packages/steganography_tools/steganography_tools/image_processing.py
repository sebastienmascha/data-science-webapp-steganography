#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Steganography-Tools - A Python steganography module.
# Copyright (C) 2021 Sébastien Mascha, Thomas Le Couedic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>

__author__ = "Sebastien Mascha, Thomas Le Couedic"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2021/04/01 $"
__revision__ = "$Date: 2021/04/01 $"
__license__ = "GPLv3"


import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy import ndimage
import cv2
import imageio
from PIL import Image, ExifTags

def img_information(img):
    "This function allows us to get the basic information of an image."
    # Opening Image as an object
    image = Image.open(img)
    # Getting the filename of image
    print("Filename : ",image.filename)
    # Getting the format of image
    print("Format : ",image.format)
    # Getting the mode of image
    print("Mode : ",image.mode)
    # Getting the size of image
    print("Size : ",image.size)
    # Getting only the width of image
    print("Width : ",image.width)
    # Getting only the height of image
    print("Height : ",image.height)
    # Getting the color palette of image
    print("Image Palette : ",image.palette)
    print("\n")
    # Showing image
    image.show()
    # Closing Image object
    image.close()
    
def get_metadata(img):
    "Check for potential metadata."
    image = Image.open(img)
    exif = { ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS }
    return exif

def rgb2grayscale(img):
    "Convert RGB image to grayscale using PIL"
    image = Image.open(img)
    image = image.convert('L')
    image.show()
    image.save('image_grayscale.jpg')
    
def plot_histogram(img):
    "Plot pixels distribution"
    fig = plt.figure(figsize=(8, 6))
    plt.hist(img.ravel(),bins = 256, range = [0,256]) 
    plt.title('Histogram representing pixel distribution', fontsize=25)
    plt.xlabel('Pixel value', fontsize=20)
    plt.ylabel('Count', fontsize=20)
    plt.show()
    
def thresholding(img, threshold=65):
    "Black or white pixels according to a given threshold"
    img = imageio.imread(img) 
    img = img[:,:,0]
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y] > threshold :
                img[x,y] = 255
            else:
                img[x,y] = 0
    
    fig = plt.figure(figsize=(8, 6))
    plt.imshow(img, cmap=plt.cm.gray)
    plt.title('Image displayed with a threshold for the pixels', fontsize=25)
    plt.show
    
def display_images(img):
    "Display images with different contrasts"
    fig = plt.figure(figsize=(24,20))

    ax1 = fig.add_subplot(131)
    ax1.title.set_text('Original image')
    plt.imshow(img, cmap=plt.cm.gray)
    
    ax2 = fig.add_subplot(132)
    ax2.title.set_text("Contrasted image : dark")
    plt.imshow(img, cmap=plt.cm.gray, vmin=10, vmax=500)
    plt.axis('off')

    ax3 = fig.add_subplot(133)
    ax3.title.set_text("Contrasted image : lightened")
    plt.imshow(img, cmap=plt.cm.gray, vmin=10, vmax=80)
    plt.axis('off')

    plt.show()

def image_manipulation(img):
    "Draw circles, lines into the image"
    img = imageio.imread(img) 
    img = img[:,:,0]
    
    img[100:120] = 255

    lx, ly = img.shape
    X, Y = np.ogrid[0:lx, 0:ly]
    mask = (X - lx / 2)**2 + (Y - ly / 2)**2 > (lx / 2)**2
    img[mask] = 0

    fig = plt.figure(figsize=(10, 8))
    plt.imshow(img, cmap=plt.cm.gray)
    plt.title('Image manipulated with Numpy', fontsize=25)
    plt.axis('off')

    plt.show()
    
    
def geo_transfomation(img):
    "Data augmentation/Geometrical trasnformation : cropping, up flip, down flip, rotations"
    lx, ly = img.shape
    crop_img = img[lx//4:-lx//4, ly//4:-ly//4]
    flip_ud_img = np.flipud(img)
    rotate_img = ndimage.rotate(img, 45)
    rotate_img_noreshape = ndimage.rotate(img, 45, reshape=False)

    fig = plt.figure(figsize=(12.5, 2.5))

    ax1 = fig.add_subplot(151)
    ax1.title.set_text('Original image')
    plt.imshow(img, cmap=plt.cm.gray)
    plt.axis('off')
    ax2 = fig.add_subplot(152)
    ax2.title.set_text('Image cropped')
    plt.imshow(crop_img, cmap=plt.cm.gray)
    plt.axis('off')
    ax3 = fig.add_subplot(153)
    ax3.title.set_text('Image flipped')
    plt.imshow(flip_ud_img, cmap=plt.cm.gray)
    plt.axis('off')
    ax4 = fig.add_subplot(154)
    ax4.title.set_text("Image rotated')
    plt.imshow(rotate_img, cmap=plt.cm.gray)
    plt.axis('off')
    ax5 = fig.add_subplot(155)
    ax5.title.set_text("Image rotated noreshape')
    plt.imshow(rotate_img_noreshape, cmap=plt.cm.gray)
    plt.axis('off')

    plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0,
                    right=1)

    plt.show()
    
def blurring(img):
    "Use gaussian filers for blurring"
    blurred_img = ndimage.gaussian_filter(img, sigma=3)
    very_blurred = ndimage.gaussian_filter(img, sigma=9)
    local_mean = ndimage.uniform_filter(img, size=11)

    fig = plt.figure(figsize=(15,5))
    ax1 = fig.add_subplot(131)
    ax1.title.set_text('Blurred image - Gaussian filter =3')
    plt.imshow(blurred_img, cmap=plt.cm.gray)
    plt.axis('off')
    ax2 = fig.add_subplot(132)
    ax2.title.set_text('Very blurred image - Gaussian filter =9')
    plt.imshow(very_blurred, cmap=plt.cm.gray)
    plt.axis('off')
    ax3= fig.add_subplot(133)
    ax3.title.set_text('Image with uniform filter')             
    plt.imshow(local_mean, cmap=plt.cm.gray)
    plt.axis('off')

    plt.subplots_adjust(wspace=0.1, hspace=0., top=0.99, bottom=0.01,
                    left=0.01, right=0.99)

    plt.show()

def sharpenning(img,alpha=30):
    "Sharpenning"
    blurred_img = ndimage.gaussian_filter(img, 3)

    filter_blurred_img = ndimage.gaussian_filter(blurred_img, 1)

    sharpened = blurred_img + alpha * (blurred_img - filter_blurred_img)

    fig = plt.figure(figsize=(18, 6))
 
    ax1 = fig.add_subplot(131)
    ax1.title.set_text('Original image')
    plt.imshow(img, cmap=plt.cm.gray)
    plt.axis('off')
    ax2 = fig.add_subplot(132)
    ax2.title.set_text('Blurred image - Gaussian filter =3')
    plt.imshow(blurred_img, cmap=plt.cm.gray)
    plt.axis('off')
    ax3 = fig.add_subplot(133)
    ax3.title.set_text('Blurred image sharpenned')
    plt.imshow(sharpened, cmap=plt.cm.gray)
    plt.axis('off')

    plt.tight_layout()
    plt.show()
    
def denoising(img):
    "Denoising"
    noisy = img + 0.4*img.std()*np.random.random(img.shape)

    gauss_denoised = ndimage.gaussian_filter(noisy, 2)
    med_denoised = ndimage.median_filter(noisy, 3)

    plt.figure(figsize=(18,6))

    plt.subplot(131)
    plt.imshow(noisy, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.title('noisy', fontsize=20)
    plt.subplot(132)
    plt.imshow(gauss_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.title('Gaussian filter', fontsize=20)
    plt.subplot(133)
    plt.imshow(med_denoised, cmap=plt.cm.gray, vmin=40, vmax=220)
    plt.axis('off')
    plt.title('Median filter', fontsize=20)

    plt.subplots_adjust(wspace=0.02, hspace=0.02, top=0.9, bottom=0, left=0,
                        right=1)
    plt.show()
    