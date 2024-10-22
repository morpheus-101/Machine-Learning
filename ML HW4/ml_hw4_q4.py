# -*- coding: utf-8 -*-
"""ML_hw4_q4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RASk9C30zEJLp6W699l1pM1fIoCjxUNF
"""

# Commented out IPython magic to ensure Python compatibility.
import tensorflow as tf
from tensorflow import keras
fashion_mnist = keras.datasets.fashion_mnist
(train_images, train_labels),(test_images, test_labels) = fashion_mnist.load_data()
import matplotlib.pyplot as plt
import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
# %matplotlib inline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import time
import seaborn as sns
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn import svm

print(f'Number of training images = {len(train_images)}')
print(f'Number of test images = {len(test_images)}')

print(f'Size of every image = {train_images[0].shape}')

"""Reshaping the dataset"""

img_x, img_y = 28, 28
train_imgs = train_images.reshape(train_images.shape[0], img_x, img_y, 1)
test_imgs = test_images.reshape(test_images.shape[0], img_x, img_y, 1)
input_shape = (img_x, img_y, 1)

print('The train image dataset has shape:', train_imgs.shape)
print('The test image dataset has shape:',test_imgs.shape)

"""Normalizing the dataset"""

train_imgs = train_imgs / 255.0
test_imgs = test_imgs / 255.0

training_size = 6000
test_size = 1000

x_train_filter, y_train_filter = np.empty(shape=(training_size, 28, 28, 1)), []

for label in list(set(train_labels)):
    sample_filter = np.where((train_labels == label))
    x_train_filter = np.append(x_train_filter, np.array(train_imgs[sample_filter][:training_size]), axis=0)
    y_train_filter += [label]*training_size
    
x_train_filter = x_train_filter[training_size:,:,:]

plt.figure(figsize=(20,20))
for i in range(0,35000,100):
    plt.subplot(10,35,i/100+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train_filter[i].reshape(28, 28), cmap=plt.cm.binary)
    plt.xlabel(y_train_filter[i])

train_imgs = train_imgs.reshape(training_size*10, 784) #28*28
test_imgs = test_imgs.reshape(test_size*10, 784)
train_lbls = np.eye(len(set(train_labels)))[train_labels]

print('The flattened train image dataset has shape:', train_imgs.shape)
print('The flattened test image dataset has shape:',test_imgs.shape)

"""<h2>Logistic regression</h2>

Training the model using logistic regression
"""

# Commented out IPython magic to ensure Python compatibility.
x_train, x_test, y_train, y_test = train_test_split(train_imgs, train_labels, test_size=0.1, random_state=0)
logisticReg = LogisticRegression(max_iter=200, tol=1e-2,solver='saga')

# % time logisticReg.fit(x_train, y_train)
# Time taken 1 min 33s

"""Making predictions, calculating the accuracy, and generating the confusion matrix for the validation set."""

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = logisticReg.predict(x_test)
# Time taken = 34 ms

score = logisticReg.score(x_test, y_test)
print(f'Mean accuracy of the validation data = {score}')

conf_matrix = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

"""Making predictions, calculating the accuracy, and generating the confusion matrix for the test set."""

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = logisticReg.predict(test_imgs)
# Time taken = 55 ms

score = logisticReg.score(test_imgs, test_labels)
print(f'Mean accuracy of the test data = {score}')

