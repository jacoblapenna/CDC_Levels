# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 15:35:46 2022

@author: jlapenna
"""

import pickle
import geopandas as gpd
import glob

shp_file = r"c_13se22\c_13se22.shp"
map_df = gpd.read_file(shp_file)
map_df["LEVEL"] = "white"

valid_time_zones = ('E','EC', 'CE', 'C', 'CM', 'MC', 'M', 'Mm', 'm', 'MP', 'PM', 'P', 'A', 'H', 'Hh', 'h')
data_files = [p for p in glob.glob("*.pickle")]

for file in data_files:
    
    with open(file, 'rb') as f:
        data = pickle.load(f)
    
    for county in data:
        fips = county["fips"]
        level = county["communityLevels"]["cdcCommunityLevel"]
        if level != None:
            if level == 0:
                color = "#30FF4B"
            elif level == 1:
                color = "#FFF130"
            elif level == 2:
                color = "#FF3030"
            map_df.loc[map_df["FIPS"] == fips, "LEVEL"] = color
    
    counties = map_df.loc[map_df["TIME_ZONE"].isin(valid_time_zones)]
    ax = counties.plot(color=counties["LEVEL"], edgecolor="#565656", linewidth=0.25)
    ax.set_axis_off()
    ax.figure.savefig(f"{file.split('.')[0]}.png")

    
# for file in data_files:
    
#     max_level = 0
    
#     with open(file, 'rb') as f:
#         data = pickle.load(f)
    
#     for county in data:
#         fips = county["fips"]
#         level = county["communityLevels"]["cdcCommunityLevel"]
#         if level and level > max_level:
#             max_level = level

# print(max_level)
        