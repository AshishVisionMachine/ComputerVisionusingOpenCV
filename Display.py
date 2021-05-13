import cv2
import matplotlib.pyplot as plt

input_with_noise="input_noise.jpg"
test_input="test.jpeg"
limit_start=1
limit_end=4

class Display:

    def __init__(self,name, height,width):
        self.name=name
        self.height=height
        self.width=width
        
    def Image_read(self):
        im=cv2.imread(input_with_noise)
        return im
    
    def display_image(self,image):
        
        cv2.imshow(self.name,image)
        cv2.waitKey(0)
        cv2.destroyAllWindow()
        
    def Display_plot(self,Image_title,Imageset,imagenum):
        for i in range(imagenum):
            plt.subplot(limit_start,limit_end,i+1), plt.imshow(Imageset[i],"gray")
            plt.xticks([]),plt.yticks([])
            
        plt.show()
    