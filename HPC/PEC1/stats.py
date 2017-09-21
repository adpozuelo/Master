import sys
import numpy as np
import matplotlib.pyplot as plt
from numpy import genfromtxt

values=[]
means=[]
stds=[]
for i in sys.argv[1:]:
    a=np.array(genfromtxt("mm_output_"+i+".out", delimiter="\n"))
    plt.plot(a)
    plt.title("Matrix size "+i)
    plt.ylabel("Seconds")
    plt.xlabel("Number of execution")
    plt.show()
    values=np.append(values, i)
    means=np.append(means, np.mean(a))
    stds=np.append(stds, np.std(a))
print "Matrix sizes"
print values
print "Means"
print means
print "Std desviations"
print stds
plt.errorbar(values, means, stds, linestyle='None', marker='^')
plt.title("Errors bar")
plt.ylabel("Mean and starndard desviation")
plt.xlabel("Matrix size")
plt.show()
