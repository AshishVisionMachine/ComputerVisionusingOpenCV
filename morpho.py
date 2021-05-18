import cv2
import numpy as np
Kernel_iteration=7

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
        
    def Opening(self):
        for i in range(Kernel_iteration):
            ima_erosion=self.Erosion()
            self.image=ima_erosion
            self.image=self.Dialation()
        
        return self.image
            
    def Closing(self):
        for i in range(Kernel_iteration):
            ima_erosion=self.Dialation()
            self.image=ima_erosion
            self.image=self.Erosion()
        
        return self.image
        
    def Morphogradient(self): # Difference of orig image and opening of the image
        kernel_val = np.ones((self.kernel,self.kernel),np.uint8) 

        self.image=cv2.morphologyEx(self.image, cv2.MORPH_GRADIENT,kernel_val)
        
        return self.image
        
    def Tophat(self):
        kernel_val = np.ones((self.kernel,self.kernel),np.uint8) 

        self.image=cv2.morphologyEx(self.image, cv2.MORPH_TOPHAT,kernel_val)
        
        return self.image
    
    def Blackhat(self): # Difference of orig image and closing of the image 
        kernel_val = np.ones((self.kernel,self.kernel),np.uint8) 

        self.image=cv2.morphologyEx(self.image, cv2.MORPH_BLACKHAT,kernel_val)
        
        return self.image
    