from numpy import *  
  
def pca(dataMat, dimen):  
    meanVals = mean(dataMat, axis=0)  
    meanRemoved = dataMat - meanVals 
    covMat = cov(meanRemoved, rowvar=0)  
    Vals,Vects = linalg.eig(mat(covMat))  
    ValInd = argsort(Vals)            
    ValInd = ValInd[:-(topNfeat+1):-1] 
    redEigVects = Vects[:,ValInd]      
    lowDDataMat = meanRemoved * redEigVects  
    return lowDDataMat 
 