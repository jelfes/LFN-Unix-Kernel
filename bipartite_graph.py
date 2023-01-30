"""
GOAL: produce the bipartite graph and generate both compile_c and compile_h graph; save both networks as adjacency lists for further re-use.
"""

import networkx as nx
import pandas as pd

# Import dataframe
compile_df = pd.read_csv('fgraph_C.txt', sep = " ", header=None)
compile_df = compile_df.drop_duplicates()

# Remove edges between nodes of the same set
hh_index = compile_df[compile_df[0].str.contains("\.h") & compile_df[1].str.contains("\.h")].index
cc_index = compile_df[compile_df[0].str.contains("\.c") & compile_df[1].str.contains("\.c")].index
compile_df = compile_df.drop(hh_index)
compile_df = compile_df.drop(cc_index)

compile_graph_bipartite = nx.Graph() 
# Add nodes with the node attribute "bipartite" (This is a convention when using bipartite graphs in networkx)
compile_graph_bipartite.add_nodes_from(list(set(compile_df[0])), bipartite=0)
compile_graph_bipartite.add_nodes_from(list(set(compile_df[1])), bipartite=1)
# Add edges only between nodes of opposite node sets
compile_graph_bipartite.add_edges_from(list(compile_df.itertuples(index=False, name=None)))

top_nodes = {n for n, d in compile_graph_bipartite.nodes(data=True) if d["bipartite"] == 0}
bottom_nodes = set(compile_graph_bipartite) - top_nodes

# Get two different graph from bipartite
c_graph = nx.algorithms.bipartite.projected_graph(compile_graph_bipartite, top_nodes)
h_graph = nx.algorithms.bipartite.projected_graph(compile_graph_bipartite, bottom_nodes)

# Save both graph to file - avoid further computations
nx.write_adjlist(c_graph, "compile_graph_c.adjlist")
nx.write_adjlist(h_graph, "compile_graph_h.adjlist")





