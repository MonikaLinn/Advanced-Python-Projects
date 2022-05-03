
#Changes I made include, changing the original photo 4 different times, the first red invert, the second blue invert, and the third green invert
#And lastly I changed the third photo to half of its original size, original being 1280 x 720 and the revised is 640 x 360. 

import image
from PIL import Image

def negativePixel(oldPixel, box):
    
    if box == 0:
        #Red Invert
        Red = 160
        Green = 255 - oldPixel.getGreen()
        Blue = 255 - oldPixel.getBlue()
    elif box == 1:
        #Blue Invert
        Red = 255 - oldPixel.getRed()
        Green = 100
        Blue = 255 - oldPixel.getBlue()
    elif box == 2:
        #Green Invert
        Red = 255 - oldPixel.getRed()
        Green = 255 - oldPixel.getGreen()
        Blue = 130
    
    newRed = Red
    newGreen = Green
    newBlue = Blue
    newPixel = image.Pixel(newRed, newGreen, newBlue)
    return newPixel

def makeNegative(imageFile):
    oldImage = image.FileImage(imageFile)
    width = oldImage.getWidth()
    height = oldImage.getHeight()
    myImageWindow = image.ImageWin(width * 2, height * 2, title="Assignment3")
    #double the width to show original and negative in same window
    oldImage.draw(myImageWindow)
    newIm = image.EmptyImage(width, height)
    #top right
    for row in range(height): #for each row
        for col in range(width): #we will reverse the pixles in entire column
            oldPixel = oldImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel,0)
            newIm.setPixel(col, row, newPixel)
            
    newIm.setPosition(width + 1, 0)
    newIm.draw(myImageWindow)
    newIm.save('Red Invert.jpg')
    #Bottom Left
    newIm1 = image.EmptyImage(width, height)
    for row in range(height): #for each row
        for col in range(width): #we will reverse the pixles in entire column
            oldPixel = oldImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel,1)
            newIm1.setPixel(col, row, newPixel)
    newIm1.setPosition(0, height + 1)
    newIm1.draw(myImageWindow)
    newIm1.save('Green Invert.jpg')
    #Bottom Right
    newIm2 = image.EmptyImage(width, height)
    for row in range(height): #for each row
        for col in range(width): #we will reverse the pixles in entire column
            oldPixel = oldImage.getPixel(col, row)
            newPixel = negativePixel(oldPixel,2)
            newIm2.setPixel(col, row, newPixel)
    newIm2.setPosition(width + 1, height + 1)
    newIm2.draw(myImageWindow)
    newIm2.save('Blue Invert.jpg')

def changeSize(imageFile):
    image = Image.open(imageFile)
    new_image = image.resize((640, 360))
    new_image.show('Small Image.jpg')
    image.save('Small Image.jpg')

    print(image.size)
    print(new_image.size)

def main():
   makeNegative("python.jpg")
   changeSize("Blue Invert.jpg")

main()