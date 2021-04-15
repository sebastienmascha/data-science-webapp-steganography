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

# Imports
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
    # Opening image as an object
    image = Image.open(img)
    # Recovering potential image matadat using ExifTags method from PIL
    exif = { ExifTags.TAGS[k]: v for k, v in image._getexif().items() if k in ExifTags.TAGS }
    return exif

def rgb2grayscale(img):
    "Convert RGB image to grayscale using PIL"
    # Opening image as an object
    image = Image.open(img)
    # Converting image to grayscale
    image = image.convert('L')
    # Showing image
    image.show()
    # Saving image to the current direcrory
    image.save('image_grayscale.jpg')
    
def plot_histogram(img):
    "Plot pixels distribution"
    # Creating a matplotlib figure
    fig = plt.figure(figsize=(8, 6))
    # Plotting pixels ditribution histogram
    # ravel() allow us to have a 1D array in order to display it on the histogram
    # Each pixel is coded on 8 bits (0 to 255 = 256 values)
    plt.hist(img.ravel(),bins = 256, range = [0,256]) 
    # Setting figure title and figure labels
    plt.title('Histogram representing pixel distribution', fontsize=25)
    plt.xlabel('Pixel value', fontsize=20)
    plt.ylabel('Count', fontsize=20)
    plt.show()
    
def thresholding(img, threshold=65):
    "Black or white pixels according to a given threshold"
    # Reading the image as an array
    img = imageio.imread(img) 
    # Converting 3D array to 2D array in order to use scipy methods
    img = img[:,:,0]
    # Going through all the pixels of the image
    for x in range(img.shape[0]):
        for y in range(img.shape[1]):
            if img[x,y] > threshold :
                # White pixel
                img[x,y] = 255
            else:
                # Black pixel
                img[x,y] = 0
    # Plotting the result in a matplotlib figure
    fig = plt.figure(figsize=(8, 6))
    plt.imshow(img, cmap=plt.cm.gray)
    # Setting figure title
    plt.title('Image displayed with a threshold for the pixels', fontsize=25)
    plt.show
    
def display_images(img):
    "Display images with different contrasts"
    # Creating a matplotlib figure 
    fig = plt.figure(figsize=(24,20))
    # First subplot : Original image
    ax1 = fig.add_subplot(131)
    # Setting subplot title
    ax1.title.set_text('Original image')
    plt.imshow(img, cmap=plt.cm.gray)
    # Constrasting image by adjusting vmin and vmax parameters
    # Second subplot : Dark image
    ax2 = fig.add_subplot(132)
    ax2.title.set_text("Contrasted image : dark")
    plt.imshow(img, cmap=plt.cm.gray, vmin=10, vmax=500)
    # No axis
    plt.axis('off')
    # Third subplot : Lightened image
    ax3 = fig.add_subplot(133)
    ax3.title.set_text("Contrasted image : lightened")
    plt.imshow(img, cmap=plt.cm.gray, vmin=10, vmax=80)
    plt.axis('off')
    plt.show()

def image_manipulation(img):
    "Draw circles, lines into the image"
    # Reading the image as an array
    img = imageio.imread(img) 
    # Converting 3D array to 2D array in order to use scipy methods
    img = img[:,:,0]
    # Drawing a horizontal white line by sliccing the image
    img[100:120] = 255
    # Image shape
    lx, ly = img.shape
    # Creating two 1D arrays using ogrid
    X, Y = np.ogrid[0:lx, 0:ly]
    # Defining a mask in shape of a circle
    mask = (X - lx / 2)**2 + (Y - ly / 2)**2 > (lx / 2)**2
    # All the pixels out of the mask are forced to 0 (black)
    img[mask] = 0
    # Plotting the result in a matplotlib figure 
    fig = plt.figure(figsize=(10, 8))
    plt.imshow(img, cmap=plt.cm.gray)
    plt.title('Image manipulated with Numpy', fontsize=25)
    plt.axis('off')
    plt.show()
    
    
def geo_transfomation(img):
    "Data augmentation/Geometrical trasnformation : cropping, up flip, down flip, rotations"
    # Image shape
    lx, ly = img.shape
    # Sliccing the image to crop it
    crop_img = img[lx//4:-lx//4, ly//4:-ly//4]
    # Using scipy methods to flip, rotate the image
    flip_ud_img = np.flipud(img)
    rotate_img = ndimage.rotate(img, 45)
    rotate_img_noreshape = ndimage.rotate(img, 45, reshape=False)
    # Plotting the figure in a matplotlib figure
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
    ax4.title.set_text('Image rotated')
    plt.imshow(rotate_img, cmap=plt.cm.gray)
    plt.axis('off')
    ax5 = fig.add_subplot(155)
    ax5.title.set_text('Image rotated noreshape')
    plt.imshow(rotate_img_noreshape, cmap=plt.cm.gray)
    plt.axis('off')
    plt.subplots_adjust(wspace=0.02, hspace=0.3, top=1, bottom=0.1, left=0,
                    right=1)
    plt.show()
    
def blurring(img):
    "Use gaussian filers for blurring"
    # Blurring image using gaussin filters from scipy
    blurred_img = ndimage.gaussian_filter(img, sigma=3)
    # With higher value of sigma
    very_blurred = ndimage.gaussian_filter(img, sigma=9)
    # Blurring image using uniform filter from scipy
    local_mean = ndimage.uniform_filter(img, size=11)
    # Plotting the result in a matplotlib figure
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
    # Blurring image using gaussin filter from scipy
    blurred_img = ndimage.gaussian_filter(img, 3)
    # Filtering blurred image using gaussian filter
    filter_blurred_img = ndimage.gaussian_filter(blurred_img, 1)
    # Sharpening image a blurred image by adding a Laplacian approximation to increase the weight of the edges
    sharpened = blurred_img + alpha * (blurred_img - filter_blurred_img)  
    # Plotting the result in a matplotlib figure
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
    # Applying noise on the image 
    noisy = img + 0.4*img.std()*np.random.random(img.shape)
    # Smoothing noise and the edges using a Gaussian filter
    gauss_denoised = ndimage.gaussian_filter(noisy, 2)
    # Smoothing noise and the edges using a Median filter
    med_denoised = ndimage.median_filter(noisy, 3)
    # Plotting the result in a matplotlib figure
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
    