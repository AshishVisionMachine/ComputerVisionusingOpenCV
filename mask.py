import numpy as np
import cv2
from random import randint
from ImageFilter import ImageFilter

input_with_noise="test_morpho_2.png"
test_input="test.jpeg"
kernel=np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)
pixelupper_saturation=255
pixellower_saturation=0
borderType = cv2.BORDER_CONSTANT
Input_image="Input"
testfunt="Tophat"
height=380
width=240




class Imagemask:
    def __init__(self,image_name,height,width):
        self.image_name=image_name
        self.imfilter=ImageFilter(Input_image,height,width)
        self.height=height
        self.width=width
        
    def twodfilter(self,image):
        filter_image=cv2.filter2D(image,-1,kernel)
        
        return filter_image
        
        
    
    def twodkernel(self):
        kernel=np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)
        
        return kernel
        
  
        
    def saturation_filter(self,pixelsum):
        if pixelsum>pixelupper_saturation:
            pixelsum=pixelupper_saturation
        if pixelsum <pixellower_saturation:
            pixelsum=pixellower_saturation
            
        return pixelsum     

    def Image_Saturation_conversion(self,input_image):
        height, width,ch = input_image.shape
        print("{}  {}  {} {} ".format(height,width,ch,height*width*ch))
        result=[]
        for k in range(3):
            for i in range(height):
                for j in range(width):
                    result.append(self.saturation_filter(input_image[i][j][k]))
                    
        return result        
        
        
    def bilateral_filter(self, image, filter):
        bilateral_blur = cv2.bilateralFilter(image,9,image.shape[0],image.shape[1])
        
        return bilateral_blur
        
    def image_border(self,image):
        top = int(0.05 * image.shape[0]) 
        bottom = top
        left = int(0.05 * image.shape[1])  
        right = left
        value = [randint(0, 255), randint(0, 255), randint(0, 255)]
        
        dst = cv2.copyMakeBorder(image, top, bottom, left, right, borderType, None, value)
        
        
        return dst
    
    def sobelfilter(self,image,config) :
    
        img = self.imfilter.GaussianFilter(image, self.height, self.width, 0.5)    
        img = cv2.cvtColor(img, cv.COLOR_BGR2GRAY)
        #cv2.Sobel(image, ddepth, 1, 0, ksize=3, scale=config.scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        grad_x = cv2.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)

        grad_y = cv2.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
        abs_grad_x = cv2.convertScaleAbs(grad_x)
        abs_grad_y = cv2.convertScaleAbs(grad_y)
        grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
    

