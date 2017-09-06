 #coding=utf-8 
from sklearn.tree import DecisionTreeRegressor  
from sklearn.ensemble import RandomForestRegressor  
import numpy as np  
from sklearn.datasets import load_iris  
iris=load_iris() 
rf=RandomForestRegressor() 
rf.fit(iris.data[:350],iris.target[:350])
instance=iris.data[50]  
print instance  
print 'prediction score:'+str(iris.target[50])
print 'real score:'+str(rf.predict(instance))       