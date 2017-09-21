#adpozuelo@uoc.edu - IA - PEC1

import numpy as np

print()
# the same thar p1_check_data
aClasses=[(l.strip()) for l in (open("./classes.csv").readlines())]
hClasses=dict()
for c in aClasses:
    if c not in hClasses:
        hClasses[c] = 1
    else:
        hClasses[c] += 1
shClasses=[v for v in hClasses.values()]
print("Statistics for classes.csv file")
print("Number of articles = " + str(len(aClasses)))
print("Number of classes = " + str(len(hClasses)))
print("Max number of articles in a class = " + str(np.max(shClasses)))
print("Min number of articles in a class = "  + str(np.min(shClasses)))
print("Mean number of articles by classes = " + str(np.mean(shClasses)))
print("Std desviation number of articles by classes = " + str(np.std(shClasses)))
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
# print statistics
print("Statistics for references.csv file")
print("Number of articles = " + str(len(aReferences)))
print("Max number of references in an article = " + str(np.max(shReferences)))
print("Min number of references in an article = "  + str(np.min(shReferences)))
print("Mean number of references by articles = " + str(np.mean(shReferences)))
print("Std desviation number of references by articles = " + str(np.std(shReferences)))
print()

# repeat above steps in keywords file
aKeyWords=[(l.strip()) for l in (open("./keywords.csv").readlines())]
aKeyWordsInt=list()
for i in range(len(aKeyWords)):
    aKeyWordsInt.append(list(map(int,aKeyWords[i].split())))
shKeywords=list()
for i in range(len(aKeyWordsInt)):
    shKeywords.append(sum(aKeyWordsInt[i]))
print("Statistics for keywords.csv file")
print("Number of articles = " + str(len(aKeyWords)))
print("Max number of keywords in an article = " + str(np.max(shKeywords)))
print("Min number of keywords in an article = "  + str(np.min(shKeywords)))
print("Mean number of keywords by articles = " + str(np.mean(shKeywords)))
print("Std desviation number of keywords by articles = " + str(np.std(shKeywords)))
print()