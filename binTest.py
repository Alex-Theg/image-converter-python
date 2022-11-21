#!/usr/bin/env python3

from PIL import Image
from numpy import asarray
import imgLib

imageURL = 'BlackBlock_6x6.png'

imageRGB = Image.open(imageURL)
imageBW = imageRGB.convert("L")

imgArrayBW = asarray(imageBW)

binnedArray = imgLib.binArray(imgArrayBW, 2, 3)

print(binnedArray)

print('')

print(imgArrayBW)