

class transform:
    def __init__(self,flag=True):
        self.flag=True
        
    def remapping_image(self,image,height,width):   
        new_img=[]
        print("transofm image heigh and width before transofrm in {} and {}".format(height,width))
        for i in range(height):
            for j in range(width):
                new_img[i][width-j/2-1]=image[i][j]
    
        return new_img