import numpy as np
import cv2
input_with_noise="test_morpho_2.png"
test_input="test.jpeg"
kernel=np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)
pixelupper_saturation=255
pixellower_saturation=0


class Imagemask:
    def __init__(self,image_name,height,width):
        self.image_name=image_name
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
        print("{}  {}  {} ".format(height,width,ch))
        result=[]
        for k in range(3):
            for i in range(height-1):
                for j in range(width-1):
                    result[i][j][k]=self.saturation_filter(input_image[i][j][k])
                    
        return result        