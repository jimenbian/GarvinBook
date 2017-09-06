def width(lst):  
    i=0  
    for j in lst[0]:  
       i=i+1  
    return i         
def AutoNorm(mat):     
    n=len(mat)  
    m= width(mat)       
    MinNum=[9999999999]*m  
    MaxNum = [0]*m      
    for i in mat:  
        for j in range(0,m):  
            if i[j]>MaxNum[j]:  
                MaxNum[j]=i[j]  
        
    for p in mat:       
        for q in range(0,m):  
            if p[q]<=MinNum[q]:  
                    MinNum[q]=p[q]    
                            
    section=list(map(lambda x: x[0]-x[1], zip(MaxNum, MinNum)))  
    print section  
    NormMat=[]  
       
    for k in mat:       
               
          distance=list(map(lambda x: x[0]-x[1], zip(k, MinNum)))  
          value=list(map(lambda x: x[0]/x[1], zip(distance,section)))  
          NormMat.append(value)             
    return NormMat    