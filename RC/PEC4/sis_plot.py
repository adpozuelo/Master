## RC - UOC - URV - PEC4
## adpozuelo@uoc.edu
## run with 'python3 sis_plot.py'

import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt
import csv

def readData(filename):
    with open(filename) as csvfile:
        
        result = []
        myreader = csv.reader(csvfile, delimiter = ' ')
        for row in myreader:
            result.append([float(x) for x in row])
            
    return np.array(result, dtype='float')

def plotData(filename):
    data = readData(filename)
    
    x = data[:,0]
    y = data[:,1]

    plt.plot(x, y)
    plt.title('SIS (' + filename + ')')
    plt.xlabel('beta')
    plt.ylabel('rho')
    plt.xlim((0,1))
    plt.ylim((0,1))
    #plt.show()
    plt.savefig(filename + '.png')
    plt.clf()
    
    return

files = ['./er_N500_p01_mu01_rho01.txt', './er_N500_p01_mu05_rho01.txt', './er_N500_p01_mu09_rho01.txt', './er_N1000_p0025_mu01_rho01.txt', './er_N1000_p0025_mu05_rho01.txt', './er_N1000_p0025_mu09_rho01.txt', 'ba_N500_m4_mu01_rho01.txt', 'ba_N500_m4_mu05_rho01.txt', 'ba_N500_m4_mu09_rho01.txt', 'ba_N1000_m2_mu01_rho01.txt', 'ba_N1000_m2_mu05_rho01.txt', 'ba_N1000_m2_mu09_rho01.txt']
for file in files:
    plotData(file)
