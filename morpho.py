import cv2
import numpy as np

class morplological:
    
    def __init__(self,img, kernal,iteration):
        self.image=img
        self.kernel=kernal
        self.iteration=iteration
    
    def Erosion(self):
        kernel_val = np.ones((self.kernel,self.kernel),np.uint8)    
        image=cv2.erode(self.image,kernel_val,self.iteration)
        
        return image
        
    def Dialation(self):
        kernel_val = np.ones((self.kernel,self.kernel),np.uint8) 
        dilation = cv2.dilate(self.image,kernel_val,self.iteration)
        
        return dilation
        
        