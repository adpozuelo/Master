## Antonio Díaz Pozuelo - IA - PEC2 - adpozuelo@uoc.edu
## Python 3.6

import csv
import numpy as np
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import manifold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB

np.set_printoptions(threshold=np.nan)

## Read data from CSV

def readData(filename):
    with open(filename) as csvfile:  
        result = []
        myreader = csv.reader(csvfile, delimiter = ',')
        header=next(myreader) # Read header
        status_id = header.index('status') # Get status index 
        header[1], header[status_id] = header[status_id], header[1] # Swap status header column by first attribute header
        for row in myreader:
            tmp_result=[float(x) for x in row[1:]]
            tmp_result[status_id-1], tmp_result[0] = tmp_result[0], tmp_result[status_id-1] # Swap status value column by first attribute value
            result.append(tmp_result)
    return header[1:], np.array(result, dtype='float') # Return header (without name column) and data 

## Confusion matrix and results

def confusionMatrixResults(test, predictions, print_results=0):
    confusion_matrix=np.zeros((2,2)) # Define matrix confusion for 2 classes
    for i in range(len(test)):
        if test[i] == predictions[i]:
            if predictions[i] == 0:
                confusion_matrix[0,0]+=1 # True positive (tp)
            elif predictions[i] == 1:
                confusion_matrix[1,1]+=1 # True negative (tn)
        elif test[i] == 0 and predictions[i] == 1:
            confusion_matrix[1,0]+=1 # False negative (fn)
        elif test[i] == 1 and predictions[i] == 0:
            confusion_matrix[0,1]+=1 # False positive (fp)
    error=(confusion_matrix[1,0]+confusion_matrix[0,1])/(sum(sum(confusion_matrix))) # e=(fp+fn)/(tp+fp+fn+tn)
    accuracy=(confusion_matrix[0,0]+confusion_matrix[1,1])/(sum(sum(confusion_matrix))) # a=(tp+tn)/(tp+fp+fn+tn)
    if print_results == 1: # If print results is requested
        print("Confusion matrix")
        print(confusion_matrix) # Print confusion matrix
        print("Error: " + str(error)) # Print results
        print("Accuracy: " + str(accuracy))
        print()
    return error, accuracy # Return error and accuracy.

## Generate training and test sets

def get_training_and_test_sets(data):
    c0=0; c1=0 # Classes's elements counters
    for i in data[:,0]:
        if int(i)==1:
            c1+=1
        elif int(i)==0:
            c0+=1
    min_elements=min(c0,c1) # Min elements in classes, max number of elements in training+test sets
    training_elements=int(min_elements*0.8) # 80% of elements for training
    test_elements=min_elements-training_elements # 20% of elements for test
    training_set_c0=list(); training_set_c1=list(); test_set_c0=list(); test_set_c1=list() # Test and training sets by class
    for i in data: # Access to data
        if int(i[0]) == 1 and len(training_set_c1) < training_elements:
            training_set_c1.append(i) # Add training elements for class 1
        elif int(i[0]) == 1 and len(training_set_c1) >= training_elements and len(test_set_c1) < test_elements:
            test_set_c1.append(i) # Add test elements for class 1
        if int(i[0]) == 0 and len(training_set_c0) < training_elements:
            training_set_c0.append(i) # Add training elements for class 0
        elif int(i[0]) == 0 and len(training_set_c0) >= training_elements and len(test_set_c0) < test_elements:
            test_set_c0.append(i) # Add test elements for class 0
    training_set=np.array(training_set_c0+training_set_c1) # Join class 0 an 1 elements to final training elements
    test_set=np.array(test_set_c0+test_set_c1) # Join class 0 an 1 elements to final test elements
    return training_set, test_set # Return training and test sets

## Exercise 1

header, data = readData('parkinson.csv') # Read CSV file

## Exercise 1 part a)

# Check if normalization is needed, uncomment it to show graph

