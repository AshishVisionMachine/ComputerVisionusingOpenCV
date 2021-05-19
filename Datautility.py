
class datasetutility :
    def __init__(self,type):
        self.type=type
        
    def knn_trainingdata(self,start,range ,datapoints):
        
        trainData = np.random.randint(start,range,(datapoints,2)).astype(np.float32)
        
        return trainData
        
    def knn_trainlabel(self,start,range,datapoints):
        responses = np.random.randint(start ,range,(datapoints,1)).astype(np.float32)
        
        return responses

