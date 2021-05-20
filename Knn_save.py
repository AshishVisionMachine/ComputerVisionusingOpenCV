import Machinconfig
from Datautility import datasetutility
from Display import Display
height=320
width=240
Input_image="knn"
color_symbol=["^","s"]
colour_aplpahbet=["b","r"]
val_range=80
colour=["red","blue"]

def test_knn():
    print("Nearest neighbour aproach")
    data_utility=datasetutility()
    #train_data=data_utility.knn_trainingdata(Machinconfig.knn_start,Machinconfig.knn_range,Machinconfig.knn_datapoint)
    #train_label=data_utility.knn_trainlabel(Machinconfig.knn_start,Machinconfig.knn_range,Machinconfig.knn_datapoint)
    
    dis_obj=Display(Input_image,height,width)
    dis_obj.Display_dot(colour,val_range,colour_aplpahbet,color_symbol)

    
    
    

if __name__ == "__main__":
    test_knn()
