## RC - UOC - URV - PEC2
## adpozuelo@uoc.edu
## Configuration Model (CM)
## run with 'python3 cm.py'

import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import random
import math

def create_network(n, p):

    y = np.random.poisson(p, n)
    for i in range(len(y)):
        y[i] += 1
    while sum(y) % 2 != 0:
        y = np.random.poisson(p, n)
        for i in range(len(y)):
            y[i] += 1

    ylength = len(y)
    xlength = sum(y)
    x = np.zeros(xlength, dtype='int')
    counter = 0
    for i in range(ylength):
        for j in range(y[i]):
            x[counter] = i + 1
            counter += 1

    selfloop = True
    multiedge = True
    connected = False
    loopcontrol = 0
    while selfloop or multiedge or not connected:
        counter = 0
        selfloop = False
        np.random.shuffle(x)
        while counter < xlength:
            if x[counter] == x[counter + 1]:
                selfloop = True
                break
            counter += 2

        if selfloop is False:
            G = nx.Graph()
            for ni in range(1 , n + 1):
                G.add_node(ni)

            counter = 0
            multiedge = False
            while counter < xlength:
                if G.has_edge(x[counter], x[counter +1]):
                    multiedge = True
                    break
                else:
                    G.add_edge(x[counter], x[counter + 1])
                counter += 2

        if selfloop is False and multiedge is False:
            connected = nx.is_connected(G)
            loopcontrol += 1

        if loopcontrol > 10000:
            break

    nx.draw_networkx(G, node_size = 4, with_labels = False)
    plt.title('n = ' + str(n) + ', p = ' + str(p))
    filename = 'cm_n' + str(n) + '_p' + str(p) + '_net.png'
    plt.savefig(filename)
    # plt.show()
    plt.clf()

    histo = nx.degree_histogram(G)
    total = sum(histo)
    norm_histo = np.divide(histo, total)
    length = len(norm_histo)
    kn = np.arange(length)
    plt.plot(kn, norm_histo, 'r-', label = 'empirical')

    poisson = np.zeros(max(y) + 1, dtype='int')
    for i in range(ylength):
        poisson[y[i]] += 1
    norm_poisson = np.divide(poisson, sum(poisson))
    
    plt.plot(range(len(poisson)), norm_poisson, 'b-', label = 'poisson')
    plt.title('n = ' + str(n) + ', p = ' + str(p))
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    plt.legend(loc = 1)
    filename = 'cm_n' + str(n) + '_p' + str(p) + '_dg.png'
    plt.savefig(filename)
    # plt.show()
    plt.clf()
    return

n = [50, 100, 1000, 10000]
poisson = [2, 4]

for ni in n:
    for pi in poisson:
        create_network(ni, pi)