print("Exercise 1 part a")
dataMean = data.mean(axis=0) # Mean of columns (attributes)
dataStd = data.std(axis=0) # Standard desviation of columns (attributes)
plt.errorbar(range(len(header[1:])), dataMean[1:], dataStd[1:], linestyle='None', marker='^') # Error bar
plt.title("Error bar")
plt.ylabel("Mean and starndard desviation")
plt.xlabel("Components")
plt.show() # Plot error bar

## Exercise 1 part b)

total_components=len(header[1:]) # Avoid status values (column 0). Get all components
pca = PCA(n_components=total_components)
pca.fit(data[:,1:]) # Avoid status values (column 0). Apply PCA to data with all components
#print(sum(pca.explained_variance_ratio_)) # Check that total variance is 1.0, OK!!

nf_components = 0 # Variance components needed
accumulator = 0.0 # Variance accumulator

while accumulator<=0.95: # While variance is less or equal than 95%
    accumulator+=pca.explained_variance_ratio_[nf_components] # Accumulate variance
    nf_components+=1 # Add one component

# Print results
print()
print("Exercise 1 part b")
print("Components needed for at least 95% of variance: " + str(nf_components)) 
print(pca.explained_variance_ratio_[:nf_components])
print("Variance with " + str(nf_components) + " components: " + str(sum(pca.explained_variance_ratio_[:nf_components])))
print()

## Exercise 1 part c)

total_components=[4, 8] # Components requested 
print("Exercise 1 part c")
for c in total_components:
    pca = PCA(n_components=c)
    dataPAC_transformed = pca.fit_transform(data[:,1:]) # Apply PCA and transforms data
    dataPAC_inversed = pca.inverse_transform(dataPAC_transformed) # Inverse PCA trasnformation

    dataInversedErrors=np.subtract(data[:,1:], dataPAC_inversed) # Difference between original data and inverse data element by element
    dataInversedErrors=np.multiply(dataInversedErrors,dataInversedErrors) # Apply cuadratic to the above difference
    dataInversedErrorsMean = dataInversedErrors.mean(axis=0) # Get mean error by component
    #print(dataInversedErrorsMean) # Error's average by component
    print("Accumulated error with " + str(c) + " components: " + str(sum(dataInversedErrorsMean))) # Print results
print()

## Exercise 2

colors=[] # List with two color, one per class
for i in data[:,0]:
    if int(i)==1:
        colors.append('r') # For class 1 color red
    elif int(i)==0:
        colors.append('b') # For class 2 color blue

print("Exercise 2")
mds = manifold.MDS(n_components=2) # MDS in 2D
#mds = manifold.MDS(n_components=2, random_state=1) # MDS in 2D, NOT centroid's random iniziation
for i in range(4): # Four graphs
    pos = mds.fit(data[:,1:]).embedding_ # Data transformation and get embedding space
    plt.scatter(pos[:, 0], pos[:, 1], color=colors) # Plot embedding spaces split points in colors (by class)
    plt.title("MDS")
    plt.show()
print()

## Exercise 3

## Exercise 3 part a)

# Get training and test sets - NOT SHUFFLE DATA
training_set, test_set = get_training_and_test_sets(data)

print("Exercise 3 part a")
k=[3,4,5]
for i in k: # For each k in kNN
    neigh = KNeighborsClassifier(n_neighbors=i) # Object from KNN class with requested parameters
    neigh.fit(training_set[:,1:], training_set[:,0]) # Fit model with training set
    predictions=neigh.predict(test_set[:,1:]) # Predict test set
    print(str(i)+"NN:")
    confusionMatrixResults(test_set[:,0], predictions, 1) # Confussion matrix and results

print("SVM -> kernel=linear, C=0.025")
clf = SVC(kernel='linear', C=0.025) # Object from SVM-SVC class with requested parameters
clf.fit(training_set[:,1:], training_set[:,0]) # Fit model with training set
predictions=clf.predict(test_set[:,1:]) # Predict test set
confusionMatrixResults(test_set[:,0], predictions, 1) # Confussion matrix and results

