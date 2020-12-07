from sklearn import datasets
from sklearn import neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
import numpy as np

iris = datasets.load_iris()

x = iris.data

y = iris.target

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=.3)

knn = neighbors.KNeighborsClassifier()

knn.fit(x_train, y_train)

predictions = knn.predict(x_test)

print(accuracy_score(y_test, predictions))

with open('./model.pkl', 'wb') as model_pkl:
    pickle.dump(knn, model_pkl)

new_record = np.array([[1.2, 1.6, 1.8, 2.4]])

predict_result = knn.predict(new_record)

print('Predicted result for observation ' + str(new_record) + ' is: ' + str(predict_result))