import pandas as pd
import numpy as np
import matplotlib.pyplot as pyplot
import pickle
from matplotlib import style
from tensorflow import keras
import random
import json
import re
from sklearn import linear_model, preprocessing
from random import seed
from random import choice
from collections import Counter
import xlsxwriter
from gzip import GzipFile
import zmq
import xml.etree.cElementTree as ET
from datetime import datetime
from datetime import date
from time import *
import dask.dataframe as dd
import csv
from builtins import enumerate
from geopy.distance import geodesic
import folium
import os
from IPython.display import HTML
HTML('<iframe src=plot_data.html width=700 height=450></iframe>')
import shapefile as shp
import seaborn as sns

data = pd.read_csv("cho.csv")
"""
# for assessing the directory
  os.chdir(r'C:\Users\Saumyajit\PycharmProjects')
    lista = os.listdir(os.getcwd())
    print(lista)
"""

v2 = data['value'].tolist()
state_geo = os.path.join('/Users/Saumyajit/PycharmProjects/saumyajitAIML4/', 'custom.geo.json')

m = folium.Map(location=[52.370216, 4.895168], zoom_start=5)

# Add the color for the chloropleth:
m.choropleth(
 geo_data=state_geo,
 name='choropleth',
 data=data,
 columns=['abb', 'value'],
 key_on='feature.id',
 fill_color='BuPu',
 fill_opacity=0.7,
 line_opacity=0.2,
 legend_name='Respondent distribution over the provinces'
)
folium.LayerControl().add_to(m)
m.save('plot_data.html')


