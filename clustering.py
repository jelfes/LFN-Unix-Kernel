"""
CLUSTERING COEFFICIENT

GOAL: estimate the global clustering coefficient of the whole graph and test its significance

1. Measure the Graph CC
2. Run Chung Lu algorithm to generate random graphs
3. Check if the coefficient is significant using the Z-Score
"""


import networkx as nx
import numpy as np
import pandas as pd

# INCLUDE GRAPH

include_df = pd.read_csv('fgraph_I_all.txt', sep = " ", header=None)
include_df = include_df.drop_duplicates()
include_graph = nx.from_pandas_edgelist(include_df, 0,1, create_using=nx.Graph)

# Transitivity
include_transitivity = nx.transitivity(include_graph)

degree_list_include = list(dict(include_graph.degree).values())

random_degree_transitivity = []
for i in range(100):
    G = nx.expected_degree_graph(degree_list_include,selfloops = False)
    transitivity = nx.transitivity(G)
    random_degree_transitivity.append(transitivity)

z_score_include_graph = (include_transitivity - np.mean(random_degree_transitivity))/np.std(random_degree_transitivity)

"""
Include graph transitivity:     0.0019509512575861534
Mean transitivity random graph: 0.014102812629210365
Std transitivity random graph:  0.00013762899752409893

Zscore:  -88.29433905813644

"""

# COMPILE H GRAPH

compile_graph_c = nx.read_adjlist('compile_graph_c.adjlist')

compile_c_transitivity = nx.transitivity(include_graph)

degree_list_compile_c = list(dict(include_graph.degree).values())

random_degree_transitivity = []
for i in range(100):
    G = nx.expected_degree_graph(degree_list_compile_c,selfloops = False)
    transitivity = nx.transitivity(G)
    random_degree_transitivity.append(transitivity)

z_score_include_graph = (include_transitivity - np.mean(random_degree_transitivity))/np.std(random_degree_transitivity)

"""
Compile h graph transitivity:   0.42939630891895725
Mean transitivity random graph: 0.43114922134656200  
Std transitivity random graph:  0.00015723785904120

Zscore: -11.14815756

"""