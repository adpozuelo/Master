## RC - UOC - URV - PEC1
## adpozuelo@uoc.edu
## run with 'python3 histograms.py'

import numpy as np
np.set_printoptions(threshold=np.nan)
import matplotlib.pyplot as plt
import csv

def readData(filename):
    with open(filename) as csvfile:
        
        result = []
        myreader = csv.reader(csvfile, delimiter = '\t')
        next(myreader)
        for row in myreader:
            result.append([float(x) for x in row])
            
    return np.array(result, dtype='float')

def plotData(filename):
    data = readData(filename)
    
    x = data[:,0]
    pdf = data[:,1]
    ccdf = data[:,2]
    tvertex = ccdf[0]

    pdf = np.divide(pdf, tvertex)
    ccdf = np.divide(ccdf, tvertex)
    
    plt.bar(x, pdf, align='center')
    plt.title('PDF (' + filename + ')')
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    plt.show()
    
    plt.bar(x, pdf, align='center')
    plt.title('PDF log-log-scale (' + filename +')')
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    plt.xscale('log')
    plt.yscale('log')
    plt.show()
    
    plt.plot(x, ccdf, 'ro')
    plt.title('CCDF (' + filename + ')')
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    plt.show()
    return

files = ['./model/ER1000k8-info_degrees.txt', 'model/SF_1000_g2.7-info_degrees.txt', 'model/ws1000-info_degrees.txt', 'real/airports_UW-info_degrees.txt']
for file in files:
    plotData(file)
