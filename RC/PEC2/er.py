## RC - UOC - URV - PEC2
## adpozuelo@uoc.edu
## Erdös-Rényi (ER), G(N,p)
## run with 'python3 er.py'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import random
import math

random.seed(1)

def create_network(n, p):
    G = nx.Graph()
    for ni in range(1 , n + 1):
        G.add_node(ni)
    
    for ni in range(1, n + 1):
        for nj in range(ni + 1, n + 1):
            if random.uniform(0, 1) < p:
                G.add_edge(ni, nj)

    nx.draw_networkx(G, node_size = 4, with_labels = False)
    plt.title('n = ' + str(n) + ', p = ' + str(p))
    filename = 'er_n' + str(n) + '_p' + str(p) + '_net.png'
    plt.savefig(filename)
    #plt.show()
    plt.clf()

    histo = nx.degree_histogram(G)
    total = sum(histo)
    norm_histo = np.divide(histo, total)
    length = len(norm_histo)
    kn = np.arange(length)
    plt.plot(kn, norm_histo, 'r-', label = 'empirical')
    
    poisson = np.empty(length)
    binomial = np.empty(length)
    lmb = n * p
    for k in range(0, length):
        if n <= 1000:
            poisson[k] = ((lmb ** k) * math.exp(-lmb)) / math.factorial(k)
        binomial[k] = sc.special.binom(n - 1, k) * (p ** k) * ((1 - p) ** (n - 1 - k))

    plt.title('n = ' + str(n) + ', p = ' + str(p))
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    if n <= 1000:
        plt.plot(kn, poisson, 'b-', label = 'poisson')
    plt.plot(kn, binomial,'g-', label = 'binomial')
    plt.legend(loc = 1)
    filename = 'er_n' + str(n) + '_p' + str(p) + '_dg.png'
    plt.savefig(filename)
    #plt.show()
    plt.clf()
    return

n = [50, 100, 1000, 10000]
p = [0.0, 0.01, 0.02, 0.03, 0.05, 0.1]
for ni in n:
    for pi in p:
        create_network(ni, pi)
