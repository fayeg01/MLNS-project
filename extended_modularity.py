"""
Extended modularity for weighted communities implemented in python

Ref:
Weighted modularity optimization for crisp and fuzzy community detection in large-scale networks
- Jie Cao, Zhan Bu, Guangliang Gao and Haicheng Tao
Physica A: Statistical Mechanics and its Applications (Volume 462, November 2016)
"""

import numpy as np

def EQ_Newman(graph, communities, weight='weight'):
    q = 0.0
    degrees = dict(graph.degree(weight=weight))
    
    U = np.zeros((len(list(graph.nodes())), len(communities)))
    for k, nds in enumerate(communities):
        for n in nds:
            n_int = int(n)
            U[n_int-1, k] = 1
    U = U / U.sum(1, keepdims=True)
    m = np.sum([v for k, v in degrees.items()])

    nodes = list(graph.nodes())
    
    for i in range(len(nodes)):
        nd1 = nodes[i]
        for j in range(len(nodes)):
            nd2 = nodes[j]
            if graph.has_edge(nd1, nd2):
                e = graph[nd1][nd2]
                wt = e.get(weight, 1)
            else:
                wt = 0
        
            q += (wt - degrees[nd1]*degrees[nd2]/(2*m))*np.dot(U[int(nd1)-1], U[int(nd2)-1])

    return q / (2*m)