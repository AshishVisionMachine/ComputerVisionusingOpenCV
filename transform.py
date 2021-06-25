import numpy as np

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