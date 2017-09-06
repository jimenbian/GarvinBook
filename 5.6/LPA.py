from sklearn import datasets
from sklearn.semi_supervised import LabelPropagation
import numpy as np
label_prop_model = LabelPropagation()
iris = datasets.load_iris()
print iris
random_unlabeled_points = np.where(np.random.randint(0, 2,size=len(iris.target)))
labels = np.copy(iris.target)
labels[random_unlabeled_points] = -1

label_prop_model.fit(iris.data, labels)
index=0
for i in range(0,len(iris['target'])):
     if (iris['target'][i])==(label_prop_model.predict(iris.data)[i]):
        index=index+1
print 'The right number of prediction:'+str(index)
print 'The total number of dataset:'+str(len(iris['target']))        