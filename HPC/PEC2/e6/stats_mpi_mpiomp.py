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
parallelEx=['base','omp']
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
                        dataMeanStd[m][i][im][imb][mpij]=dict()
                    for p in parallelEx:
                        if p not in dataMeanStd[m][i][im][imb][mpij]:
                            dataMeanStd[m][i][im][imb][mpij][p]=list()
                        if p=='base':
                            points=np.array(genfromtxt("./barr_sync_base_"+str(mpij)+"_"+str(m)+"_"+str(i)+"_"+str(im)+"_"+str(imb)+".out", delimiter="\n"))
                            dataMeanStd[m][i][im][imb][mpij]['base'].append(np.mean(points))
                            dataMeanStd[m][i][im][imb][mpij]['base'].append(np.std(points))
                        if p=='omp':
                            points=np.array(genfromtxt("./barr_sync_omp_"+str(mpij)+"_"+str(m)+"_"+str(i)+"_"+str(im)+"_"+str(imb)+".out", delimiter="\n"))
                            dataMeanStd[m][i][im][imb][mpij]['omp'].append(np.mean(points))
                            dataMeanStd[m][i][im][imb][mpij]['omp'].append(np.std(points))
print "SpeedUp MPI+OpenMP vs MPI (matrix size = 100, iters = 30, imbalance = 20, imabalance_base = 70, mpijobs = 16)"
print dataMeanStd[100][30][20][70][16]['base'][0]/dataMeanStd[100][30][20][70][16]['omp'][0]      
        
        
        
        
        
