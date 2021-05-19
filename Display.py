import cv2
import matplotlib.pyplot as plt
import numpy as np
import datasetutility from Datautility

input_with_noise="test_morpho_2.png"
test_input="test.jpeg"
limit_start=1
import Machinconfig

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
    
    
    def Display_dot(self,colour,range,colour_aplpahbet,color_symbol):
        
        datasetutil=datasetutility()
        knn_traindata=datasetutil.knn_trainingdata(Machinconfig.knn_start,Machinconfig.knn_range,Machinconfig.knn_datapoint)
        colour=knn_traindata[responses.ravel()==0]
        plt.scatter(colour[:,0],colour[:,1],range,colour_aplpahbet,color_symbol)
        plt.show()

        
        
    