import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

marks=['^','o','*','x']
mSize=[10,50,100,200]
ompThreads=[0,2,3,4]
schedule='static'
dataMeanStd=dict()
points=[]
for m in mSize:
    if m not in dataMeanStd:
        dataMeanStd[m]=dict()
    for o in ompThreads:
        if o not in dataMeanStd[m]:
            dataMeanStd[m][o]=list()
        if o==0:
            points=np.array(genfromtxt("./mm_serial_"+str(m)+".out", delimiter="\n"))
        else:
            points=np.array(genfromtxt("./mm_omp_"+str(m)+"_"+str(o)+"_"+schedule+".out", delimiter="\n"))
        dataMeanStd[m][o].append(np.mean(points))
        dataMeanStd[m][o].append(np.std(points))
i=0
for m in mSize:
    meansValues=[]
    stdValues=[]
    for o in ompThreads:
        meansValues.append(dataMeanStd[m][o][0])
        stdValues.append(dataMeanStd[m][o][1])
    plt.errorbar(ompThreads, meansValues, stdValues, linestyle='None', marker=marks[i], label='m='+str(m))
    i+=1
plt.legend(loc=1)
plt.title("Errors bar - Mean and starndard desviation")
plt.ylabel("seconds")
plt.xlabel("OpenMPThreads: 0=serial case")
plt.margins(0.1, 0.1)
plt.show()
print 'SpeedUp omp_4 vs all'
for m in mSize:
    serialTime=float(dataMeanStd[m][4][0])
    print '\nMatrix Size ' + str(m) + '\n' 
    for o in ompThreads:
        print str(float(dataMeanStd[m][o][0])/serialTime) + ' '