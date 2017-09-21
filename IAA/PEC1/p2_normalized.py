#adpozuelo@uoc.edu - IA - PEC1

from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
import numpy as np
import itertools as en
from sklearn import preprocessing

print()
aReferences=[(l.strip()) for l in (open("./references.csv").readlines())]
aReferecesInt=list()
for i in range(len(aReferences)):
    aReferecesInt.append(list(map(int,aReferences[i].split())))
shReferences=list()
for i in range(len(aReferecesInt)):
    shReferences.append(sum(aReferecesInt[i]))
xReferences=list()
for i in shReferences:
    tmp=[i]
    xReferences.append(tmp)
X = np.array(xReferences)
# Normalize (standarization) data before clustering
X_scaled = preprocessing.scale(X)
kmeans = KMeans(n_clusters=6, random_state=0).fit(X_scaled)
finalClasses=kmeans.labels_
k=en.permutations(range(6), 6)
lk=list(k)
aClasses=[(l.strip()) for l in (open("./classes.csv").readlines())]
maxA=-10
aClassesInt=list()
for a in lk:
    aClassesInt.clear()
    for c in aClasses:
        if c == 'Agents':
            aClassesInt.append(a[0])
        elif c == 'IR':
            aClassesInt.append(a[1])
        elif c == 'DB':
            aClassesInt.append(a[2])
        elif c == 'AI':
            aClassesInt.append(a[3])
        elif c == 'HCI':
            aClassesInt.append(a[4])
        elif c == 'ML':
            aClassesInt.append(a[5])
        else:
            print("Wrong argument data in classes.csv file")
    tmpA=adjusted_rand_score(finalClasses, aClassesInt)
    if tmpA > maxA:
        maxA = tmpA
        maxComb = a
        bestAClassesInt = aClassesInt
print("Best classes's codification -> Cluster quality")       
print(str(maxComb) + " -> " + str(maxA))
print("Classes predictions")
print(kmeans.predict([xReferences[0], xReferences[1], xReferences[3], xReferences[4], xReferences[9], xReferences[17]]))
print("Classes reference")
articlesReferences=[0,1,3,4,9,17]
for i in articlesReferences:
    print(bestAClassesInt[i], end= " ")
print("\n")