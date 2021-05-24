import Machinconfig
from Datautility import datasetutility
from knn_train import knntrain
from Display import Display
height=320
width=240
Input_image="knn"
color_symbol=["^","s"]
colour_aplpahbet=["b","r"]
val_range=80
colour=["red","blue"]
knn=None


def test_knn():
    print("Nearest neighbour aproach")
    data_utility=datasetutility()
    train_data=data_utility.knn_trainingdata(Machinconfig.knn_start,Machinconfig.knn_range,Machinconfig.knn_datapoint)
    train_label=data_utility.knn_trainlabel(Machinconfig.knn_start,Machinconfig.knn_range,Machinconfig.knn_datapoint)
    
    dis_obj=Display(Input_image,height,width)
    dis_obj.Display_dot(colour,val_range,colour_aplpahbet,color_symbol)
    knn_new_point=data_utility.knn_trainingdata(Machinconfig.knn_start,Machinconfig.knn_new_point,Machinconfig.knn_new_data_point)

    
    knntr=knntrain(knn)
    knntr.knn_train(train_data,train_label)
    ret, results, neighbours ,dist=knntr.knn_predict(knn_new_point,Machinconfig.kvalue)
    
    print("resulr : {} neighbours: {} distance: {} ".format(results,neighbours,dist))
    

    
    
    

if __name__ == "__main__":
    test_knn()
