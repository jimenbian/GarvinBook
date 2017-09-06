import random
def RandomSampling(dataMat,number):  
    try:  
         slice = random.sample(dataMat, number)      
         return slice  
    except:  
         print 'sample larger than population'  
  
def RepetitionRandomSampling(dataMat,number):      
    sample=[]  
    for i in range(number):  
         sample.append(dataMat[random.randint(0,len(dataMat)-1)])  
    return sample  