# -*- coding: utf-8 -*-
"""SNA_part_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QPAHZwl2FbiLHM6WZem6aU0V5giye3BS
"""

import networkx as nx
from networkx.generators.degree_seq import expected_degree_graph
from matplotlib import pyplot as plt

N=1000 # number of nodes
k=0
degree=[] #list of degree
NgbyN=[] # list of Ng / N for corresponding k
while k <= 5:
    degree.append(round(k,1))
    w = [k for i in range(N)]
    G = expected_degree_graph(w)
    connected_components = (G.subgraph(c) for c in nx.connected_components(G))
    giant = max(connected_components, key=len)
    Ng = len(giant)
    ngbyn = Ng/N
    print("Degree = "+ str(round(k,1)) + ", Ng = " + str(Ng) + ", Ng/N = " + str(ngbyn))
    NgbyN.append(ngbyn)
    k += .1

plt.plot(degree, NgbyN)
plt.xlabel("Average degree <k>")
plt.ylabel("Ng / N")
plt.xlim(0, 5)
plt.show()