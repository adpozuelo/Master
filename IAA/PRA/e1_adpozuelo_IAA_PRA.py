from __future__ import print_function
from time import time
import logging
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import PCA
from sklearn.svm import SVC
import numpy as np
import operator

print(__doc__)

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

###############################################################################
# Download the data, if not already on disk and load it as numpy arrays

lfw_people = fetch_lfw_people(min_faces_per_person=70, resize=0.4)

#### Exercise 1-a

# Histogram min_faces=70
d70 = {}
for i in lfw_people.target:
    if lfw_people.target_names[i] in d70: d70[lfw_people.target_names[i]]+=1
    else: d70[lfw_people.target_names[i]]=1
#print(d70)

# Plot histogram of person image's number
fig = plt.figure()
ax1 = fig.add_subplot(221)
X = np.arange(len(d70))
ax1.bar(X, d70.values(), align='center', width=0.5)
ax1.set_title("Histogram of person image's number (min_faces=70)")

#### Exercise 1-b

lfw_people = fetch_lfw_people(min_faces_per_person=40, resize=0.4)
# Histogram min_faces=40
d40 = {}
for i in lfw_people.target:
    if lfw_people.target_names[i] in d40: d40[lfw_people.target_names[i]]+=1
    else: d40[lfw_people.target_names[i]]=1
#print(d40)
print("People min_faces=40: " + str(len(d40)), end='\n')

# Plot histogram of person image's number
ax2 = fig.add_subplot(222)
X = np.arange(len(d40))
ax2.bar(X, d40.values(), align='center', width=0.5)
ax2.set_title("Histogram of person image's number (min_faces=40)")

# Histogram min_faces=40 - min_faces=70
d40m70={}
for i in d40:
    if i not in d70: d40m70[i]=d40[i]
#print(d40m70)
print("New people min_faces=40 not in min_faces=70")
print(d40m70.keys(), end='\n')

# Plot histogram of person image's number
ax2 = fig.add_subplot(223)
X = np.arange(len(d40m70))
ax2.bar(X, d40m70.values(), align='center', width=0.5)
ax2.set_title("Histogram of person image's number (min_faces=40, not in 70)")
plt.show()

print("Sorted people by number of images")
sorted_d40 = sorted(d40.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_d40, end='\n')

#### Exercise 1-c

min_faces=[40, 70]
for mf in min_faces:
    lfw_people = fetch_lfw_people(min_faces_per_person=mf, resize=0.4)

    # introspect the images arrays to find the shapes (for plotting)
    n_samples, h, w = lfw_people.images.shape
     
    # for machine learning we use the 2 data directly (as relative pixel
    # positions info is ignored by this model)
    X = lfw_people.data
    n_features = X.shape[1]
     
    # the label to predict is the id of the person
    y = lfw_people.target
    target_names = lfw_people.target_names
    n_classes = target_names.shape[0]
    print("Total dataset size, min_faces("+str(mf)+"):")
    print("n_samples: %d" % n_samples)
    print("n_features: %d" % n_features)
    print("n_classes: %d" % n_classes)
     
    ###############################################################################
    # Split into a training set and a test set using a stratified k fold
     
    # split into a training and testing set
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42)
     
    ###############################################################################
    # Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
    # dataset): unsupervised feature extraction / dimensionality reduction
    n_components = 150
     
    print("Extracting the top %d eigenfaces from %d faces"
          % (n_components, X_train.shape[0]))
    t0 = time()
    pca = PCA(n_components=n_components, svd_solver='randomized',
              whiten=True).fit(X_train)
    print("done in %0.3fs" % (time() - t0))
     
    eigenfaces = pca.components_.reshape((n_components, h, w))
     
    print("Projecting the input data on the eigenfaces orthonormal basis")
    t0 = time()
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test)
    print("done in %0.3fs" % (time() - t0))
     
    ###############################################################################
    # Train a SVM classification model
     
    print("Fitting the classifier to the training set")
    t0 = time()
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
                  'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
    clf = clf.fit(X_train_pca, y_train)
    print("done in %0.3fs" % (time() - t0))
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)
     
    ###############################################################################
    # Quantitative evaluation of the model quality on the test set
     
    print("Predicting people's names on the test set, min_faces=" + str(mf))
    t0 = time()
    y_pred = clf.predict(X_test_pca)
    print("done in %0.3fs" % (time() - t0))
     
    print(classification_report(y_test, y_pred, target_names=target_names))
    #print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))
      
#### Exercise 1-d

# introspect the images arrays to find the shapes (for plotting)
n_samples, h, w = lfw_people.images.shape
 
# for machine learning we use the 2 data directly (as relative pixel
# positions info is ignored by this model)
X = lfw_people.data
n_features = X.shape[1]
 
# the label to predict is the id of the person
y = lfw_people.target
target_names = lfw_people.target_names
n_classes = target_names.shape[0]
print("Total dataset size, min_faces:")
print("n_samples: %d" % n_samples)
print("n_features: %d" % n_features)
print("n_classes: %d" % n_classes)
 
###############################################################################
# Split into a training set and a test set using a stratified k fold
 
# split into a training and testing set
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.75, random_state=42)
 
###############################################################################
# Compute a PCA (eigenfaces) on the face dataset (treated as unlabeled
# dataset): unsupervised feature extraction / dimensionality reduction
n_components = 150
 
print("Extracting the top %d eigenfaces from %d faces"
      % (n_components, X_train.shape[0]))
t0 = time()
pca = PCA(n_components=n_components, svd_solver='randomized',
          whiten=True).fit(X_train)
print("done in %0.3fs" % (time() - t0))
 
eigenfaces = pca.components_.reshape((n_components, h, w))
 
print("Projecting the input data on the eigenfaces orthonormal basis")
t0 = time()
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)
print("done in %0.3fs" % (time() - t0))
 
###############################################################################
# Train a SVM classification model
 
print("Fitting the classifier to the training set")
t0 = time()
param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],
              'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1], }
clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid)
clf = clf.fit(X_train_pca, y_train)
print("done in %0.3fs" % (time() - t0))
print("Best estimator found by grid search:")
print(clf.best_estimator_)
 
###############################################################################
# Quantitative evaluation of the model quality on the test set
 
print("Predicting people's names on the test set, 75% test set")
t0 = time()
y_pred = clf.predict(X_test_pca)
print("done in %0.3fs" % (time() - t0))
 
print(classification_report(y_test, y_pred, target_names=target_names))
#print(confusion_matrix(y_test, y_pred, labels=range(n_classes)))