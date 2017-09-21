import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

serialValues=[]
serialMeans=[]
serialStds=[]
parallelValues=[]
parallelMeans=[]
parallelStds=[]
mSize=[100,1000,10000,100000,1000000,2000000]
for i in mSize:
    serialPoints=np.array(genfromtxt("reduce_serial_output_"+str(i)+".out", delimiter="\n"))
    parallelPoints=np.array(genfromtxt("reduce_openmp_output_"+str(i)+".out", delimiter="\n"))
    plt.plot(serialPoints, label='serial')
    plt.plot(parallelPoints, label='parallel')
    plt.legend(loc=2)
    plt.title("Matrix size "+str(i))
    plt.ylabel("Seconds")
    plt.xlabel("Number of execution")
    plt.show()
    serialValues=np.append(serialValues, i)
    serialMeans=np.append(serialMeans, np.mean(serialPoints))
    serialStds=np.append(serialStds, np.std(serialPoints))
    parallelValues=np.append(parallelValues, i)
    parallelMeans=np.append(parallelMeans, np.mean(parallelPoints))
    parallelStds=np.append(parallelStds, np.std(parallelPoints))
plt.errorbar(serialValues, serialMeans, serialStds, linestyle='None', marker='^', label='serial')
plt.errorbar(parallelValues, parallelMeans, parallelStds, linestyle='None', marker='o', label='parallel')
plt.legend(loc=2)
plt.title("Errors bar - Mean and starndard desviation")
plt.ylabel("seconds")
plt.xlabel("Matrix size")
plt.margins(0.1, 0.1)
plt.show()
