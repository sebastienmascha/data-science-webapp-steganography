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

import math

import numpy as np


class LSBSteganographyException(Exception):
    pass


class LSBSteganography():
    """
    Main class to handle Steganography encrypted data.
    """

    def __init__(self, im):
        self.image = im
        # Save the image height, width and the number of channels
        self.height, self.width, self.nbchannels = im.shape
        self.size = self.width * self.height
        
        self.maskONEValues = [1,2,4,8,16,32,64,128]
        # Mask used to put one ex:1->00000001, 2->00000010 .. associated with OR bitwise
        self.maskONE = self.maskONEValues.pop(0)  # Will be used to do bitwise operations
        
        self.maskZEROValues = [254,253,251,247,239,223,191,127]
        # Mak used to put zero ex:254->11111110, 253->11111101 .. associated with AND bitwise
        self.maskZERO = self.maskZEROValues.pop(0)
        
        self.curwidth = 0  # Current width position
        self.curheight = 0 # Current height position
        self.curchan = 0   # Current channel position

    @staticmethod
    def is_inputs_valid(data) -> bool:
        """
        Check if inputs are valid.
        """
        l = len(data)
        if self.width*self.height*self.nbchannels < l+64:
            raise LSBLSBSteganographyException("Carrier image not big enough to hold all the datas to steganography")

    def put_binary_value(self, bits):
        """
        Put the bits in the image
        """
        for c in bits:
            val = list(self.image[self.curheight,self.curwidth])  # Get the pixel value as a list
            if int(c) == 1:
                # How mask is working: https://en.wikipedia.org/wiki/Mask_(computing)
                val[self.curchan] = int(val[self.curchan]) | self.maskONE  # OR with maskONE
            else:
                val[self.curchan] = int(val[self.curchan]) & self.maskZERO  # AND with maskZERO
            self.image[self.curheight,self.curwidth] = tuple(val)  
            self.next_slot()  # Move "cursor" to the next space
        
    def next_slot(self):
        """
        Move to the next slot were information can be taken or put
        """
        if self.curchan == self.nbchannels-1:  # Next Space is the following channel
            self.curchan = 0
            if self.curwidth == self.width-1:  # Or the first channel of the next pixel of the same line
                self.curwidth = 0
                if self.curheight == self.height-1:  # Or the first channel of the first pixel of the next line
                    self.curheight = 0
                    if self.maskONE == 128:  # Mask 1000000, so the last mask
                        raise LSBSteganographyException("No available slot remaining (image filled)")
                    else:  # Or instead of using the first bit start using the second and so on..
                        self.maskONE = self.maskONEValues.pop(0)
                        self.maskZERO = self.maskZEROValues.pop(0)
                else:
                    self.curheight +=1
            else:
                self.curwidth +=1
        else:
            self.curchan +=1

    def read_bit(self): 
        """
        Read a single bit int the image
        """
        val = self.image[self.curheight,self.curwidth][self.curchan]
        val = int(val) & self.maskONE
        self.next_slot()
        if val > 0:
            return "1"
        else:
            return "0"
    
    def read_byte(self):
        return self.read_bits(8)
    
    def read_bits(self, nb): 
        """
        Read the given number of bits
        """
        bits = ""
        for i in range(nb):
            bits += self.read_bit()
        return bits

    def byteValue(self, val):
        return self.binary_value(val, 8)
        
    def binary_value(self, val, bitsize): 
        """
        Return the binary value of an int as a byte
        """
        # bin() returns the binary equivalent string of a given integer e.g. bin(14)=0b1110
        # The prefix 0b represents that the result is a binary string.
        binval = bin(val)[2:]  # Assign the binary value without the prefix
        if len(binval) > bitsize:
            raise LSBSteganographyException("binary value larger than the expected size")
        while len(binval) < bitsize:  # Add zeros until we reach the bitsize
            binval = "0"+binval
        return binval

    def encode_text(self, txt):
        l = len(txt)
        binl = self.binary_value(l, 16)  # Length coded on 2 bytes so the text size can be up to 65536 bytes long
        self.put_binary_value(binl)  # Put text length encoded in the image
        for char in txt:  # And put all the chars
            # Returns the number representing the unicode code of a specified character
            c = ord(char)
            self.put_binary_value(self.byteValue(c))
        return self.image
       
    def decode_text(self):
        ls = self.read_bits(16)  # Read the text size in bytes
        l = int(ls,2)
        i = 0
        unhideTxt = ""
        while i < l:  # Read all bytes of the text
            tmp = self.read_byte()  # So one byte
            i += 1
            unhideTxt += chr(int(tmp,2))  # Every chars concatenated to str
        return unhideTxt


class Compare():
    def __init__(self, img1, img2):
        self.img1 = img1
        self.img2 = img2
    def get_results(self):
        print("meanSquareError: %s" %(self.meanSquareError()))
        print("psnr: %s" %(self.psnr()))
    def correlation(self):
        return signal.correlate2d (self.img1, self.img2)
    def meanSquareError(self):
        error = np.sum((self.img1.astype('float') - self.img2.astype('float')) ** 2)
        error /= float(self.img1.shape[0] * self.img1.shape[1]);
        return error
    def psnr(self):
        mse = self.meanSquareError()
        if mse == 0:
            return 100
        PIXEL_MAX = 255.0
        return 20 * math.log10(PIXEL_MAX / math.sqrt(mse))
