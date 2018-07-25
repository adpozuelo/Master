## RC - UOC - URV - PEC2
## adpozuelo@uoc.edu
## Gamma empirical regresion
## run with 'python3 reg.py'

# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import csv

def readData(filename):
    with open(filename) as csvfile:
        result = []
        myreader = csv.reader(csvfile, delimiter = ' ')
        for row in myreader:
            result.append([int(x) for x in row])
            
    return np.array(result, dtype='int')

def gamma(n, m):
    filename = 'ba_n' + str(n) + '_m' + str(m) + '_dg.txt'
    data = readData(filename)
    y = data[:,1]
    x = data[:,0]

    kni = m
    while True:
        if y[kni] == 0:
            break
        kni += 1

    y = y[m:kni]
    x = x[m:kni]

    length = len(y)
    ylog = np.zeros(length, dtype='float')
    xlog = np.zeros(length, dtype='float')

    for i in range(length):
        ylog[i] = math.log(y[i])
        xlog[i] = math.log(x[i])

    a, b = np.polyfit(xlog, ylog, 1)
    r = np.corrcoef(xlog, ylog)

    plt.plot(xlog, ylog, 'o')
    plt.xlim(np.min(xlog) -1, np.max(xlog) +1)
    plt.ylim(np.min(ylog) -1, np.max(ylog) +1)
    plt.plot(xlog, a * xlog + b)
    plt.title('n = ' + str(n) + ', m = ' + str(m) + ' -> ' + 'y = {0:2.3f} x + {1:2.3f}'.format(a, b))
    print('n = ' + str(n) + ', m = ' + str(m) + ' -> y = ' + str(a) + ' x + ' + str(b) + ' -> gamma = {0:2.3f}'.format(a))
    filename = 'ba_n' + str(n) + '_m' + str(m) + '_regresion.png'
    plt.savefig(filename)
    # plt.show()
    plt.clf()
    return

n = [1000, 10000]
m = [1, 2, 4, 10]

for ni in n:
    for mi in m:
        gamma(ni, mi)
