## RC - UOC - URV - PEC2
## adpozuelo@uoc.edu
## Barabási & Albert (BA)
## run with 'python3 ba.py'

import networkx as nx
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import random
import math

random.seed(1)

def create_network(n, m):
    m0 = 20
    G = nx.Graph()

    for ni in range(1, m0 + 1):
        G.add_node(ni)
        for nj in range(1, ni):
            if nj != ni:
                G.add_edge(ni, nj)

    nconnected = m0 + 1
    gsize = G.size(weight = 'weight')
    for ni in range(m0 + 1, n + 1):
        for mi in range(1, m + 1):
            attached = False
            while not attached:
                for nj in range(1, nconnected):
                    if ni != nj and not G.has_edge(ni, nj):
                        p = G.degree(nj, weight = 'weight') / gsize
                        if random.uniform(0, 1) < p:
                            G.add_edge(ni, nj)
                            attached = True
                            gsize += 1
                            break
        nconnected += 1

    nx.draw_networkx(G, node_size = 4, with_labels = False)
    plt.title('n = ' + str(n) + ', m = ' + str(m))
    filename = 'ba_n' + str(n) + '_m' + str(m) + '_net.png'
    plt.savefig(filename)
    # plt.show()
    plt.clf()

    histo = nx.degree_histogram(G)
    total = sum(histo)
    norm_histo = np.divide(histo, total)
    length = len(norm_histo)
    kn = np.arange(length)
    knm = np.add(kn, m)
    plt.plot(kn, norm_histo, 'r-', label = 'empirical')

    exponential = np.empty(length)
    for k in range(0, length):
        exponential[k] = (k + 1) ** (-3)
        
    total = sum(exponential)
    norm_exponential = np.divide(exponential, total)
    
    plt.plot(knm, norm_exponential, 'b-', label = 'exponential(-3)')
    plt.title('n = ' + str(n) + ', m = ' + str(m))
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    plt.legend(loc = 1)
    filename = 'ba_n' + str(n) + '_m' + str(m) + '_dg.png'
    plt.savefig(filename)
    # plt.show()
    plt.clf()

    if n >= 1000:
        plt.plot(kn, norm_histo, 'r-', label = 'empirical')
        plt.plot(knm, norm_exponential, 'b-', label = 'exponential(-3)')
        plt.title('n = ' + str(n) + ', m = ' + str(m) + ' (log-log)')
        plt.xlabel('Grado k')
        plt.ylabel('Fracción de nodos')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(loc = 3)
        filename = 'ba_n' + str(n) + '_m' + str(m) + '_dg_log_log.png'
        plt.savefig(filename)
        # plt.show()
        plt.clf()

        plt.bar(kn, histo, align='center', label = 'empirical')
        plt.title('n = ' + str(n) + ', m = ' + str(m) + ' (bar-log-log)')
        plt.xlabel('Grado k')
        plt.ylabel('Fracción de nodos')
        plt.xscale('log')
        plt.yscale('log')
        plt.legend(loc = 1)
        filename = 'ba_n' + str(n) + '_m' + str(m) + '_dg_bar_log_log.png'
        plt.savefig(filename)
        # plt.show()
        plt.clf()
        
        filename = 'ba_n' + str(n) + '_m' + str(m) + '_dg.txt'
        file = open(filename, 'w')
        for i in range(length):
            file.write(str(i) + ' ' + str(histo[i]) + '\n')
        file.close()        
    return

n = [50, 100, 1000, 10000]
m = [1, 2, 4, 10]
for ni in n:
    for mi in m:
        create_network(ni, mi)
