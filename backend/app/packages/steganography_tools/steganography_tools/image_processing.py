#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Steganography-Tools - A Python steganography module.
# Copyright (C) 2021 Sébastien Mascha - https://smascha.ai
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
