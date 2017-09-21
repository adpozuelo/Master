#adpozuelo@uoc.edu - IA - PEC1

import numpy as np
import sys

print()
aClasses=[(l.strip()) for l in (open("classes.csv").readlines())]
hClasses=dict()
# create histogram from file values
for c in aClasses:
    if c not in hClasses:
        hClasses[c] = 1
    else:
        hClasses[c] += 1
# create a list from histogram values
shClasses=[v for v in hClasses.values()]
# print statistics
print("Statistics for classes.csv file")
print("Number of articles = " + str(len(aClasses)))
print("Number of classes = " + str(len(hClasses)))
print("Max number of articles in a class = " + str(np.max(shClasses)))
print("Min number of articles in a class = "  + str(np.min(shClasses)))
print("Mean number of articles by classes = " + str(np.mean(shClasses)))
print("Std desviation number of articles by classes = " + str(np.std(shClasses)))
print()

aReferences=[(l.strip()) for l in (open("./references.csv").readlines())]
# ensure that number of articles are the same
if len(aClasses) != len(aReferences):
    print("Number of articles in CSV files doesn't match!!")
    sys.exit()
hReferences=dict()
# create a histogram with article's references values
# histogram is needed (no reduction) since we must check values (strings) from file
for i in aReferences:
    ref = i.split()
# ensure ensure that number of articles are the same
    if len(aClasses) != len(ref):
        print("Number of articles in CSV files doesn't match!!")
        sys.exit()
    for j in range(len(ref)):
        if int(ref[j]) == 1 or int(ref[j]) == 0:
            if int(ref[j]) == 1:
                if j not in hReferences:
                    hReferences[j] = 1
                else:
                    hReferences[j] += 1     
        else:
            print("Wrong values in references.csv file")
            sys.exit()
# create a list from histogram values
shReferences=[v for v in hReferences.values()]
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
if len(aClasses) != len(aKeyWords):
    print("Number of articles in CSV files doesn't match!!")
    sys.exit()
hKeyWord=dict()
a = 0
for i in aKeyWords:
    art = i.split()
    for j in art:
        if int(j) == 1 or int(j) == 0:
            if int(j) == 1:
                if a not in hKeyWord:
                    hKeyWord[a] = 1
                else:
                    hKeyWord[a] += 1
        else:
            print("Wrong values in keywords.csv file")
            sys.exit()
    a += 1
shKeywords=[v for v in hKeyWord.values()]
print("Statistics for keywords.csv file")
print("Number of articles = " + str(len(aKeyWords)))
print("Max number of keywords in an article = " + str(np.max(shKeywords)))
print("Min number of keywords in an article = "  + str(np.min(shKeywords)))
print("Mean number of keywords by articles = " + str(np.mean(shKeywords)))
print("Std desviation number of keywords by articles = " + str(np.std(shKeywords)))
print()
print("There are not invalid or not present values\n")