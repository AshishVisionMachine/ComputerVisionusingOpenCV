import numpy as np
import cv2
input_with_noise="test_morpho_2.png"
test_input="test.jpeg"
kernel=np.array([[0, -1, 0],[-1, 5, -1],[0, -1, 0]], np.float32)


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
        
  
        
        