## RC - UOC - URV - PEC2
## adpozuelo@uoc.edu
## Watts-Strogatz (WS)
## run with 'python3 ws.py'

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import scipy as sc
import random
import math

random.seed(1)

def create_network(n, p, k):
    G = nx.Graph()
    kd2 = int(k / 2) + 1

    for ni in range(1, n + 1):
        G.add_node(ni)
        for nj in range(ni + 1, ni + kd2):
            if nj > n:
                nj %= n
            G.add_edge(ni, nj)

    for ni in range(1, n + 1):
        for nj in range(ni + 1, ni + kd2):
            if random.uniform(0, 1) < p:
                if nj > n:
                    nj %= n
                G.remove_edge(ni, nj)
                rn = random.randint(1, n)
                while G.has_edge(ni, rn) or rn == ni:
                    rn = random.randint(1, n)
                G.add_edge(ni, rn)

    if n >= 1000:
        nx.draw_networkx(G, node_size=4, with_labels=False)
    else:
        nx.draw_networkx(G, nx.circular_layout(G), node_size=4, with_labels=False)
    plt.title('n = ' + str(n) + ', p = ' + str(p) + ', k = ' + str(k))
    filename = 'ws_n' + str(n) + '_p' + str(p) + '_k' + str(k) + '_net.png'
    plt.savefig(filename)
    #plt.show()
    plt.clf()

    histo = nx.degree_histogram(G)
    total = sum(histo)
    norm_histo = np.divide(histo, total)
    length = len(norm_histo)
    kn = np.arange(length)
    plt.plot(kn, norm_histo, 'r-', label = 'empirical')

    kd2 -= 1
    diracdelta = np.empty(length)
    # https://en.wikipedia.org/wiki/Watts%E2%80%93Strogatz_model
    for ki in range(0, length):
        if ki >= kd2:
            sumatory = np.empty(min(ki - kd2, kd2) + 1)
            for ndi in range(0, len(sumatory)):
                sumatory[ndi] = (math.factorial(kd2) / (math.factorial(ndi) * math.factorial( kd2 - ndi))) * ((1 - p) ** ndi) * (p ** (kd2 - ndi)) * ((p * kd2) ** (ki - kd2 - ndi)) * math.exp(-p * kd2) / math.factorial(ki - kd2 - ndi)
            diracdelta[ki] = sum(sumatory)
        else:
            diracdelta[ki] = 0.0

    plt.plot(kn, diracdelta, 'b-', label = 'dirac delta')
    plt.title('n = ' + str(n) + ', p = ' + str(p) + ', k = ' + str(k))
    plt.xlabel('Grado k')
    plt.ylabel('Fracción de nodos')
    plt.legend(loc = 1)
    filename = 'ws_n' + str(n) + '_p' + str(p) + '_k' + str(k) + '_dg.png'
    plt.savefig(filename)
    #plt.show()
    plt.clf()
    return

n = [50, 100, 1000, 10000]
p = [0.0, 0.1, 0.2, 0.5, 0.9, 1.0]
k = [4, 8, 16, 24]
for ni in n:
    for pi in p:
        for ki in k:
            create_network(ni, pi, ki)
