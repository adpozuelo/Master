import sys
import re
import numpy as np
import matplotlib.pyplot as plt

ompThreads=['2','4']
mSize=['A', 'B', 'C']
dataResults=dict()
for o in ompThreads:
    if o not in dataResults:
        dataResults[o]=dict()
    for m in mSize:
        if m not in dataResults[o]:
            dataResults[o][m]=list()
        lines = [line.rstrip('\n') for line in open('npb_omp_cg_'+o+'_'+m+'.out')]
        finalTmpData=[]
        for line in lines:
            rawTmpData=re.findall(r"[-+]?\d*\.\d+|\d+", line)
            finalTmpData.append(float(rawTmpData[0])*60+float(rawTmpData[1]))      
        dataResults[o][m].append(np.mean(finalTmpData))
        dataResults[o][m].append(np.std(finalTmpData))
markers=['^','o']
i = 0;
for o in ompThreads:
    means=[]
    stds=[]
    for m in mSize:
        means.append(dataResults[o][m][0])
        stds.append(dataResults[o][m][1])
    plt.errorbar([1,2,3], means, stds, linestyle='-', marker=markers[i], label="OpenMP = "+o)
    i+=1
plt.legend(loc=2)
plt.title("Errors bar - Mean and starndard desviation")
plt.ylabel("seconds")
plt.xlabel("Benchmark size [1=A][2=B][3=C]")
plt.margins(0.1, 0.1)
plt.show()
print("\nSpeedUP 4 OpenMP VS 2 OpenMP")
for m in mSize:
    print("Size " + m + ": " + str(dataResults['2'][m][0]/dataResults['4'][m][0]))
print()