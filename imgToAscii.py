#!/usr/bin/env python3

from PIL import Image
from numpy import asarray
import imgLib

highDefinition = False
# imageURL = 'WhiteBlock.png'
# imageURL = 'BlackBLock.png'
imageURL = 'Sample.png'

# 70 levels of gray
gscale1 = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
 
# 10 levels of gray
gscale2 = '@%#*+=-:. '

imageRGB = Image.open(imageURL)
imageBW = imageRGB.convert("L")

imgArrayBW = asarray(imageBW)

binnedImage = imgLib.binArray(imgArrayBW, 2, 3)

convertedArray = ''

for x in binnedImage:
    for y in x:
        if highDefinition:
            gsval = gscale1[int((y*69)/255)]
        else:
            gsval = gscale2[int((y*9)/255)]
        convertedArray += gsval
    convertedArray += '\n'


print(convertedArray)