print("Decission tree -> max_depth=5")
clf = DecisionTreeClassifier(max_depth=5) # Object from D-Tree class with requested parameters
clf.fit(training_set[:,1:], training_set[:,0])  # Fit model with training set
predictions=clf.predict(test_set[:,1:]) # Predict test set
confusionMatrixResults(test_set[:,0], predictions, 1)  # Confussion matrix and results

print("AdaBoost")
bdt = AdaBoostClassifier() # Object from Ada-Boost class with requested parameters
bdt.fit(training_set[:,1:], training_set[:,0]) # Fit model with training set
predictions=bdt.predict(test_set[:,1:]) # Predict test set
confusionMatrixResults(test_set[:,0], predictions, 1)  # Confussion matrix and results

print("Gaussian Naive Bayes")
gnb = GaussianNB() # Object from GNB class with requested parameters
gnb.fit(training_set[:,1:], training_set[:,0]) # Fit model with training set
predictions=gnb.predict(test_set[:,1:]) # Predict test set
confusionMatrixResults(test_set[:,0], predictions, 1)  # Confussion matrix and results

## Exercise 3 part b)

print("Exercise 3 part b")

# Get training and test sets - SHUFFLE DATA, NON-deterministic method
kk=10 # Cross validation sets
k=[3,4,5]
error=list(); accuracy=list() # 2D matrix for get errors and accuracies 
for p in range(kk): # Repeat proccess for kk random training and test sets 
    tmp_error=list(); tmp_accuracy=list() # Errors and accuracies for each set
    for j in range (3): # Number of shuffles before get training and test sets
        np.random.shuffle(data) # Shuffle training set
    training_set, test_set = get_training_and_test_sets(data) # Get training and test sets - SHUFFLE DATA
    for i in k: # The same proccess in above part (Exercise 3 part a)
        neigh = KNeighborsClassifier(n_neighbors=i)
        neigh.fit(training_set[:,1:], training_set[:,0])
        predictions=neigh.predict(test_set[:,1:])
        e, a = confusionMatrixResults(test_set[:,0], predictions) # Get error and accuracy
        tmp_error.append(e); tmp_accuracy.append(a) # Add to errors and accuracies from each set
    clf = SVC(kernel='linear', C=0.025)
    clf.fit(training_set[:,1:], training_set[:,0])
    predictions=clf.predict(test_set[:,1:])
    e, a = confusionMatrixResults(test_set[:,0], predictions)
    tmp_error.append(e); tmp_accuracy.append(a)
    clf = DecisionTreeClassifier(max_depth=5)
    clf.fit(training_set[:,1:], training_set[:,0])
    predictions=clf.predict(test_set[:,1:])
    e, a = confusionMatrixResults(test_set[:,0], predictions)
    tmp_error.append(e); tmp_accuracy.append(a)
    bdt = AdaBoostClassifier()
    bdt.fit(training_set[:,1:], training_set[:,0])
    predictions=bdt.predict(test_set[:,1:])
    e, a = confusionMatrixResults(test_set[:,0], predictions)
    tmp_error.append(e); tmp_accuracy.append(a)
    gnb = GaussianNB()
    gnb.fit(training_set[:,1:], training_set[:,0])
    predictions=gnb.predict(test_set[:,1:])
    e, a = confusionMatrixResults(test_set[:,0], predictions)
    tmp_error.append(e); tmp_accuracy.append(a)
    error.append(tmp_error) # Add error and accuracies from each set to all sets 2D matrix
    accuracy.append(tmp_accuracy)

errorMean = np.array(error).mean(axis=0) # Error mean of all methods and executions
accuracyMean = np.array(accuracy).mean(axis=0) # Accuracy mean of all methods and executions
print("Mean    3NN    4NN    5NN    SVM    Tree   AdaB   GNB") # Print results
print("Error " + str(errorMean))
print("Accur " + str(accuracyMean))
print()