from PIL import Image
import numpy as np
import sys
import ctypes

if len(sys.argv) < 2:
    exit()

# Get screen resolution
# Takes into account character size 
user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
screenWidth, screenHeight = user32.GetSystemMetrics(0) / 9, user32.GetSystemMetrics(1) / 9

imgSrc = sys.argv[1]

imgOriginal = Image.open(imgSrc)
imgWidth, imgHeight = imgOriginal.size

# Resize image to fit in command prompt console with font size 5
if imgWidth > screenWidth:
    scaleFactor = screenWidth / imgWidth
    imgWidth *= scaleFactor
    imgHeight *= scaleFactor

if imgHeight > screenHeight:
    scaleFactor = screenHeight / imgHeight
    imgWidth *= scaleFactor
    imgHeight *= scaleFactor

imgResize = imgOriginal.resize((int(imgWidth), int(imgHeight)))

imgLuminosity = imgResize.convert('L')
imgArray = np.array(imgLuminosity).astype('str')

asciiEquiv = {
    252: '$',
    248: '@',
    244: 'B',
    240: '%',
    236: '8',
    232: '&',
    228: 'W',
    224: 'M',
    220: '#',
    216: '/',
    212: 'o',
    208: 'a',
    204: 'h',
    200: 'k',
    196: 'b',
    192: 'd',
    188: 'p',
    184: 'q',
    180: 'm',
    176: 'Z',
    172: 'O',
    168: '0',
    164: 'Q',
    160: 'L',
    156: 'C',
    152: 'J',
    148: 'U',
    144: 'Y',
    140: 'X',
    136: 'z',
    132: 'c',
    128: 'v',
    124: 'u',
    120: 'n',
    116: 'x',
    112: 'r',
    108: 'j', 
    104: 'f',
    100: 't',
    96: '|',
    92: '\\',
    88: '*',
    84: '(',
    80: '1',
    76: '{',
    72: '[',
    68: '?',
    64: '-',
    60: '_',
    56: '+',
    52: '~',
    48: '<',
    44: 'i',
    40: '!',
    36: 'l',
    32: 'I',
    28: ';',
    24: ':',
    20: ',',
    16: '"',
    12: '^',
    8: '`',
    4: '\'',
    0: '.'
}

# Convert pixel to ASCII character according to luminosity
for rowIndex in range(len(imgArray)):
    for pixelIndex in range(len(imgArray[rowIndex])):
        for luma in asciiEquiv:
            if int(imgArray[rowIndex][pixelIndex]) > luma:
                imgArray[rowIndex][pixelIndex] = asciiEquiv[luma]
                break

# Output to console
for row in imgArray:
    rowString = ''
    for pixel in row:
        rowString += pixel * 2
    print(rowString)

input()