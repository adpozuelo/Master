import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

marks=['^','o','*']
mSize=[10,50,100,200]
ompThreads=[2,3,4]
schedule=['static', 'dynamic', 'guided']
dataMeanStd=dict()
points=[]
for m in mSize:
    if m not in dataMeanStd:
        dataMeanStd[m]=dict()
    for o in ompThreads:
        if o not in dataMeanStd[m]:
            dataMeanStd[m][o]=dict()
            for s in schedule:
                if s not in dataMeanStd[m][o]:
                    dataMeanStd[m][o][s]=list()
                points=np.array(genfromtxt("./mm_omp_"+str(m)+"_"+str(o)+"_"+s+".out", delimiter="\n"))
                dataMeanStd[m][o][s].append(np.mean(points))
                dataMeanStd[m][o][s].append(np.std(points))
for m in mSize:
    for o in ompThreads:
        meansValues=[]
        stdValues=[]
        for s in schedule:
            meansValues.append(dataMeanStd[m][o][s][0])
            stdValues.append(dataMeanStd[m][o][s][1])
        plt.errorbar([1,2,3], meansValues, stdValues, linestyle='None', marker=marks[o-2], label='m='+str(m)+'_o='+str(o))
    plt.legend(loc=2)
    plt.title("Errors bar - Mean and starndard desviation")
    plt.ylabel("seconds")
    plt.xlabel("1=static, 2=dynamic, 3=guided")
    plt.margins(0.1, 0.1)
    plt.show()
