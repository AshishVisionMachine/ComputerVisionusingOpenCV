import numpy as np
import cv2
class transform:
    def __init__(self,flag=True):
        self.flag=True
        
    def remapping_image(self,image,height,width):   
        new_img=[]#np.zeros((height,width),int)
        img_x=np.zeros((image.shape[0],image.shape[1]),dtype=np.float32)
        img_y=np.zeros((image.shape[0],image.shape[1]),dtype=np.float32)
        print("transofm image heigh and width before transofrm in {} and {}".format(height,width))
        for i in range(image.shape[0]):
            for j in range(image.shape[1]):
                if (j>img_x.shape[1] *0.25 and j<img_x.shape[1]*0.75 and i>img_x.shape[0]*0.25 and i<img_x.shape[1]*0.75):
                    img_x[i,j]=2 * (j-img_y.shape[1]*0.25) + 0.5
                    img_y[i,j]=2 * (i-img_y.shape[0]*0.25) + 0.5
                else:
                    img_x[i,j]=0
                    img_y[i,j]=0
    
        return img_x,img_y
        
    def remapping_image_180(self,image,height,width):   
        new_img=[]#np.zeros((height,width),int)
        img_x=np.zeros((image.shape[0],image.shape[1]),dtype=np.float32)
        img_y=np.zeros((image.shape[0],image.shape[1]),dtype=np.float32)
        print("transofm image heigh and width before transofrm in {} and {}".format(height,width))
        
        for i in range(img_x.shape[0]):
            img_x[i,:]=[img_x.shape[1]-x for x in range(img_x.shape[1])]
        for j in range(img_y.shape[1]):
            img_y[:,j]=[y for y in range(img_y.shape[0])]    
            
            
        return img_x,img_y    
        
    def remapping_image_360(self,image,height,width):   
        new_img=[]#np.zeros((height,width),int)
        img_x=np.zeros((image.shape[0],image.shape[1]),dtype=np.float32)
        img_y=np.zeros((image.shape[0],image.shape[1]),dtype=np.float32)
        print("transofm image heigh and width before transofrm in {} and {}".format(height,width))
        
        for i in range(img_x.shape[0]):
            img_x[i,:]=[img_x.shape[1]-x for x in range(img_x.shape[1])]
        for j in range(img_y.shape[1]):
            img_y[:,j]=[img_y.shape[0]-y for y in range(img_y.shape[0])]    
            
            
        return img_x,img_y    

    def Img_warpAffine(self,image,height,width):   
        new_img=[]#np.zeros((height,width),int)
        srcTri = np.array( [[0, 0], [image.shape[1] - 1, 0], [0, image.shape[0] - 1]] ).astype(np.float32)
        dstTri = np.array( [[0, image.shape[1]*0.33], [image.shape[1]*0.85, image.shape[0]*0.25], [image.shape[1]*0.15, image.shape[0]*0.7]] ).astype(np.float32)
        
        warp_mat = cv2.getAffineTransform(srcTri, dstTri)
        warp_dst = cv2.warpAffine(image, warp_mat, (image.shape[1], image.shape[0]))

            
        return warp_dst          