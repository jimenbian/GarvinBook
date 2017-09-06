from numpy import *
import matplotlib.pyplot as plt
def kMeans(dataSet, k):
    m = shape(dataSet)[0]
    n = shap(dataSet)[1]
    clusterAssment = mat(zeros((m,2)))                                     
    for index in range(k):
       centroids[:,index]=mat(5+5*random.rand(k,1))    
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf; minIndex = -1
            for j in range(k):
                vecA=array(centroids)[j,:]
                vecB=array(dataSet)[i,:]
                distJI=sqrt(sum(power(vecA - vecB, 2)))
               
                if distJI < minDist:
                    minDist = distJI; minIndex = j
            if clusterAssment[i,0] != minIndex: clusterChanged = True
            clusterAssment[i,:] = minIndex,minDist**2
        for cent in range(k):
                ptsInClust=    dataSet[nonzero(array(clusterAssment)[:,0]==cent)[0][0]]
                centroids[cent,:] = mean(ptsInClust, axis=0) 
    id=nonzero(array(clusterAssment)[:,0]==cent)[0]
    return centroids, clusterAssment,id
