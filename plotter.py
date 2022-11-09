# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:35:46 2022

@author: jlapenna
"""

import pickle
import pandas as pd
import numpy as np
import geopandas as gpd
import matplotlib.pyplot as plt

shp_file = r"c_13se22\c_13se22.shp"
map_df = gpd.read_file(shp_file)
map_df["LEVEL"] = "white"

valid_time_zones = ('E','EC', 'CE', 'C', 'CM', 'MC', 'M', 'Mm', 'm', 'MP', 'PM', 'P', 'A', 'H', 'Hh', 'h')

with open("data_09012022142926.pickle", 'rb') as f:
    data = pickle.load(f)

for county in data:
    fips = county["fips"]
    level = county["communityLevels"]["cdcCommunityLevel"]
    if level == 0:
        color = "#51EF80"
    elif level == 1:
        color = "#FCFC44"
    elif level == 2:
        color = "#EF8051"
    elif level == 3:
        color = "#EF2D2D"
    map_df.loc[map_df["FIPS"] == fips, "LEVEL"] = color

counties = map_df.loc[map_df["TIME_ZONE"].isin(valid_time_zones)]
ax = counties.plot("geometry", color=counties["LEVEL"], edgecolor="#565656", linewidth=0.25)
ax.set_axis_off()
    