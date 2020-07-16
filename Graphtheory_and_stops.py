import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import sklearn.model_selection
import requests
import random
import json
import csv
from pandas.io.json import json_normalize
import networkx as nx

data = pd.read_csv(r'C:\Users\Saumyajit\PycharmProjects\saumyajitAIML4\Graphtestdata.csv', error_bad_lines=False) #you can also include header=None
data['newcode'] = np.sort(np.random.randint(300,30000000, len(data)))
data1=data
#data1 = data1.rename(columns=data1.iloc[0]).drop(data1.index[0]) # this is to drop particular row
locationnames = data1.iloc[:,1]
locationnames1 = locationnames.unique() # it is automatically converted to list...
g=nx.DiGraph() # for directedgraph...... advantage is that you can have edges
#g=nx.Graph() # for undirectedgraph.... remember the undirected graph dont have edges
for x in locationnames1:
    g.add_node(x)
timedata = data1.iloc[:,4] # to make time as a weight on the edge
count=0
while count<(len(locationnames)-1):
    t = timedata[count+1]
    (h, m) = t.split(':')
    result = int(h) + int(m) /100
    nx.add_path(g,[locationnames[count],locationnames[count+1]],weight=result)
    g.add_edge(locationnames[count], locationnames[count+1], r=result)
    count=count+1

pos = nx.circular_layout(g, scale=2)
nx.draw(g, pos,with_labels = True)
edge_labels = nx.get_edge_attributes(g,'r')
nx.draw_networkx_edge_labels(g, pos, edge_labels = edge_labels,edge_color = 'b', arrowsize=15)
plt.show()
#pos = nx.circular_layout(g)
#nx.draw(g, pos, with_labels = True, edge_color = 'b', arrowsize=15) #arrowstyle='fancy'
#plt.show()

