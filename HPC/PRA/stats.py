# Antonio Díaz Pozuelo - adpozuelo@uoc.edu
# HPC_PRA - Energy-Potential N-Body Problem (Lennard Jones Interaction Potential)
# Statistical study
# Python 3.6

import sys
import re
import numpy as np
import matplotlib.pyplot as plt
import csv

def readData(filename):
    with open(filename) as csvfile:
        
        result = []
        myreader = csv.reader(csvfile, delimiter=' ')

        for row in myreader:    
            result.append([float(x) for x in row])
            
    return np.array(result, dtype='float')

s = [100, 500, 1000, 5000, 10000, 20000]
s_et_mean = []; s_tet_mean = []; c_et_mean = []; c_tet_mean = []
s_et_std = []; s_tet_std = []; c_et_std = []; c_tet_std = []

for si in s:
    data = readData('interact_serial_cuda_' + str(si) + '.out')
    dataMean = data.mean(axis=0)
    dataStd = data.std(axis=0)
    s_et_mean.append(dataMean[0]) ; s_et_std.append(dataStd[0])
    s_tet_mean.append(dataMean[1]) ; s_tet_std.append(dataStd[1])
    c_et_mean.append(dataMean[2]) ; c_et_std.append(dataStd[2])
    c_tet_mean.append(dataMean[3]) ; c_tet_std.append(dataStd[3])

# print(s_et_mean)
#     print(s_tet_mean)
# print(c_et_mean)
# print(c_tet_mean)

plt.errorbar(s, s_et_mean, s_et_std, linestyle='-', marker='^', label="Serial eTime")
plt.errorbar(s, s_tet_mean, s_tet_std, linestyle='-', marker='+', label="Serial TeTime")
plt.errorbar(s, c_et_mean, c_et_std, linestyle='-', marker='^', label="CUDA eTime")
plt.errorbar(s, c_tet_mean, c_tet_std, linestyle='-', marker='+', label="CUDA TeTime")

plt.legend(loc=2)
plt.title("Errors bar - Mean and starndard desviation")
plt.ylabel("Miliseconds")
plt.xlabel("Particles")
plt.margins(0.1, 0.1)
plt.show()

plt.errorbar(s, s_et_mean, s_et_std, linestyle='-', marker='^', label="Serial eTime")
plt.errorbar(s, s_tet_mean, s_tet_std, linestyle='-', marker='+', label="Serial TeTime")
plt.legend(loc=2)
plt.title("Errors bar - Mean and starndard desviation")
plt.ylabel("Miliseconds")
plt.xlabel("Particles")
plt.margins(0.1, 0.1)
plt.show()

plt.errorbar(s, c_et_mean, c_et_std, linestyle='-', marker='^', label="CUDA eTime")
plt.errorbar(s, c_tet_mean, c_tet_std, linestyle='-', marker='+', label="CUDA TeTime")
plt.legend(loc=2)
plt.title("Errors bar - Mean and starndard desviation")
plt.ylabel("Miliseconds")
plt.xlabel("Particles")
plt.margins(0.1, 0.1)
plt.show()

speedUp=[]
for i in range(len(s_tet_mean)):
    speedUp.append(s_tet_mean[i]/c_tet_mean[i])
print(speedUp)
