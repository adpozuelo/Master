import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

marks=['^','o','*','x']
mSize=[10,50,100]
iters=[10,20,30]
imbalance=[0,10,20]
imbalance_base=[50,60,70]
mpijobs=[8,12,16]
dataMeanStd=dict()
points=[]
for m in mSize:
    if m not in dataMeanStd:
        dataMeanStd[m]=dict()
    for i in iters:
        if i not in dataMeanStd[m]:
            dataMeanStd[m][i]=dict()
        for im in imbalance:
            if im not in dataMeanStd[m][i]:
                dataMeanStd[m][i][im]=dict()
            for imb in imbalance_base:
                if imb not in dataMeanStd[m][i][im]:
                    dataMeanStd[m][i][im][imb]=dict()
                for mpij in mpijobs:
                    if mpij not in dataMeanStd[m][i][im][imb]:
                        dataMeanStd[m][i][im][imb][mpij]=list()
                    points=np.array(genfromtxt("./barr_sync_base_"+str(mpij)+"_"+str(m)+"_"+str(i)+"_"+str(im)+"_"+str(imb)+".out", delimiter="\n"))
                    dataMeanStd[m][i][im][imb][mpij].append(np.mean(points))
                    dataMeanStd[m][i][im][imb][mpij].append(np.std(points))
for mpij in mpijobs:
    i=0
    for im in imbalance:
        meansValues=[]
        stdValues=[]
        for imb in imbalance_base:
            meansValues.append(dataMeanStd[100][30][im][imb][mpij][0])
            stdValues.append(dataMeanStd[100][30][im][imb][mpij][1])
        plt.errorbar(imbalance_base, meansValues, stdValues, linestyle='None', marker=marks[i], label="m=100, mpi="+str(mpij)+", iters=30, imbalance="+str(im))
        i+=1
    plt.legend(loc=2)
    plt.title("Errors bar - Mean and starndard desviation")
    plt.ylabel("seconds")
    plt.xlabel("Imbalance_base")
    plt.margins(0.1, 0.1)
    plt.show()                       
        
        
        
