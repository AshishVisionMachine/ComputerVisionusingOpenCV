import cv2
class knntrain:

    def __init__(self,knn):
        self.knn = cv2.ml.KNearest_create()
        
    def knn_train(self,train_data,label):
        self.knn.train(train_data, cv2.ml.ROW_SAMPLE, label)
        
    def knn_predict(self,predictionpoint,kvalue):
        ret, results, neighbours ,dist=self.knn.findNearest(predictionpoint,kvalue)
        
        return ret, results, neighbours ,dist