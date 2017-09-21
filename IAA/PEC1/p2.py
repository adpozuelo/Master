#adpozuelo@uoc.edu - IA - PEC1

from sklearn.cluster import KMeans
from sklearn.metrics.cluster import adjusted_rand_score
import numpy as np
import itertools as en

print()
aReferences=[(l.strip()) for l in (open("./references.csv").readlines())]
aReferecesInt=list()
# for all articles create a list of integers with its references
for i in range(len(aReferences)):
    aReferecesInt.append(list(map(int,aReferences[i].split())))
shReferences=list()
# for all articles reduce the list of integers with its references
for i in range(len(aReferecesInt)):
    shReferences.append(sum(aReferecesInt[i]))
xReferences=list()
# convert row vector to column vector (one file per article)
# sklearn's input is a list of lists where inner list represents object's attributes.
for i in shReferences:
    tmp=[i]
    xReferences.append(tmp)
X = np.array(xReferences)
# call sklearn methods
kmeans = KMeans(n_clusters=6, random_state=0).fit(X)
finalClasses=kmeans.labels_
# create permutations to get best classes's codification
k=en.permutations(range(6), 6)
lk=list(k)
aClasses=[(l.strip()) for l in (open("./classes.csv").readlines())]
maxA=-10
aClassesInt=list()
# check every classes's codification quality
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
# store the best classes's codification quality
    if tmpA > maxA:
        maxA = tmpA
        maxComb = a
        bestAClassesInt = aClassesInt
# print results
print("Best classes's codification -> Cluster quality")       
print(str(maxComb) + " -> " + str(maxA))
print("Classes predictions")
# predict some articles
print(kmeans.predict([xReferences[0], xReferences[1], xReferences[3], xReferences[4], xReferences[9], xReferences[17]]))
print("Classes reference")
# print reference classes of predicted articles
articlesReferences=[0,1,3,4,9,17]
for i in articlesReferences:
    print(bestAClassesInt[i], end= " ")
print("\n")