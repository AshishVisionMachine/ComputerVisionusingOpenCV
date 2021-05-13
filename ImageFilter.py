import cv2
class ImageFilter:
    
    def __init__(self,name, height,width):
        self.name=name
        self.height=height
        self.width=width
        
    def GaussianFilter(self,img,kheight,kwidth,std_dev):
        Fltimg=cv2.GaussianBlur(img,(kheight,kwidth),std_dev)
        return Fltimg
        
        
    def MedianFiler(self,img,ksize):
        Fltimg=cv2.medianBlur(img,ksize)
        return Fltimg
        
    def bilateralFilter(self,img,width,sigmacolor,sigmaspace):
        Fltimg=cv2.bilateralFilter(img,width,sigmacolor,sigmaspace)
        return Fltimg