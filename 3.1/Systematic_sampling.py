import random  
 
def SystematicSampling(dataMat,number):      
      
       length=len(dataMat)  
       k=length/number  
       sample=[]       
       i=0  
       if k>0 :         
         while len(sample)!=number:  
            sample.append(dataMat[0+i*k])  
            i+=1              
         return sample  
       else :  
         return RandomSampling(dataMat,number)     