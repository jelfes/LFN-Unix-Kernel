import networkx as nx
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

"""
GOAL Compute the betweenness centrality of include graph
"""


# Get Networkx graph Include Graph
include_df = pd.read_csv('fgraph_I_all.txt', sep = " ", header=None)
include_df = include_df.drop_duplicates()
include_graph = nx.from_pandas_edgelist(include_df, 0,1, create_using=nx.DiGraph)

# Compute betweennes
betweenness_dic = nx.betweenness_centrality(include_graph, k=100,normalized=True)

# Pie chartb
def draw_pie_chart(keys, values):
    n_bins = int(max(values)/np.std(list(values)))
    range_bins = int(len(set(values))/n_bins)
    bins = [sorted(list(set(values)))[range_bins*x] for x in range(0,n_bins)]
    bins.append(max(values))

    df=pd.DataFrame({'node':keys,'cc':values})
    df['central_range'] = pd.cut(x=df['cc'], bins=bins)
  
    cr_counts = df.groupby('central_range').size() 
    
    plot = cr_counts.plot.pie(figsize=(10, 10),autopct='%1.1f%%',cmap='winter')
    # plt.legend()
    # plt.tight_layout()
    plt.show()


draw_pie_chart(betweenness_dic.keys(),betweenness_dic.values())