conf_matrix = metrics.confusion_matrix(test_labels, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

"""<h2>K nearest neighbours</h2>

Training the model using K nearest neighbour
"""

# Commented out IPython magic to ensure Python compatibility.
x_train, x_test, y_train, y_test = train_test_split(train_imgs, train_labels, test_size=0.1, random_state=0)
KNN = KNeighborsClassifier(n_neighbors=5,algorithm='auto',n_jobs=10)

# % time KNN.fit(x_train, y_train)
#  Time taken = 10 s

"""Making predictions, calculating the accuracy, and generating the confusion matrix for the validation set."""

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = KNN.predict(x_test)
# Total time = 11 min 37 s

score = KNN.score(x_test, y_test)
print(f'Mean accuracy of the validation data = {score}')

conf_matrix = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = KNN.predict(test_imgs)
# Time taken = 19 min 15 s

score = KNN.score(test_imgs, test_labels)
print(f'Mean accuracy of the test data = {score}')

conf_matrix = metrics.confusion_matrix(test_labels, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

"""<h2>Support vector machines with linear kernel</h2>"""

# Commented out IPython magic to ensure Python compatibility.
x_train, x_test, y_train, y_test = train_test_split(train_imgs, train_labels, test_size=0.1, random_state=0)
svc = svm.SVC(probability=False,kernel="linear",C=2.8,gamma=0.0073)
# % time svc.fit(x_train,y_train)
# Time taken = 14 mins 48s

"""Making predictions, calculating the accuracy, and generating the confusion matrix for the validation set."""

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = svc.predict(x_test)
# Total time = 2 min 7 s

score = svc.score(x_test, y_test)
print(f'Mean accuracy of the validation data = {score}')

conf_matrix = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = svc.predict(test_imgs)
# Time taken = 3 min 31s

score = svc.score(test_imgs, test_labels)
print(f'Mean accuracy of the test data = {score}')

conf_matrix = metrics.confusion_matrix(test_labels, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

"""<h2>Support vector machines with rbf kernel</h2>"""

# Commented out IPython magic to ensure Python compatibility.
x_train, x_test, y_train, y_test = train_test_split(train_imgs, train_labels, test_size=0.1, random_state=0)
svc = svm.SVC(probability=False,kernel="rbf",C=2.8,gamma=0.0073)
# % time svc.fit(x_train,y_train)
# Time taken = 9 min 47 sec

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = svc.predict(x_test)
# Total time = 

score = svc.score(x_test, y_test)
print(f'Mean accuracy of the validation data = {score}')

conf_matrix = metrics.confusion_matrix(y_test, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

# Commented out IPython magic to ensure Python compatibility.
# % time predictions = svc.predict(test_imgs)
# Time taken = 

score = svc.score(test_imgs, test_labels)
print(f'Mean accuracy of the test data = {score}')

conf_matrix = metrics.confusion_matrix(test_labels, predictions)
plt.figure(figsize=(10,10))
sns.heatmap(conf_matrix, annot=True, square = True)
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
plt.title('Accuracy score: {0}'.format(score, size = 10))

accuracy = [0.845, 0.845, 0.8401, 0.8873]

"""<h3>Part c</h3>

1. Logistic regression

>> Test set Accuracy =  0.845

2. Nearest neighbours

>> Test set Accuracy = 0.8524

3. SVM with linear kernel

>> Test set Accuracy = 0.8401

4. SVM with rbf kernel

>> Test set Accuracy = 0.8873

<h3>Part d</h3>

1. Logistic Regression

>> Train time = 1 min 33 sec

>> Test time = 55 ms

2. K nearest neighbours 

>> Train time = 10 s

>> Test time = 19 min 15 sec

3. SVM with linear kernel

>> Train time = 14 min 48 sec

>> Test time = 3 min 31 sec

4. SVM with rbf kernel

>> Train time = 9 min 47 sec

>> Test time = 3 min 56 sec

By looking at the resuts of part d, we can conclude a few things:

1. Logistic regreesion is the fastest when compared to the rest of the classifiers. Both train and test times are extremely low. We can also see that inspite of being fast, logistic regression gives a decent accuracy.

2. KNN has a very low training time because there is literally no training happening in this stage. All the work is done in the testing stage. Because of this the test time of KNN is the highest amomg the four. Accuracy of KNN is also quite decent.

3. SVM with linear kernel has the largest training time. But the test time is significantly lower than KNN. Accuracy of this comparable with KNN and logistic regression. 

4. SVM with rbf kernel has lesser training time than linear SVM. This algorithm has the highest accuracy among the four. Test time is almost the same as that of linear SVM. 

From these points we can conclue that the fastest algorithm is Logistic regression and the most accurate algorithm is SVM with rbf kernel.
"""

